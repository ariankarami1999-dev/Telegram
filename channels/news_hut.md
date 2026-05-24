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
<img src="https://cdn4.telesco.pe/file/NYP6B4bi5hMTRgjG_WkP27OgAloKLtd3j4c83ZjRPNINZq_ufVNy6RWWhTVrLDZ_9nPc-N5oWj-wJRDrj2LZgWQl4igpnDqFfRdWTbtO3w4jvY5CH3jwRWRSDSpDXbqNJzjBGnNWnPeV-2nWNx0Ziyrt5KvaIVsI_OLFqUN85jgcqSjI9BtU-65afWjY2I9MNYKaJb4JmW3x5C3sAyFrZQbcDNJ0Va5RN6G13tUpXpUPCo9_AkJLFhxmco2oyh0JQUdc4HGaSpHOZBvxYwfDBtm-PpE7amdGlghmCuipzVr79enZUEEZmNARgXZ5A-BKkXIVjvl4BewoK_aMQKNsXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 138K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 15:16:57</div>
<hr>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=m9ZMCi3xJQOna9uSOaxUDoe2YqS7MbtW34j7o6uPFMpgpQ5AEJz4WOKRMnRREVqmZl-URJCAG30OJKrSWKCvzELMxFBOM2RRafRiuHllibG1MHPKc9Oi9eBKo1KhwGfmf8FFcHFE7GUIjm3Q0oMM1iWDPbwb73QwPevDalORYqnAfCRdT3hKC3lLFNDkksv-CXy5mAjnuAcpQq6SeMuNKhmf4AsWEB_2-IDLZATvcxQVwD4O7k-m1FnDa_Vdhi_D0ZpmaLhz9mn-3LzBeHUglfdZy2cTbYCbTw0A4kiu3G7UNyBpplqK1MjzW2wDvWHHgX2PmqhFuOZIVvvu0bPyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=m9ZMCi3xJQOna9uSOaxUDoe2YqS7MbtW34j7o6uPFMpgpQ5AEJz4WOKRMnRREVqmZl-URJCAG30OJKrSWKCvzELMxFBOM2RRafRiuHllibG1MHPKc9Oi9eBKo1KhwGfmf8FFcHFE7GUIjm3Q0oMM1iWDPbwb73QwPevDalORYqnAfCRdT3hKC3lLFNDkksv-CXy5mAjnuAcpQq6SeMuNKhmf4AsWEB_2-IDLZATvcxQVwD4O7k-m1FnDa_Vdhi_D0ZpmaLhz9mn-3LzBeHUglfdZy2cTbYCbTw0A4kiu3G7UNyBpplqK1MjzW2wDvWHHgX2PmqhFuOZIVvvu0bPyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By_8ixAwQ5jAZGVpd-I0SgIYsss95q7_PE_xA4uhbX3c2KpahwbMY6Gi7Cj99j3GIPVD8XxjnVPZnp9nvk1JKChfbSZ2_O_MkYU1O_4ObGYqW4zrByK5nUSKDGHM8aCULEjoAcJlIpLxCUw-8TRA5gSyoZqW0yJ-CKaFE9TVoNXiQC_GsL85JukWFK4z2-qT09FyNr8ejO5HqmOaZgZZZaeqvWPMbwtEgnQ6bZafp3Z7ys3Q2KB85C7DICVUI5kzrRJRBTRLCH6EJybUhgGp9hjG9P3ESTonHQFdNQUY179QaA8ka55OU25slIUZQp0HRNn6FwPSC7gdcZGsg7c2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nv6OMfQDnHYY8BTC-nhJgRa0d83E0Nk86o4SY1Fon54nKonXaPTLSvtLxg08-fapcdspVWIWhbB7f1WcjuRBk6Fcm4v_rXmonMLl8qVx5WXJnt8_akMUa5sPxHnMa5gEnTvsjUqgYmLKyFO9hTaHMz786Jl7g7v6Kv3Dbv7jKtrr64NHdR-2Q4t2zDbe_FO23iYSEr4lLh3FKSjFLlU_23HRf65904K8zmxCtg3GE1kxKXJQyebF3R8Z-eAwIYb3iNpFYagqJeIbcuNayscwIFdlvY_OsOW8fQTDAaFqm-jKgIsteEKIWDg5z3vdcPjgfWUEn1xopZOGlV6MeMelQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Q3QKam1ZuetRednLenOyo-FZUTE4crRKfv7OiojytJYJcm-Se3mkB_SViWuYJMvs8327YGemYU40C7GYL1zmXZKjO1ru2CU9BbvE2ybI5AxSQnjfEqdnuv0OIlkvCASjKUj4jRfhRrlFXU62zLpqehuVcnnSMD-7fY-OWZPZt0ADrq8oXdhaTHtbXuB1xsONxiaEKI9O5jPs6BHtbh3y5U9s46Ke1CspZoR1Tiad1p3NhpHMQMvaKSr4xN4nJcFW573a_lluWtI1S1kFtZBK1NK6BgDwQnKiwGOCFgKPLf0YKQUf9Zo1JOiD1NiegzpeuKBiL6Chl7H78x0ZxrrZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Q3QKam1ZuetRednLenOyo-FZUTE4crRKfv7OiojytJYJcm-Se3mkB_SViWuYJMvs8327YGemYU40C7GYL1zmXZKjO1ru2CU9BbvE2ybI5AxSQnjfEqdnuv0OIlkvCASjKUj4jRfhRrlFXU62zLpqehuVcnnSMD-7fY-OWZPZt0ADrq8oXdhaTHtbXuB1xsONxiaEKI9O5jPs6BHtbh3y5U9s46Ke1CspZoR1Tiad1p3NhpHMQMvaKSr4xN4nJcFW573a_lluWtI1S1kFtZBK1NK6BgDwQnKiwGOCFgKPLf0YKQUf9Zo1JOiD1NiegzpeuKBiL6Chl7H78x0ZxrrZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=H7gkaVAQCe8OZ8dUrmii9WI0Eo37up1O-8r3aPwToZ3SgpJRM0uztSexo5S1QCZB3Q_l98yTuOVE9FXmoHITIXAemEKHvZ-_VryMTWV13_P5FDG4mQD0o8z5sUY5tt6cyLyRe--u-vX3X-RcO6NUyltJcmt59HDXppIsYyue-r2EnYZURu8Zqbnh6kGC-kV3aIRKk8oG2ZIzrtW0cW0ymCSB2o382R8nR83cfbOLsa_GW4YS-VGR896zrzmIjjYbXg4CRjfT4ZuA0f-3W7PA5eETaR_UCy6hnT3BmuKv54pZKprtRfw337gg11Rlj0MKb4MO37TWScABKX1Kws_k2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=H7gkaVAQCe8OZ8dUrmii9WI0Eo37up1O-8r3aPwToZ3SgpJRM0uztSexo5S1QCZB3Q_l98yTuOVE9FXmoHITIXAemEKHvZ-_VryMTWV13_P5FDG4mQD0o8z5sUY5tt6cyLyRe--u-vX3X-RcO6NUyltJcmt59HDXppIsYyue-r2EnYZURu8Zqbnh6kGC-kV3aIRKk8oG2ZIzrtW0cW0ymCSB2o382R8nR83cfbOLsa_GW4YS-VGR896zrzmIjjYbXg4CRjfT4ZuA0f-3W7PA5eETaR_UCy6hnT3BmuKv54pZKprtRfw337gg11Rlj0MKb4MO37TWScABKX1Kws_k2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l2TzFSGKSAvzIWbb8UWmPbzskQ-nypc5ed83BqI8rlUSBNwiKRqchHGiUcauQLT5ic98w6aKR5Fi0VzijKGhXNpI8CCqWHOikKoHv-v1XBjffdktz0MXVW7JnrCXCH4M5ip2BTlHgw2bb7umaQFlxiTDpv0LI8xsnqFDLUs8sTKEXqS4JlB8Tb4RGlejZ5d_ZaJEFdbND_M3vvTpLbuX7EOQ7w2afL8EyyKItrK-kIDkzjifM7me2EBzMyBKObT5oO1ZYmDogEkmLzYBchcGWufFPy-BEYdWJeEcsmCWhhJb20vxaq9sPoEgbBCejUgEQphtxUJWag9cuu_7w4dnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0xOhwt87enRVtxV5Tvw62HCq6E8QBzx592MO_mVokfvrse5GzylfR42m2CoL5N0bUNRglVYvnX53ffjUmAqe6dWaf75eQUdJc49fd3x1r6UcXAXe_7MTEOPHW2ykc4kAcr5bvGecHnZw6BeDMr70zy5Wtwt1g_w52HOF5qBwidJq3oyV2NPsUmSZzkGufEP3f39ln63zwJPlTaSGqI9lDsjbHp4a9PTBvFlVJGfdUyZPbRZCL8XbgSlWOnYz-kybzRsQf51BmYgjcs6Vix16PendMApzz-mgsucptnjsVOnUTaLTTGZ-qefPnPDVspSvqa3j8gSwzTFxVjrkXrvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=LKY4YlSUyKduwXkUI4b3xI629DMPnwzcy6wkxIvtqkWi7wIVqYY8dqqkU2g4_sbBIUWF3ijC2Drw7RGvUZkC8LHHrT7P_FbnCl5WSthM5NIXQORWm1IT8X-qqQp8Tqsiy2T618Fblx3IwFK-n5_wjFofZ822G973gNjj7LAaS74NekcXqU7SLBPBHlnUWTc_OukgjS8V27CLjt8BFVzsjL8scDf0tIMUM6qmpCkHSXuXUPZnl5u_raQhVFCtGGE_agtVWqz1PMzEBzmEFr07o0HbsEb5K09adIj2YwTaa4MoGWLdFPWjw7z5FC4MSg4KsdTfeHc1JN4g8DJmzXzBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=LKY4YlSUyKduwXkUI4b3xI629DMPnwzcy6wkxIvtqkWi7wIVqYY8dqqkU2g4_sbBIUWF3ijC2Drw7RGvUZkC8LHHrT7P_FbnCl5WSthM5NIXQORWm1IT8X-qqQp8Tqsiy2T618Fblx3IwFK-n5_wjFofZ822G973gNjj7LAaS74NekcXqU7SLBPBHlnUWTc_OukgjS8V27CLjt8BFVzsjL8scDf0tIMUM6qmpCkHSXuXUPZnl5u_raQhVFCtGGE_agtVWqz1PMzEBzmEFr07o0HbsEb5K09adIj2YwTaa4MoGWLdFPWjw7z5FC4MSg4KsdTfeHc1JN4g8DJmzXzBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=q3WawO1uHWs9-a0WXoKzZRcvLUxc7PZkAvx1imIEUywbLiR9hWOHJzew73cMFa466Xpz6N_F6_eghrVBlMhmA2OYAWtD7leO7rKo3Td6xh6hrSEwgfpe3xBx7TFQUoSNioRNP-_-I1vg8v8CINVnVj_b-cUPoCd8a4tDdU5ztO_8tFfl8NVxu6gADwMJdkJ75FURQnrTDcZHIllRDan1g-660WeIyoIbJVGUvKuuuGsfW7ppc--Hu1fbNt6_MSfu3CvK6njkaJsnxZWXuxZ0f3mVr-kvpLtxcKdEZUEmBcWfEBgPCVGlvctvUsLGI0SiXAmR1m4oHV5dDMh3qumkfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=q3WawO1uHWs9-a0WXoKzZRcvLUxc7PZkAvx1imIEUywbLiR9hWOHJzew73cMFa466Xpz6N_F6_eghrVBlMhmA2OYAWtD7leO7rKo3Td6xh6hrSEwgfpe3xBx7TFQUoSNioRNP-_-I1vg8v8CINVnVj_b-cUPoCd8a4tDdU5ztO_8tFfl8NVxu6gADwMJdkJ75FURQnrTDcZHIllRDan1g-660WeIyoIbJVGUvKuuuGsfW7ppc--Hu1fbNt6_MSfu3CvK6njkaJsnxZWXuxZ0f3mVr-kvpLtxcKdEZUEmBcWfEBgPCVGlvctvUsLGI0SiXAmR1m4oHV5dDMh3qumkfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qk1uC8T2cp35uMFSwNM7Z3HHImzzu2u33o3L9zoUxbZFv_caFycze8VOtG2Gf_2lm6-3nwTpyXi3aTIfR7FqbO84vpas7pkKBD2jqkJ5KY_xpYf530AaOVSIW5tGDPleuCtjDu0lnweR_0oKG3M1pEZVy3RaD4nh3vUH4jwup5KqDZxy-i4zlzOJTxTJ3oCJhCnocQzhJNxuf5lljE0ToTrrf9_xr17NewBmqJZ6cnJ5VSTSIOoMMDnw6uYaUTaiAPFRlPrpRWLxybgdHFzUPnLfb_bZqJjoVafDznsKZ-jR1i-jpZLCjt6i9aBG0NvhwHWAfOHYNNM7cTqboKZVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y64O2_w7EgWl-l_RiHOSplkYBhsOVlU0S9-CZfxr8hGKZr2e3CqGNx-Q60K88mvUzr3D-loWryAIkgU-XIZhjZkJO3wNUmB4zo1HMGOXJT2AWbbftv9x3Y-cmVB5NhU2yO0dwe5J9LW707G2gb9ACeZcBJwIzTODTsHqP3kFXktkgiDO3xJdmK73JcV7FM_6dG_14jtsoxqNFg6hX6M_xFi7vRGB2HkGsoE8V91YORbtrdAFumPp5VIMwrMsJzzK3jmHXzUCnxwQo8tZr3mv_FD7Q-5_Zc82On90ide86JAuNxVSzwgKKuWpfzN3UqFlR6mk1FwppCWk0lhlNyEx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=qzvbq8xxq96fzFpx54Qyc25R5BKWVKsgdUGK8zPB0yERhAavWXw920vKLFyPXVBsxF-OQeCvIKC3s5ikCQTplz2bsamaDYpIWk-hljylL9RfdVkIRTSBuC2k1qppwdCBoGcfPlSvQf9ztE_4WoaXW4Szgm7FZMrooPE0BUV0zzCfBp1-JfMZAJ9A3oN6j8uSsuSYl3oV-GELYlH4LfBvPjjVX1q4WS4Rb2Gs5khDqVB491AqcfuWRdebJQEIwZTXhJ328nnmp4dkNl3MADjiyvCoPkEI6n32uEAORqMoyH_7erNj9LdwJEk7EfKF3owL8Ts3HrJEhmOjbrmZwOkwRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=qzvbq8xxq96fzFpx54Qyc25R5BKWVKsgdUGK8zPB0yERhAavWXw920vKLFyPXVBsxF-OQeCvIKC3s5ikCQTplz2bsamaDYpIWk-hljylL9RfdVkIRTSBuC2k1qppwdCBoGcfPlSvQf9ztE_4WoaXW4Szgm7FZMrooPE0BUV0zzCfBp1-JfMZAJ9A3oN6j8uSsuSYl3oV-GELYlH4LfBvPjjVX1q4WS4Rb2Gs5khDqVB491AqcfuWRdebJQEIwZTXhJ328nnmp4dkNl3MADjiyvCoPkEI6n32uEAORqMoyH_7erNj9LdwJEk7EfKF3owL8Ts3HrJEhmOjbrmZwOkwRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=iK3UK5tD1kAJtieg5Pg5UBpkRtnlJZnDC2PXZF5yFGb4cLZ6pLEm7i4IgJW7NL7SdS2zcz9rpx8r85UUpwJK9Tel71_42_NuY4UXynkAFuk0FepACKSLBbsZHijXymiWwCzLoMHsXb_xRgzKEx4LobGuDaXnqcH83gZbkntYK7M0Kn9SV93D4UadHbfZ0WCQ4Cl0FExbYYe5ItOlYoq280QI4rqTDyGcdNgRN7OydCWtfGdGTiLVEgEyltg5DkTheU9i_989oy0_rh8j3GxNNC6SfkhBhv21BrYH_9ef5Ioj8bgu3i_4CS1L4dBpPlu2Zun9syINod-m2-9tuL-SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=iK3UK5tD1kAJtieg5Pg5UBpkRtnlJZnDC2PXZF5yFGb4cLZ6pLEm7i4IgJW7NL7SdS2zcz9rpx8r85UUpwJK9Tel71_42_NuY4UXynkAFuk0FepACKSLBbsZHijXymiWwCzLoMHsXb_xRgzKEx4LobGuDaXnqcH83gZbkntYK7M0Kn9SV93D4UadHbfZ0WCQ4Cl0FExbYYe5ItOlYoq280QI4rqTDyGcdNgRN7OydCWtfGdGTiLVEgEyltg5DkTheU9i_989oy0_rh8j3GxNNC6SfkhBhv21BrYH_9ef5Ioj8bgu3i_4CS1L4dBpPlu2Zun9syINod-m2-9tuL-SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=On2Uc16Qx8N0ZtlttPQrbTizlNDHee9VCnv4Usoe6-uiCbT7F2GVyU6W_rh889Dmj0YGGY3yy4XZZm-gozVNcbv_QG61ruWN1DuYZHd2tKZpEJ7lynmoprQReAL2_nAemmER3wozacU_E6IZFRljURWsofVk3EcKe-EueCTBQXMEgBH3WPmJ6FFGscuNNiSxXfnXPy8TneiisuvHbHPD6IhWgj5SQzpScglpCmvSnafNBQecD3iqoyFUQRV3AP3DNLwVrp51aLmR-2M_ExPH_AQmQkiE5k7Z5hS2xfiCTjprImxE-arTxb6yZTW_HonxUk7DPRG15W3oLcO1hdQonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=On2Uc16Qx8N0ZtlttPQrbTizlNDHee9VCnv4Usoe6-uiCbT7F2GVyU6W_rh889Dmj0YGGY3yy4XZZm-gozVNcbv_QG61ruWN1DuYZHd2tKZpEJ7lynmoprQReAL2_nAemmER3wozacU_E6IZFRljURWsofVk3EcKe-EueCTBQXMEgBH3WPmJ6FFGscuNNiSxXfnXPy8TneiisuvHbHPD6IhWgj5SQzpScglpCmvSnafNBQecD3iqoyFUQRV3AP3DNLwVrp51aLmR-2M_ExPH_AQmQkiE5k7Z5hS2xfiCTjprImxE-arTxb6yZTW_HonxUk7DPRG15W3oLcO1hdQonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoo8guTUV65lq3oG8wH-BfdM6swDijvSIWvXtvyYjSMDHoi37lJ_VoJazNJGlVTE3CDDxPyl4fNy5KMUfGk8FHFXMhKjqm2MmAzRp8NKa-XWZgHeGRJBce4eZTALjj8-F8muYH5sTdkrMi-E4tGmLbGk_WKt_uWrjGhnm29Wdi7O0mQKXtwgWM1ocMg1JyoCjFz87YaIdiSU4PNLEI-66at9eHUpmCDAOg6EpbsPJv7vEvFzDKJJ4z03Fd3Z0ITkOwMQMfNtJN0gOa6tsqH794LVohBDXRA8a_WHgrY7rnkb8hBJUIToc7u43p2XOIFeRPNZ11uwO4kFd3jQ-LGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
📰
رویترز: یک تیم مذاکره‌کننده قطری امروز به تهران آمده است با هماهنگی ایالات متحده برای کمک به پیشبرد تلاش‌ها به سوی توافقی برای پایان دادن به جنگ با ایران و حل مسائل باقی‌مانده.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64997" target="_blank">📅 17:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHfEAI2uzP49zZj-2eIWuh8sKGWDputmFROvzWUBBerZbUAb5TPGmW1C_pLcBxBzWMB53_AqxNk9RmX4M9d_WkNCcqOKpl021O_0ULzodaZG3L8jENeZiuhi-BmBbyogS3AdBHdSUJhMyhud3ZspzI1KFIuHyutQGUekFjm9-G98OLYCpQVeOl2o62lAAlC_dnjFYITFIhn3CT1wDUacsIYRjE_YVXRa90LPsj7WopE38QqxQAPOplNg1U2whUPAqWzWVjJX4_rYlNHjKFRfg4r5l3EE_QLDUnVYsWtUwOG0OFUHoMNA9a7IKg95-A63f1zJoEyK1T9lvgZ5uKqODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیما دولتی پاکستان راهی ایران شدند؛
احتمالا عاصم منیر در راه تهرانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64996" target="_blank">📅 16:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eb7TMUGRpQt7V40PG7-OsimVyTBDaIZPE3wng3sIAWe-Luo4n6UkXqzycGuu4YLC_mKyZUqU-Kk-0ZEAkp5FuYINq2rdNwEUwb1PJatMyEineV-nNB4dJW--COPKrhKD-xlwCu-ybyZu4PySP6nbBP-_M8PYKgZK1jJU3scNHOnOAqw3yfyLrPs59owT8Zv5DUDeJgmc-gDM91EB_DOdQ1kgxCawgwz4CpM4r82tf7Bw9hi0hxpprMMsCVmPtG5FQ_d42_Px56Sz_uUOLMNvFdc3MxlRBHJsm62WQsyoE6-Dp4bJ4l51uZ31VHZOZkY0q61Bus8j8nTXa6n33GF71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: نهادهای بالادستی به این نتیجه رسیدن که بازگشایی اینترنت به صلاح همه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64995" target="_blank">📅 14:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه: تو ۲۴ ساعت گذشته به ۳۵ کشتی اجازه ورود و خروج از تنگه هرمز رو دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64994" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=H2Do92CDS_M52ZbY1g9w-rz1frqjNbUTZ6sqYlPI-wfy4tlDOFHtqcZQ4un6g5bic7wN9oimBpO3r-Uo0Gbyh9X4c2OBglS3SGze8z3WyFdW5o_TVOJGo3KVlhXPt7Tspah37vgzv0OswbR_nwp56HPWY7dfLbtbPgApDHC_9exZICWo6Lovt7HnT1-2Fbf_RjA9VjpRejixS_JjKg0v_ByllUSZ9gtsnxdG6vbq27_0IRQXUbDG3hz1GLA87YTWJ8No-MC92QIxsUPDMK6TzPinObi-BUXW4R3xxvM-JSKVSQGgo_LsvmbsHqGwXm1iB3r_oINt6FvNpQUzlgxH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=H2Do92CDS_M52ZbY1g9w-rz1frqjNbUTZ6sqYlPI-wfy4tlDOFHtqcZQ4un6g5bic7wN9oimBpO3r-Uo0Gbyh9X4c2OBglS3SGze8z3WyFdW5o_TVOJGo3KVlhXPt7Tspah37vgzv0OswbR_nwp56HPWY7dfLbtbPgApDHC_9exZICWo6Lovt7HnT1-2Fbf_RjA9VjpRejixS_JjKg0v_ByllUSZ9gtsnxdG6vbq27_0IRQXUbDG3hz1GLA87YTWJ8No-MC92QIxsUPDMK6TzPinObi-BUXW4R3xxvM-JSKVSQGgo_LsvmbsHqGwXm1iB3r_oINt6FvNpQUzlgxH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=iN-IhaYYVikEwl0J3yqHz9q5TcOuHQuHvcmhAM435psq-LP3hshvj3j5vy9POjy0XHQ9xaTLUFbRnEDtgpWRHfy6u530RG_lIgA9Nq7cVtLvfOTivuAGf-hKijvqKF267WA1NIrAKqgisV-d5T1Mkszf6pa3s_Uq9GtjyFvlBlwZXUaXuRR3j8uTS7nlJtYtBKkF4UAdElUJjjMVVjZwLm4ZI0bfZmtWX7C47ebVGpE0_FIN_gKUXhFZrEDMTRxjFlr2wBIIRXJtrcNjr3dhc-BKYZS9jWmf-jXogDjtGeEN7r17b_l7lrWqeSZoVXea-8xyBqTcy8uWkQTXvZ_CuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=iN-IhaYYVikEwl0J3yqHz9q5TcOuHQuHvcmhAM435psq-LP3hshvj3j5vy9POjy0XHQ9xaTLUFbRnEDtgpWRHfy6u530RG_lIgA9Nq7cVtLvfOTivuAGf-hKijvqKF267WA1NIrAKqgisV-d5T1Mkszf6pa3s_Uq9GtjyFvlBlwZXUaXuRR3j8uTS7nlJtYtBKkF4UAdElUJjjMVVjZwLm4ZI0bfZmtWX7C47ebVGpE0_FIN_gKUXhFZrEDMTRxjFlr2wBIIRXJtrcNjr3dhc-BKYZS9jWmf-jXogDjtGeEN7r17b_l7lrWqeSZoVXea-8xyBqTcy8uWkQTXvZ_CuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIGDVzZKKpIwvDdr1VkonBhev7Q0sI2lp5qsOeEWbaviII3ZT-7CturhwUcZuPW7Cc66boiJ_4ESprp0L9qbQBRAN0Gb4H_24S3EFZTjmveXRJlvaGGyVqGvi0D9ouDZtK73tSQuNKPcFM72spElQ7p_vZ6_oh5fTjj2uTEJotIB1oH5eglffhV65TNGDnv2sLzXmozthOm2FX9WSqY7LMaPtgWsfZCPcwmNYv1EXmrjpRneGaTmTg-7pDQ8dFmyGoIY_135bz_dKV1kmaRyrollizAX3pnTjxfirJwcqj5dZXTpzJ7NQpC6Q3L_g7psFUnN_U4Zs0-PVxkvExxLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r62n18g88-XWixOUZdjoIq-Q21K7BvoygQnvXI1HxneNTkcEifkoSqVAowRjhyCVpY2i1ByE_odtaTwJvs98XHrwSd6yHRX4GAPr3aGYS4OaJA33vLzC4280S0BJt5VX0VGbnsDwDsRn0copVI731IPpO-YNUzm9VRWI_r300oMT3BeQnDefb5fS7JgL61oTGQ3Bt5xlt-CNOqeoYCr_KQ7xS3p2b3O5J-TvkghDs47cSYBkfYQp94yUhCj4pSfSEnK25LJ5uNcoxjCRNZYW_tx20kK--rjC-FWEegnKdJTQ6RZ8xbBC7jZWkYmSbYz9HWpkGCL2yxjUGXkErqpMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3MxJIdQYThSSmWPa-n28m6KLNUbxAIrGRejHanOU-jLsAR3KM05ABL8xK0OL9lCz-boFlHT3KKOeQfQoG_ZYX0ADNcM-mfm1fQtLkTmDnPcQ_l0Gz51zBXlGs9I5OswZL5xAsunHI8FXCAIzgf-pk2zh_yMToeYUUzZXHUDGuBTiJYvE6bapSrb0JYs_5Pi4EoBoyuqNUjeYh6NQOihBUF80FxggKZExxUmhR0laVz7eoEKj8_CXj12UE6n_uNZDAirN4IgRXnmnHiph8FnZ_j-_0o-YRaHNYQ4TwrkX0epc-dfDoUX8Hh-CXO9KUvUZMjYfIAURHjk2jdnlyRSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K4UdHenL4X1jgXe8I-MVnbOe5rWQNUT-reP0Z0YhZ9027Mbw_Pep3X1pP7hYMcJ15Aqd0-sqMHz_-1w5zRurx_q3tzBCvlCx59Zj-n2-KS7lUYQ5DPmIb9-IfrzIOfBFZBMcjqZjOmMVjL-xchNVJS63C-2yi7oXAcFktNTUjhUsFy-hjbnPWJJs59f_x5fAor6hKVZaENsc6V44qyUCJySlXZds3JkGmIVkB4cTtKFF3k4jXSRR0RIvinEbIH2QUUVbzh_5mcnNmHxcytF1cMJOWKWryPQFjyQyJlzHMfDkQGYAd0tt0ptXWNnSYzq4q6KgbZONdtnn-oLeM_DEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2eVBpwQE-CUtvb199BmDtc8QR8Q8xj32pxLt41twEvvmK5gzHqhXGD0UL-b9ZRbTUaElbfJG4jhWzjq9edXL_RJG-QMXBDb9SsCgGiTTXKkattZK_-bwDkSt2aJTV2HRRQ0R6O7kd8GJ8qySAWUpQ74rkjKlm7xQM_gtR4kuw_767BoGOWIuYggiESXUyRzJeHKeSWpQVPUPg2m0hjHwBrpdu2hPApWKxravY77DnrY8dZX88IF7UTdCG8-UJOmgbjeMmfBx_as7ELpwibi5MXEJL1mK_XJFNk26xcyeQ7Ux5osze4blBYgRx0emwnRhQZkd8pf09qIu2zzHKTUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8eF3gid6e60l6jvBOQ18fPqmEFcUwrGS6R7KY9pXFZXQyzrysl1KIqGSWO1LfFn35eCJhoDMUuc50XNLCELWbMHwEa_kBkGwjQbGDxM73iayCRKSdDdLw4dY_8WZ-oX8z0orXc7v6Sx6asfztLiyXNzc6nekXbhdjst7H6iFSw1D6ykARsqMXQmy9hj13KjRSIf2tuNaE294KxPLuUpFScUK-682IaYXpVF8uh8VmKT8MCQKgZnFAhGZAjcTgcYtL6ijkygjqwKZXn1B1R393gxyEChFBbC5TPLZhnRA8D4jNopYG4EtrTz0fWgEz3auo-eJ9IWbYHC1oLZSCPENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN9QmD8_OUDD6lgLuVor74Mp7yEG7nynXxQ6GVkVVrgeFRWTU-d4TEYDPxFcYgo8f0bV3B8p6gXnM_JkX-Z_08BIjnYwn4cZe9ESuNfddre2cF6lNx4U5Vm-fVOAthAxCy-1p21SQ-Lsuq2rbiVPeRTYGbNxp9bTge0gGM-Tkj1X0QlA2QOSHIByOUE_-IaT9lHS5kEMZcEapI6CCRBk8WKXrU_fs_4Mxvibt9aMyfhi7eQH9mAYksanhm40xa8JleCacWy2AlUzIb7Yw8zgYPW11667XybENT8f8JX2wZPuaNNvyB3p1Nw29poOUluxxI3716zXan7iLLul1JM0_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=R7tgp0dd-73lHs-ilKgNbskKyfSmBNmW5Ww7EQnEeRRc4EdwwOWhQkGgiXT1FLP2hqMC4tkLI-PtAUA3Ld0aE7bOC7zAo2qaQ8jnPJ4aww2AjKc9vHyYGyF6KAyueha7-l026JqbVm3MWhKO834RWd8DR7RvH-Vfbs_mVySYq4y8-6yEdnkfMkhdxXiw1dXsTym1q0KTLK5i74eL8QUbuHyHR-Vz-NLqdP_UzeeuMuIwZm62b7jv8PNoF15zDYV_GdA7arj_gJcs_RjR2w1LPd9jO7Xxtf6h9Ko6r4vQjsfsOXOsGFHUYLY9Vl1WVCIG00ot9RI_FZEub7TC--zt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=R7tgp0dd-73lHs-ilKgNbskKyfSmBNmW5Ww7EQnEeRRc4EdwwOWhQkGgiXT1FLP2hqMC4tkLI-PtAUA3Ld0aE7bOC7zAo2qaQ8jnPJ4aww2AjKc9vHyYGyF6KAyueha7-l026JqbVm3MWhKO834RWd8DR7RvH-Vfbs_mVySYq4y8-6yEdnkfMkhdxXiw1dXsTym1q0KTLK5i74eL8QUbuHyHR-Vz-NLqdP_UzeeuMuIwZm62b7jv8PNoF15zDYV_GdA7arj_gJcs_RjR2w1LPd9jO7Xxtf6h9Ko6r4vQjsfsOXOsGFHUYLY9Vl1WVCIG00ot9RI_FZEub7TC--zt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy1xRTE5qRqdZtcI5cJemaDqJXBFRYflBBazJB4-1KCflIeuLit95gcVuSKDVFnpdGZCJ8foOU-Orz8ilFHqx1V69xrOjmW5NXZn3ysnlePycqO4p-tjoNcuoqmuQDjTTF7-6TsccekdWoOE9i7WHp-o3wjzzIpP2B--cQujxUl5Jqle-fGrIvO8buaBQn_T3Nt9JfvPNwt4WifoWYeratIEOb2VbnZJTUGY6N-TcpmOMwuNNghgNEH0XSgU6sW3agRFx8NdGSbkUlPbDa7v4OaBNgrh249IBpeSL6MbgTazFdv0NLvhAahjEkzcB2Nh-dYpqRMBMAZ0b-jl_-6ZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Oo0VfsIswHlg2zrbO4J0dxXl9lnrRI3ULw46brsYmmwnKPQq3MQH4U5g3h-nHaz3zey9GucN4bdUaCknMZkabp0GEz7wDefYA8sGYI-yTH0G7513qRe8KXYWEVL4MXjyjCTDHNxUj54pHS5kwo2_LraPL77m1i-2x4uBwnEpuVjms7byvQoQhT3qcy7O7il1aez3r-ccV4CjS7GIu19ZeZyOCWfgkOsIvbrK8EYMe-frFB6_ywjOUCc309D6RDqiIE-poQQsDOvEYKvpYRudANuq69rmNNV_pxzTBjlFqOwMzvznlMWPYGFrMiRrce4m32vYU7T38pWwMYrJXUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=nwXJUGdxxuu5OnSUKOjsW66BQIfMc03OBYAdRBbLbi4mtjMoHfFBcn3Sg_8ToG4ejLzsjzz2JfNrnuxWSNM0CZpgR_0Y8YDRMJPpVua7f9ZoglkWTlJ9ZSYqCB9D9auwA4l2klcsiXuaGisFhkcRkhko8UBfoCeqsvu2pU7TqlJQ3p4rhy-xGc6vYBPv3BxlStEJpo8h51bpi_v86War5lA-wLsS9WwKsOVOmt_Cs7-CW-x2YUcoZqQDUqYbC9Wz2MGVHubX1-bEd12lEC_e9D6Kup22N63yVId61uNIgwBCwZ1TyFd3jrDmAsNuzIvMStaOX5Lk9UoUmeWY1JUouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=nwXJUGdxxuu5OnSUKOjsW66BQIfMc03OBYAdRBbLbi4mtjMoHfFBcn3Sg_8ToG4ejLzsjzz2JfNrnuxWSNM0CZpgR_0Y8YDRMJPpVua7f9ZoglkWTlJ9ZSYqCB9D9auwA4l2klcsiXuaGisFhkcRkhko8UBfoCeqsvu2pU7TqlJQ3p4rhy-xGc6vYBPv3BxlStEJpo8h51bpi_v86War5lA-wLsS9WwKsOVOmt_Cs7-CW-x2YUcoZqQDUqYbC9Wz2MGVHubX1-bEd12lEC_e9D6Kup22N63yVId61uNIgwBCwZ1TyFd3jrDmAsNuzIvMStaOX5Lk9UoUmeWY1JUouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=k8lAGa_iROId2dyAONKDrpNdOcZCTpKFMGkLklJoCvCykryfS2lkA-qdWNsk5dsjaynilyF5sqxfG_xqX31Cmm4Ajd6BYaZr4hDfIlFG6ANkODa9OYAySHkzvS0hWr1_XvP7HAT6KOp5YvqoyZJSvAR-lwIh71RLtn5Rna75IhVU6ap3E3DaXxrZKaQLyMzh7NKbTZwzOHPNEUAd_M68yBAq9LIqKCkeHBc339H_hf8epZemxhy6iuQSJUlh31thzyS8J9uZUgRCfG6aKy0vb9EirSl9qDJYZkvozumS6TwswMwWuxkjF91gOhMYSXdK2Ypa3uBHTRZusBwOOAkFlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=k8lAGa_iROId2dyAONKDrpNdOcZCTpKFMGkLklJoCvCykryfS2lkA-qdWNsk5dsjaynilyF5sqxfG_xqX31Cmm4Ajd6BYaZr4hDfIlFG6ANkODa9OYAySHkzvS0hWr1_XvP7HAT6KOp5YvqoyZJSvAR-lwIh71RLtn5Rna75IhVU6ap3E3DaXxrZKaQLyMzh7NKbTZwzOHPNEUAd_M68yBAq9LIqKCkeHBc339H_hf8epZemxhy6iuQSJUlh31thzyS8J9uZUgRCfG6aKy0vb9EirSl9qDJYZkvozumS6TwswMwWuxkjF91gOhMYSXdK2Ypa3uBHTRZusBwOOAkFlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=sTMG4UubWL4slbiWGUq39tcRczLbniSpmkwgNQrAp0JPrdWgL74qdAWM2Zy8vRa92t-2B4oElysYYysrpI__2EDMBpXM_AJgt-ii9TtrJl_8ntvlbZQlcFmzQUtOjmkzKcNE6m03WAPPdrOpqJoASdEjbw_Ws2P886qU4X1AG4UIapoipR4EZqDyRasCH_A5Hn5wHH2mhRTs0LD1eSetw9G_Q_csjoSKo7c2ndTGVO-cLA1jzP3_Rp-SBusPHLwyRwCuAmZOZ94yFU_ijyWV7FpObmV9Ypybt6S_6Vr22TlQJ23W70I_zNi_KAqTz4EmQwk3Z7lz9LWXIBlorKGfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=sTMG4UubWL4slbiWGUq39tcRczLbniSpmkwgNQrAp0JPrdWgL74qdAWM2Zy8vRa92t-2B4oElysYYysrpI__2EDMBpXM_AJgt-ii9TtrJl_8ntvlbZQlcFmzQUtOjmkzKcNE6m03WAPPdrOpqJoASdEjbw_Ws2P886qU4X1AG4UIapoipR4EZqDyRasCH_A5Hn5wHH2mhRTs0LD1eSetw9G_Q_csjoSKo7c2ndTGVO-cLA1jzP3_Rp-SBusPHLwyRwCuAmZOZ94yFU_ijyWV7FpObmV9Ypybt6S_6Vr22TlQJ23W70I_zNi_KAqTz4EmQwk3Z7lz9LWXIBlorKGfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=n-sC7xGkY0q4rlxLDbRVu_Uo93HKp2Xxa2OxvyYHwFxAOUwdMvgzPocQ8Pr7KEMA5jQef5wFjMKTmdNeskbLwqI7Rj-FC0h0VA6IPp32egDmMrHqeVrOvPcaVzP6Kks5YDe7CPkehxa2amkI8ywKDhXAJXX81ZnkRREo-JiMDns-NYdwCldDtTgwKcJjijQjDdY6hraVLBGC4x3vLSgAjTU1iYjdWGWsnLxwujKREgegsv6uodAebJl_sGL-lJeSSalRsNCMpbVGGqJsw5PzHViav-ghwTNixMezOqJ9oNy-01rNFKbjePEKRevMK2cergP9OTcdZb2em15sjrMLhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=n-sC7xGkY0q4rlxLDbRVu_Uo93HKp2Xxa2OxvyYHwFxAOUwdMvgzPocQ8Pr7KEMA5jQef5wFjMKTmdNeskbLwqI7Rj-FC0h0VA6IPp32egDmMrHqeVrOvPcaVzP6Kks5YDe7CPkehxa2amkI8ywKDhXAJXX81ZnkRREo-JiMDns-NYdwCldDtTgwKcJjijQjDdY6hraVLBGC4x3vLSgAjTU1iYjdWGWsnLxwujKREgegsv6uodAebJl_sGL-lJeSSalRsNCMpbVGGqJsw5PzHViav-ghwTNixMezOqJ9oNy-01rNFKbjePEKRevMK2cergP9OTcdZb2em15sjrMLhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=WaBAuk2dXdtgPRuxQvudwEwsWzTNnptvFW9MdM-P452ku35Z6QUEvPnaH7Atl90jBDHpNBa0MnfBiWhPwlUAjtvynW2Oqap627KdBTSZ5CmjBIOfzFOa8n-YcMUVhy9UtUKeOXtnb0PgYj1LjxfJXLqpfkAkFjLQWHoc-Or3DX-WdgZ3i7LSjGJZ3Oia-0azA6czVzKUNx9wUUioEyeqEBAcJqXrs3VosP0x6OwTQJjggyyvmwkMNKRYwTJvS5qFfTHJfCAvo4zF1SIDdxIhUstFQfvSB7EX3RDBUulv3MRaXgGJpTuL0yTpEiX3gV2jlSoH0sr9ruLJvnngpOEr5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=WaBAuk2dXdtgPRuxQvudwEwsWzTNnptvFW9MdM-P452ku35Z6QUEvPnaH7Atl90jBDHpNBa0MnfBiWhPwlUAjtvynW2Oqap627KdBTSZ5CmjBIOfzFOa8n-YcMUVhy9UtUKeOXtnb0PgYj1LjxfJXLqpfkAkFjLQWHoc-Or3DX-WdgZ3i7LSjGJZ3Oia-0azA6czVzKUNx9wUUioEyeqEBAcJqXrs3VosP0x6OwTQJjggyyvmwkMNKRYwTJvS5qFfTHJfCAvo4zF1SIDdxIhUstFQfvSB7EX3RDBUulv3MRaXgGJpTuL0yTpEiX3gV2jlSoH0sr9ruLJvnngpOEr5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL7SDSEsYLJcs0CooQTuJXDBy36Dr5A0rk8iyBI666DldTKGWjKRvOAMjFxv2RDwtNfVoCIyL8ZTGGIJT0Xsa-uzApL2UJ8Do925AXEc2fRiT3kAGE0ovbXNbJVYEF50niJpzNs1IpNYfBeio-WWJ4sBBY1-yNEFZ2bxx9g7Z8Uo2qHykI-78hB6lH2g-4WCdkBnVmcwxWWef6OJBKmSacJCDtsTXQGTEPWjwqNuf1VBDGtOEPCR8xE0yLmcKXIgagDMIIKkOCdCGXK8KV6ta9RJNFYHPzZczJav8JEuBizUVc1XTaa4vBZwbWDam4ndwGjgQwzB5nqMa4c4PX1kLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1eFp5kI_80TzQoDNzjrR8j-yZqN8wXAYyvO0ZsR0OZhhtUBmnTiWE4HIjURPaV6GRwk9VTs-g2dFOXpn1GOEghxNotHddN4jxbhxrhXKMMum7xbNEjlHMKsOt5dlZsnmT9QI4PR_Op1aD-ZV0DE4lJgcFv6E4uGnYlqNQIxG20EsLO1B37YQPPN94CdT1FIZb8vT3vnEqFyEAHoovRvVasy3pKHMkTqjmIX7yY-0Rb6i0T5uyBNyITNHdAWKyutjxPJCY3BlwGY0ExIH-hu4wPmZDXR-bey7q5txsNKi7EOs8yhv20M61J0XUx0mfMYXIb5hW_LL9FyHG-39c11Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxatIOD4K52c-JBUwhPGXanYFyj4YvcVNVMUW3yW9yD00hdyyHAhk7_BD-V4GKCVfu08DCHzBTwDNPxvCIeEDYq4CanIHMyJ6ED2xlVXeAPaqhX6kGdRLeEDD1uokSJA8PF-dhW5gC6Xg5V9okRYd7CNu-W3qBlk84FhBgKg8EQi3HLUaACKkLeXLEtwNukXth2DOgrDcdJ9XnnUhjJq3Byu-63x4cre1rvlu7mI8aqn1_Vkmsb8egISP1cuQkIt55MJW3aa5knR3oi-Ud9M9MD6U5d3mbVmEUDqAGRDRwtLbJjnblVxVIkdIK1zoXiK-HVET0lla3sQFpGosmnB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h83WFuBXtwOzReL5ttnUCRHIp1AxUyTpdEzlM650FGOH0BqPeGi8qNmeE5EH2Xxkza5QfEoKrbby7ag7Ac575hQusJtiJA4EWzxrgnINVwtHn7mh9Vjr-X7UH4RDy7qe1rjbFwBLo6Ns_iPjykaur3sQXj2MT_jBTzc2cW5GWKSgmI1BFytWW5ztEiI8R0QvU7T_Gnstn_0Cqi5s8go9KHBRh487pZBVJNNOO1LjfKEYJNxxiS4owoSN4TioZl0JeieiexAqDzXEXty-fm_CEHh-2mDafrHWgeOEVSXj5UInHXTQz9VgwZRTsWBSwAcVd6WG19lh6EOnHpRjTpHeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzUtlR_fOD5qUo_j8izOeAl3inqxxZ9O3WUt8kWHd0xjTaul1aRuWeOigkXJni_yeWQKo38bgCcjBtwTsAOi7SjLNb-YJZPmSAZRjE4WU015sQiJ3MKqNLge59-lbyS2NkPIxNsFrc_j5QPiuNoNebPsK-otbWT6TS6MA6sM27Uk5804hwveK3qNah5nuTYse8OjRCbYtapEvyONiVzZ1zM_3_lp7vOGEkaI3Ip2QxFbkGFeeAB0oXB_RYLPg1vLxuST2cQxBO1XKO1N7jlz3_RETC6Wc2GgtlOz5QVJZ4ePXUGdU_dDMkWr5SbhVf2yeb4Uxcqhn8gUPHXhb8zQvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DH_HelpXZPvitH9UtBN-1AKCV2qrrlRxV-6ECYotpEgQTFbWAswO99UfasRdcmIMyGEECffw83cyvaVWREBZpS7E9twGQYRVAHNfNJD-Ji7sNJhyNEWqkrUUwZg63Usg89s5bfirYULLpVwYME5jjWx45rF5ly4hbFH_0q6eFbsRoiEw0eZKLGrHW5Vc9PbgGrlH8hfai7c_r_kBfqmQAC2UdfR_0dTXIM-nAZFKqN5QKgfJEzNpj9sGZTEJQcx5ME6AMKykO8T3BvJH-AcoLo0_KFBER_eS9rTFonbGelWUEjez64ugDz-C5ds_xmMvhR3QgUiZ2tykLEU2T65aUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SNAENv333gpXQhTLF-2G2HNJ9a3mopz1JVLutfEKn51zTpbhLxFu85dbEo8snwEN1BabUtncO9ygBqaWqEyGh0Q3iiePSKHYYi6oX3l8oXVXDWpTTR8WrCl9tKk0CLN_kV5Af1m6WW6eAZqtZyjvZdIOcf1mahrJYmnRRoZ5vycRRVWY5GvetqaWFYp8qqMvdedAUmxaqT8AjmRdfKFjXKR_zYsfEzt6rCBN9knarv8TG1X5johnhy9cWVBfvDlGKXy73BzJPqk0t-XDCcIUcajWppQU5Qeo6YXn_oJEaZCSq5A4GNXJrcVzrNBViYfhjqXV0CRPnwT-rhiha5xphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ly2e_lezHSJvmhh877wenQPmcr50lATkV4ZliFhlvALKA1fUxBLk0kzsvPyh8TgvQuF5lNNwS2fdV9oED-ekJ9GOwUiCKvnTEMJIQSu-rIctZztCRdFgUElU7i6IoCf90WcC7W7Kea9XTL0Eja3__8iuMpYLO8SBdS6Y77TKU2qYwShKCF3VhZ0iVZpQyEyyAdsRaqS-a0FXFaJ_SQYsd93HlP8HDJuO4wWwwsU56xe4DdnBHrKwSO3u9Ox7E9qbGNeihxCSyHor_7wjkJr-YUhTvvmz-qb3Ce6P0hVLB60YzfXC9WCvriHwH4qPR6TC9ufRDnuR2yhNpAyQqkz_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hYbT70CmOZTLntQ4WYbM8t6V0v08YfbjFRSYBozGcXqnNCHPJtmv7pukC4_Y3gwqQS5Lotv-CLq6YFMZ-f0e1HlnjcBjabENbBUMJ8yFbTLhIWCn2C6lusnRa4ZWnaoIzQfZZVWnoXmbc5_pfhwn1DOFGWifwRu24Rbo2W_wHLYfIi2zpwId6CwLbyZq0jzNIK8lDO_W4Tnx71qpSu0AGPT3F7ukZ9eAKTdFpUTcwk1N_tgjhrTgJx-h73oRlZhok_uBweFEX4wnvwFbEiSB-GAF0dttAWAIh04oY06vGKDaAdlRtNHkFPh5KePN1hrx3iibr8Dv-cEa-Zihh_dirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fXTMy0qiFsRx8DSuOd0Dr2s0Ouy7ntBexdTs28Qfo6NrzGUp0f1WFyY2mIh868luILl--foMbHXbMUIlw3ry16x-1x_EAXpIfM57f4YERCsN5ZUqD28qm4TMhOfx1tZG-hVVMrDxnSmEavH4LEGr6TxmnA-uDk-awITf53WQ1yP61DCZxs2raOmPw0pve3ltIX8kqVWekbLenlfgjtFZwnVl4htErHyhImHeKk4xN5pm6X4gPrdIZ8IIVKznpc362OylYZ9nne9nTzWaoE-Vs4U8QgSOypP6QTVWNy1WApSs6u_AzGKAHnRk-v7MKLKW5UWXVM4XngOrFJnvuQgi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulYegn_aD3pRMIBPx8BPSMhqXQch5ohC_u7X_NVg2hF3DokAK7pGWZn8g4EALQgpVE_YdzgAVPk_XizG2QcYcm3YZZa_7CSB8bs6y0J9z9jtsjmZSdAXEmF-172wUKkUUR2gIaLkwUvoRzY1wlp48kbXdivZPFyfq-ZuA1pow2-eJdOWI0-y6GNHJ16ilYUHbXtUn8mPWpxYqbPwNw4ZdN-zkDh8MgNiimQ5wOGbXLhBYwjOwy8QVa8NpZvPNmXWY7u8VripSi2i-vEFFww1hjWKJv5MoGj2rRf8LDb7pTdBrXFE2WrAeU4qXJQRElkGWcE6cHgF6AKs9jeWuuJcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PpQfrZPR9p34Ai9u6dwj_g37YuKTk91vXbb5HIwIw88kn5ts7sdNPL1lvzScM8wvefpTSRmDIp2Z7YBk7kv6dtai4a_YUuXgDzW3LJkijSPWOHYPqgSZd4TO5IuZorWlYOkPqJfaWRm0-WL40P3xpOajzg7lXThMcR518Wotc8qAOUYBRe58irQzI2KTSL7gkHQ_Gf_J5fUM7vWKxWpvth4PYqLrsAPS1CydD97cGW2FKrsLIchL0izEmjtDqNKApP_GHpO0j6KQHFktJpoj8l0LRwOz7d4ffxEyGuc2gC9StajHjDEbe1rcUQhe2NYZ8XzcVu23OkemOW21EZf6mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggeUlim7Vlbn4sr6I-CSs7kEDciQONsjT29Vq_Qx1r40mcIVoORfNyxayCWRzxrOZC9TcHMmkPGx2hrK-Ms9AyzSuh_QEb4ltL480iyUutFCxaKAL-18a6eYL1zq4GWLDUqyDlWfpBkyWUBOYkM7WJNkuPsCvOB2lPU2njNkkX86YXVaKgv-0JJk0JHdK0eSCcPXVJmZItd_NxDAkjhoZDnyBrDetfq9HCtTM6PfanCYuSe2gkQasEWQ9txK1BM2y-CXfuJmtMqOSzBgemomOA_SRwZ9xRIAtIgSj476OEUPs-FoKoY5RpWWSHJ15EzyqCU1-BHoXyg9MhTQ6ipyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OoF5o4U1dP5enr8Vy9VKtUly8MjHQ14HN2bDdtDVfjoSL4uejZXMmY_zPJrG3Ui0BE-1bjI3ntKqtItjhP0HIBdUOxhQ8YQtw8hzrVfcPuLAwUftOZlpQ80pZx-hhrJYOtP3x6bucrPxibDmxAxcxzwbEQlSd9LATRdY215zLNNRFSIQ4zzNqGbSftekDxcgIcKNmU2IICSkX2mP-eH6F9r8twppDDY9pO6GLYKPEKcVt6f7oA2ZOVi06_2d2gj45OcNOhZwhDmzqpQDvQXoIGtgJjGuSPpq_zjRfJjcsuGDDCyRHi5F4tL-sh6s0FDn5y7nXlM3Ru10BD74aLYmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNPG6QBwIAjQBiFldVa75OgS6B43ALBVy-Jf9qcg5Vfjc9-yOb6VKEQ2MhalTZOTO6X8ITOwNr29HKZmqnsAkWdEG84KfKpcxoePMLkW_Ev-wqV6Z8I9wJr79Ie8rEaFx1uns3mpVhMwEs01joDM1PH1cGZpmSr-EK97CU_TcOgOOk22ZmygT-Ojl_w7qvzhtYLlKfCAJGi7CEfhEisf_M7qG_-Cczf5SNoQnuoVbmJHnMFUU-iju7BJ03NOomwgnx7UCEr-4ZJq0SV-9GMLWHOqUANv3WbtLRk1NwAEAdcZjUJsyb9s37uKc2uULQsZRtyaQE6C69nPr6IxqgilQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=R04yknzItse9TB3hdXcGjbECUYmsEtNMJok7xcoetf5AhwL3eECZ543N3AtO3gGknqxs3t49hZ3EZuBOgUGWtllOblFIo8ib4xnhSI6XYuJQKJEtzjgFn4LwFdmwrsA_9yOBYGDqUWX6L6_3P4QwkglYDpLYIkd08EkYpdWPLMq5EkAQsexhwgN1PYSTopIU1kWyxPcpjw3gdk_GOxIOBVMuZtjIRD-zn49KbdICBCXRkW5Fygmqip_ucTJir7Aa03mHSiudA4VZc696MajjjgHVqYwiydymhTfHQ1eOSXOi0A0CljPaeh7dEah5MGfyjaaJu8ZBexbsQLTCR5DKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=R04yknzItse9TB3hdXcGjbECUYmsEtNMJok7xcoetf5AhwL3eECZ543N3AtO3gGknqxs3t49hZ3EZuBOgUGWtllOblFIo8ib4xnhSI6XYuJQKJEtzjgFn4LwFdmwrsA_9yOBYGDqUWX6L6_3P4QwkglYDpLYIkd08EkYpdWPLMq5EkAQsexhwgN1PYSTopIU1kWyxPcpjw3gdk_GOxIOBVMuZtjIRD-zn49KbdICBCXRkW5Fygmqip_ucTJir7Aa03mHSiudA4VZc696MajjjgHVqYwiydymhTfHQ1eOSXOi0A0CljPaeh7dEah5MGfyjaaJu8ZBexbsQLTCR5DKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=dOFNTloa-NBtvXTmYV9mtUj2zJouiTDcsXWiY4U6sdjaYN8A31mW8FDytaol6-H5q-jlRclubbFIwnHln8TUFT789vPL4Rjna2Jkvl-vWpR7QPn19PD6fyu6-9DC0rVVzzyxlMb6igyOj9xZ87PMcx45DmgvOqZ8ru79oGpmfJ6s2VC-pDj9kc3rx5JlubcCqF5c3IN8HghvfJE5JR51nc8JynvgCzO3YAh1TkSsXPGBL2gjHM7CG1Kd0J9zlYPeGRbr0RtXbN8BZvdUcXpX-dJMQv3jptVl0A3iWStwsjLw628_QkOS2oMXnq2NNAP0BlsUWEPsj6Z9kAKivETW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=dOFNTloa-NBtvXTmYV9mtUj2zJouiTDcsXWiY4U6sdjaYN8A31mW8FDytaol6-H5q-jlRclubbFIwnHln8TUFT789vPL4Rjna2Jkvl-vWpR7QPn19PD6fyu6-9DC0rVVzzyxlMb6igyOj9xZ87PMcx45DmgvOqZ8ru79oGpmfJ6s2VC-pDj9kc3rx5JlubcCqF5c3IN8HghvfJE5JR51nc8JynvgCzO3YAh1TkSsXPGBL2gjHM7CG1Kd0J9zlYPeGRbr0RtXbN8BZvdUcXpX-dJMQv3jptVl0A3iWStwsjLw628_QkOS2oMXnq2NNAP0BlsUWEPsj6Z9kAKivETW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/M74TU5160TvNX-NuKUVKPFB6pJwXveH2EBL5WFrF9W6gSunXt6P4hg9rLBlmOb5A-jmGTudwzKnVNVL2OodmpE_3W2jSTzJf2f844RAyroFM92Km-IvXWv4LdPUb3lYWCGKYxfbmh9MR5pF__Fa78HjVkbGpLlyvU_UZNQeRrqSih7eGRiFopAxigticdUlkmQD8Yl8-pV9PWwI4DyzhL8SPfYgA5Fp8wBtUkYhW-6Zk4IVqGCRDYyuQ4iXGtPhg2IAoEcMQLShtYjwjMYL46hs7R0Gih8ce503L6298vfZ6wtTNq-agY-LTlpaoyhWtEOodVkY73FjUgPtDVTXjPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuLHN3wZG0jiFhe2lM1rTdooc93YXmXDDDl8JTG7va55tn9YqMzmIEnX2DVuo8zsqH3qHhOmMLw5DJr_w4tNRLjtbt5XjNnHNQWZFmpCjpmRCjZ5HB5PzqGHqUOcrnwuPEVq5pF0XsKT_SMgCD7n0VBZmBBSk5H0x6nI1m2Tt18j47fISVO0O9AUilpSvcHlq70JI8ZAYryV6RaHhc6ZyXOL8Nlc6ZpiOdM8BLdXBjCnNCpw54svOpyDG5vBhOAIiTtKibgzE_uYDjW2XxTX2SHi6tUoquVayYemnm-0a0Gmdbt9jCd9S_Mx2tWCLXQ9Ut0KnLx67EZWFlr2E2xyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahTvj1TBQrIyjRjX2aCo2Fk2iTPUeoUO5CLNgAxC2EjhIoiNQZ0fFx0y13-9t182jTz6gY_XfQ7h-l06LbaCNS2DFthjWejZ4-CrUwXqNg9XpKzR6qCvwFBH_pTOijAm0Ca0qGCo7933ZRo2KvKXQGrpjRoklkQ9vnTuTn-h_VKey22KeTkcYedUgL1h4sCt9NPE2PZusyrjKG4NHohqWyAiPxRRQlgj-cK5PB_G2IQKRqKZfNAzkBbkt94BQs6hLtDEV_xDKJQ6x1IywRhBzwLsiQP0H8vIxNmqx4G1iqybPG-FWTiMQmNu40ZEmM4Vi43maS6Wzdx_JzTLtcNWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=CSTKY90B754I9Sh1D4y3UBIggNzZbeESJFJN-x7nJLDQtBLYQaxPMpqbfal0R9cpOJJVoUO2_wxiQUKT88mMye7k843yPgofuQHPPOthpA0BL5r-bwT7pRydjDre-c-y-c9stkLhzYrnkMJa-pqx1sOXZtPLHzzDJDVbTHkehRUsFxwFLWM0eMEGYI1WDAwBV4Df0jN9-vsQriTLzXymQiMwDuPYzsVIGkt_V1CxgPZkN09kqoJ1QM31_D7wxUwexhrdR-a_ylXCdqTijO6UPJQ7hSgU1FTNJ1zeqSyvmzHfJb_3PJAvAaUYcsAefnak1c1YTcyt9YPgfuniLfxqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=CSTKY90B754I9Sh1D4y3UBIggNzZbeESJFJN-x7nJLDQtBLYQaxPMpqbfal0R9cpOJJVoUO2_wxiQUKT88mMye7k843yPgofuQHPPOthpA0BL5r-bwT7pRydjDre-c-y-c9stkLhzYrnkMJa-pqx1sOXZtPLHzzDJDVbTHkehRUsFxwFLWM0eMEGYI1WDAwBV4Df0jN9-vsQriTLzXymQiMwDuPYzsVIGkt_V1CxgPZkN09kqoJ1QM31_D7wxUwexhrdR-a_ylXCdqTijO6UPJQ7hSgU1FTNJ1zeqSyvmzHfJb_3PJAvAaUYcsAefnak1c1YTcyt9YPgfuniLfxqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5HxRZ8P5J54vGsNksmCI_dZ6vzOh5g3DnrUioFz3f900oFSWAlArBKDzmGz2OoJRiDLkzlqq-HXnrCDKMVWRvk8G4MyhqC24_73rm9qxwAF5n91_WzIcJaeUmnWd6uMhNhF6DcIfczvPG-WyBRI2teqDMmbg065GzqNRKT1hK6Z-eI3N1MOcysQHWEVMQ0_eh0db7ddvbBZA7ilx5P0Ju91KLOug95nxIL0B4d3hBpMHvdqkNAhrdh95w6b82KONeYhahU_ucmX-bwU3OqZiQLaL28U3jx7oZprua1_6rL8YqnhXtZRNxDm4qxjTBmNelXHXx8ALSF-25zBRRSGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGrrh3q7Gl4ZQ6FEOfLi5QRThuL0-sWa0-6IIboR1fb2qh5SR7mJagr8Pb-7aac-EgOxKL7nq3gGPUHeiU8boV30p-ZiZEYyPE8hF46elE9tR862mAR_6oG0q3BFLIum7ZxdkCLK4pX9uoMU9ws9a01xtuv-KYEKD2cVudquqqPS05LaxmmYrVNR2QhRpSHBArX5sWu7Jtyy0N_hIJV_IAcMRzrRAqHorCMun-lb91VD8i1-aMsZJIOWcYRDrWenb63CZnCJfukkmZodtqJIUh01lkI8DBWRDoSu8sNSqa_LNyTIGVO4SNlTAwgaPlt563X2vsG7qqnaE0dPVEOL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCdGLXjtlvV0XzCR1lQdtjmEA8VuWC9Ly2Kri0nYLtfK26ZHT8td1cidbb6EMqcr8a3oHUKNHpqgqAz0OchP_V_K6Ydfx0paC2sC1f8WqbkxsFvpT0glVynNXXV2t28TEG1Rq_G1xbg9divwpjZi5I4UShVWD7rLmAgKDF4CzQ9PHEIuZ7ezI1RWusiH8pFIZEyWH3UU-tp_8Yx0bN0-WeWenUxO2WJCdqHwDkirmiwjfdPyGqJzPKjECk-CDJ6tcKBwVFskeTM3UhYM7kUKHuM7O4pN5NUwtKeyATH3pbwcAlzuG5iWB4vtrwaQm9riu3Lw5vMdrrW5fqvNjYOERA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLvC1bOdfrTEz84fkFpTiFdah49WkiKKCZsPA-fSdURT3EtrMfAa1Mm6Gf1lOeucyNqoerK1nIdy2o0nK9P75tn7Cs8ipF1NW0cPhZNiwgb1JFCHILh9ZyFkxhEX23_xY3qjHF8uw7sFqR8PN8h8o_UiBxEfQNNVmW0lWsy9g6SCYFfty2Br43NyQuwcKqOoKyegu_ncSFhQym4hjyK2PN5aibmerrdloBTKHryOlFJ-i0QOQ-E6FCodTEZKvIOOU9Weyjn5xVg-9bmE9crPJkrfaLXrQfPf0EFNNJ3n2I4VCYpnBuv3hnhocA4bXDddf-BJtqjn_1Q3_bwN5DSXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=m_mL9KhbhoXsR1x4nBumyAZGUHs6PtRtLMTVhGBwhWbTuuNhVFrVcQrL7EAPCx6TICIqpA9eniwyY3LRS4ZSRNwBx9X9il5L5FoNKkjM4xB4Ef08N8IgARWnmA7DMSLMAWDYBVK3JIvLwnJifxC3bizsfQNz-zprIgLu-jknWO0qk4xIB9YouleDK-5ozx9cUuBzkjajgwhw0XznLS88Us8eElFM2FWKhWsj7F-RIAaTD6B2C2GNToT8LeY7KtjlhoJbIZVQp71O1mVaJXulwu3FwnE3_2C8EY-XnmiGSR0OA0XBM2rYfm9ymaWY81mh7SJS6IlUv5rQIubkK9Tagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=m_mL9KhbhoXsR1x4nBumyAZGUHs6PtRtLMTVhGBwhWbTuuNhVFrVcQrL7EAPCx6TICIqpA9eniwyY3LRS4ZSRNwBx9X9il5L5FoNKkjM4xB4Ef08N8IgARWnmA7DMSLMAWDYBVK3JIvLwnJifxC3bizsfQNz-zprIgLu-jknWO0qk4xIB9YouleDK-5ozx9cUuBzkjajgwhw0XznLS88Us8eElFM2FWKhWsj7F-RIAaTD6B2C2GNToT8LeY7KtjlhoJbIZVQp71O1mVaJXulwu3FwnE3_2C8EY-XnmiGSR0OA0XBM2rYfm9ymaWY81mh7SJS6IlUv5rQIubkK9Tagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0sThUUnv2R7NNiimSqkhvappFevgR1mmUxiuDmYzRAzHs-5o8YDpv1J4iLaxeFua_iLf7p1GiusZcJdJZczjGWsRnUMCncN-QEAXPC4S128RcGpmYPYn_P7Iz3PxlDOGAqMA0P27WbqPVYCdPGoqLEVN23K__B43N5aCsjolWXfHU1GBiME8PnPwkI7eQrUfZ2UHg91dYIpzm49_gvAfxJXbLoxJow3M4uyz4nv5H83iMwocVGxV676c5j694_UUtPVNcJ4LcKV5Dymkl2QMOKCN6zcg06pv1sdkfd-3eD-Cd73MizFXSsSpNidiCmTnlDfY-HinGWKkdKmQD3w5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

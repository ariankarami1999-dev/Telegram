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
<img src="https://cdn4.telesco.pe/file/kSSYCMxRQ3ZabGWMtc8p1Rp023JJtPm5kAYcFjrM9zVT4SNACixkbA8cdT66mQUl8UzwYU3Yl_VqRYa4UOO-PDssssI3tJNoAA020W5ucMEWtF7GIpQreeoqVJgzfsqyYbuLF4ziGCfXo7xxBUN7Ff-xuuu1gGB5KFa_YP7K1pewm4WbRJCiCWRmKOeG0sxqGo9cqqPBVqCrLwEGfL_Mo5mT_0zYjj81ndUiW6M497nJmFq5O7h3G8NPhWB45e9xKj745-t3NUhMVSehJ-Y100deKGTZOIx5SB2hQVpToM23XjDeMNTyUrr1_EqDVjGzkSeM39Y7G9Wl038qciBeAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=sVVTgW1HL4mRT7fz0ULBirjtRSpmGJtFHBStw9ntYedA9Bhsd7NCqsfr1Om_eyXMRwCY0WsUXhQFBiDkKRcKsKuvXF-JQQQvezhLAy5Mo4tGwfF33lqLJtJ5ZvzVdwiJ-kxcHQY2i8OQkti2mGzqnz7Thoxha4URJVgzXunLEf7b5nVVjmMrvH7qu5UGc-B1TffGYxzg7hEvGPwowN7_PmtQ5PHOquYtVswIJGi52t-tYFTN9WBAy4zcI_E3bPdkNqi8pG5M4lokQ5Q3x8VbBRZyBLHFI8E5EjF5mt94ppNxnUCsXFVnkis5T_CHTUreB3umPq-dt0ogUiyDnCbugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=sVVTgW1HL4mRT7fz0ULBirjtRSpmGJtFHBStw9ntYedA9Bhsd7NCqsfr1Om_eyXMRwCY0WsUXhQFBiDkKRcKsKuvXF-JQQQvezhLAy5Mo4tGwfF33lqLJtJ5ZvzVdwiJ-kxcHQY2i8OQkti2mGzqnz7Thoxha4URJVgzXunLEf7b5nVVjmMrvH7qu5UGc-B1TffGYxzg7hEvGPwowN7_PmtQ5PHOquYtVswIJGi52t-tYFTN9WBAy4zcI_E3bPdkNqi8pG5M4lokQ5Q3x8VbBRZyBLHFI8E5EjF5mt94ppNxnUCsXFVnkis5T_CHTUreB3umPq-dt0ogUiyDnCbugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=YPebOmA3jsPGu-0XWWPsTxMWEzIEUKo371h7xOnAXEk3vCIwhnBNdN9zYieK5mfTbms1nZ7ESR4CZuvThcmk15H9vTBUBhmcbXqWSA3RRWWLS0NgwbUOolFoh4RvpAlqMzVb0rtGWQqGDHSfiDanRPE8WL7agyKp3mmTwiuRp40HbwepbMYhYa1A6kthYfTSEGvlXvaF2TwXVMPARu0P9TjE-AZiZ9kdKWsrK9tReO8R1q1403buYpqQIxVABT_qZSMRNn_cpVhnIOu9e4PffohqLgy3845OCXYyTtKC_QzSKsYIrnKwcSdOf46BNW0lNX1e_2Ui80khJltxeiVNJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=YPebOmA3jsPGu-0XWWPsTxMWEzIEUKo371h7xOnAXEk3vCIwhnBNdN9zYieK5mfTbms1nZ7ESR4CZuvThcmk15H9vTBUBhmcbXqWSA3RRWWLS0NgwbUOolFoh4RvpAlqMzVb0rtGWQqGDHSfiDanRPE8WL7agyKp3mmTwiuRp40HbwepbMYhYa1A6kthYfTSEGvlXvaF2TwXVMPARu0P9TjE-AZiZ9kdKWsrK9tReO8R1q1403buYpqQIxVABT_qZSMRNn_cpVhnIOu9e4PffohqLgy3845OCXYyTtKC_QzSKsYIrnKwcSdOf46BNW0lNX1e_2Ui80khJltxeiVNJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=J0dw_f_5bYZgvLKqgb_qYD5nZl_8Xvizc3YmythrX01loNq9bc2y4_TPQxvjt3vT9H5r9zY9LOJDRCVZbtCkzRmLfekA0MnpirIV9oAXlTDwPKKjy9BsVY3GyJZoQ2I9r9ObAnfipbi9CDDyt8xY8Q33bqj4F_1zQpy5QMWBStBLfE2VN9HzZXfI0HCC7b-TzT1tUw1GKm_WFrW72EXCq31U9wt2iV6DBfXiT0RNDe_Ks5cOUH7KVOl-p696NFjZnx_9lryjjlnu_XfSw0ydHpeBtBWMEZgjPBlSHAir2W64ns8o96WX7ta--4pEfiL86Wt46GZ8EFjlsBWIHO_zDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=J0dw_f_5bYZgvLKqgb_qYD5nZl_8Xvizc3YmythrX01loNq9bc2y4_TPQxvjt3vT9H5r9zY9LOJDRCVZbtCkzRmLfekA0MnpirIV9oAXlTDwPKKjy9BsVY3GyJZoQ2I9r9ObAnfipbi9CDDyt8xY8Q33bqj4F_1zQpy5QMWBStBLfE2VN9HzZXfI0HCC7b-TzT1tUw1GKm_WFrW72EXCq31U9wt2iV6DBfXiT0RNDe_Ks5cOUH7KVOl-p696NFjZnx_9lryjjlnu_XfSw0ydHpeBtBWMEZgjPBlSHAir2W64ns8o96WX7ta--4pEfiL86Wt46GZ8EFjlsBWIHO_zDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=bSJvrpXSTK0XrcandeCArcG1oo00CkAPfXPtHVAcRNo_h7I-StogSEhzH1E7g8qHAbyKB3lrHzeUPF1fI5Q6COtlvecwLX6aQQwboscrPWsFPiPh6MZrzL_iVXeJ0vUE8x-YHJyR-1_vW5T0RFmAVupK29a9R1OYcPvQfBg2pI9BPwmeZDGKaOzvW7BCgVl-1yx18pS1KvYn14sLFI7l8g7iRzb-AetsdHo014K1y_LHJzlP71aJqZP6y4d9M_vibxes4laIzaBJjObtRq6K1FVZGsC118vuRpymJgxzMjjrfaGXR1GQ4jcaenugmX7zJ9TcQBShnT1ipsDOzDNSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=bSJvrpXSTK0XrcandeCArcG1oo00CkAPfXPtHVAcRNo_h7I-StogSEhzH1E7g8qHAbyKB3lrHzeUPF1fI5Q6COtlvecwLX6aQQwboscrPWsFPiPh6MZrzL_iVXeJ0vUE8x-YHJyR-1_vW5T0RFmAVupK29a9R1OYcPvQfBg2pI9BPwmeZDGKaOzvW7BCgVl-1yx18pS1KvYn14sLFI7l8g7iRzb-AetsdHo014K1y_LHJzlP71aJqZP6y4d9M_vibxes4laIzaBJjObtRq6K1FVZGsC118vuRpymJgxzMjjrfaGXR1GQ4jcaenugmX7zJ9TcQBShnT1ipsDOzDNSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66166">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود.
@News_Hut</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/news_hut/66166" target="_blank">📅 17:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ub1mZ0cqtVMopH2_CUjPKI4HAEogGZxpcHPrVdIr2ElkIRnWF7jQtlxzmZPJzzSPr4FEPQVQvHV4SI8uYCpoYiSdOTLjHKNbmYjGMc6GuIXKOZGPCF5IInxd3LSHFY2n9Vv3INRCx1JiY20I4tSUz1a32aT6aDJER_ZavQNx_e75lDkIbJfT7j91D-tehHViwklDpxmszGzVI36vX7BgOoVAWKNXDnOiScOt-FF6xao1QGnhpQ1mKikIuD7f03akTnXV6kfgtS4CvhKX9aWBnIMIxJXX5vVIGwObzDjzlN_tE_whOJmuaZBniRmXZ-84o_WVVx7V_JzgdytYQyHWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/news_hut/66165" target="_blank">📅 17:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66164">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MABrT9wUWvNiLxpuyiN1iCfpqfInefS3ddYUiXI92MlJpHHob400AY-amXIPZS5RfDY0wH9ZJaMkfnZp8oVilMVl_gC0xcgYMt0ZfDXUjvskdUzWfs7cvYZMzbOWfUTDb8jsqhE-E7zwZhKxyyptm0BX1A7MMWXTdoLsV12HI_taXPREsBPVhAKYbX0auiqTytQTfBsC48zuAWX0NN5sol7Q2D4dKXmfOlfHOWNYyCR2noOQOTPjioFRtC2jVfP4L0ziqkRy8xtu48VK_KKrkH-yjQpC_OU9tpuG8MgdvQmVbAdBIPVgQIQRU6d9BazVGICyEoTlfVpqS0B0MNv0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ در تروث سوشال :
پس از توافق تاریخی حاصل شده با ایران در آخر هفته، کشتی‌ها شروع به خروج از تنگه هرمز کرده‌اند، که بسیاری از آنها «پر از نفت» هستند
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/66164" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66163">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
صداوسیما:
تنگه هرمز تا اطلاع ثانوی بسته است و سپاه بیش از ۹۶ساعت هستش که اجازه عبور به هیچ شناوری رو نداده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66163" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66162">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=tz_UMxixm14Nwdxy-5xElOg_-fVIGYYUPoo0gqp_6ntuWjPnzKr0OOHI7O-FM7gHXaf6WoONv3l4-wuQqvw4dnyJ55C0vhOGwDrGAZeoLeDLyogCzucSwtivoVaAOvbJgCEYt-olZbZeBdoiT29rfcIc0vBeJTG9Qdld4MAA0MfDhj-p6W0JhSnJnne-RKgHlh4qj7a4ZCFQE_FiQWS8CVLrWrvxOYnycS6wC3fSgQJe3byAXVacHhrb-wOgDAkGAN60t78iTOanZKrD-lGh5ZtKQidRcS5d__iq6IS1RuEtiyW2kysiWn5jpLRWwtG9eml34NbloeV9Ozm2de_etw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=tz_UMxixm14Nwdxy-5xElOg_-fVIGYYUPoo0gqp_6ntuWjPnzKr0OOHI7O-FM7gHXaf6WoONv3l4-wuQqvw4dnyJ55C0vhOGwDrGAZeoLeDLyogCzucSwtivoVaAOvbJgCEYt-olZbZeBdoiT29rfcIc0vBeJTG9Qdld4MAA0MfDhj-p6W0JhSnJnne-RKgHlh4qj7a4ZCFQE_FiQWS8CVLrWrvxOYnycS6wC3fSgQJe3byAXVacHhrb-wOgDAkGAN60t78iTOanZKrD-lGh5ZtKQidRcS5d__iq6IS1RuEtiyW2kysiWn5jpLRWwtG9eml34NbloeV9Ozm2de_etw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممدباقر۲۰بهمن۱۴۰۳:
با قاتلین قاسم سلیمانی مذاکره نمیکنیم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66162" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66161">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=r14udfnmicc4Nnvxy1QCaiQ8uxw8ohrHuX2QnlInpGp56y1wRpzP7uEnMrlzZ6id0WoGMb-kNsItPoHY4N2kijASiFXQ6lJ399BdHVhQrJ9xZj0cqE_5vzugxiX0kBaadbFZcs6HI4R5HTamYclVBT4uJppY9UDIqZGdnkgX3Ur2YtZ8MHg-3_UGZRHm50JSvbGd4xvCfhxJmEK8Bcs-fm5LxDqBAqcFUnR0yfbBDCuqgs_jkbEh1OJPoIfVhDM6QHrtnJBn6hldSAx1bFbJ2R8nEPaTACke_-XvSDMz11HZXoYmb5Rj_46npZ46QvCsba-1Hh6FnBSf9k8zTVzuIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=r14udfnmicc4Nnvxy1QCaiQ8uxw8ohrHuX2QnlInpGp56y1wRpzP7uEnMrlzZ6id0WoGMb-kNsItPoHY4N2kijASiFXQ6lJ399BdHVhQrJ9xZj0cqE_5vzugxiX0kBaadbFZcs6HI4R5HTamYclVBT4uJppY9UDIqZGdnkgX3Ur2YtZ8MHg-3_UGZRHm50JSvbGd4xvCfhxJmEK8Bcs-fm5LxDqBAqcFUnR0yfbBDCuqgs_jkbEh1OJPoIfVhDM6QHrtnJBn6hldSAx1bFbJ2R8nEPaTACke_-XvSDMz11HZXoYmb5Rj_46npZ46QvCsba-1Hh6FnBSf9k8zTVzuIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله پزشکیان به منتقدان و اراذل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66161" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66160">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvRL3GmaiipcS9SosFZY8HfzAOGEzTfpT2oIUWNczi9rfxMAhWIP4_Uu1yUmoh6-zFDVe_0hNHCh6E57chwd8Bu3IfSsuMSTCrq8UNNYj50mJXEc-NK2gFCRzTgvoN19nlgDtLHMd7EZ8P2UW-31tCqSor01lr64V0MRUhL7gSt3BBUMEQoaWyskWdM2OHMXLwHt7ayie-Rn4RivjynaH2VvujqgOGKFD1l_x10jIK-0b2OyStISHY-LwCP59uM_wgSkC8NDydUmTfbJUUJU5FWT6Op90QLztxvfuSiVOe4hTj8jnbDu3a_YFifJXYVTzEf3nBpHHJcynIn5RgTWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابوالفضل ابوترابی، نماینده مجلس:
استیضاح مسعود پزشکیان مطرح نیست، شاید خدا شهیدش کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66160" target="_blank">📅 15:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=sCcro5m33VzU5YjN9Ha9xX9Qjx5o9oxZXlbcrA37Ai8plMiDwymmGGrLf4UMqOPHZ46sZ7EcKe1iZeNpDsySD4IXP2iJBvA5RFjY-0VkYsYLDTt_9pUikLLivR1EqjgbCjf0XeaWToXjAEq1jeZQPCUYqVpCfjPfzNLJK_4LljFmFZ1B-R68kN_rOAc5vzGx11yDUxAvk9wCPmG8n5b_caYjkr11XdwaRK73iiG3SKnoMxYmZ7f42Z2aj-FaD3KhTzPO1UYh0BxU5jMdX-aqCZXPWkyPsiUkRrrxSGK8U5ZreGbZPJF3YEf95_z425Fgcqtf69euJfTdWSp17DbUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=sCcro5m33VzU5YjN9Ha9xX9Qjx5o9oxZXlbcrA37Ai8plMiDwymmGGrLf4UMqOPHZ46sZ7EcKe1iZeNpDsySD4IXP2iJBvA5RFjY-0VkYsYLDTt_9pUikLLivR1EqjgbCjf0XeaWToXjAEq1jeZQPCUYqVpCfjPfzNLJK_4LljFmFZ1B-R68kN_rOAc5vzGx11yDUxAvk9wCPmG8n5b_caYjkr11XdwaRK73iiG3SKnoMxYmZ7f42Z2aj-FaD3KhTzPO1UYh0BxU5jMdX-aqCZXPWkyPsiUkRrrxSGK8U5ZreGbZPJF3YEf95_z425Fgcqtf69euJfTdWSp17DbUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ برای شرکت در اجلاس گروه هفت به فرانسه سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66159" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cp6UxIrg4z2CtfSamIKRpiFs960Sn3CQKCJi7z2sOUH3CHsXNt4ysiOp251PNlamGCwEDdM4IMSzjoeIPvgay0kQojpZm_waAL7pF2I2k1M16-RP63pbR_8TAYU1192uVkWQEip04w4QAn358MVUAdHtzPnW2wC5AuS6F5Fs1sKQiMGZvFr25SgCfIgppNuEgjzZ2FmpMw_eEoroGXKVJXot4pz6fcIVMbKRuNOxd1_7hT6SQEzhtDXMADecpvAxjBZcCrh7dFB5kSWwUosOTkDeE5RKpddGNM677TYOFnLtsopdZYQwvsqMN6f6giBM606a-3oWiJ4jpvcxjz0Baw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید حساب اسرائیل به فارسی:
یک سال پیش در چنین روزی جمهوری اسلامی با ساقط کردن چند فروند F35خلبانان اسرائیلی را به اسارت گرفت و ما همچنان در انتظار پخش اعترافات آنها در صداوسیما هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66158" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=uKKezdXWoaMftVBmN_g2ocAvejdrdFenKigZkLHItDk2l7-fHg14pf3Vlb_uoeBXCylactK6q6gN0whjYBYYCMafGn2Pm03WLivrWnRHtYzNuYTCjEgCeJbWIpLPDomFFR0oUBYGK6Vq5ENF8oP5whBKXF158L47mGxUvyFdNAdqp4lv7BUPoEYfMbmJjDL_z_psN68716Wf40CjwHl61s0vdqtT5rhH0HeekKQ-iFN5WSWfjKH9_rdJ4L6cLWi08O78p5MB1ltSjyZqq8xO0sUiWMvlKOqfPDM6VehnjaE9tXpowVt7z2YAuiWm7PpsAxcSahwvmZVbiwARfQhwkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=uKKezdXWoaMftVBmN_g2ocAvejdrdFenKigZkLHItDk2l7-fHg14pf3Vlb_uoeBXCylactK6q6gN0whjYBYYCMafGn2Pm03WLivrWnRHtYzNuYTCjEgCeJbWIpLPDomFFR0oUBYGK6Vq5ENF8oP5whBKXF158L47mGxUvyFdNAdqp4lv7BUPoEYfMbmJjDL_z_psN68716Wf40CjwHl61s0vdqtT5rhH0HeekKQ-iFN5WSWfjKH9_rdJ4L6cLWi08O78p5MB1ltSjyZqq8xO0sUiWMvlKOqfPDM6VehnjaE9tXpowVt7z2YAuiWm7PpsAxcSahwvmZVbiwARfQhwkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت«
ال ریسیتاس
» بازیگر اسپانیایی از اتفاقات جنگ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66157" target="_blank">📅 13:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=E-xUnCgNQSeqdaidKQaGQP8sLnS-SvqGdhC47MMxu_lXJAd3sBg8tlM4NOfgMDr-1VtXJiG_T1fq2kWuzJ7kMnLYLSDlFgXOrQnaol2i1h__Z8Jtz_ghnBJ942JRRRo0vY9IWW9ieWCReXNkxALX3Qr2tsvRnSEbICnfkGjUnMSUzXELa8VsscLWrhY4bWTy460JtEcuuJB-Jyxx3xyp-JHyZJtxH3pQWEQUKZu74Y3nv9DIqF5VdF1_bC7Z0bhUzbIQvKdpfCbpCiQClk8En8dxJrWPSyfainKC0DaoqzmoOZS_GRU5B6SSb2rwCOQozURetI8bk_daVwyQXS0-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=E-xUnCgNQSeqdaidKQaGQP8sLnS-SvqGdhC47MMxu_lXJAd3sBg8tlM4NOfgMDr-1VtXJiG_T1fq2kWuzJ7kMnLYLSDlFgXOrQnaol2i1h__Z8Jtz_ghnBJ942JRRRo0vY9IWW9ieWCReXNkxALX3Qr2tsvRnSEbICnfkGjUnMSUzXELa8VsscLWrhY4bWTy460JtEcuuJB-Jyxx3xyp-JHyZJtxH3pQWEQUKZu74Y3nv9DIqF5VdF1_bC7Z0bhUzbIQvKdpfCbpCiQClk8En8dxJrWPSyfainKC0DaoqzmoOZS_GRU5B6SSb2rwCOQozURetI8bk_daVwyQXS0-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حمله اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66156" target="_blank">📅 13:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skd7v1zR9cW2Xi2SWOjpuvUHtYiUGNsVhs3upGzqKLT8AThneQODynrwmwlYPotGk243xbAKsyDvlKflsibFID49xlqr0hgB6xOUbaaIcagGwlQP63P0AL6e1Bx-DQKAZGAdL5UgukeSo9IxkWDkKgS_91UGgK9uJSb8Nk-vXANnUUZu94YVQ_glAEPXcE9uad1-_oOofYcI1vnv3l2Nvw-jngkhincwEheXsk-ASo8bFunQ4Op4J_vCnTeBFbaIAq0Nn2A_4V_I7JCvt5hgzIXRoqyFUFx-ecu_70FGH1nfQOI3SHNvoOUGEI7ASJoAJ-wsjcgnVB4hDDwnUdbpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیس پزشکیان به تندروها:
متأسفم که به کسانی که دارن با مأموریت قانونی برای حفظ منافع و عزت کشور کار می‌کنن، برچسب خیانت و وطن‌فروشی می‌زنن. انتقاد کردن حق همه‌ست، ولی تخریب و له کردن این آدما کار مردونه و عادلانه‌ای نیست.
دولت باید از نیروهای خط مقدم که جونشون رو برای امنیت مردم کف دست گذاشتن کامل حمایت کنه. نمی‌شه ازشون انتظار فداکاری داشت ولی امکانات و نیازهاشون رو فراموش کرد.
ما جلوی هیچ قدرتی سر خم نمی‌کنیم، اما در برابر همهٔ مردم ایران و خواسته‌های درستشون پاسخگو و مسئول هستیم؛ نه فقط یه گروه خاص.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66155" target="_blank">📅 13:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66153">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8OTKe4xKbSQNAF2rDFce2edS9S7ON2LwYnjflkT_nBrqFLYnNSbwS-9xuOAe4WZGOzAAd_-CHq9t6UHqlQod-64A5pCXyNiG2PtQcbawPOK0hBcsDHjo5hqJgdKdnMOoZ61myoP3Zis-k1CvaHBMxfLXaUcrQbPxBFG-n1xVrutcoDyEmg1YreOrmteXRIfkdLlEYNuWwlqTulY7KC3UNX9n1IPutNtzgx73G4yrC7HSiO2FtvqZgYO70VKPmtQLZONBo6Ot4o1WBXjMDKOAusG58GQB7TPDuZg95c9MPUyZ2YjiwP-edhx2HhwPd4Nxe8OTCGcfKy5-raqNX9-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/td4b2xUlHcvH3eEz1-US7_KTonP36-13i-cF5Ej_u7L08EGqycv4-Tjy1tIq1cI9UI2BHIcQQYS-incs0DBj6EbNtJEOr0ZqaxBjGZQzoljZBQb2QM0kWkUe-ZM8Tatk5P_mSlc4-XbJNGcPwA92HWzSvifO8Kmqh3R7dWSy3Lgr2yUehCYXQq9Qjyu5TQvUBRbDbSz3rjuEHcbOjGSyItaqcL-WQ8gJlzUycEv_uSu0iIESLjQWiHVkxFU4Y6oqnz3eV4_gcSGFtJyBp6GgIE4cQx83dxrSuspl_7tQJdVrMSJ9LcAGDAaAqTOiM3GSwjBKgS3YaZgd8-724DR-fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حمله هوایی ارتش اسرائیل به الخیام جنوب لبنان!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66153" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66152">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66152" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i61XjR0DGQi9zag7_egWdBc14G12aLynyUFqxBHBWcoJcle-E6Ap2AC78_VkGbOOuPx2M9lBXRvTePKjScvhmyj_gjd5ko4gXu92J4_-zy8lAW-C0xp2xgKtUl9E5jlKGCL7zYx2jkIY5__a_NWrqaaMmHkvzdFvoX1enNhkGYo_O19ZtiC0nCcI4bXhWfbKG6W6SiwpQsmiRV2cMogTAeFw9IYPPzYvf2OJuyCWlyRHHOOMeK2fC_r1rAIhCkxBYFOydCaNhYO3ZqnUo40IaTO2kkC8S0I1nzJCs-uy5bMp0vzrZkT1EnjW8xzlJM4cZsYVJ5XVI0JB-mZDwRomgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66151" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH3bUHNs2j99SpQvtbERZlIR8P1yrGVubLZVosYqt-ZBkJ9CbS14s91Ct3ebB6Ty0Er8o-SCzOw2zap8LJ3rEXFap7fgoImvW-ICvBQZsHO2mXFTpkHVQJx3GliZAzZmw9IHS9oK6FMoPA9EOq4teggSQWHb65yLsbVcPvz4IvZGiwDTIdcUHCjQ4cpYoF8iPb6VRkY8g8GcVkJ04fMEOg8u7iUFifGowb132GHIqOur1bTe0jDnQq-3T5ASqDyDtkqKNflqiYThlzrK2nWhA72HM5QCjCo4ce8WFC_kF5cNfEC0QUqCbhGw0srvnhuC_PQ8eECxtFzgGdL92g5h9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیده شده در تجمعات
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66150" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APN6xYnnCSigNhzZ1uhDT2ertdmqJOxR-vCvNUxohKPhuXWxGVLj0n2NXDgB-dfUiZZ-tLFoPoyEILVW6D0MhGaYyU15H5QZpNAIZSZmtfgjs4TA6jFIv4HzPUURY2tSzkhJXPXd5yCJoxFj8GsVT11I1Mug_t_VDM1ZmGJgNUvsonhLkE1Vuojj_SNU-gqhvhwkVBWCyLSeK71gUEN2ezKvoYS_ExIz7WB617XSRrSkW_2ZY6A27Kh6wW0CyF_lMLw4hr0dFtX8xB07QAOr6ZnnrdscVD9V-_R3nOTYPHxMWt34dUhYfd2HqbSToiFp1QztVu7Kgzru47vtL0I7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66148">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=FnTXZBvdHtK5eP3IRamk4mQDIdcyT9yL06kNfZX6pYCW_n-O2bJxmX7WER8irZBHfYa-ST-Ez1_TE9xW4vYG5njO7sVwpWZoawVVVRXanHtkfhli8EPDmIEYeAklwwdzyxi0ise9zbNwie1ctP950N58hx5HRbVXg2s1f-gHx0GztGW_k7Kwkys0TPTIlEcsYHq1sWpD-kqQdxknbaLiDEQLBgtb9uQMl-PLD4aue8DvcQmKA3pxdxjtric0Urw1VWPOz7phHB6N6mfs42dzqikBD2vE0PmRxz377YRkAkqufc9zrPw639u7pbWppnAyZ6pLQXXPfeVHpSnQXnQUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24ffc7435.mp4?token=FnTXZBvdHtK5eP3IRamk4mQDIdcyT9yL06kNfZX6pYCW_n-O2bJxmX7WER8irZBHfYa-ST-Ez1_TE9xW4vYG5njO7sVwpWZoawVVVRXanHtkfhli8EPDmIEYeAklwwdzyxi0ise9zbNwie1ctP950N58hx5HRbVXg2s1f-gHx0GztGW_k7Kwkys0TPTIlEcsYHq1sWpD-kqQdxknbaLiDEQLBgtb9uQMl-PLD4aue8DvcQmKA3pxdxjtric0Urw1VWPOz7phHB6N6mfs42dzqikBD2vE0PmRxz377YRkAkqufc9zrPw639u7pbWppnAyZ6pLQXXPfeVHpSnQXnQUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان مقیم آمریکا طبق درخواست قلعه‌نویی واسه حمایت از تیم ملی ریختن جلوی هتل
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66148" target="_blank">📅 11:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66147">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzx4IG2GzlLe_3XpiR1NND13DCPQQOp34jXE9FQJ6Jo58GJAuOVPupsGYv2B-BzV1CtD29q6QHkbxAkCLhtynYa7_H2cGfaZjWkmwKnlATfvWrtHQG-fBs3upRqQNA5zgdqmyk-14I6pQXjTmPTBc-l-Wv264oy5okgRmniIDvTJNXW-RgbLIg_3tWS2DrMz4mPDGPsB_pWHfanNOmDyCUvFl4VqjAbu2zfBMSAtdy-fQFJjEMoSD-4FkXv75J2KVkPuORK3fGKyyNNV2KFXIeGwjtkIeIIHokBUJlOCKgJkH749UvLRru5w3FH1i9I5wyYgCDDkLhndHB7SFrbOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت عرزشیا هم اکنون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66147" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66146">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoXGUbIg7VkMNZjsQ5F2Dd3_YynIUTnMyhovAoKrPea4tmt3ot7tElzwvbGw-iGWq144KzeVR_8XSPZxuJr39yyTDlhFL49lLYmkG-JKZJr7_dwzMqEA5MM6w7duD4Gyugv0Sb-wH-XnYXEGWKVVePUZdZmr3TlXYRKL97_NjApDFm9QEEnVgbFv169TAHGmFU_keGZfkrrBjia3DInCfB8umDmGTMqI5oJLm4am1Yyaqpt2pWp_zsWEZk8RvCcgSwCyJ2xVGTbriZOGoscv5NiaNTEVe2Pi9qBjLGjH_swBkbSvfxW0Zm4dl1vAjYjg_DFh1cEzP09UAZFzbnQj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عایشه قذافی دختر معمر قذافی در کتابش:
به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66146" target="_blank">📅 10:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66145">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccd116404.mp4?token=IS0-E60OF__xUhQz2RIj6Si0e5gvx0cFc2syTtGS9f-QjEPPXfHBfzPGtNlkHsRfoIDlG608oCj8ANJ9D5bf-sre_iY8DG2mBJ6u83wriYiLTi9Q5WSaEuyFX48A-pMbsZ1fXS7uhVZvVb5Bo2nnEo7RmuqToQS8EbLF0EVOk4n_FH5caXXsBTKNRcfPuro2NQ9R_6ADPpjNaWFXUfKgPKV_oMGgYvjilG_lV87O_cA9efXN3IQlb60gSbsPM30xjKSaaidQOvxL5Q684N-uG7uuvyME3zF-641xtcyiG2VqonkTw7xAikQbtBiriN27CuXGtZw6CLecb22iTBq_Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccd116404.mp4?token=IS0-E60OF__xUhQz2RIj6Si0e5gvx0cFc2syTtGS9f-QjEPPXfHBfzPGtNlkHsRfoIDlG608oCj8ANJ9D5bf-sre_iY8DG2mBJ6u83wriYiLTi9Q5WSaEuyFX48A-pMbsZ1fXS7uhVZvVb5Bo2nnEo7RmuqToQS8EbLF0EVOk4n_FH5caXXsBTKNRcfPuro2NQ9R_6ADPpjNaWFXUfKgPKV_oMGgYvjilG_lV87O_cA9efXN3IQlb60gSbsPM30xjKSaaidQOvxL5Q684N-uG7uuvyME3zF-641xtcyiG2VqonkTw7xAikQbtBiriN27CuXGtZw6CLecb22iTBq_Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس معاون ترامپ:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66145" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66144">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=QaqkYP6D3pSMge0TQTBc4aXWhhUhEzAD3Mggw_lUlfjA6HLWjOP8xKLII6O3zSO3OHj4mCAeUemcfE-oWB6JAcDBrqdCLNM_guDAEK-fbMCok32Viohg3jWK2Yjdkl-6qOgL9IEE06XHs2fizxx2orl99EVl-nowUGNf9jbjBBLk0Qykoo01NfbAXVhXJWGp-MLquzr743X3PyvB9kYXV-WbjVbUY3dFuhWjx947qICm9S_5_b5BBPA34XSKn5WDoZid8RE--ckKOhEBad2rvNAFPFh-QrypEp35JaRNN6oEo0Gh6H6R7eF5ZJMGcMtBD-GE_zcfiTA_vdWZelsvVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4991d46b.mp4?token=QaqkYP6D3pSMge0TQTBc4aXWhhUhEzAD3Mggw_lUlfjA6HLWjOP8xKLII6O3zSO3OHj4mCAeUemcfE-oWB6JAcDBrqdCLNM_guDAEK-fbMCok32Viohg3jWK2Yjdkl-6qOgL9IEE06XHs2fizxx2orl99EVl-nowUGNf9jbjBBLk0Qykoo01NfbAXVhXJWGp-MLquzr743X3PyvB9kYXV-WbjVbUY3dFuhWjx947qICm9S_5_b5BBPA34XSKn5WDoZid8RE--ckKOhEBad2rvNAFPFh-QrypEp35JaRNN6oEo0Gh6H6R7eF5ZJMGcMtBD-GE_zcfiTA_vdWZelsvVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی خطاب به بسیجی‌ها:
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66144" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=ZlQmrBF_O4wTxHOUrUCsIXbE_xZCrq07xloVmc9VRrPlhWKlMU-IL-AVkKZZqDLOKEJQ2qy4kKqL_G0i1hDdv1SmbNgYaLZ2kTkKtjBzl4pwFCF4KZnnpBYmc1Ci9VSCj3mvWlVDGtXukYXXlATLIWiISXkAWSk8K9O9dNvOX5jTC9Yl_A2_O1zsFioKpjQMIJ2FU3mskc_Z0uBH2B0pJA7NsH2W-_ElkkAsNz-KiS_6tEXt0Rmw61rHpOK9P5pzBd9ooA6zR6h8E8Fw5t8zSo5S6JR_wDlGUuj6mGJ_TiTbvZrO8qyqOBVizQgy5kh1UlhpQ2glPNfJv4DVwnH9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=ZlQmrBF_O4wTxHOUrUCsIXbE_xZCrq07xloVmc9VRrPlhWKlMU-IL-AVkKZZqDLOKEJQ2qy4kKqL_G0i1hDdv1SmbNgYaLZ2kTkKtjBzl4pwFCF4KZnnpBYmc1Ci9VSCj3mvWlVDGtXukYXXlATLIWiISXkAWSk8K9O9dNvOX5jTC9Yl_A2_O1zsFioKpjQMIJ2FU3mskc_Z0uBH2B0pJA7NsH2W-_ElkkAsNz-KiS_6tEXt0Rmw61rHpOK9P5pzBd9ooA6zR6h8E8Fw5t8zSo5S6JR_wDlGUuj6mGJ_TiTbvZrO8qyqOBVizQgy5kh1UlhpQ2glPNfJv4DVwnH9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0jnRlMI6kTvkTwt4qkn8JZdEAo2RI0LKtG7-aMTwvtjL8pVCiQ6I4-5jnOuuBsy5ZM519PBWy4SN8mtOnD-nkgBnlvmhKGegdDHbrqv8l3jDmmTeBLAG84qWzEk_y-MRwlHUt43s0s3ToTPjH8nP-WWHn8xrJwG8TuBNGQDhxxcgEpyV--2DmmaIZEBL4QT07celj31aau5wghHrhhUfOKsfni-ww7LFI6Ggih8onmqJz6TQdE-pOWzHqJGKo5-LGKFHmzc2icQHLp2FtNRvwkFPJI7yEt27WGai9yAjbF3RESMGpfGqAzr7ReGW5DLUUpgxdKui_lq61CGm0nU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nySRiOuIyIJ-JBe7NgLA0d-f3RNDweGPR_MWJbgM8cWV2Vcss0cAimYg57SJVn1Xl6wzLAyuVkNRFaVcIHze1PUe5yAEYRSWn92kNB-1GMN8NLXCJJyXiVDnS3HKbGBa6bR_g67oGCeU-rVqJSiwfmejEczlGPuB4peo12UC6nLv3e4j5izTRKgGqlm18Src5Ksy5_7Rfuq1QK2bOhcw3Q6rststCZ8hhvCKcm9aOgatwd78y15kIhaG1afpJpHApib4bcYpqdUi8dxsIN4i2IC8mVS7wMjT2eqwzeJQvOZNWWiUBD3udDKg5HXnhurpSaJVhpvuqkB0NLlTwFUK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkqZIHHxbqClggJ-AeoJ1F6CX7W8KI2e7ShnaIyqBA6RJXFcELAl2ruJdXkbx7D3700Ib_6KnC4_Sa-ArgNlINmBrser8EqSNo4ygVgULacpwljzxF4QeTdNRjYqvLSf_Q5HxwaiICnvQ7mcw9_tEvQ6roAMDr5X0TWcArzzCFbbW6qg-eb1taozvucPdsxvJoRNApvQYiGSknAMKLufqWmLS_NwEUPQdHUGsbdOK7G5gxJlhAqOuankD1YQ2a7u5EUPZAdBcxUFtLRn2MqwMAR0meu1FiGJaRrD_kVFglgpgfsdS5qZfouOKBlNRglHt4vNnCAIXSJSUcXsfKKr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=JTPJt0vm_TMdIM2ns-2E8mS3XH8uKPI7H31TkpHnEtMN-Irqcj4bqGOQ8lKbBiluTxHiITzMmSpwHHkUbViEWMFWyFdzhasNpez8P5OgEqK0_W66Rd2TbMGrrB15K6UCgRbJ6WTiP8xZOcYo6RrcPm242R2SKedoM9lHVKFwoUk-6liOZQUJCEAQEy9ZisB0Ayd3nTPnkmalYeBdeIuNGacL6K7WKo-OGCC3tnkdGDHe2HYgcg8ERDLAmyfD1xWqoD8K7S7nzTTUeCDwmnhikMlpiJrshrtLfmO4-KYSKeLDBQ07NHoJ9imeVLTHhIuBZ-sxbunsg9zpX_tBMU3AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=JTPJt0vm_TMdIM2ns-2E8mS3XH8uKPI7H31TkpHnEtMN-Irqcj4bqGOQ8lKbBiluTxHiITzMmSpwHHkUbViEWMFWyFdzhasNpez8P5OgEqK0_W66Rd2TbMGrrB15K6UCgRbJ6WTiP8xZOcYo6RrcPm242R2SKedoM9lHVKFwoUk-6liOZQUJCEAQEy9ZisB0Ayd3nTPnkmalYeBdeIuNGacL6K7WKo-OGCC3tnkdGDHe2HYgcg8ERDLAmyfD1xWqoD8K7S7nzTTUeCDwmnhikMlpiJrshrtLfmO4-KYSKeLDBQ07NHoJ9imeVLTHhIuBZ-sxbunsg9zpX_tBMU3AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=b4sFSg5RgbgqPVIeOyKTNFfALarz89LJxuedBYBx5Rh2I7xnKz63NlERsZzkPEGnwAdS67cMhwT0R9h5aFDdWxvhr75J4xR2YYNR1Qx9YnHn5pswOwDDDf0rhMA72T5r7XUajtb1_9aZLACOcVqdQWLckYSAIq6ag-rMavl0_5qYTvT16i5SZegfDpVZdv9_UYRjy8UKWMYqn3IyxtK_bj_e08z1DUNn7PQvJbI0DftlkUFNy4JfIfiHVMvpWaTNeIZg3_fRzwvj6x75tgDzGD8tnxwBu6gS6rSDEXpsHAblAf6Z_MZhpSx9cSVRKWVWUhyr_XtqGsC0X78bh0cj4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=b4sFSg5RgbgqPVIeOyKTNFfALarz89LJxuedBYBx5Rh2I7xnKz63NlERsZzkPEGnwAdS67cMhwT0R9h5aFDdWxvhr75J4xR2YYNR1Qx9YnHn5pswOwDDDf0rhMA72T5r7XUajtb1_9aZLACOcVqdQWLckYSAIq6ag-rMavl0_5qYTvT16i5SZegfDpVZdv9_UYRjy8UKWMYqn3IyxtK_bj_e08z1DUNn7PQvJbI0DftlkUFNy4JfIfiHVMvpWaTNeIZg3_fRzwvj6x75tgDzGD8tnxwBu6gS6rSDEXpsHAblAf6Z_MZhpSx9cSVRKWVWUhyr_XtqGsC0X78bh0cj4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=kEfdvzxO5w1pAJwXF_Xy2Uzuv6iTiiDeGV_RDX9bH-qvdrf60mEjSoH3SgWNOUdh1BNjbZciAMkAPIJRGk8m4zzeJpBzx8rYXiNWoaU15wGa6hczyX9khfgZD_wClRR8Y-Xk-TsxPci6WJhwRQE_8LtwnrKA85Xkkkt-sQgwgYqrl4vF1d_vGsPDluSf8-MUdYRTRbuVEiQ3ZcQZiaEa3ZgwF2WIzUsm9D9s5FmtWhtu0AP70AI_n55vqe0oyRqU4ar38iAaJSpXgHzXtnLrDovslspgbi73JTRZgBTo5cnNwW_2Zol6QEgOY1rjEqXWev30bemLZLNtosDW79nIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=kEfdvzxO5w1pAJwXF_Xy2Uzuv6iTiiDeGV_RDX9bH-qvdrf60mEjSoH3SgWNOUdh1BNjbZciAMkAPIJRGk8m4zzeJpBzx8rYXiNWoaU15wGa6hczyX9khfgZD_wClRR8Y-Xk-TsxPci6WJhwRQE_8LtwnrKA85Xkkkt-sQgwgYqrl4vF1d_vGsPDluSf8-MUdYRTRbuVEiQ3ZcQZiaEa3ZgwF2WIzUsm9D9s5FmtWhtu0AP70AI_n55vqe0oyRqU4ar38iAaJSpXgHzXtnLrDovslspgbi73JTRZgBTo5cnNwW_2Zol6QEgOY1rjEqXWev30bemLZLNtosDW79nIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN7y8w9oO9Jvo6IKBIk8O10EbmAPOgr_hHb_90b0QlOcvdhMpX7EpyNRoUTptbjGmi0JgrzyoYyCVaia8vDmryQxPUo9PdorRkqHjBTwrUnEwtWTNBwHVIAiIla4_S4MFg08kwt76zK1RSJKy3gbAkTgBqMXagxjcUevFbsINPPs9B1AQyDNzR34xb1-VscLenO8u-m1oVMGNFx5Y3ORTqqgbf6VSwv9TSr1uguktVJgGUeTSZIUGtJ01HvQlgNG0ba97RuBfPayAsM9-wk1eVhKxrS1fsL_txLJ7-ow1nI-1g1paNPVq8wgu5zayRaL05bZ9x4sTOc6nEBFGRzUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7xsmdAtrxpuACJs-1g7vEM8umM1zvSXwdB7TyhAyMVKdM4zK1F6VfJWV6z433HDtY6hplYnVyy4QLt6pjJqCSUhOmnoQseLXsYdfTkE46dq1oiCkaKuxNw7I7aTUskILtxegFGAynR2MZ0KyVpZSdvgkJoEwntcdmGY8oUUd7cfkDJf-I0tXC_jOZu84i6mY27SGP6v85tCRRyK4Btt5BzqJpVadqUDP7Hr0MMlfhxAHPnbAEmZooUlxGF4dlbFwgt6AYfTRYeb87CwSZQUXMrYMwtn71GqSKLQp12GLhvOXqx8ZD3FNbfAXnD_gJOqaixX4OUTEZ9mDUTkcKuPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpy1sc1Ex0ikWFrVEibNWwZhmm89V85_d96MlZ0e-oWSxzMwfCndwIWfeqMYm_WSE676O0WcIdhbTFyVJGnwt0QobPRPq8ulkEDOXFLEGsaxvxHkwBopfF9jzodj6iFUULNZi9z1vFKp4dZvTR_wXF53YQQNxj-kB-3g2KFF_iaoD3riORbgU9ixEJDAM3O61UlE7yt6zDvKoD2jvqcJs7DQI2dn-od2M6fiv7W9cPTK-LU301jYDFUUp_aCiCdORAGue-JHG5AyCjnmfZvf3qHPp0m9zrmRb1gYcZ3bymbOTUbd3xCF3_jYKnN4AfaVh3q2OflI7JApLmOlTcOU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=YQpEyIdVaOpy1qe8DNjvbkSECwRis2z7p6-OUBDJT9xjnGSpGhurxHzJRRXKRknZ8vbngE9pfmZhbzb5wKnpHMdXYznIVwPmxdjov-VO7dgQCd96vT0rOdOFJoBbXXY_5T1oTzUh0p6vpgO2vXwUJQAO14xW9ylJs4C5H49dSjMwoKYWXcf7__QCoIMexXGDUo3sYJXDr8w57ahR_GBRniPoTjUs1ubMk4ncZsrgNWu4TVkSY7PuCQvMCJKz_wcPjUm4NWeE8KAL98QljCk_2zpzOEEF-r0IMEpwPDC5js6TBVuS6Vse7MuddKHBpDuT3_eGSDha8z99PMKIo5m5Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=YQpEyIdVaOpy1qe8DNjvbkSECwRis2z7p6-OUBDJT9xjnGSpGhurxHzJRRXKRknZ8vbngE9pfmZhbzb5wKnpHMdXYznIVwPmxdjov-VO7dgQCd96vT0rOdOFJoBbXXY_5T1oTzUh0p6vpgO2vXwUJQAO14xW9ylJs4C5H49dSjMwoKYWXcf7__QCoIMexXGDUo3sYJXDr8w57ahR_GBRniPoTjUs1ubMk4ncZsrgNWu4TVkSY7PuCQvMCJKz_wcPjUm4NWeE8KAL98QljCk_2zpzOEEF-r0IMEpwPDC5js6TBVuS6Vse7MuddKHBpDuT3_eGSDha8z99PMKIo5m5Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDMHiOtXiuQWA0HH8f43DEcj4asp9tLnaDiBgeO2xxg9WvmxGtL3PYLP5-RJTW_SPqCtH8u22b7iANYuNdzWnhwhHQ9uBM7KBEXfJVp7Lu1IDQMcKn5-IXFvRNqWdGlzVgIE4slPfVtK0O7RiPwDcBDCtIa1y1RCJ50p38BZ-7Rb4fYKZ0C2xQiviYY9UWOY_tHTJcGXqKVI-2SdUn2Drh-GBjG3snT6EnQDliqVQtIGp5DgPE36dkBoE9qAgHp48txVwmzTVk-XKDPB__-2F2h9zrmIUrEQs0lxWysHOE8q9bJ5mOIxpfm_PDO0JIECg2kysi0HvNglLmU-AXyORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری
؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66125" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsztON_2v879pBRrXBKFto65yup3g3wJUjCj6qOgL-VaQtsktUM3plnJGjlPWiEn2kOFxEmkEMIndAgsuXkM72qBDVZnY3_lwB8iFRSgkzNCPXy4qxwfvxblVhPc73S3LoTlUIfm5SmaxarHuaEszinIOvtJdrq7u_Nv4Y3Ar-ZTzU2fnliqFGWKjLQgrTV-7wu6eWsB6_-GiZhpIa70BBS4mAHVnTZTYE5lSNH4EJDalpIGFWFKi-sNM_WwBe1nIZjU22qB4udR-x9eZdO91vwoxsO2A8Ky1RHL_017s7E2tpSO8B-arj6KT6ORXA3hMLzRHPYMsHyehl6e6Z2BtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زیر نویس شبکه خبر:توافق با آمریکا انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66124" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
مراسم رسمی امضای توافق روز جمعه 19ژوئن در سوییس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66123" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66122">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🇵🇰
🇵🇰
شهباز شریف نخست وزیر پاکستان:
پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران دست یافته‌ایم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد.
مراسم امضای رسمی این توافق‌نامه روز جمعه ۱۹ ژوئن در سوئیس برگزار خواهد شد.
از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این منازعه صمیمانه تشکر می‌کنیم. همچنین از برادرانمان در تلاش‌های میانجیگری و رهبری خردمندانه کشور قطر برای حمایت‌شان در رسیدن به این توافق قدردانی می‌نماییم. به طور ویژه از رهبری خردمندانه عربستان سعودی و جمهوری ترکیه برای مشارکت‌های ارزشمندشان در این زمینه تشکر می‌کنیم.
پس از امضای توافق‌نامه، میانجی‌ها تسهیل‌کننده سلسله‌ای از جلسات در این هفته خواهند بود. این بحث‌های مقدماتی پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم امضای رسمی را فراهم خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66122" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66121">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
نتانیاهو از این توافق حمایت می کند و این برای او خوب است زیرا تحت هر شرایطی مانع از دستیابی ایران به سلاح هسته ای می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66121" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
محاصره دریایی اعمال شده علیه ایران موفقیت‌آمیز و قدرتمندتر از حملات است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66120" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
من هرگز به تغییر رژیم در ایران علاقه‌ای نداشته‌ام و در حال حاضر با گروه سوم که منطقی‌ترین هستند، سر و کار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66119" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: ایران در ازای توافق پول نقد دریافت نخواهد کرد، اما ممکن است تحریم‌ها کاهش یابد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66118" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
ما وقتی آماده باشیم، مواد هسته‌ای را دریافت خواهیم کرد و این اتفاق ظرف یک یا دو ماه رخ خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66117" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHbUWd13WD-ACSC_1_8K5NunM52WGOSX97prhLtkoe5eEvq34gfZPx0yOm5zPLj5wkSXHlxpX5cE5fkVzDiRhhl8LkpCRa9WUp-adyp0MDdZZJOhXghL-kO35r2FZlkSyYpPIueeVC_nWzvZZGBL0gGRpFHl1T9rNVJ8Q8nvwXQY1HksUz_fL_21bmT4kqrykxykvLxmL-FFAqaejLBoXqq2OMpzKaqyfS7qk758VzTZelQ1cg9LUoHxcjQ5UR4fnedi9vFPlBNIV8xMyLtdYiwIG4JEiJiNutGmb8oB6aMZKYUaTGpMDmOCiByK-OZsAB4lpg8slejtoDFRec-ImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتوای تماس بی‌بی با ترامپ:
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66116" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ و نتانیاهو دقایقی پیش به صورت تلفنی گفتگو کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66115" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66114" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66113">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
بزودی بیانه ای صادر خواهم کرد تا تایید کنم ایالات متحده با توافق با ایران موافق کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66113" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی؛تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66112" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66111">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3CBzQXWoGxY6--2PvOMnz0-hYfFOl9wSAX_H1bdn56RCHStAWlREVF6xB9IgV_22SoXLubbmSyyy3OazZzNdoBmXr4yujDnydQIg3I6Y_yTpWO_PhYVq7XCIhegPw55HwNpek5S5ts0BPSGF30nNb6SRabjMHqSAExA9p7K134dHUpmHX47Yyph1s91a4tEprWs5t1uKgN8BBqh9W8OFEDEQ5zaf6UL7ZOunyrMk1K9QrXLRkZC-gqROv683pm5kew1V3EC-HogSzCmvMHuVFqS0LWEiBwNdTF_tDKZP4cjaTlO6UxPwctViuE3Buii0Z7xkbnQN8TRDACsWnL7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت وزیر کشور پاکستان: الله اکبر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66111" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66110">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=Re4xejeAYWF82DqVGpi9v2EY39e4unR98evi0dX9Gr-5euvSFVmFMSTP-CU3vYjohZ-7THK2Fqm0UmFZRnBDFaRwmPs79qegJdQTUcavNTomy6h7a-SUsgf3-0C5ZSD9oWSu2qz_-gN7r-nWk6n0ZePZp_edjesiwf69CQkM3-Hyt9uE3kBOSl6-_TTl8yb6epV6GKEtHoLaHMIBkoKHs-ZscREwGXeRHuZw1NV4B7DLCsSiZ_VFx4s4VzgoCaMTPOx3CtvUezC-FBtl6PjXifeYIHWGHnS1GsilqzZ1Vh-hHlJ1jBPAVYKG197x2whSHNbV2sQuk_ieA-vyEQUvUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=Re4xejeAYWF82DqVGpi9v2EY39e4unR98evi0dX9Gr-5euvSFVmFMSTP-CU3vYjohZ-7THK2Fqm0UmFZRnBDFaRwmPs79qegJdQTUcavNTomy6h7a-SUsgf3-0C5ZSD9oWSu2qz_-gN7r-nWk6n0ZePZp_edjesiwf69CQkM3-Hyt9uE3kBOSl6-_TTl8yb6epV6GKEtHoLaHMIBkoKHs-ZscREwGXeRHuZw1NV4B7DLCsSiZ_VFx4s4VzgoCaMTPOx3CtvUezC-FBtl6PjXifeYIHWGHnS1GsilqzZ1Vh-hHlJ1jBPAVYKG197x2whSHNbV2sQuk_ieA-vyEQUvUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما تو لبنان:
انشاالله امشب قراره ایران، یمن و حزب‌الله به صورت همزمان به اسرائیل حمله کنن و انتقام بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66110" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66109">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی
؛
تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66109" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk8BKZ7afau1bljt-Jrq2AheVi6_QPTvEjjhp-S1znP2ST8W2pd0dpj7T0HtU5ayrUUhtxkiDp1OBFQBLxxcig2zLksGSDRdYFfPkgDTGIm8B4GVihpmm94ZR-cYj41R8BsPUmxc_2rIAIRlCosO2WSesrSdjcs1AC02ibIZesrGk7Zkx4kVNhtjNddGMujScNNHPlcUnEU285IdKOMtXYmH1rEFjtRjyNvQKvnNET_lydZX9DgpVOaZdV0-KZ9M9_reiqtLjn1xk5p2do6JMYcJbexuJNCVh_3-G8U11A8qMgUon7s9XmznmwKKKYcaVwham9lYo3nGJtDr3hXERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرزیدنت ترامپ از طریق Truth Social:
ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66108" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66107">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
#فوری
؛ ynet:
ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایران به اسرائیل جلوگیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66107" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمد باقر قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی‌ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66106" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66105" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66104">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
کابینه اسرائیل:
اگر ایران حمله کند، ما نیز حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66104" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxc-1OEe68igwJL6PDhN3iIEOSOZ_mgXmHLCbUZtIYrPoe16-IVrmdvoul3BK-SEJXwyszQJ88oFQd97X-NXUDgHoar7wTDzqikXBoouufx69bZEshiLOGW7yCRKmI5znDD9HmmABIQxMJO5CKCFmzW3KTcneYDhmqWG_OhC8Z7cu-9jULGPAeeESWM9Q6cynTsPhnrKvI213ypJ63ZGsoKxSJh_z4pvpoeeLDpLxhToTsfn1d2fPjaDcxHeF-x5EODnnM8Npbrs1HTn35hMFQ6wPVH2FiuJ1DFNHpK1BK3WkqXaF-w2dIJpirmECuW4Hu324TKdANptNcLmrThceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور هیتلر در ورزشگاه و حمایت از تیم ملی آلمان.
آلمان این بازی رو۷/۱ برد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66103" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAWAP9Y3GjSE4QPxxi75zWKs8cmDO8GSotWpTDKOp8_NBRRAATJfjQAH0ntNwRyO8YOIutzSNHGTK063NXbreK2rd3XlSoV_wl2g7fLbtRLv0m5msm8UQKdRw6kznMo2djmWzUk_ZMEwZAWIUVpu6LRsCdyFH0P9bjsDo2BiIzckFc-RGES0Z-Qq-Nyepl7R8SHXwiABrfs1PEYYr5sysqfqwLNFA3oUpfVoDZE2hoC5mwlGff9LMx6lkj-i56hyHjmfq_KrvFdobBRxx03NpVNybIkZdmm9CmjOuHsYsgdQiGsVDNddpDEQzhzKeaTHxUurV_6YjDWFhtq9RO5CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان غیور لبنان و دیپلماسی مقتدرانهٔ جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66102" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
به گزارش Ynet:
نتانیاهو درخواست‌های ترامپ برای توقف آتش‌بس علیه لبنان و عقب‌نشینی نیروهای ارتش اسرائیل از این کشور را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66101" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری تسنیم: حریم هوایی غرب ایران بسته، و تمام پروازها در این مسیر لغو شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66100" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=AMS4PAEg8hc-NSO5wzZED_iQTEqhUhR_dIpEvtxwLPoBtFebfbiraOFlXyjyvGwjdOAMst2i8QKVLqCe-immb7B4BIwe25aFbb0t1K2rWHCqqAEKOD-DBph1EB2W6yyKWmVKhV1Vpnrm2JZhgK1Yp3fHpQtap5j4eC6ExSP3dUnVH-9tbwK0com7Belpm-kfVIYomGeAxR9T8JdvBKMlUwEy0izIWv2pi-l3HxJKc9P1RoYpwe4x-kuUfyw-x3ERHIQs-XoYxkzocKKLrUEhJ06ZAOMtMpeLEug9cA8hCUtCYOGc00O4zI0PtnTH9GfboN8VdEZMsNFQU7Imj19HwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=AMS4PAEg8hc-NSO5wzZED_iQTEqhUhR_dIpEvtxwLPoBtFebfbiraOFlXyjyvGwjdOAMst2i8QKVLqCe-immb7B4BIwe25aFbb0t1K2rWHCqqAEKOD-DBph1EB2W6yyKWmVKhV1Vpnrm2JZhgK1Yp3fHpQtap5j4eC6ExSP3dUnVH-9tbwK0com7Belpm-kfVIYomGeAxR9T8JdvBKMlUwEy0izIWv2pi-l3HxJKc9P1RoYpwe4x-kuUfyw-x3ERHIQs-XoYxkzocKKLrUEhJ06ZAOMtMpeLEug9cA8hCUtCYOGc00O4zI0PtnTH9GfboN8VdEZMsNFQU7Imj19HwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار تجمع کنندگان تندرو
عراقچی بی غیرت اعدام باید گردد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66099" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
#فوری
؛لغو پروازهای غرب کشور تا اطلاع ثانوی رسما تایید شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66098" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XewZtAEKdtoluStXDo9NW43RaWv5myvJx_KmE4bXKvQUa3rL78NSvg1LGVotKJA3GQnNJoowYuLF-r1izvgzlivXeO1LQIT7pOtTS5tvjfgqP0EugCSfPVrgZ7reqNFHv95hSXNa6rp6p1TRwRlT4ibsn6rbn1F4Fah9YL-Tyifp2VsizCq0O0i9yLJeDViKXkojherM0GKyP_BvWNioGn-EMyaEwmNMc_BorDDTcMDUAPwPkxm-sBikx-uYjewgo7nqQ1RwZBzvS7dTdyAHBOpxpPOBCEyUBAAKaN1Fs_-UBhai_FzWAzb3o_u0ghtWXlYDEfO_Oohfud9qKhkZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به نظر میرسه ایران حریم هواییش رو بسته.
«هنوز به صورت رسمی اعلام نکردن»
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66097" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه #hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66096" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
حنظله:
تا ساعاتی دیگر، آغاز خروش آتش های سریع و خشن، به نقاط جدید الکشف حنظله در آسمان تاریک سرزمین های اشغال شده، هم اکنون به پناهگاه مراجعه کنید. شاید هنگام فرار حوادث دیگری رخ دهد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66095" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
یدیعوت آحارونوت:
ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66094" target="_blank">📅 21:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
زیرنویس شبکه خبر:
پاسخ به حمله اسرائیل قطعی است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66093" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXxmber3nqAzu269arV4zrlUafjvMX3WEdMWoAMU3CPOCAC-njXKJ6auEjS-2mC5YNp-K-4ivrkT8FmJfpOu6dCgQRkLnDPkefg7Ajnl1_uREJL3Dx8g9Njn6Z4Y0d7NKsI9bFDWU3r5w5-Y_wm0K2MYTv87aFWpiH2IpSZTM4ICUcvlj9mkYUqcWhNzVPsrGHQeX3L8SmB4PWeiO-JCuSa15g35hQC0T09Gy1NqSTobk0wNSNd7rT7Hxw3M6vO-pFAF9LQRQegCjsefhRBuA7LnT186HvHN013EsiFB_vInrEsfwPB4nlUh77Yo-DLTW96fJtZVXvViAH_M1gun6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی:
‏
پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66092" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66091" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h35Neh8V_3IYvMVZVb2GgfkzjvaaxCbtuuG-ed1ahrkDOZGln0rfAB7NyK0z_DbqBZtFhLVqEiFo_HgIMdY-kwSe4PEd29zuLbTJt3E9cjqBpE7O2CLPjWie8BNGacvFvK2Uiv3LJ9uhpZE_m-MmToVrEKSJI18pw827jUCwRhw2T85RltORCIdHReGgm2Q4fmybuKH4z1HFoj0HzwvQovIA_hcSyet2jBardv6fE_Rkmnk8IgC5boq7J0a4LHFBJ2WckCe5ot_ddbSz8yq9LNQPPx3zmHJnXY0IsKSB1cuIA6O7ubQiPW33g0LWI0SklbWD_zZQ6Nkpnjt6IwFzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66090" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66089" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JavVwtBHXwN1hExsvSoujQf2WolT5lX2KcrXcSQPz-3ly8w6NUyNpfTaoIJwHQpcp7A9QdLXfELYP9Nura5OmTPa3B3EZW6XbQ3u8GMb2avSFH_dJ5yhc2t83KGMNRXFPlYrNe9mwQVIjYol8JJmpTVU9SSCvsXXWVn5ifUd0zv5pJb__D4h1uBuJvgF2iS4VBiONhEdx9WOvb4QnVEsDtz9HckBHdQU7GKtS_TmYfRyqRaDWdrOhG2IWo1-_DNU6ZErTR4ljs1t-W0IrX4CDWZXfJVxL3MKtEIRuhajU8m2CJEZb3lhAiFSM9EEEa_x3poh4GQgV2Y4mXcchw9egg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66088" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=CD3MdnakrsEzfUuYUFtqUzNyhdhsCAUFEp_zLuKdOeIk6j8TsaC44T2OT-R0zL5GBN6KZhvQ3VWLYUQKhiVGH9Jq3RuuQef7tvJh6DVpolyEPxD4YsKhxE9dgvQETKiMCDX-M34GWzMbKMZ_SfdDxXnxnM_aGusXrac5l2qvomvbeiXlY-fha03RG0fGOtyKUCkoISE8xBoQQS-m1mLqlxWhvF21QgcKQmdVoBDMXnEMQNUTVINZrwyNPHx3h0VSRwXz64lw0eemMa6VB73hEb3UnR2RZYcc4cbwI6p4VIT0hzyASwnZnxOHuk43wVam5TyzfKRuVnyT60IG2y2aYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=CD3MdnakrsEzfUuYUFtqUzNyhdhsCAUFEp_zLuKdOeIk6j8TsaC44T2OT-R0zL5GBN6KZhvQ3VWLYUQKhiVGH9Jq3RuuQef7tvJh6DVpolyEPxD4YsKhxE9dgvQETKiMCDX-M34GWzMbKMZ_SfdDxXnxnM_aGusXrac5l2qvomvbeiXlY-fha03RG0fGOtyKUCkoISE8xBoQQS-m1mLqlxWhvF21QgcKQmdVoBDMXnEMQNUTVINZrwyNPHx3h0VSRwXz64lw0eemMa6VB73hEb3UnR2RZYcc4cbwI6p4VIT0hzyASwnZnxOHuk43wVam5TyzfKRuVnyT60IG2y2aYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ به خبرنگار فاکس‌نیوز گفت انتظار می‌رود ظرف چند ساعت آینده توافق  با ایران حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66087" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeiFrp6RJ7ALEVysw-F2oBtgxCMfugpUz4aUB70UsWEKoRSu1I11XUH-qSJsX-D75CPG4tgT4esUm4p-SHNA2bPlw4e0_-DS-z_mBFchoNCilSrSfyO4wEEeVnyRovfeoJ0UHimJruvMGBurBi68Hde4LDJtqPLcJ4p2IsaWKcBKFc5UtpLXV7X9Rccpsuzd-B7m8qJwCHkKDWhtQ-r7N60PBGHNPGJwwAIYYEh2Rca9MT3gFCv1uwknUw3eW80G6v2XZvXLnKpr7AFLM7LChpFy_032OEqEPxHnVGw6XmfMwSbfLPcGnckzAdR9Xg1z5D-1WWVUetcj4IbmiB0aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید: رئیس جمهور ترامپ در یک مصاحبه تلفنی به من گفت که معتقد است علیرغم حمله اسرائیل به بیروت، توافق با ایران امروز امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66086" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پزشکیان:
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
رسانه ملی در حالی بیانات رهبری در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی "نه جنگ، نه صلح" گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66085" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgc1wQwZ2_R-PiBAtXGqnrvs2L9VJnBMWDNHvHQflZNJoV5S60r6siIK3xxpdj9l93zDSKVERltArrZsc_VlpUoq6HNzfj1Op4-MstiEMFPKvReK7_R4iOrO6DDRg99C6DX508v6UEWN7BMu4LMs1ms0_MEDnT-gugyjcwnIKZJtAnIlPzqTjORsvkAsaCn24n9W2PYpBYV22LFbCPJdbAI97DG8rzUKLPa4FrQ6CSoiixCZarAxdmLNRdUAVw9OwyyQKKyQRLR01SMwV1lnaEfRiBfn-lgg0CBVR22jL3kzl11QMu-7l9iO2vv7VkBtgV111j-Q-0HuIaMNEt_R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ در مورد حمله به بیروت:
«این نباید اتفاق می‌افتاد، ما به توافقی که صلح را به منطقه می‌آورد بسیار نزدیک هستیم. بیایید آن را خراب نکنیم.» او از همه طرف‌ها می‌خواهد که عقب‌نشینی کنند و حملات را متوقف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66084" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
وزیر جنگ آمریکا به سی بی اس:
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت توافق با ایران را مختل کند.
ما در مسیر امضای توافق با ایران هستیم و مسئله این نیست که آیا این توافق را امضا خواهیم کرد بلکه مسئله زمان امضای توافق است.
اگر ایران میخواهد این موضوع دوام بیاورد باید افسار حزب‌الله را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66083" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGzKKNIEM3hsJyMm1HY1dwMqYH5213xsxGX9DyewFR4hqqUas1q9qqOns20co7uZ9jdPOOTDhlwKx-SrQ9nmuSHIhdY5IXKebJcBjpXxzWmPeCNRp9914xtlnuaotTkeQYCkjg-5c_e4Nj873IDAbWniYSTN_npWdn3nrmoHcry-AjUrYfQ6aGdaGN2oJk2wMEjueB7Woh2cOaQsfFt3y6H8oaZYQiCJFSi1Mlp4yXWPukQgftmiYrHguJ4aVjHpiCelBfSKUQol_ShXbKrgbPzT0aKVEXrOCGdaqLtwe-XpAxjnQ8BN0aT98OkyULWWuZuxECwtMEizrAT7xV-o-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIEYtgC93Bt4ziwhSfdhSaEDm3tFFBmgfQiNW1_XD5bPltpYpKv7xJ2rd-3eB8B4STAlI-gZ1gBLEZfC1Xc3ahyzzGdf1Q723U9DbZnK8AFmkddahADS-fRyZOO9u3wXKypxdkE-dqRVMF0slEWkrPl22wiRRWa_0meUsFtGZb139UdguQkLoMr-Dmk_YPKD2M-2GzvC6jj8C32dc3k-LFjAJ8Mgx1btA2GfziPun9sXxbvuNTVXGV9zFXTDrC6OqqLd5eaNfpZl5uCzqw-tHygRjC6VzXRT6NsmOFN1NC6mn6_Q2dNALUr443OWB52dmURVlZePcmI63sTy7C8igw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=fRScdQvCAZjIK9W0dSxmY3m8AuDeBIB_AbS5tDKly1-d27NUKc3CeCsorZXmwdhtKObnzhId3e2TAArPHAhr81GukSYPQ5kBBvrGGWF0mPgr-jeJ7IuxBN7eU3-snutbMvTP7fL6JScsq8c-jOHnnU30f6fxxBARIv73SOua7qwIhxmeWeSKAYzkp7yIS_tz076jJpbcIgXlrPI4By5wynC2iQnE0tsLCVGgnfwgjVPShbB6IWDndpYUM3oIacptRX1-QOpwivq6OuQgzNY_oITdxZsF9ppbAnJ_tggIk88PS078U25uD-28KJY2jjm94L0M3wpNsMeXkGHlIllDFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=fRScdQvCAZjIK9W0dSxmY3m8AuDeBIB_AbS5tDKly1-d27NUKc3CeCsorZXmwdhtKObnzhId3e2TAArPHAhr81GukSYPQ5kBBvrGGWF0mPgr-jeJ7IuxBN7eU3-snutbMvTP7fL6JScsq8c-jOHnnU30f6fxxBARIv73SOua7qwIhxmeWeSKAYzkp7yIS_tz076jJpbcIgXlrPI4By5wynC2iQnE0tsLCVGgnfwgjVPShbB6IWDndpYUM3oIacptRX1-QOpwivq6OuQgzNY_oITdxZsF9ppbAnJ_tggIk88PS078U25uD-28KJY2jjm94L0M3wpNsMeXkGHlIllDFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=k1ieMaid5JOWbMeAgyN3op12JoRAUAMGXRr3TwY8SAdFR02v8Rh4_JNm3xzMHNsGtPgppcpIziK2jhQjYMaq6blK3uUvWcAoREaBXPo-lY9yppqBWJNts3azk9o798OTGIzj2sq4ftfj9hZmV3uySLkADkBZ36-1LV9WDSSygUVGPfirBFyN-cJY3_UQMjiMVyJzfnz4Ut6gBHp_XrJoyEADI-JbonqqV5AFV8BhNoXB4PX51_-ZDAA0yjzP3GBKxAQNQvEhc6_OCUx2CV4CUZhLF02j1Kfo7_a5IG-kFEgB7Jn-QMzit-GQtq2JwswD7vKnBZkWE7z9WDf3WFbeug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=k1ieMaid5JOWbMeAgyN3op12JoRAUAMGXRr3TwY8SAdFR02v8Rh4_JNm3xzMHNsGtPgppcpIziK2jhQjYMaq6blK3uUvWcAoREaBXPo-lY9yppqBWJNts3azk9o798OTGIzj2sq4ftfj9hZmV3uySLkADkBZ36-1LV9WDSSygUVGPfirBFyN-cJY3_UQMjiMVyJzfnz4Ut6gBHp_XrJoyEADI-JbonqqV5AFV8BhNoXB4PX51_-ZDAA0yjzP3GBKxAQNQvEhc6_OCUx2CV4CUZhLF02j1Kfo7_a5IG-kFEgB7Jn-QMzit-GQtq2JwswD7vKnBZkWE7z9WDf3WFbeug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp5rIGCG1NZQiIKaoCFxAQD50hH87QCIpB_dubEHv6YVjfmhxcCFfaXhwmMRBPfP4p52-4ZyC-KvQQks8F2jG--K7ZUHMdaOILQv6Tbse_Y_MTcio0JqwrkBPN_AicY1sPXJFFa7fpTuyxM-s7RpWAPK7LgXZRtnmZUCMFqSDqrnAPiRKN1E6bU_v72NMk68nrK3-KhdI3Vdq43pGBWER2ifMjNp1eZ4oqIjVDtv4Og2awNktSK1Ze8t9Ni5W6KeR9BuwkowPXrivFMu7H9BNQu4LGtMpXLu6nHnTlntMz-PdrQK3F3mhYWkJvTfkhI3Ig3ndU24D4eQjJOb_a1ZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=CnTMAs86dW0ekTrvvUdMVS53fy5pMj0fg7bIRtgoTMcKft7AmlpTxsH8nPABZf670_64BE_YWSUO4SzgrRcgSxoq2jqdvTFGEQ8oKql1t4t--pxS10YYxGPjveud8zAaprBST4u8alKYe6evn1IFvohJs4UkHwZcoh6u751_nDTq1SFhTjmoe8J4eftKr8MIGeZy7aUcMSwbGw89iR0G-SxHiZZ2VmHcAakLWY61tGNDQY7grd8nHi1vgqQHN4sTiDxKdOoKqQLYySQVqZZlA44hbiGDkMd0cvAgEdJYoiYatF6M22JEKD94gBEPcOk2r-H_VBccahzpicGWrGghnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=CnTMAs86dW0ekTrvvUdMVS53fy5pMj0fg7bIRtgoTMcKft7AmlpTxsH8nPABZf670_64BE_YWSUO4SzgrRcgSxoq2jqdvTFGEQ8oKql1t4t--pxS10YYxGPjveud8zAaprBST4u8alKYe6evn1IFvohJs4UkHwZcoh6u751_nDTq1SFhTjmoe8J4eftKr8MIGeZy7aUcMSwbGw89iR0G-SxHiZZ2VmHcAakLWY61tGNDQY7grd8nHi1vgqQHN4sTiDxKdOoKqQLYySQVqZZlA44hbiGDkMd0cvAgEdJYoiYatF6M22JEKD94gBEPcOk2r-H_VBccahzpicGWrGghnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

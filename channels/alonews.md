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
<img src="https://cdn4.telesco.pe/file/TYpCHI7OhRB_ihME0vi5QUjmqQTELvdNXq8KuSYTn2eB33Ga3rS6BbRBvQ4zwA8qid5Z4KIdxIaMhRnMvbQ_8RQuY66G-Ks51zhOD1Dca2lqSTcBwJVWzt9ZYTwVHo9JlOetGTJTMYulzgifRZJ4ky47tnqIfuUM0huLnf3Sio9PXPVnZgh5zafwU7zPZE4K6ZDPx4jWgkFomkQs3mDaZ-vpW6OJ_1AZXxdEoq8RYM9YyVQBx1J_gRNeoUU_UryhvLvCEGkiqMu9GgBrCgnHHHqqb80wsW0X8bFeNyyFQM7bRB5RMDbtjh-0tbeegxdt-yHA3_nwNo0HVu68E0KWSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-151592">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLv7KCPIPVFBc7sqK8m_tr7QqvrIUuRIdIaLtlXyZ6nlLEZMnsEi6WhpU_rbxItn8At4vPuBetmhF6BtA5rY1R9LPLuI40efvDk39lZRZRuCCV_l0CP-bJSXkGJsokyQ3iHcjkBaybRTEfgG79NH3ThS3Lg8SJAy9m8yfP3Wx__UGbeGsYg7VS73_AlKixOiG9X3HPzqypqXZguQlsZnHu9_VHdfIM9H6g2-PdN4x1nhZtNNyJHubjdC00-4nAj9COrqWq1lC6peV9hxTCHo-EV1IEgfpkQZuokyIYfCd8pzVEXeBu77ciSvtEJMQf0fvRXMg9TtC2HqJiecyOgnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز، ۱۶ مهر، روز بزرگداشت داریوش بزرگ است؛ پادشاهی که امپراتوری هخامنشی را به اوج قدرت، نظم و گستردگی رساند و تخت جمشید را بنیان نهاد. یادبود مردی که نامش برای همیشه با شکوه تمدن ایران گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/151592" target="_blank">📅 12:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151591">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFeUoCu_S_ZHI7171Juiro9DxGMk18xmIrN1vRakhT1q2dDIKIarybWp-c-FENHuVitMWZuZdPvG5jr2_FRpivNjMMwun-vWmTW7VbhFLiSXJZoP0r1DujManF_bITopmx5So5MxxNW7jQifxqlqjZk7444PjW9DCCRTwybxf7-8Fgn6AVx5OQ_NIIQYg9PUCUMUcVz8iKNbJlkvg9wmJ0GheO6p3YlXUG9Rvg3hU0uPK0WzDt5LTdY9ZzasGmeERd7QRHqnrCWymyt2Q-QjB8f48hJ5-QVhoUbistBJvQeBXIILN-FA0arKFejCpq2Fc4xT1K5pPc6krB2zXSbniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش آکسیوس و به نقل از مقام‌های آمریکایی: پنتاگون به سنتکام دستور داده که آماده‌سازی‌ها برای احتمال ازسرگیری عملیات‌های جنگی گسترده علیه ایران را نهایی کند. هنوز هیچ تاریخی برای این عملیات تعیین نشده و دونالد ترامپ نیز هنوز تصمیم نهایی را نگرفته است.
‏
🔴
با این حال، منابع آمریکایی و اسرائیلی می‌گویند حملات مجدد ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر آغاز شود و حتی احتمال دارد یک هفته زودتر، یعنی پیش از انتخابات اسرائیل، شروع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/151591" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151590">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4v4Mal8v6jOytcxgymVWXi7fsO4tga3MEvhSya6acodMZycaLs7Mc7Qke0tJXllSRvSXuMsm4LN2TM9zgxp7RONxglYbgABsAY2a2a4gLjmgINbwBDesgZkL7Wu-Pew_pau6f-f19aW3C5OuUNIrbjXJDIrtIRFTvzjZtRw7PdG5EXxE3O2B8xN2AkFkbRzgRQVA_GeTAbqBywFwdQSAfn8gFSdcJDV7poD8h5wI_rv--IzIDujuBNogyi1NNkvWhjXusqxC-lo9Orz3Nie4LJPhGqzv1F2FwcJJK7Z2M-cIFm6jvrP6VIqJmS5tTWJDpXpUnkVp2thuvDj4NeMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای نظامی نوع C-130J متعلق به کویت، به پایگاه هوایی الخرج در عربستان سعودی رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/151590" target="_blank">📅 12:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151589">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afe7ea756.mp4?token=KNUIzcZ0VS-aVFclAHl3C7GOUaFRfdte85Z_aowWNALHhYTS0pWJgN59v04hu9Z2KRwB5V4YSqJ3fuKmYzvdxUfiEYE0xMuUD5Dq05FxvW9ktj82J9XglXNCo_eJyVxCumj99M05nVzK7o6x_RGpYrh65TGPcS8x1U8lQUzhOrz1aNl9uczIAPOUakYN60JXKE4tGhcwIZOUNhWgk9iVGjG8SFmDoP3KZICyP6xuHEgYTtpbSQznQOd-6HXHi7-HbKxteluXx_Zy94jXPQ1QGo8qW8-YIS1vLGx8R2_ABDYw_aQux0jm6MkwyD4lYOs7qwHXpmQOJDqNwuadeY7Mug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afe7ea756.mp4?token=KNUIzcZ0VS-aVFclAHl3C7GOUaFRfdte85Z_aowWNALHhYTS0pWJgN59v04hu9Z2KRwB5V4YSqJ3fuKmYzvdxUfiEYE0xMuUD5Dq05FxvW9ktj82J9XglXNCo_eJyVxCumj99M05nVzK7o6x_RGpYrh65TGPcS8x1U8lQUzhOrz1aNl9uczIAPOUakYN60JXKE4tGhcwIZOUNhWgk9iVGjG8SFmDoP3KZICyP6xuHEgYTtpbSQznQOd-6HXHi7-HbKxteluXx_Zy94jXPQ1QGo8qW8-YIS1vLGx8R2_ABDYw_aQux0jm6MkwyD4lYOs7qwHXpmQOJDqNwuadeY7Mug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پل هوایی آمریکا به سمت خاورمیانه همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/151589" target="_blank">📅 12:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151588">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خارجه اسرائیل: کنسولگری بریتانیا در قدس امروز فعالیت‌های خود را پایان می‌دهد و در نتیجه آن، انگلیس هیچ اقدامی علیه ما انجام نخواهد داد
🔴
بریتانیا می‌تواند فعالیت‌های محدود خود را در این ساختمان با حضور تنها ۷ دیپلمات ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/151588" target="_blank">📅 12:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151587">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ایلام با تورم نقطه‌ای ۱۱۴.۳ درصد در شهریورماه صدرنشین استان‌های کشور شد و فاصله تورمی استان‌ها به ۳۹.۷ واحد درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151587" target="_blank">📅 12:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151586">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری رویترز:  یک ماه پیش، ایران 200 میلیون دلار به حزب الله کمک کرده.این پول خرج مردم آواره میشه، حزب‌الله قصد داره تو مرحله اول به هر خانواده‌ آواره، 3 هزار دلار پرداخت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/151586" target="_blank">📅 11:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151585">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNsS8_ThokPxqYpDMlVwFt2-1JliEbYkfvpaPIMNDJYPcy9A8IqHKxez1Naph9PnsN8uUCmmLdFteYruiKQ99yGLOLv3o7TxfJrLL-4sTIfBDuuqGut-Xpmo5z0m2aDYlQz_1t015H6ujpjbhrLrpvNmQmj2W9z_aKnRKPFNP9DWPS6ackESAzQaLr8D-reOPypMSpwAT07gs9qneyCeHY1TDIksHCCVDT4yeuuFXkQTLURntmVMhix1N3-dHNnMIOdPKyC3zcssbjBiJSDKPnH7fwA_LsqSJpJo9t_ddWgx04NJcAgMMw2GbqdTHMxi1_8fmlombqymublzRjS7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردانی که فقط در برابر خدا زانو می‌زنند؛ تصویری از سال ۲۰۱۵ در سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151585" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151584">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp6AeqDnrC4Y1RO8KdlUuYY-2g-HPDt0PEEXRaiSWloE9Cw-65SjbKjjCRCkib1NIQaEPu49SYygnKZxVUEyKt5ryIG6z8WTr0gup_ED2yPRTWtxHUD-zJSR5FMKZjeUMG6bpDesoF9zDiM2ifZ_xR3BV50akT9Gy_Ll30xEpAZIpawJ0IkkrUBZN9wB0_MxJ9yptV-NgdrYZ5SYoaVoVI-jo_v35s5tbDkFrBoukJTnAna9c0ifyLT27p75ul0oAH9B0nbKgUfKNNtawo4UFDPcogRfgjTpPeYDDnsjzn3GR6VJBdlGbCgE0-bYsupiELzATAvVeRbK1nBDj45-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ممنوعیت پروازهای هوایی به فرودگاه بین‌المللی ریاض در یمن همچنان برقرار است. ۱۱ هواپیما از فرود آمدن در این فرودگاه خودداری می‌کنند و مسیرهای دایره‌ای در نزدیکی آن پرواز می‌کنند، و برخی از آن‌ها مسیر خود را به سمت فرودگاه‌های دیگر تغییر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/151584" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151583">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151583" target="_blank">📅 11:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شرکت هواپیمایی عراق (Iraqi Airways) پس از ماه‌ها توقف، پروازهای خود از فرودگاه بین‌المللی نجف به تهران را ازسر گرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151582" target="_blank">📅 11:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151581">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دولت سوریه پیوستن این کشور به جنگ علیه حوثی‌ها را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/151581" target="_blank">📅 11:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151580">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94aa88e0.mp4?token=jgsDLCzGLAbFdYJi2H-U8A2RmJucykX05SUJT62JgUBU3gIZWxzw-_sMkO8Iq0gf8UL4ZKaI2Dt-Y3AGJEFALgTjxUNkYmcQSw61SPYh5hQXjiUwazr7BDOk0lIew_nHgwFJj9qZztFJ8h9kH7ZgYYsea9plbxxgicLlPQcxaMz_lQPH46ixifodFreu1HfarinWvgE8J9fDeHSgEhISuK1nnNq0t4EviScf4NqgVJipxFc-paCWqRn71lVSBHiirXVCmjyFK7PTdRQXOgrRCtn1cGmrWhkZW5iQisCDBCydU3wi0TlhOSNFcdtJNDhRPZCUFPbKDlTyRmSU2hOhoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94aa88e0.mp4?token=jgsDLCzGLAbFdYJi2H-U8A2RmJucykX05SUJT62JgUBU3gIZWxzw-_sMkO8Iq0gf8UL4ZKaI2Dt-Y3AGJEFALgTjxUNkYmcQSw61SPYh5hQXjiUwazr7BDOk0lIew_nHgwFJj9qZztFJ8h9kH7ZgYYsea9plbxxgicLlPQcxaMz_lQPH46ixifodFreu1HfarinWvgE8J9fDeHSgEhISuK1nnNq0t4EviScf4NqgVJipxFc-paCWqRn71lVSBHiirXVCmjyFK7PTdRQXOgrRCtn1cGmrWhkZW5iQisCDBCydU3wi0TlhOSNFcdtJNDhRPZCUFPbKDlTyRmSU2hOhoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد دانشگاه امام صادق: برای دفاع و حمله دیگه چیزی نداریم و همشو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151580" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151579">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02b0d385.mp4?token=Fxdp0tUF8nMyTURWXmglngPYK0WfZjx24fzjcuvrKjtHEt8NqqGKOEEWNksDE0RgmG7I3WDzRqYFDN9ef3QdVfUM-ZVoMzr8wsAdmW2p18c9liNzfJuY3opasPpyw33N5f7J-8ekhWiUTtO5WEUNBlwqJxfpVFVMy-P2XkHB1olVuEAptUzYTE2kHzHS1A5hMSZuC6qP3Lky1hVFSga_kWmOERRS8nt4-epkv8MiU24IWRRxIutFj-CcKTCqkUyaU164Pt-H7b0LBf3y--Vbd2dRRQsEyXg9ckFdaSSXnsXL8T2sRkqZT8oi3DWwxXhdb7Fu1BLTXww3zz-4kTRiOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02b0d385.mp4?token=Fxdp0tUF8nMyTURWXmglngPYK0WfZjx24fzjcuvrKjtHEt8NqqGKOEEWNksDE0RgmG7I3WDzRqYFDN9ef3QdVfUM-ZVoMzr8wsAdmW2p18c9liNzfJuY3opasPpyw33N5f7J-8ekhWiUTtO5WEUNBlwqJxfpVFVMy-P2XkHB1olVuEAptUzYTE2kHzHS1A5hMSZuC6qP3Lky1hVFSga_kWmOERRS8nt4-epkv8MiU24IWRRxIutFj-CcKTCqkUyaU164Pt-H7b0LBf3y--Vbd2dRRQsEyXg9ckFdaSSXnsXL8T2sRkqZT8oi3DWwxXhdb7Fu1BLTXww3zz-4kTRiOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه درگیری دیشب در تگزاس وسط سخنرانی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151579" target="_blank">📅 10:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151578">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: پنتاگون به فرماندهی مرکزی آمریکا (CENTCOM) دستور داده است آماده‌سازی‌ها برای احتمال ازسرگیری عملیات‌های گسترده نظامی علیه ایران را تکمیل کند
🔴
بر اساس این گزارش، حملات ممکن است پیش از انتخابات اسرائیل و آمریکا آغاز شوند؛ با این حال، دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده و هیچ تاریخی نیز تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151578" target="_blank">📅 10:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151577">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNvnKegI-ZKD5nqqO18AQxPQmXAIrAe7ARMUlsHQ2bTTPPnExeZxkb_Vaf2pTwesAWRkQ7SC3lINe6Dg_3cLywINmF2S1lKlG6vTL90jKMYbHem6w2IT1wP5AKPuJz5pQFnAch3YVTjlil0wBkVX7jYzFph80NNHxftV1KA9qbZQQRqoS_INcGOHYdHhGM9ybqbPmrKsbtek3MOb7GkuH4cdo9m6BlK6f-mwrKPX_yuMlogs4DNqYJsY52T8tKNt_AVqiVcjLbqHqsRkWypRreVECZRBY0F5vwRSCBQmTbUuqlSoeQuGbrfJYbh0MLAD1ODRZ8_QoxecT2pHbzbpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اسطوره کریستیانو رونالدو پست لیونل مسی رو لایک کرد و نوشت: «لئو، سال‌های زیادی برای کشورت جنگیدی و میراثی از خودت به جا گذاشتی که برای همیشه ماندگار خواهد بود. تمام احترام من برای تو بابت تمام دستاوردهایی که با آرژانتین کسب کردی. یک بغل گرم!.»
@AloSport</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151577" target="_blank">📅 10:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/151576" target="_blank">📅 10:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151575">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ان‌بی‌سی: دولت ترامپ خواهان توافقی است که مسائل مهمی مانند برنامه هسته‌ای ایران، را حل‌ کند
🔴
واشنگتن علاقه‌ای ندارد تا بار دیگر با تهران به یک یادداشت تفاهم درباره تنگه هرمز دست یابد و مذاکرات هسته‌ای را به آینده موکول کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151575" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151573">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c407317afc.mp4?token=ECo0dXtLfw2QottIA7LuJCLqiukDSUsQ1MkraJfak3Sj7MQU5s0KMh-Ujd91JaPlpkDoo2ojouEbTh0CaoAcY01dVtnja35v1Bvre47hbds5a8hbH7W3yV5lTWrZvtBu19FvWolwtRgBqyoa2Dt62Qysyo__Bq9opKv5bjo8UUkYuPWBX2JIeM-HlB7nJuALiMd1cUY6O1XPRVOI0rIVQ558S8xeUHr0C1p9WZJuUNthQcYD_RAqilKVVdQ9ahCOFpGW1PDtYFZ3Ysz7hLvP2XccgN-k72lmELC2WbQGLWi0U7vrjAVcydYa8zYob8n3G-FVZYQAGgK6fvDdEGZa2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c407317afc.mp4?token=ECo0dXtLfw2QottIA7LuJCLqiukDSUsQ1MkraJfak3Sj7MQU5s0KMh-Ujd91JaPlpkDoo2ojouEbTh0CaoAcY01dVtnja35v1Bvre47hbds5a8hbH7W3yV5lTWrZvtBu19FvWolwtRgBqyoa2Dt62Qysyo__Bq9opKv5bjo8UUkYuPWBX2JIeM-HlB7nJuALiMd1cUY6O1XPRVOI0rIVQ558S8xeUHr0C1p9WZJuUNthQcYD_RAqilKVVdQ9ahCOFpGW1PDtYFZ3Ysz7hLvP2XccgN-k72lmELC2WbQGLWi0U7vrjAVcydYa8zYob8n3G-FVZYQAGgK6fvDdEGZa2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، دود برخاسته از بندر دوحه در قطر را نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151573" target="_blank">📅 10:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151572">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOzVtq9ct_pK4WtDuL2AujgqnujALcvZDReTq8w5_2F30nUeaUHIW6PChipQbDruAVf4Vlsuzt73VAS4-UMRoeBVCyjw2xjNBObqlBUjyLmQhNUF9TeBkvGiaVQhOkLYTDXT4ge7bXQo3S-aA9ct7xZOjBtODP0WaHhTQxb-dHslhgKON3yu5FfLURQcViAhwLS0n-sxmhJSGvVv-02NIoBDPq3jH0aNfkBL7hvbOkeFn3bT5PCA9y8zYfwOwzjYEPoVHsciYXRvatr_lOXYR5hJ_L5e_p84QOvrnpgqubZgGG6reL1KSh-1oWyVo7wdNr3tvYaxqZw1EujFyavPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل: خرج خونه با دخترم بود، ۳۵میلیون حقوق میگرفت که خرج خونه میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151572" target="_blank">📅 10:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151571">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش در سواحل قطر هدف اصابت یک پرتابه قرار گرفته است.
🔴
این حادثه در حالی رخ داده که گزارش‌هایی درباره تلفات جانی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151571" target="_blank">📅 10:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151570">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ در مورد محاصره دریایی ایران:
اما آن‌ها مایلند هر چیزی را به ما پیشنهاد کنند تا ما متوقف شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151570" target="_blank">📅 10:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151569">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VrjkAK5Zcv1uGsqs1wAbMKG3ZzjQilXiqgywzWzoHGAWNbhdwPu-g_lKdpdYXYlRWceQi6Xln74T1qxnF_jCIiIKKHP0kooFlsAL041pxk60vVy677ESG8PSvq2l9iaHdJzSmxL504ahPxA2HJAVrv-BW6gLCYs6_c1OU9jvKzi5xVAfZV0qr6peueqrXk7_X2UKBmMILfW9OCqi5B3fK5Sk-GpIMzSaOagztrO9iB2PZX8-UCDRdxK1xbffk8p8Pkq2Cv97zZ76FvHAuO8y7USP2fqXm7jONzhG-YVmxEmxYLamYX-7fQJ1MOx0QN0KxFOi0flk0MQQPYw1OZTOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اثر برخورد صاعقه به یک هواپیمای هندی، دماغه‌ی هواپیما آسیب دید.
🔴
خلبان هواپیما را به سلامت فرود آورد و به کسی آسیبی نرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151569" target="_blank">📅 10:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151568">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_El5z3Hwqb8Fng6IxmONkF2GmW6RyACGeMj47UOkfiV24lmHaCEG2sUusu2xnX2kC48xyucxwYVpUVXyQWzF9sNqGxO-Wpeky96TAT3IyFqcnXRLZgXPFSu3bknoI4DrQk64UUarANJRyJT-x7d6RoSkFajD417yXGZFilwrfziqPqDNkjcYQo7kL4UNi6NlgHWxSyH7-h3PyodQHnj1ZILgCkMX47YgtsRx6PbzvACcchoTKjSPR1oyxX0teiOrjZhiQblOiIcK1gz_sdrH_GJFg4azd37M9T_5gx70ECzhgxYIAdVCBLWDB8ZQzStx_Op03H76mhcJS39EuzguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
قیمت نفت به سطح پیش از جنگ رسیده است!
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151568" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ie99SVncIJhvQelRoCEtB1zi1jLRP_Rt5F02d-6oERWmHnViZu9Kcbcd5qDaMbdJRexp5ZaqO0Tpl6NqzEntVfeqoQrBByR86Fw1f4JppstPjG3h_TjRHnEyu17zLUsiO86iKc85u7QGOTE2FnZocE9cVG_yiWlcg1kqXl75LQULtN3RKjV5ERThaobnvP24rPt4FSei4wsPIGOel9RSnRg5pFRvzDPV2nezAbb2lOiOrGRzBBtsXxR62hPbiVmq_IWci7lbfJ2wy26NVTNVXjV6Vjt_p_Ac1hHjlorzI5Suat7xe5rfMqSeo1jwPOtcQ7a_t2EVPrNhcHdwN0YDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3i-ZzCGpHHVUSl4j-sAiRx9NpVV1rROCwGrc7mX8fcKCBc6FRDHLEJPAy9u5uo46bgzseiGofbDFXDjbDlIwwwXKdH6F7mwcPIbPng1ZjwCsj7hPYCuhy0d9MgzRmlaX3tr8Zcg5WrCI95YLUlk_-tw-MzSOuF2lGYNDYazzQcia8XkfuM2OQUfno5ILWoExMK8Xecob_tAfUi6Y5KITHd4pC6DnflGbfXy49R698U-SuJitahtEWlF0m2xO3_bBoj-pAQmw1egH3rBAlKrRrW55bqAFiPQUqoPvwlxPGgV5oh_OFLh7K4YEThH72qAKfpq8ucw9WScqxwuSkSO3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید، آتش‌سوزی در خلیج عمان را نشان می‌دهند. این آتش‌سوزی در فاصله حدود 30 مایلی دریایی به سمت شرق شهر الفجیره، در سواحل امارات متحده عربی، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/151566" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUZnl1i1g55OXok_U74jAVBJBgxxLu5H0MvIGAHnphnUxEYv9bo2B4Lq8ymRlLCJuB_GXN8vpV5DnKVVnGgeeuOvNSBCrwZmrvfkYM8GeIdJ49n28mn-dnun9dHtc6Ok905hHKgw7Xw2nkW_J_y80QDyHrKWcYFc7hAxodIzc3t1fjWkjlZGDjPq28FMKkNqaJceJyHOHaH5QTl-M2SXsCtkCQErBf7kGzfGYVwoSNuaeO1L1NfQyce7QqKCgDvL41W-GnACxR47cpnuEAukY6v0AwtdOVpEpH7Rq8CqM14FbVXC3S_DSI_IDKVe4z6pKttdEemu9eSFCm4eRBI2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه قرار است طی روزهای آینده، توافق‌نامه ائتلاف دفاعی مکه با عربستان سعودی و پاکستان را برای تصویب و تنفیذ به پارلمان ارائه کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151565" target="_blank">📅 09:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رویترز: با پایان یافتن مهلت تعیین‌شده از سوی اسرائیل برای تعطیلی کنسولگری بریتانیا در قدس، این نهاد دیپلماتیک اقدام به پایین آوردن و برداشتن تابلوهای خود کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151564" target="_blank">📅 09:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5284d320.mp4?token=bcMQ2SVgbaoW0hl_yyYnPWFoYk5xPikYv66w8p3OzJYktTGNMI2sHJPLCJXqJ0OMZW9pl181BooqoXXLJ1yd_osKCSpIGZNAjHSNQTuvsq02os53SkM3b5jo5lkCAKlJspgmb3Bswh9anbiSUcZO7DQMO1OWIwCizQP0ect_psZUDH_qGaci3-SEr8DHh0fNZXRK8S27Nag7s94OO2jLhQzxtOJ885jgu-ioscdypPF_f1QkVrS9cLwGzGZP_6h8yzSoNwcHhAWc1PrtPVPqacTK-37dQTbS8BcfnnwA4T34iNyJ5WxB5cr5KkApK62dIVwD7iQV3xigVY1qDpQMlHIWmOV_8-fFt8Du6W9Ywu6EhmxLmRqgo1hWRCKmRD3AJvwNvNTKEr70bacw_qyvsglcYEnRWH3h7NnkzuO5xEgx-i7st1YOc4v00lJbp02Ks6LjtYjN87tvK6wUXq7fNPH4lEpLz-z8QHsswRvUVw5B_L0hCB2IL54uE4WfumY2KkS6l_PiBIJabjhB3FIx1GPJJo_qPwWFyj_obPNZsi2B51UqQUBngOsQqnkFyNb1k0_bI4EihInQJNhZwobKYHhul50EwbM6vszhIFa6Boi0jNClYSEWHFq2hk2jWWm9UEj_0BPZEU93CY-UDhZlOiSi7MeEtPIO4xtx3QjygIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5284d320.mp4?token=bcMQ2SVgbaoW0hl_yyYnPWFoYk5xPikYv66w8p3OzJYktTGNMI2sHJPLCJXqJ0OMZW9pl181BooqoXXLJ1yd_osKCSpIGZNAjHSNQTuvsq02os53SkM3b5jo5lkCAKlJspgmb3Bswh9anbiSUcZO7DQMO1OWIwCizQP0ect_psZUDH_qGaci3-SEr8DHh0fNZXRK8S27Nag7s94OO2jLhQzxtOJ885jgu-ioscdypPF_f1QkVrS9cLwGzGZP_6h8yzSoNwcHhAWc1PrtPVPqacTK-37dQTbS8BcfnnwA4T34iNyJ5WxB5cr5KkApK62dIVwD7iQV3xigVY1qDpQMlHIWmOV_8-fFt8Du6W9Ywu6EhmxLmRqgo1hWRCKmRD3AJvwNvNTKEr70bacw_qyvsglcYEnRWH3h7NnkzuO5xEgx-i7st1YOc4v00lJbp02Ks6LjtYjN87tvK6wUXq7fNPH4lEpLz-z8QHsswRvUVw5B_L0hCB2IL54uE4WfumY2KkS6l_PiBIJabjhB3FIx1GPJJo_qPwWFyj_obPNZsi2B51UqQUBngOsQqnkFyNb1k0_bI4EihInQJNhZwobKYHhul50EwbM6vszhIFa6Boi0jNClYSEWHFq2hk2jWWm9UEj_0BPZEU93CY-UDhZlOiSi7MeEtPIO4xtx3QjygIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ما اخیراً اعلام کردیم که قرار است عدالت نهایی را درباره یک قاتل شرور، نضال حسن، عامل تیراندازی فورت هود، اجرا کنیم؛ کسی که در اینجا، در تگزاس، ۱۴ انسان بی‌گناه را به قتل رساند و ده‌ها نفر دیگر را زخمی کرد و هنگام این حمله فریاد می‌زد: «الله اکبر، الله اکبر.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151563" target="_blank">📅 09:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
«همان‌طور که قول داده بودم، اطمینان حاصل می‌کنم که ایران هرگز به سلاح هسته‌ای دست پیدا نکند. آنها این را می‌دانند.
🔴
ما به‌زودی از آنجا خارج خواهیم شد و خواهید دید که قیمت نفت مثل سنگ سقوط خواهد کرد و قیمت همه‌چیز نیز پایین خواهد آمد.
🔴
این عملیات بزرگی بود که روسای‌جمهور قبلی باید طی سال‌های گذشته انجام می‌دادند. باید انجام می‌شد، اما هیچ‌کس حاضر نبود مسئولیت آن را بر عهده بگیرد. ما چاره‌ای نداشتیم، چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151562" target="_blank">📅 09:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151561">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=ORWpH-FCrGZxBwRO2KMHE8POAt9Bxmw01vi5mcLhQmkrfF_FzTp5lR6Dh696bKuL4c-13bSkDKkohk2GZ4buDi8m1DV-PE0bs95G34aMvtJlmj2Qf0HtJcLyFUJoGaCrPCrh1X68U6AARjP1nySSvjCLmvpUzG23xqW5ZcSKsOb_W_qVWitCk4wxTMr1-nsQWMlc7NwuvU2NBdl1Le9-ckN9B3y58l_6GLma3wM8vB5RHorAEHA62nM4daQB-L5eDg7v3s9KTEdGZ40l1Dq2XJ04uyjzhlcJg3x515R0DqdgIgnK3wiVYyMln2fmDZnyvP7weHhL616YN5gIb933Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=ORWpH-FCrGZxBwRO2KMHE8POAt9Bxmw01vi5mcLhQmkrfF_FzTp5lR6Dh696bKuL4c-13bSkDKkohk2GZ4buDi8m1DV-PE0bs95G34aMvtJlmj2Qf0HtJcLyFUJoGaCrPCrh1X68U6AARjP1nySSvjCLmvpUzG23xqW5ZcSKsOb_W_qVWitCk4wxTMr1-nsQWMlc7NwuvU2NBdl1Le9-ckN9B3y58l_6GLma3wM8vB5RHorAEHA62nM4daQB-L5eDg7v3s9KTEdGZ40l1Dq2XJ04uyjzhlcJg3x515R0DqdgIgnK3wiVYyMln2fmDZnyvP7weHhL616YN5gIb933Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : استیو ویتکاف در حال کار روی توافق با ایران است و عملکرد بسیار خوبی دارد
🔴
فکر می‌کنم این توافق واقعاً چیزی نیست که من بخواهم انجام دهم، اما آنها حاضرند هر چیزی به ما پیشنهاد دهند تا این درگیری متوقف شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151561" target="_blank">📅 09:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151560">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad876addc2.mp4?token=kxdyOKbsioMnho5dsYaGIxWezyAE_k9juhdJtrIE6DLfMnq_8r4qBMoujgpDEgO6N24HLnFPtbiMo2svMu94RYr199i34sdA2Y5HN-N2FYZ-VL5Bnu8yNl6PQ2vyTD1TdfclzCVT7aKApw4O16OQnC4g2GCZUhZca-ZM96-Jk-Wu0CS7ZG0CXm-6rwtLKtej1eOZEekEziHrz4IubOC6wfjOgGrZi3d61ZW2lYHkNszPVe5Np90sYU9VuEj_tbDoNXuF22FqJ9ak_Px5S5RfmglEpfBGPtwg6hQeE6BIWBisNfNwS8lbSBNM8Kmkab2_p59La3E9iJB3QDfj6O2-QSmjTo_IaqEmhqoPTyKyZ9FZCXJBuc04YqTirxFQUMLf0SmE2w_YwZWY8VmQ-Jc9pX9oN4-yGbAP8yCIUmk1L7f6jJiwkHTagg6CkSX9VBIOCinNFk8KQti3mAZyPk5WV5c3yWY2EKo_3hvxylrDy1KoBVmqFe1HwcTZGwJ0stjjeLPbgPVQ0Mi6r8_lFBHliS4IX7ty30e3IVFL1ZhfYDeDfjCvKibLKczMfKzCTcEsJGC2irl-KiMbR1ee7FJ3ae-nZu6k3Co0QoSzCJwUD4epVUaeDJa5EMrCPHu8OXipP-7mBqAR7KrcRF3ddOlYe_P22BCk-1izXqFJbmLTuqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad876addc2.mp4?token=kxdyOKbsioMnho5dsYaGIxWezyAE_k9juhdJtrIE6DLfMnq_8r4qBMoujgpDEgO6N24HLnFPtbiMo2svMu94RYr199i34sdA2Y5HN-N2FYZ-VL5Bnu8yNl6PQ2vyTD1TdfclzCVT7aKApw4O16OQnC4g2GCZUhZca-ZM96-Jk-Wu0CS7ZG0CXm-6rwtLKtej1eOZEekEziHrz4IubOC6wfjOgGrZi3d61ZW2lYHkNszPVe5Np90sYU9VuEj_tbDoNXuF22FqJ9ak_Px5S5RfmglEpfBGPtwg6hQeE6BIWBisNfNwS8lbSBNM8Kmkab2_p59La3E9iJB3QDfj6O2-QSmjTo_IaqEmhqoPTyKyZ9FZCXJBuc04YqTirxFQUMLf0SmE2w_YwZWY8VmQ-Jc9pX9oN4-yGbAP8yCIUmk1L7f6jJiwkHTagg6CkSX9VBIOCinNFk8KQti3mAZyPk5WV5c3yWY2EKo_3hvxylrDy1KoBVmqFe1HwcTZGwJ0stjjeLPbgPVQ0Mi6r8_lFBHliS4IX7ty30e3IVFL1ZhfYDeDfjCvKibLKczMfKzCTcEsJGC2irl-KiMbR1ee7FJ3ae-nZu6k3Co0QoSzCJwUD4epVUaeDJa5EMrCPHu8OXipP-7mBqAR7KrcRF3ddOlYe_P22BCk-1izXqFJbmLTuqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما کارتل‌های مواد مخدر را به‌شدت سرکوب کرده‌ایم و ورود مواد مخدر از طریق اقیانوس و دریا ۹۷ درصد کاهش یافته است.
🔴
ما تلاش می‌کنیم آن ۳ درصد باقی‌مانده را هم پیدا کنیم؛ چون از نظر ما، کسانی که هنوز این کار را انجام می‌دهند، از شجاع‌ترین افراد دنیا هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151560" target="_blank">📅 09:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd6090717.mp4?token=lhjaLrkJv4-6J7CPotNHVZcqoK-7UNRzMlEMRgt5JvtA9cLCtNf4RmWZMJoox-nQyM6eWIyEgxavHOL-V9NjdQ9Dcn-7_cS3O6p5xinZtnDyixHAOvjJS9guaNrW3Y9fyj3L1OLHH0zIpaCTLYTWWgYSRsvhMNItu7tO_d0CmtivTcpm9rmxzvxe3HHTDeyMoCwDQCzMx60WbzVfSIZyk4BN85oYyPqd0C5l0Fj0sqnPlGy0FUTuoZD6E4Oj9Cm_RVhCmiIgSV2V_mm_xgdjI3hJMfXDEPKXD7wUDcLmfcCq2pCXPPi3i72EHGjQMdjoYpPQg_8QEEpo_sqhMrLmCxGCcjhS3Dha3nB5VLyViaEH5UWp9RBbPxW4uDSEH4k-CY8vlxr-nIpWevUUmhFufPodxHsf4K90zLXC9irs4TOtlgwfsYYs_bNjtOmIIN_vdg95fh5A3RoAT-TtfMLVW0oOR_cZMJZSBiPnihsYC7w0jV3Lbnjw5iYXWXwtFYCfyXAZOm4_xpNkVg9znMBMTrdbg2ywF4dGgupQu1EslhDVNGDzQr6WwMtxAOJCxjNb8Y0MG2vT9tSrSTFXILTPCisr5LzOG8TUWNnzz2pa0lfBvOwQGchaKTt7W7BeRCN_DAxJ3tRTYCfMiu8v0CT8c3Mmje2y_WUAkuhRTSRWMUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd6090717.mp4?token=lhjaLrkJv4-6J7CPotNHVZcqoK-7UNRzMlEMRgt5JvtA9cLCtNf4RmWZMJoox-nQyM6eWIyEgxavHOL-V9NjdQ9Dcn-7_cS3O6p5xinZtnDyixHAOvjJS9guaNrW3Y9fyj3L1OLHH0zIpaCTLYTWWgYSRsvhMNItu7tO_d0CmtivTcpm9rmxzvxe3HHTDeyMoCwDQCzMx60WbzVfSIZyk4BN85oYyPqd0C5l0Fj0sqnPlGy0FUTuoZD6E4Oj9Cm_RVhCmiIgSV2V_mm_xgdjI3hJMfXDEPKXD7wUDcLmfcCq2pCXPPi3i72EHGjQMdjoYpPQg_8QEEpo_sqhMrLmCxGCcjhS3Dha3nB5VLyViaEH5UWp9RBbPxW4uDSEH4k-CY8vlxr-nIpWevUUmhFufPodxHsf4K90zLXC9irs4TOtlgwfsYYs_bNjtOmIIN_vdg95fh5A3RoAT-TtfMLVW0oOR_cZMJZSBiPnihsYC7w0jV3Lbnjw5iYXWXwtFYCfyXAZOm4_xpNkVg9znMBMTrdbg2ywF4dGgupQu1EslhDVNGDzQr6WwMtxAOJCxjNb8Y0MG2vT9tSrSTFXILTPCisr5LzOG8TUWNnzz2pa0lfBvOwQGchaKTt7W7BeRCN_DAxJ3tRTYCfMiu8v0CT8c3Mmje2y_WUAkuhRTSRWMUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
«می‌خواهید تروما و مشکلات را ببینید؟ بگذارید آنها در مسیر، یک موشک به سمت سن‌دیگو یا لس‌آنجلس شلیک کنند.
🔴
می‌خواهید صحنه‌ای وحشتناک ببینید؟ می‌خواهید مشکلات را ببینید؟ بگذارید سن‌دیگو یا لس‌آنجلس را هدف قرار دهند.
🔴
ما اجازه نخواهیم داد چنین اتفاقی بیفتد. ما از شهرهایمان و کشورمان محافظت می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151559" target="_blank">📅 09:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ : ما دیکتاتور قانون‌شکن ونزوئلا، نیکلاس مادورو، را دستگیر کردیم و در آن جنگ پیروز شدیم. ما آن جنگ را بدون هیچ کشته‌ای پیروز شدیم؛ هیچ‌یک از نیروهای ما کشته نشدند.
🔴
ما یک خلبان بالگرد بزرگ و خوش‌هیکل داشتیم. پای او وضعیت خوبی نداشت. اما ما این عملیات را بدون هیچ کشته‌ای انجام دادیم.
🔴
این یک یورش خشونت‌آمیز، باورنکردنی و در عین حال زیبا بود که به‌طور کامل انجام شد؛ برخلاف دولت‌های قبلی که در آن‌ها بالگردها با یکدیگر برخورد می‌کردند، زندانیان و سربازان به گروگان گرفته می‌شدند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151558" target="_blank">📅 09:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692423844c.mp4?token=CtSwXHkiJeb90QGDmvuiNHjIzolmI0GpS1FViXJzqXC6LLHqmHw_Ag4VltVt702VhvnGngu02Qn7CGKzmMHL-n3wYYAksq_fePkadGzomzCJZqzlfy5yRLy4-BUtbXoFeGVaaKJS-r_jH9ByfZ7ChBGBmaRhv9i9bMnfYVzdRM816Y6oFP4CSn9KFTCBznCflK8h3VsVY5lXzXSIIck8-w3Xfc6bO89VbfvvGVAdtq36saTpe0HKipUEc76dOl9d3PKc0aJaaec2k_pWTn4Sb-LoTmOrZQ7cevFoC0OXQcUnhh_bzlsuintFE_wjzC37XvuxCxVmhbIM2uCI75WqcJaC_QJtpwvxCE7_dpxmNhrUsX_Co172K32fY-vTuUGhgRoF4pRPM3Z-9lc1CE1iSan9jo9WZtrngpnhO7_sGBPMPorHeGGETU1d35nHAlJ1oab9JbGlBxydCeSD7i1TDVXaVzyPjS_R62ZtXuotOXStigt_KL-cGvaOgpNCNGRpw1E_urp-dZbTG98hnahYjUmus0Yqhk756TyXbJS7AW1OSIpvAO3-clZDPlQ9MCBkM9UNvWz6RtDD8gzXyAmEGJW-5gyTl8qnpfkuGAxV5egI806doemsFaGV4W9dc75fzCNWcYuIp09FVLhQ9v9kG570MI9txTCdS_4bdodoKq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692423844c.mp4?token=CtSwXHkiJeb90QGDmvuiNHjIzolmI0GpS1FViXJzqXC6LLHqmHw_Ag4VltVt702VhvnGngu02Qn7CGKzmMHL-n3wYYAksq_fePkadGzomzCJZqzlfy5yRLy4-BUtbXoFeGVaaKJS-r_jH9ByfZ7ChBGBmaRhv9i9bMnfYVzdRM816Y6oFP4CSn9KFTCBznCflK8h3VsVY5lXzXSIIck8-w3Xfc6bO89VbfvvGVAdtq36saTpe0HKipUEc76dOl9d3PKc0aJaaec2k_pWTn4Sb-LoTmOrZQ7cevFoC0OXQcUnhh_bzlsuintFE_wjzC37XvuxCxVmhbIM2uCI75WqcJaC_QJtpwvxCE7_dpxmNhrUsX_Co172K32fY-vTuUGhgRoF4pRPM3Z-9lc1CE1iSan9jo9WZtrngpnhO7_sGBPMPorHeGGETU1d35nHAlJ1oab9JbGlBxydCeSD7i1TDVXaVzyPjS_R62ZtXuotOXStigt_KL-cGvaOgpNCNGRpw1E_urp-dZbTG98hnahYjUmus0Yqhk756TyXbJS7AW1OSIpvAO3-clZDPlQ9MCBkM9UNvWz6RtDD8gzXyAmEGJW-5gyTl8qnpfkuGAxV5egI806doemsFaGV4W9dc75fzCNWcYuIp09FVLhQ9v9kG570MI9txTCdS_4bdodoKq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره معترضان در تجمع خود:
«می‌دانید، من هیچ‌وقت درباره ظاهر افراد صحبت نمی‌کنم، اما اینها واقعاً آدم‌های بسیار بدقیافه‌ای هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151557" target="_blank">📅 09:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23de0481a.mp4?token=RpV9G01cOrc03HJ5ZkIrpUtt9iZm3Ig2toYmWfQjNyjhPrGCZlfDFxCrwHpJT_FiSrUmFxwsjLD2Y6e0mCOK6poRqZjKGsOnFmJpk8i2Be7ZteArbxFz-V1cRPqJPWt-jzptWS7-8V5-JcS_mLRjzelZABllPzVCwJ91RmXXDeyE6IJfd7M9YpepXs1aJYGlUQuryrqIlguBuZpCE4VGRhiazrw0lqov-90VJ_ChcTDEbo2nAEjXkEDnzMXGcPio2JOTsXF4lhw9velkSfjuGn89F_BNw2tRCklcl6eUc3Sxdo-ffE3VOjI5ulOBswaRsikDSnfBSl9D3TczhXSzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23de0481a.mp4?token=RpV9G01cOrc03HJ5ZkIrpUtt9iZm3Ig2toYmWfQjNyjhPrGCZlfDFxCrwHpJT_FiSrUmFxwsjLD2Y6e0mCOK6poRqZjKGsOnFmJpk8i2Be7ZteArbxFz-V1cRPqJPWt-jzptWS7-8V5-JcS_mLRjzelZABllPzVCwJ91RmXXDeyE6IJfd7M9YpepXs1aJYGlUQuryrqIlguBuZpCE4VGRhiazrw0lqov-90VJ_ChcTDEbo2nAEjXkEDnzMXGcPio2JOTsXF4lhw9velkSfjuGn89F_BNw2tRCklcl6eUc3Sxdo-ffE3VOjI5ulOBswaRsikDSnfBSl9D3TczhXSzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ‌ : در سه شب گذشته، ما بیش از هر مقطع دیگری در تاریخ تنگه هرمز، نفت بیشتری از این تنگه خارج کرده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151556" target="_blank">📅 09:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4b9c74ae.mp4?token=S-ZljOdTV9_hrmOZ37k6-NAw08Zz0ixur4_w3U8yl0gd2P-ssJbd3STpAqY5KjuCU-dED7QxlTQpealqmZw1ZJuqCT_8sa25N5yH6Fj--7-i7vxclZ0GBaWJ5fBHgA_MZyZt7UErFyeLDmRZhFuMPjgVnnTHSHeLT9sWFE9bAAnwjupGkebnUn2k-54rVzFthM2a-bGwDrbuGlDH5NjWFCBLsiPoPeLW4qLBMsEN2FMPj8xS499UOvdw7ok5Qu4g761b5ExlGLmBktPRuzyY9zyX6qxQUsj5jBSx6OVRqp16yGZgQKjFh5ZsT0Z5KzNueQxgWr0R1f8jVE1Fq9h6RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4b9c74ae.mp4?token=S-ZljOdTV9_hrmOZ37k6-NAw08Zz0ixur4_w3U8yl0gd2P-ssJbd3STpAqY5KjuCU-dED7QxlTQpealqmZw1ZJuqCT_8sa25N5yH6Fj--7-i7vxclZ0GBaWJ5fBHgA_MZyZt7UErFyeLDmRZhFuMPjgVnnTHSHeLT9sWFE9bAAnwjupGkebnUn2k-54rVzFthM2a-bGwDrbuGlDH5NjWFCBLsiPoPeLW4qLBMsEN2FMPj8xS499UOvdw7ok5Qu4g761b5ExlGLmBktPRuzyY9zyX6qxQUsj5jBSx6OVRqp16yGZgQKjFh5ZsT0Z5KzNueQxgWr0R1f8jVE1Fq9h6RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ،درباره ایران: «جنگ خیلی زود به پایان خواهد رسید. آنها یک کشور شکست‌خورده هستند.
🔴
هنوز کمی توان و جسارت برایشان باقی مانده، اما خیلی زیاد نیست؛ واقعاً زیاد نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151555" target="_blank">📅 09:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل: «حماس، قطر و ایران همیشه می‌خواستند ما را از جهان منزوی کنند. و حالا این جهان است که خودش را از ما جدا می‌کند.
🔴
آن‌ها سال‌ها روی این موضوع کار کردند و حالا این اتفاق در حال رخ دادن است. صدور حکم‌های بازداشت در لاهه، بازرسی کیف‌های اسرائیلی‌ها در فرودگاه‌های هلند، فوتبال در ایرلند، تحریم یوروویژن و همچنین تمام نمایندگانی که هنگام سخنرانی نتانیاهو در مجمع عمومی سازمان ملل از سالن خارج شدند.
🔴
این‌ها اتفاقاتی نیستند که صرفاً برای ما رخ داده باشند. این همان نقشه‌ای بود که آن‌ها دنبال می‌کردند. این هدف آن‌ها از ابتدا همین بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/151554" target="_blank">📅 08:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb31c29d7.mp4?token=q4KbWJtLLk0WccsD3ylEvkINuYEzeSBgk3KXJv59zJgU5BRk9RFanoCBiqeUS9wJHHO2QZEEscRvrwooytiiHbXR6X3mFrCuOwiJjzC-B5jKlSDeFgWAqn2cF2n0A24l3HibzJ5U3sfeIw50t8oozSyRfKvGYJDVW4IltTfmDeld9D0hV4t7c988MSW6r_PKJUeyhPQTutLQU2jzcODRJGllUad8Zp7Jya6BuRLUUv1zi0wI24SP5T68tXOHIvSLjbcie7YI4NBwQY6mveMb1hWROkUl1D8CkLUV5_zJY1IcMKn6KB2wxbDtpoAiOzuNoJ2WkAV8UgdA2_6KgY4Tp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb31c29d7.mp4?token=q4KbWJtLLk0WccsD3ylEvkINuYEzeSBgk3KXJv59zJgU5BRk9RFanoCBiqeUS9wJHHO2QZEEscRvrwooytiiHbXR6X3mFrCuOwiJjzC-B5jKlSDeFgWAqn2cF2n0A24l3HibzJ5U3sfeIw50t8oozSyRfKvGYJDVW4IltTfmDeld9D0hV4t7c988MSW6r_PKJUeyhPQTutLQU2jzcODRJGllUad8Zp7Jya6BuRLUUv1zi0wI24SP5T68tXOHIvSLjbcie7YI4NBwQY6mveMb1hWROkUl1D8CkLUV5_zJY1IcMKn6KB2wxbDtpoAiOzuNoJ2WkAV8UgdA2_6KgY4Tp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، بار دیگر از سوی یک معترض مورد هو کردن و اعتراض قرار گرفت و در واکنش گفت:
🔴
«اون یارو باید خیلی وزن کم کنه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151553" target="_blank">📅 08:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دونالد ترامپ، خطاب به یک معترض: «او همین الان
دارد برمی‌گردد خانه پیش مادرش.
نمی‌داند که مادرش به ترامپ رأی داده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/151552" target="_blank">📅 08:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqs3mhqHFC3ubeGCzlMJd2WaD_Q2pUyma1ic_fJiRRDnm5PF74O4T8qUEKlyuc-_CgMMEnG4YDY5_AqUJGRtLoba_E1Lb29eyPTsb-H2yyfOiyky_hZk17-gt-wUkiRKFx0VxAXyPYxlQ5yG9pA3B6-FVSRt8yRihxV5vFmEdckGovBoOBtfgI5Eai9bAQyjm_IyXReicuOL-SKHreQRvOlaNN9o5Xv-wiXs9cM5I7Wm9ZrGhJQOxH05AZSAMy79sS4AOV4SJYaCRM4N6g11_6_Slc61T6-bMwoGeAlYf_UIqR7OK9SqWT1LvY5G3v-N2Ot4p9-zlQeR8IhXdxNQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم تحلیل‌گر ارشد صداوسیما: ۵، ۶ تا مین دریایی هوشمند ببریم و در خلیج فلوریدا بندازیم تا این تنگه استراتژیک آمریکا را ببندیم و آنها را به مصیبت بیندازیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/151551" target="_blank">📅 08:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UIfYm1Pal0tXoDD93j8NRioHWSpfPqVVsBMqHd7Uo5XoUEholtHRo4dLNwf8FL9fvMhsgpzmrKZk_fSY_ciZuSi5tBq0WFlgqpemeku_v00IrdAtbqCEt7Gy0B51QBmaAjNrvT6lzmYK-NyVmCRSbkK0W7WKackpM6OScVvFUSukdppkgcxrew1z0RPaP41mhOId8ln1KP4XF2xlmG_SqDuicgdR1BIfrUUHffm8vNEk-tJXY3rznwcEuENGo863AEhwpDQGoQgLBReNSYC2J_QpJ3hLZ-xStwa4lGFggWupcncP5pPoxuIYMYiB16b5fOqapMlq5Ud8kyINMTRsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ارتش آمریکا دستور داده برای احتمال ازسرگیری جنگ گسترده با ایران آماده باشه، در حالی که ترامپ هنوز داره زمانش رو بررسی می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151550" target="_blank">📅 08:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: چه سناریوهایی انتظار می‌رود؟
🔴
۱- ممکن است شکاف دیپلماتیک دوباره ایجاد شود؛ تهران در حال بررسی واکنش‌های خود است و واشنگتن منتظر است، در حالی که میانجی فعال و مؤثر است.
🔴
۲- واشنگتن ممکن است لحن تهدیدهای خود را تشدید کند و بدون ورود به رویارویی، تا آستانه تقابل پیش برود؛ با این هدف که امتیازاتی از تهران بگیرد.
🔴
۳- رویارویی نظامی؛ ایران آماده است و واشنگتن به دنبال یافتن یک سناریوی موفق است که هنوز مشخص نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/151549" target="_blank">📅 08:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXO_dl74ATe_x5WYPftu1DeulOdrSL1kBrvgYrGuQIAHZkfkKG8RIUN_aEcXhH5FPsBUQQU3UkgJuphOw9wjg_DaqzDp3P0hLLNP0BFdNrteLNhPuRg8lJ9Cp4S5RJcTSwDsR0axPA6gyfypTIyIwgkzdUmFtHpkaz4K0sMaKkfTpV-UWKUeuZhi4bB4VLQhKv-ilBA94bMFRm75zyWypGJLsGAPhEVxrlE3IAVbLH6Qv9piMrnZrPrlGoSLfzJKWyxgYVy-gZ6DXc-_mBsmOmjY8wuGzoyXdKrWRWtJxbo0GQD1IoQT_Jm8DwKJnN4p19KNO2L_ogU0H9ENTmKyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاپید: رهبر حزب مقابل نتانیاهو: 30 ساله هر روز تو جنگینم, مردم اسرائیل خسته نشدین ‌؟! به من رای بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/151548" target="_blank">📅 01:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آکسیوس به نقل از 3 مقام ارشد آمریکایی:
چندین لشکر ارتش سوریه به تعداد 20 هزار نیروی نظامی در حال آماده سازی برای اعزام فوری به یمن و جبهه های جنگ با حوثی ها می‌باشند
🔴
دولت سوریه در ازای این حمایت نظامی تمام عیار ده ها میلیارد دلار سرمایه گذاری عربستان سعودی در این کشور را دریافت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/151547" target="_blank">📅 01:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpF9u7Lsmi52HXUR3ftwZSp2qqMyJ6NKPR2xbKEGsUg4PbuifQl5W1XzJ4xFdBwg6iCu-cKwNL2_wwm7l2cOYnYjoWntk9IWs9VWArV_lGnBZu_k9KRu7VDicP7-kuuZQh5rfsh6LvG6DYUgbUukIzcfWeyceR4OfFxIzKxw1lQAYWB8sPJN7haKVftNwtbDe33o_q3F1HnOgBAFzNw0d1MMzMcfGMD0hGg9Um2BxAS0_IMCxR790jNWTjpWXWIddVYUqIePt9wkbuYnCXoOJbKSpfS95McmubjNzZ1sN75Yj5FWB3jI69ZoaJodyPCVcuy9g_jZKgwTF2WfEES6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتشر شده که در آن خلبان یک فروند میگ-۲۹ اوکراینی پس از سرنگونی یک پهپاد تهاجمی روسیه، در مقابل لاشه در حال انفجار آن انگشت فاک نشان داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/151546" target="_blank">📅 01:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgauW1MM4Nhqcrd-Byb4QkUqqOs8tMOF1UNzwYfKnMPqkS2Gh7smc1SRR6h8wU_IOxiW-uAEfLplSpDIVpHwvlGMu3pAL5J1bnt9zIF3cllWzqcFBRy4fdel6nU1zERjP7E4bl1sSJ6FTAgj5fxjysBCM3iLzXx8gTVadghmqdIIj3lf-i0uhqBk_VNxFz3nfzfUcbAil4RK0vjPUHb_B2Rxiias_FqQrD46wr52Eta864IRw0Gf3Mvs9LlRjKOaZWbZCqyLeIEI2J17GdQ29KMGLNUCFs023tocplCHyYtyJeuJRKS-qZGdVJbLosRwuqU7I2DMet0uiKuAuptGIkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgauW1MM4Nhqcrd-Byb4QkUqqOs8tMOF1UNzwYfKnMPqkS2Gh7smc1SRR6h8wU_IOxiW-uAEfLplSpDIVpHwvlGMu3pAL5J1bnt9zIF3cllWzqcFBRy4fdel6nU1zERjP7E4bl1sSJ6FTAgj5fxjysBCM3iLzXx8gTVadghmqdIIj3lf-i0uhqBk_VNxFz3nfzfUcbAil4RK0vjPUHb_B2Rxiias_FqQrD46wr52Eta864IRw0Gf3Mvs9LlRjKOaZWbZCqyLeIEI2J17GdQ29KMGLNUCFs023tocplCHyYtyJeuJRKS-qZGdVJbLosRwuqU7I2DMet0uiKuAuptGIkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز عده‌ای الاف تو تهران ساعت ۹ صبح کفن‌پوشیده به سمت قوه قضاییه رفتن و به پسر پزشکیان لعنت فرستادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/151545" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
نشریه آتلانتیک : کاخ سفید از پنتاگون خواسته تا برنامه حمله به اهدافی در ایران برای پیش از انتخابات (۱۲ آبان) رو آماده کنه. ترامپ قصد داره قبل از‌ انتخابات حملاتی رو به ایران انجام بده.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/151544" target="_blank">📅 00:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کارشناس مذهبی تلوزیون: افرادی که ناخن‌هایشان را تا ته می‌گیرند، جن‌ها شب‌ها به سراغشان می‌آیند و ناخن‌هایشان را لیس می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/151543" target="_blank">📅 00:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو: اگر ما علیه ج.ا اقدام نمی‌کردیم، بمب‌های اتمی ۱۰ میلیون اسرائیلی را نابود می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/151542" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c552576b68.mp4?token=XzXsZlVyDxMBM-09yVokm8cVYkME1HzYL_obm_C8g8lz4m1EImp-pE7dFQzQC5CYvRDYhO4tlGJc3JbAHwCczFz7FA8DuqfdIV30eOCOaj-yzKCw0zOziOzpWOYKKPODN_68kyHfvDHcyiyorFJBvltYNAE3OaAhUimcTwccAhl0r8jUSwFkUDEJ2RtogRbQW1KfFiSzCCSl6GlUjAqOJPVBSZ-DBSAm_WjMtZXGpkB4oXE_U_oOYI_yKfwTfostHoAOiDfg_AkVdEY_EG7D3R4oqbbCPKhhNggdYpysdzlCXwCGFKikwbsAotj3DTkavHylw6sso8cHjK10-Fi4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c552576b68.mp4?token=XzXsZlVyDxMBM-09yVokm8cVYkME1HzYL_obm_C8g8lz4m1EImp-pE7dFQzQC5CYvRDYhO4tlGJc3JbAHwCczFz7FA8DuqfdIV30eOCOaj-yzKCw0zOziOzpWOYKKPODN_68kyHfvDHcyiyorFJBvltYNAE3OaAhUimcTwccAhl0r8jUSwFkUDEJ2RtogRbQW1KfFiSzCCSl6GlUjAqOJPVBSZ-DBSAm_WjMtZXGpkB4oXE_U_oOYI_yKfwTfostHoAOiDfg_AkVdEY_EG7D3R4oqbbCPKhhNggdYpysdzlCXwCGFKikwbsAotj3DTkavHylw6sso8cHjK10-Fi4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی این آهنگ تو صدا و سیما ممنوع الپخش شده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/151541" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خدا باعث و بانیش رو لعنت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/151540" target="_blank">📅 00:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
تبادل پیام (میان ایران و آمریکا) از طریق میانجی‌ها انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/151539" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmnrnZ-Kso3GGSkR1FKtR2aX9lRYNGTdxfT8z0JXA6iE9DryY8bQN0_AOi9zA60dwW7XOj4LCTATf97riT3490uQ0uE7fcf3-JRCKj5aO4LaTy05A8EvgYtNteNfCGBRGnwQCqmlB7_g5qqUXtZLm7cssZfv0aW-dSzH85mfbGOrDbA5oeTjsokGQYQ_XHgeNEi3AclMZ_Pa2Fz1vO4ggFCQVNiVCVvKNLkoLPi-EUFM-Ca8PO76nM5fUKow9X2R-Rc9tPpR6Vst8_boXodeL9AZ-qTe4Q92OphZqYG3z3NC8_2Cxcjqtl1Da15QK9R_2G-E7Rdgxc_VJXuO5sQwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: یه موشک داریم که پنتاگون و غرب تو کف موندن چی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/151538" target="_blank">📅 23:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151537">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/151537" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کانال 15 اسرائیل: ایران در روزهای اخیر شلیک به سمت کشتی‌ها در تنگه هرمز را از سر گرفته است
🔴
‏ ارزیابی این است که حمله‌ای از سوی آمریکا انجام خواهد شد و بنابراین ممکن است آنها بخواهند ابتدا حمله کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/151535" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پزشکیان : من یک دانش‌ آموز شلوغ و بازیگوش بودم و درس هم نمی‌خواندم اما وقتی وارد جامعه و نامردی‌ها را دیدم تصمیم گرفتم درس بخوانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/151534" target="_blank">📅 23:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a58a5239b.mp4?token=R-rkd3VsZOlaH6X-_3t8JYjWZcwlsumcHGN6JFM9XKZFUV96OKSMV9Mn2slLp3V68wWiBl9xUnUF06V62COkoA6djnH-kIuRqvwdi7d1dA2Z6X-exmmCu4MVylXPnwLDdgWfkCKl6YhiYh1BXwlLrNHXFIJlIhO2cva2UYiPRmTNc_7A8a8K8eaAavw5dMLFlUgQCe0v4lqWRl5aeJvj5I2oE6Fx7pG6gSu96P5xFhagiGQdkAvGoIgLa7tI8aKk05hU3tQxicEiMSM13dLP-6UdLvooeEuge3Lv9bNK18qpNbrBdIAievvsa_Vs4kKSThZA5NazXLa06St7Vu1d_W1LEZKXqbHioG9eJ4wTEEBbS8fCBBXRlYt2GWG9VZwrCIZoUIfgyWMzzFUQiztl0tNWWfg4c-PpZlA5DqvPbUCi7uQkWAmj5kStLGQ-WhkGsQ-iJGxFqH408Hplhq2qpNMuWkMEQ0w8HWMb9orsrCBHyoBVX1v-WeIhUG0cDWjs0u1z-UlrIBmZYLEK1FWG20AU8COUrFTLKLwmWs2-YhKGYmQdUpF0eSjLcQbOvY3kZpv27vy0vnD5UPOmJA2eYLd2_9QIOWXUAs6_ju-a6AVr8FB8JCASPMSlZXa3swz3lUdBUi_PFBwjI1nqHYMeWDbHExGWGvNAeEw0Pb8hPUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a58a5239b.mp4?token=R-rkd3VsZOlaH6X-_3t8JYjWZcwlsumcHGN6JFM9XKZFUV96OKSMV9Mn2slLp3V68wWiBl9xUnUF06V62COkoA6djnH-kIuRqvwdi7d1dA2Z6X-exmmCu4MVylXPnwLDdgWfkCKl6YhiYh1BXwlLrNHXFIJlIhO2cva2UYiPRmTNc_7A8a8K8eaAavw5dMLFlUgQCe0v4lqWRl5aeJvj5I2oE6Fx7pG6gSu96P5xFhagiGQdkAvGoIgLa7tI8aKk05hU3tQxicEiMSM13dLP-6UdLvooeEuge3Lv9bNK18qpNbrBdIAievvsa_Vs4kKSThZA5NazXLa06St7Vu1d_W1LEZKXqbHioG9eJ4wTEEBbS8fCBBXRlYt2GWG9VZwrCIZoUIfgyWMzzFUQiztl0tNWWfg4c-PpZlA5DqvPbUCi7uQkWAmj5kStLGQ-WhkGsQ-iJGxFqH408Hplhq2qpNMuWkMEQ0w8HWMb9orsrCBHyoBVX1v-WeIhUG0cDWjs0u1z-UlrIBmZYLEK1FWG20AU8COUrFTLKLwmWs2-YhKGYmQdUpF0eSjLcQbOvY3kZpv27vy0vnD5UPOmJA2eYLd2_9QIOWXUAs6_ju-a6AVr8FB8JCASPMSlZXa3swz3lUdBUi_PFBwjI1nqHYMeWDbHExGWGvNAeEw0Pb8hPUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: گاو که دلار نمیخوره پس چرا قیمت شیر دلاری زیاد میشه؟
🔴
مدیرعامل اتحادیه تعاونی‌های لبنی: اتفاقا دلار میخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/151533" target="_blank">📅 23:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ارتش پاکستان: سربازان پاکستانی در «ظرفیت‌ها و حوزه‌های متعدد» در عربستان حضور دارند
🔴
نیرو‌های نظامی ما تحت ائتلاف دفاعی مکه در عربستان مستقر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/151532" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی از وقوع یک حادثه در فاصله ۵۱ مایلی دریایی از شهر الشمال قطر دریافت کردیم
🔴
در پی حمله به یک نفتکش با چندین پرتابه در آب‌های نزدیک قطر، شماری از افراد زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/151531" target="_blank">📅 23:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ درباره لهستان: مردم لهستان را دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/151530" target="_blank">📅 23:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151529">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unanZ8VnpA1vN7ZYCcb54X9FF2_GgA-3JUn7ajp2YrLfbd7_-RQGMXcjRLJrZi6pI2hZlA2XnkVrQFJMf7dEKe44NnNf7yJ_LTwa_cP7F-BwYHAMnhOnV1N2pdwnDWviq2YcX4Vws7aN2PBzElhn1c4DmICupAYoa0b9iFWlx1wImyzXystbO-OA6atfmNg0OpdJjujWSa55BoYV6Gn2P-EHwNVKnltvCB7t3c5QJdDuOuj7RkA8GbL2g4Fdlj6JwdphruN2L7pEuaFF4yKWdkAvnzjeJpEOht4wGDqDP-x3mqntMsybfMwkfSuMhDcm7nxzCIYs7Ddcd6tl9t188Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتلانتیک: ترامپ پیش از انتخابات میان‌دوره‌ای دستور حمله گسترده دیگری به ایران را صادر می‌کند
🔴
کاخ سفید از پنتاگون خواست گزینه‌هایی برای حمله به ایران قبل از انتخابات میان‌دوره‌ای آمریکا آماده کند. تصمیم نهایی هنوز گرفته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/151529" target="_blank">📅 22:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ درباره ایران:
فکر می‌کنم داریم خیلی خوب پیش می‌ریم. داریم ایران رو خیلی بد می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/151528" target="_blank">📅 22:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: ایران در شرایط سختی قرار دارد و هرگز به سلاح هسته‌ای دست نخواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/151527" target="_blank">📅 22:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گزارش ها شنیده شدن صدای ۴ انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/151526" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / ترامپ: من با نتانیاهو صحبت کردم و طرف مقابل بهای سنگینی برای کاری که در هفتم اکتبر انجام داد، پرداخت.
🔴
درگیری با ایران به زودی، به هر نحوی، پایان خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/151525" target="_blank">📅 22:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151524">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ4Wpz0BSOdzcAVQBkv2hJN_MGnI8PCX06ZiwoHPBg2XohM2s0uvy4mb-HQJpIImxjsnye6AePzh2cu5sWfBUKJTFcZVEJ-dadtHB9z__sotDJdGuVBFbfP2LO8PKFmw5NwA-9SYHNEurSMVGNSo9-qQdcz4pPtc15TmMbRAUiwm5esUdjydDirTXDBlc7GA9cLHoWC52mWbpjvnGNtU3rPLwNOY-hkHPTGGtVayJAzA5CJSiTneEtHXVrWS0ALPal9CrGWe5ix2tKVvbPzKnDbi0O-CKEnbon40CIK58y8n18FqCNtz8MP9Is6Ke0HKdhpFYNeBlx8E-mege5IPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ: استیو ویتکوف چراغ را روشن نگه می‌دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/151524" target="_blank">📅 22:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151523">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / ترامپ: درگیری با ایران به زودی، به هر نحوی، پایان خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/151523" target="_blank">📅 22:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151522">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دو منبع دیپلماتیک منطقه‌ای به i24 نیوز: احتمال دارد تهران یک حمله پیش‌دستی را آغاز کند - به دلیل نگرانی از یک حمله آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/151522" target="_blank">📅 22:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151521">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbc004919.mp4?token=LNwcGLjX3-N1up14c_FNFDyVI-uZ1opKBGVgvolBlIFr4YDW32i_k8pOvkxyaXv-lu6vhyq3wz9rJ8snSTb7nE81XgZJXLHkxtlAf9ZpNF9q44P83ib53fHe8Av1ssTvQhXs27ha5hEID5SKmmJYl_snHb28NmZhlrrE7d0eh_xPxwNoMU-lP1cWYgQtwkg2e88kFqfdeKTGdU3wMypx7ZwUh5yMVmdV26a8MoTt9YbE9WtFx8OY8SYYC9nSe8Cn7KRgUcVUJTEsi_9D5w3x2-8yQ64ZUePl_jNKoKzPF74QNWXlpj3zeQ_rozRLccTQnrko61IkvKVKW1mAKVrT9bZtvlya78dGaypiOfbOX3UK08xyAKx3ZAWX6Yr5nLeJziY9ywVeN558St6jGBH0qUdQlR_d70U86EXCZQqU8_GoreRYFZ0L8pRNpEd8vWa82-ZFoltvgEJz1qsv3TKU8GXXS3idr0CFqT1Q_Qt8G068fznDqQPF1P1ZwPh81XUHoE8tjKV9to-bXjAj1fUurBedibtha9AYPjWJdzlmZcQWiLFz8LPJOY9cvOjPjhbge8LTjiTeQKh4Ber3IvpJltLRXBvPpuaMWik3N86J_FZ9KJn8A7X7f2ATaR0gnpxYGXVi8Qp48bOY-cOyk-1erjT2oCIKkHd97RMGfBRwDcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbc004919.mp4?token=LNwcGLjX3-N1up14c_FNFDyVI-uZ1opKBGVgvolBlIFr4YDW32i_k8pOvkxyaXv-lu6vhyq3wz9rJ8snSTb7nE81XgZJXLHkxtlAf9ZpNF9q44P83ib53fHe8Av1ssTvQhXs27ha5hEID5SKmmJYl_snHb28NmZhlrrE7d0eh_xPxwNoMU-lP1cWYgQtwkg2e88kFqfdeKTGdU3wMypx7ZwUh5yMVmdV26a8MoTt9YbE9WtFx8OY8SYYC9nSe8Cn7KRgUcVUJTEsi_9D5w3x2-8yQ64ZUePl_jNKoKzPF74QNWXlpj3zeQ_rozRLccTQnrko61IkvKVKW1mAKVrT9bZtvlya78dGaypiOfbOX3UK08xyAKx3ZAWX6Yr5nLeJziY9ywVeN558St6jGBH0qUdQlR_d70U86EXCZQqU8_GoreRYFZ0L8pRNpEd8vWa82-ZFoltvgEJz1qsv3TKU8GXXS3idr0CFqT1Q_Qt8G068fznDqQPF1P1ZwPh81XUHoE8tjKV9to-bXjAj1fUurBedibtha9AYPjWJdzlmZcQWiLFz8LPJOY9cvOjPjhbge8LTjiTeQKh4Ber3IvpJltLRXBvPpuaMWik3N86J_FZ9KJn8A7X7f2ATaR0gnpxYGXVi8Qp48bOY-cOyk-1erjT2oCIKkHd97RMGfBRwDcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، پس از اینکه متوجه شد دریانوردان کشتی جنگی یواس‌اس آبراهام لینکلن در طول جنگ با جمهوری اسلامی ایران عملکرد بهتری نسبت به آنچه او در ابتدا تصور می‌کردند داشته‌اند، دو بار شنا انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/151521" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkCL5R5SvUgVoLQf6E6rZWWyHl2nBTaaY00fuiPKHC4dKjS7E7Hn5I0F4AYOjVHBgNxK6mY-6kXYeyLF2kh0mucc9Mhrs2_nbwDJf8wQqZTgjbc2yF9lT1IKBfxHl5y4ebInMyL8UjjvRFlCvaTSxUtU_zccq-LX4B3X1syCIu9o12-vemmLTSiWMwdy3e1fexMjNycKZ2PsbO6I3wYjE1taCpvAtDhYhvZFpWniVYj4L8WnuPto5f3tK64xkZdtpGz4cno7zySj00UbkP5lM0ncD_MXqpsCDit4PY03YMqhprzItGaqAfFdFudQ09NhbrPK2tj4Wn9mCS_oWuo3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/151520" target="_blank">📅 22:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151519">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، پس از اینکه متوجه شد دریانوردان کشتی جنگی یواس‌اس آبراهام لینکلن در طول جنگ با  ایران عملکرد بهتری نسبت به آنچه او در ابتدا تصور می‌کردند داشته‌اند، دو بار شنا انجام داد.
🔴
ما با نیروی دریایی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
🔴
نصف پایین را آن‌ها گرفتند.
🔴
چند نفر در رسانه‌ها سعی کردند ناو آبراهام لینکلن را به نمادی از بی‌نظمی، روحیه پایین یا مأموریت ناموفق تبدیل کنند.
🔴
وقتی به شما نگاه می‌کنم و با رهبران شما صحبت می‌کنم، می‌دانم که دقیقاً برعکس این است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/151519" target="_blank">📅 22:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151518">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفارت آمریکا در عربستان به حالت هشدار درآمد
🔴
در پی تشدید محاصره یمن علیه حریم هوایی عربستان، هیئت دیپلماتیک آمریکا در ریاض با صدور یک اطلاعیه فوری، سطح تدابیر امنیتی برای اتباع و کارکنان خود را افزایش داد.
🔴
به دلیل احتمال بالای تشدید درگیری‌ها و حملات به فرودگاه‌ها، سفارت آمریکا نسبت به لغو گسترده پروازها و انسداد حریم هوایی عربستان هشدار جدی داد.
🔴
تردد کارکنان دولت آمریکا در شعاع ۲۰ مایلی مرز یمن ممنوع اعلام شد؛ همچنین سفر به استان‌های جیزان، عسیر، نجران و شهرهای قطیف، ینبع و طائف نیازمند مجوز ویژه امنیتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/151518" target="_blank">📅 21:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151517">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حمله مسلحانه به مقر انتظامی در گلشن
🔴
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/151517" target="_blank">📅 21:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151516">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: سازمان سیا به اسرائیل فهرستی از حدود ده مقام ارشد ایرانی که نباید هدف ترور قرار گیرند، تحویل داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/151516" target="_blank">📅 21:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151515">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ : به محض اینکه جنگ با ایران تمام شود قیمت نفت مثل موشک سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/151515" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151514">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e69a46df1.mp4?token=AKrN6YSPIzzvnxOIQYazbPH5AxrDnTBDjnMwV3EgJB6-u5LWd8ShYztQUB1sbS8hV1yPvGIVaQZf0fa0sjX4m9B1w2DV6hSsdnOsbn6JAPMVMIp-XX7LeJN-nwBMyPAfEjG2qtB5ngAoWcxgvEMo_8bDa8qBD5cFOgm8I4H2VB1XEib7erTDa98nD8MxpIix6hjq899YltGPSXtk6TmTpqg3R6LiQxs4NqLfB15LEYaU_FqvhTizDSB4SzMIWxUfgc_3p_qGzLw7Gq7S2xjwQr2hKq38gN2B4crnHgB8nibPQkT5yJDaTy7jc28qtsi3xMjBBhZkWBJFjmi7pkiEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e69a46df1.mp4?token=AKrN6YSPIzzvnxOIQYazbPH5AxrDnTBDjnMwV3EgJB6-u5LWd8ShYztQUB1sbS8hV1yPvGIVaQZf0fa0sjX4m9B1w2DV6hSsdnOsbn6JAPMVMIp-XX7LeJN-nwBMyPAfEjG2qtB5ngAoWcxgvEMo_8bDa8qBD5cFOgm8I4H2VB1XEib7erTDa98nD8MxpIix6hjq899YltGPSXtk6TmTpqg3R6LiQxs4NqLfB15LEYaU_FqvhTizDSB4SzMIWxUfgc_3p_qGzLw7Gq7S2xjwQr2hKq38gN2B4crnHgB8nibPQkT5yJDaTy7jc28qtsi3xMjBBhZkWBJFjmi7pkiEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا روسیه اطلاعات کافی در مورد وضعیت طاعون در سیبری ارائه کرده است، و آیا ایالات متحده درخواست اطلاعات بیشتری کرده است؟
🔴
ترامپ: آن‌ها مقداری از این اطلاعات را با کارشناسان ما در میان گذاشته‌اند. ما انتظار داریم که آن‌ها اطلاعات بیشتری را با کارشناسان ما به اشتراک بگذارند.
🔴
من همین الان با کارشناسان خود ملاقات کردم. ما متخصصان بسیار باهوشی داریم. آن‌ها از تمام جزئیات آنچه در حال وقوع است، آگاه هستند، و تمام این اطلاعات از طریق آن‌ها منتقل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/151514" target="_blank">📅 21:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151513">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1e7109c3.mp4?token=NZi_EsNB8Ti19vNAY-tiaZNyeq62BZSUJCZqAQAKYhofS7Wm3aisawJvmgQ4EaX_fRF2WeYdJz8Kc5jIG9cbkQ8-cU_D5n1iU0uV8C5jKVYbyNJAe_CIBd56QePdgP2s8FOnBYVhnf-5Y-mXXAUm_F6Wpa8sJWwSG1gtDsbicRIJSGMWPYmGAmXDy07VixL3UiqGWPdx93l4nbrD-ckZjRzV8M-aSXkGfAmscb0yk3f28iTmgxz1qiY-kOcMWA3Nrw0MYcdbFijVVMBj4HMXQu1nyZXL1VN9cpba_rsTMyj0_HQM8VAUhkkpZS_wH85r949HBs_Kb5ftuGjiT_KzIgy1P4y7EetwyzCm5b4gWU3eb88Ea3KF7A1vrUYByH6P1qOkA-mZiq0TZraksj5GTlueUe5VsSocyCyqW6MhQDrQVnPgBtm0OwSaGCbnqbstoT6xWOR9oY075C4WLGM2iug-ZeLTfGESkuNsR0R7NivlnK0FQUimWouFnEUeOwh96uGYYh4qboWUfQDkZxhrEwuoaHrxJXD2CysH8SKlaaR18Q-bdIwajcEzlxqPTmx7ro896u8AcPioY20DWcpY5P768rmDk5Gqd630LctAIn3vWLdbP7geMwM56zgT4_f5SXDJfADn-f1fb0SjserchawVX_iH7l4lMzlk9_j2nUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1e7109c3.mp4?token=NZi_EsNB8Ti19vNAY-tiaZNyeq62BZSUJCZqAQAKYhofS7Wm3aisawJvmgQ4EaX_fRF2WeYdJz8Kc5jIG9cbkQ8-cU_D5n1iU0uV8C5jKVYbyNJAe_CIBd56QePdgP2s8FOnBYVhnf-5Y-mXXAUm_F6Wpa8sJWwSG1gtDsbicRIJSGMWPYmGAmXDy07VixL3UiqGWPdx93l4nbrD-ckZjRzV8M-aSXkGfAmscb0yk3f28iTmgxz1qiY-kOcMWA3Nrw0MYcdbFijVVMBj4HMXQu1nyZXL1VN9cpba_rsTMyj0_HQM8VAUhkkpZS_wH85r949HBs_Kb5ftuGjiT_KzIgy1P4y7EetwyzCm5b4gWU3eb88Ea3KF7A1vrUYByH6P1qOkA-mZiq0TZraksj5GTlueUe5VsSocyCyqW6MhQDrQVnPgBtm0OwSaGCbnqbstoT6xWOR9oY075C4WLGM2iug-ZeLTfGESkuNsR0R7NivlnK0FQUimWouFnEUeOwh96uGYYh4qboWUfQDkZxhrEwuoaHrxJXD2CysH8SKlaaR18Q-bdIwajcEzlxqPTmx7ro896u8AcPioY20DWcpY5P768rmDk5Gqd630LctAIn3vWLdbP7geMwM56zgT4_f5SXDJfADn-f1fb0SjserchawVX_iH7l4lMzlk9_j2nUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: به کسانی که این نظر را مطرح می‌کنند که شما صرفاً قبل از انتخابات، پول به مردم می‌دهید تا برای جمهوری‌خواهان رای دهند، چه می‌گویید؟
🔴
ترامپ: خب، کاری که ما انجام می‌دهیم این است که رشد اقتصادی فوق‌العاده‌ای داریم. شما همین حالا هم شاهد آن هستید، اما اعداد رشد اقتصادی را خواهید دید که هیچ‌کس قبلاً ندیده است.
🔴
ما می‌توانیم کارهایی را انجام دهیم که دموکرات‌ها نمی‌توانند، زیرا آن‌ها نمی‌توانستند مانند ما، از تعرفه‌ها به این شکل هوشمندانه استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151513" target="_blank">📅 21:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151512">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2920ff853.mp4?token=qtJ9ab14bUcEXJm-szjjWfBMr2iX4GRRA6f7eS2SwNnRkERRadDMHJboIuLEniPyTh_4n5b9sIzSk_frScMM3jX4WzdgzXtOEVbS2WzO4CIeIbSQozzghDa0SPkcXW1tRuqPkaP-bdiNy6NJ2YQ1OK-tlw4GeurkEGRnbKrpZNSYOPcQsrSuRylbV0IQ617MZVcWugQhHUgUQNnEx3u131RGc4jQdsHnxTFWmfMeu4jMebIy6DMp6WLMNIpud_ZPAu4pFXJniFb-9vk5SpoWiFAzamLymi1Znc9jzlYe8TwP-sTwK1Ns-fAUjEO9CkoIuhVjK6vTj1x4gbL3d6gjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2920ff853.mp4?token=qtJ9ab14bUcEXJm-szjjWfBMr2iX4GRRA6f7eS2SwNnRkERRadDMHJboIuLEniPyTh_4n5b9sIzSk_frScMM3jX4WzdgzXtOEVbS2WzO4CIeIbSQozzghDa0SPkcXW1tRuqPkaP-bdiNy6NJ2YQ1OK-tlw4GeurkEGRnbKrpZNSYOPcQsrSuRylbV0IQ617MZVcWugQhHUgUQNnEx3u131RGc4jQdsHnxTFWmfMeu4jMebIy6DMp6WLMNIpud_ZPAu4pFXJniFb-9vk5SpoWiFAzamLymi1Znc9jzlYe8TwP-sTwK1Ns-fAUjEO9CkoIuhVjK6vTj1x4gbL3d6gjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما باید کمترین نرخ بهره را در جهان پرداخت کنیم
🔴
کشورهایی وجود دارند که اگر به خاطر ایالات متحده نبودند، متحمل زیان‌های هنگفتی می‌شدند، و آن‌ها را کشورهای پیشرفته می‌دانند، در حالی که آن‌ها نرخ بهره‌ای بسیار پایین‌تر از ما پرداخت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/151512" target="_blank">📅 21:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151511">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d789c09213.mp4?token=hPJcpAaF7gRuH20es6OZ1_O9jTTIrrxCtHjj6Sz5PxyhN9PQOhJywI2UEC1xoRTcc1uzD_0OeS8WKdCVH7Y-pdT6DE3Isp7uCLeas1EfLkIY1He9VOuyKY4iPF_K6h6ySZyl9Y3ga3nu9edzlsyOoMWTUZv2JXNPb-J1eWN5BWvSGn9Ej-_oK3Zg7dmn9ut_lm1pmUjjw-S3OBsLUJcvp_Eumhlf96K6WFOTLFa3YmJwO9PHvkQnU8Ul6_GQiOBC8vie5ZF1Fw4gfIBAZnNb6_Ife8-hBRjdmNU6UD6yi7ujp686FTH47q1YvnFetxI7ny-8FR41suwde2I_vYwh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d789c09213.mp4?token=hPJcpAaF7gRuH20es6OZ1_O9jTTIrrxCtHjj6Sz5PxyhN9PQOhJywI2UEC1xoRTcc1uzD_0OeS8WKdCVH7Y-pdT6DE3Isp7uCLeas1EfLkIY1He9VOuyKY4iPF_K6h6ySZyl9Y3ga3nu9edzlsyOoMWTUZv2JXNPb-J1eWN5BWvSGn9Ej-_oK3Zg7dmn9ut_lm1pmUjjw-S3OBsLUJcvp_Eumhlf96K6WFOTLFa3YmJwO9PHvkQnU8Ul6_GQiOBC8vie5ZF1Fw4gfIBAZnNb6_Ife8-hBRjdmNU6UD6yi7ujp686FTH47q1YvnFetxI7ny-8FR41suwde2I_vYwh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سوئیس:
اگر به سوئیس نگاه کنید، کشوری بزرگ، بسیار بزرگ و زیبا با کسری بودجه قابل توجه. با این حال، آن‌ها را از نخبگان می‌دانند.
🔴
خب، اگر تصمیم می‌گرفتیم ساعت از سوئیس نخریم، دیگر نخبگان محسوب نمی‌شدند و ما حدود 40 میلیارد دلار صرفه‌جویی می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/151511" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151510">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ : نمی‌توانید با ریاست‌جمهوری با بی‌احترامی رفتار کنید.
🔴
من فرصت‌های زیادی برای انتقاد از بایدن، هیلاری کلینتون و باراک هوسین اوباما داشته‌ام و همچنان هم دارم
🔴
و افراد زیادی به من گفته‌اند: "بیا بریم و آن‌ها را شکست دهیم." من گفتم: "نه، شما نمی‌توانید این کار را در حق ریاست‌جمهوری انجام دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/151510" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151509">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ : من می‌توانم هر کاری که بخواهم انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/151509" target="_blank">📅 21:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151508">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b33175d5d.mp4?token=mHRmfw_OixODhwqY__2Gz-IjtLsQaoDjTyzRZNH7qcG3Y6nV6KyTUwv_bjhmaXe-ERjy7i5rG9Fz3K81lf60YdTqM-yGguNOc2BoeGrtGKt7G1zZpZP824hF87CGqr_j0vU5TFAjN3GAiSfTSMXMWdLzg7E8BoNZ2ZZ_8Sw-KD17AN2x2HojDHhUhVYYH7HY5N78A30aL0XYuEkguQQ8Dj9IGtOx0c-UWdEAyBLiGzLbjsZJMWN_rn9ABOwCgCa_sDpBQGLi4vv7FBXsbX61TfslL1vmbGHhIKikfJ_1hQb64eRAWg11LkFDPXZOJZnT0XFb0vbtex6ClkJHNCTesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b33175d5d.mp4?token=mHRmfw_OixODhwqY__2Gz-IjtLsQaoDjTyzRZNH7qcG3Y6nV6KyTUwv_bjhmaXe-ERjy7i5rG9Fz3K81lf60YdTqM-yGguNOc2BoeGrtGKt7G1zZpZP824hF87CGqr_j0vU5TFAjN3GAiSfTSMXMWdLzg7E8BoNZ2ZZ_8Sw-KD17AN2x2HojDHhUhVYYH7HY5N78A30aL0XYuEkguQQ8Dj9IGtOx0c-UWdEAyBLiGzLbjsZJMWN_rn9ABOwCgCa_sDpBQGLi4vv7FBXsbX61TfslL1vmbGHhIKikfJ_1hQb64eRAWg11LkFDPXZOJZnT0XFb0vbtex6ClkJHNCTesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من می‌توانستم کارهای بسیار بدی علیه هیلاری کلینتون انجام دهم. می‌توانستم کارهای بسیار، بسیار بدی علیه جو بایدن انجام دهم. می‌توانستم کارهای بسیار بدی علیه باراک اوباما انجام دهم.
🔴
من فکر می‌کردم که انجام این کارها نامناسب است، زیرا باید با مقام ریاست‌جمهوری با احترام رفتار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/151508" target="_blank">📅 21:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151507">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2922b16b.mp4?token=SSRudYsNPTxGxeskUUuQfaKKrBUuUvT63WJdXRbYdD5DA6BGINYfET3SdBUyU1h4m3iSmJydeWtk_b1nvCyYTCygxPaEnrW5KvUAj7v3EnoDcW2B1f387mkSHs0Qnbmg5CXfNJW_Qt90Ad7BJGP3mvtHG1u-QqMK3dMwtLUXyUpfivzoTWZMdpM9icAVZPvOy3b3YEwFiIlDTCEqcOW9KKahfnkxfLIpuUQdJq_p_54zFhHoI9QtEsGkjMtIm_u7vdNeb-jxEmRFUIt7znCn573Tg9QESue38Vjbp-TJ7dOvXV99NKa6CwNwGn9aCCwX5h7lhTP3mVaEX7kuoPFnTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2922b16b.mp4?token=SSRudYsNPTxGxeskUUuQfaKKrBUuUvT63WJdXRbYdD5DA6BGINYfET3SdBUyU1h4m3iSmJydeWtk_b1nvCyYTCygxPaEnrW5KvUAj7v3EnoDcW2B1f387mkSHs0Qnbmg5CXfNJW_Qt90Ad7BJGP3mvtHG1u-QqMK3dMwtLUXyUpfivzoTWZMdpM9icAVZPvOy3b3YEwFiIlDTCEqcOW9KKahfnkxfLIpuUQdJq_p_54zFhHoI9QtEsGkjMtIm_u7vdNeb-jxEmRFUIt7znCn573Tg9QESue38Vjbp-TJ7dOvXV99NKa6CwNwGn9aCCwX5h7lhTP3mVaEX7kuoPFnTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جایزه صلح نوبل: صرف نظر از اینکه من این جایزه را دریافت کنم یا نه، من کارهای بسیار بیشتری انجام داده‌ام، و فکر می‌کنم این موضوع باعث تضییع اعتبار آن‌ها خواهد شد.
🔴
[باراک] اوباما آن را دریافت کرد، اما هیچ کاری انجام نداد. او هنوز نمی‌داند چرا آن را دریافت کرده است. او آن را زمانی دریافت کرد که انتخاب شد، درست در ابتدای کارش. و او هیچ ایده‌ای نداشت که چرا آن را دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151507" target="_blank">📅 21:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151506">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پیتر دوکی از شبکه فاکس: شما می‌گویید که دموکرات‌ها شما را استیضاح خواهند کرد. به چه دلیلی؟
🔴
ترامپ: آن‌ها نمی‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151506" target="_blank">📅 21:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8ed562e7.mp4?token=vmp-emckdZG-p4ZJNLYG6buOkELBMWjqgSv_gvW-NeMjvN-6tYHGGNZqK8IriYff5z6RMKTwWFAo4Q8_Svp1qA71pXnDF8Iocffd7BPe3azuUq-j4v1Z4ibTxqAsH3qMYU7fM_-iUAwOgjDvfHD8oiNXSC2uqsbmFJuS7oEb8rRzMXVkxKYj2RWVrRtGkOTP6Ev8kXba2ezo2vwUeHirS8qVKni1xD8N4Dhpt-paFBlQgfafdAThAy_1HZDduhbvVVc7vaOsauxIejhXsvSBiY3mKeIyVr1RLuOQwlDu7SCuLWD0WEZISRvDizgfH1f78Brg2k7s3_vLMAi-DzTaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8ed562e7.mp4?token=vmp-emckdZG-p4ZJNLYG6buOkELBMWjqgSv_gvW-NeMjvN-6tYHGGNZqK8IriYff5z6RMKTwWFAo4Q8_Svp1qA71pXnDF8Iocffd7BPe3azuUq-j4v1Z4ibTxqAsH3qMYU7fM_-iUAwOgjDvfHD8oiNXSC2uqsbmFJuS7oEb8rRzMXVkxKYj2RWVrRtGkOTP6Ev8kXba2ezo2vwUeHirS8qVKni1xD8N4Dhpt-paFBlQgfafdAThAy_1HZDduhbvVVc7vaOsauxIejhXsvSBiY3mKeIyVr1RLuOQwlDu7SCuLWD0WEZISRvDizgfH1f78Brg2k7s3_vLMAi-DzTaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا تا الآن با ولادیمیر پوتین صحبت کرده‌اید؟
🔴
ترامپ: امروز یک تماس هماهنگ کرده‌ام. امروز تولد ولادیمیر پوتین است. مطمئنم که شما تولدش را جشن می‌گیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/151505" target="_blank">📅 21:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=WgJnB-mG-6DfmQIPCqAGxEhXQ0gRBs3txymdSVc6OHcgpe8jQxCeq1LwIhzRIgSa5FDbmILlAGZDk0OIe8JAN5egGaiJH1cuLY7weiib5HM-KNbbhUkEECdFLNfnRlOd4Q2q93I20Lf4ljW05IwWVm9dOu_jfbw2oIsUReV1emuurHW0onykapNwLZXHuMpkzVB0gnlxsCp0PBTtONbdBhW2dR2zvp-b-kInbXU5KSW0UX3fTF-t4N-Vk9OV1dr2BIFJob6i8fZlgm1Lke5skfTP3tMVureSJ2sLUoLfwKB8HuC9gaVgwTNjkhf1oyP234gglSFOo5y0WImmMSP5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=WgJnB-mG-6DfmQIPCqAGxEhXQ0gRBs3txymdSVc6OHcgpe8jQxCeq1LwIhzRIgSa5FDbmILlAGZDk0OIe8JAN5egGaiJH1cuLY7weiib5HM-KNbbhUkEECdFLNfnRlOd4Q2q93I20Lf4ljW05IwWVm9dOu_jfbw2oIsUReV1emuurHW0onykapNwLZXHuMpkzVB0gnlxsCp0PBTtONbdBhW2dR2zvp-b-kInbXU5KSW0UX3fTF-t4N-Vk9OV1dr2BIFJob6i8fZlgm1Lke5skfTP3tMVureSJ2sLUoLfwKB8HuC9gaVgwTNjkhf1oyP234gglSFOo5y0WImmMSP5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: من، شاید، از نابودی کامل جهان جلوگیری کرده‌ام، زیرا ایران هرگز سلاح هسته‌ای نخواهد داشت. و این یک اتفاق بسیار مثبت است
🔴
رؤسای جمهور دیگر باید این کار را قبل از من انجام می‌دادند، یا کسی باید این کار را انجام می‌داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/151504" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ : من هشت جنگ را خاتمه دادم. یک جنگ دیگر هم در راه است. من تمام گروگان‌ها را آزاد کردم.
🔴
من کارهایی را انجام دادم که هیچ کس دیگری هرگز انجام نداده است. من در حال تفاخر نیستم، فقط حقایق را به شما می‌گویم.
🔴
احتمالاً هیچ رئیس‌جمهور دیگری جنگی را خاتمه…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151503" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ : من هشت جنگ را خاتمه دادم. یک جنگ دیگر هم در راه است. من تمام گروگان‌ها را آزاد کردم.
🔴
من کارهایی را انجام دادم که هیچ کس دیگری هرگز انجام نداده است. من در حال تفاخر نیستم، فقط حقایق را به شما می‌گویم.
🔴
احتمالاً هیچ رئیس‌جمهور دیگری جنگی را خاتمه نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/151502" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151501">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b240a5223.mp4?token=npNIubGZYLmaPXeowrWdKx2xEeYp2zet9RsnFEbOvSfnd340wU8yZMuosqVaBVtYmZYFOcCW_0rYk2uzD6JGg4mruE2gZYy9-w8UhAy525b0uWZLMFKRcQ_vvQnJ7ppLl6ggNyJBocWhGtJW8GYzXM7CuJpM2AjsjqyrmiC5CteG14EEYtbMsKW1wTxR9zG70PFyCtYegl0c1ibAYYp7zl8FYGOyk9OCGuh6fpoP-5irCT4G-m72PWqR4aDkafzlI1_HpA8NQ9Dyes_iUFPtxd7W6eD4ihsxFjNHvtyYj-5YZOpXyMS6LhdH8Yi-3CtV9Ukhbmf1enfWNXY-yYWKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b240a5223.mp4?token=npNIubGZYLmaPXeowrWdKx2xEeYp2zet9RsnFEbOvSfnd340wU8yZMuosqVaBVtYmZYFOcCW_0rYk2uzD6JGg4mruE2gZYy9-w8UhAy525b0uWZLMFKRcQ_vvQnJ7ppLl6ggNyJBocWhGtJW8GYzXM7CuJpM2AjsjqyrmiC5CteG14EEYtbMsKW1wTxR9zG70PFyCtYegl0c1ibAYYp7zl8FYGOyk9OCGuh6fpoP-5irCT4G-m72PWqR4aDkafzlI1_HpA8NQ9Dyes_iUFPtxd7W6eD4ihsxFjNHvtyYj-5YZOpXyMS6LhdH8Yi-3CtV9Ukhbmf1enfWNXY-yYWKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ما شاهد آشوب‌هایی در فرانسه بوده‌ایم. شما این پیام را منتشر کردید: «آنچه در فرانسه اتفاق می‌افتد، از کنترل خارج است. مهاجرت گسترده.» آیا این می‌تواند در ایالات متحده نیز رخ دهد؟
🔴
ترامپ: ما جلوی آن را گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/151501" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVp4dz76V9BvjU9YNuItE4Mp1VqCY-Xg31A2Fzxldjaaio4CzWnd3NO1MiHVlNmqZYIDuk1HI4DD6QNXr_TDm6oWUcCyXI439i2iQCJKiVdZhOn0_VGxRNqHKgnYZuls0-cUgP72ju_c25suuw5XhMSwIP-_mDKGD1kf4PxYdB3JwuogegybscReK_f7QT7ugb-wVJ5M1BildEEtDX49EGsxMXT4PIMofGY4-riJ5ALGsvhQ78dAGjUhUdCCrGPLMIsaYVjlUMWa9C9BcA7GizP6Le7OcGH8_NAzBTwW3ij3Vi81oW3GvdNxkVVKZC6RoOQ1xAJwlaH3MBjxvn0G5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین در حالی که بازدهی اوراق ۳۰ ساله آمریکا به بالاترین سطح خود از سال ۲۰۰۲ رسید، به زیر ۸۳,۰۰۰ دلار سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/151500" target="_blank">📅 21:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02a2eddf.mp4?token=UUDLd726KIu7L_Dtgb12-8q8hM7pnY6AcVLldFPdjQasUx9m6eQJ-JuQacXsnMeARaloGPRGiv-vksbPMv1nzxf28n9NXel-Iy2kbJIqU0WqEITXnX2ms7i9ZismKJMizphbWcyYYCsobBWjgI6j7LlXwq6N34e0tMoY09RafA9OAXbxl6vYEaROER7goBkSPtYjYU9oqBVTMZBv17B5NGKuTg-6SqG-9cLwMprb4V-e-5-H1fb4ptqNh8xb7XBdfQ7wtnkDlYyju7HDS2Q3lrk5LLhotBxJoedkcHGSTYLiDygSv7R_5LG0bc4BKGYDTHMVoQviSUyA-jQ4zPfGJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02a2eddf.mp4?token=UUDLd726KIu7L_Dtgb12-8q8hM7pnY6AcVLldFPdjQasUx9m6eQJ-JuQacXsnMeARaloGPRGiv-vksbPMv1nzxf28n9NXel-Iy2kbJIqU0WqEITXnX2ms7i9ZismKJMizphbWcyYYCsobBWjgI6j7LlXwq6N34e0tMoY09RafA9OAXbxl6vYEaROER7goBkSPtYjYU9oqBVTMZBv17B5NGKuTg-6SqG-9cLwMprb4V-e-5-H1fb4ptqNh8xb7XBdfQ7wtnkDlYyju7HDS2Q3lrk5LLhotBxJoedkcHGSTYLiDygSv7R_5LG0bc4BKGYDTHMVoQviSUyA-jQ4zPfGJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : این کودکان خردسال... فکر می‌کنم می‌توانم از این اصطلاح استفاده کنم. باید مراقب باشید
🔴
گاهی اوقات، شما کسی را کودک می‌نامید که حدود شش ماه از سنی که باید کودک نامیده شود، بزرگتر است، و در نتیجه، خشم رسانه‌ها را برمی‌انگیزید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/151499" target="_blank">📅 21:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
🔴
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
🔴
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/151498" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578f2076e4.mp4?token=pVeSl1ZXtFS-_PZTxYlJ_DmvdSXJ7upzHWJEDiKY8VfHWQBpgGdvX0Q5UG2JFUXWCRKYEcXxjba6hVZ2cwxKNSq9pYPm9iQ-4klGGzeWI3WGCJHKrj-ViGeTxek-Yb4HO2D4xXBKEwBitFavu_6EjrGbXs6lAUpOFAp7pIqxmjjFkvOv3aMjq-OoZJYjam3htI02nDY8l1xqemy9sIB2HpvLph5botzgEgEB3O8NQQdaQjrkealRN4qXALmIG705ykM0xFbQUAzyCrW7N1hKgeOEOJzylEvqT7iw3a-5Okcp37QvSMTFkLs8M9JihTaUwvOsCfsk1EK4x0gk95qJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578f2076e4.mp4?token=pVeSl1ZXtFS-_PZTxYlJ_DmvdSXJ7upzHWJEDiKY8VfHWQBpgGdvX0Q5UG2JFUXWCRKYEcXxjba6hVZ2cwxKNSq9pYPm9iQ-4klGGzeWI3WGCJHKrj-ViGeTxek-Yb4HO2D4xXBKEwBitFavu_6EjrGbXs6lAUpOFAp7pIqxmjjFkvOv3aMjq-OoZJYjam3htI02nDY8l1xqemy9sIB2HpvLph5botzgEgEB3O8NQQdaQjrkealRN4qXALmIG705ykM0xFbQUAzyCrW7N1hKgeOEOJzylEvqT7iw3a-5Okcp37QvSMTFkLs8M9JihTaUwvOsCfsk1EK4x0gk95qJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
🔴
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
🔴
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/151497" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcpsTU9Y1RSXmoXosKg5hBydCoIpzv4yfv-5qQ2Gc4Ut0oGbWfWtIw9JOo_2BPuDw09d-5bPP6h2Zi1aFJ5_D-uj1tkaPr_R3NlbKZAEIz_6mGvz10p7utHjIgmIa6e1JXAt1mZ8sRkuoVgoYwpw7_KrR2ugif8h4EJSaWLeBPaDEeyM6SUVhSYaoco8osNi2GiH5UY8zvelAmVJh1p12CvCPT-rgBjZ0a3PKRL2Ss8Dg8yQRKBeD-rt6ehvAnhpevw2o0TF5ovWumzfGyRQQqCiTxFWjnaV6NyU0OeEwYmLG8T99r2pQkG1u2G8oP-dWEEKsj-o2Y-kU2hZN_UEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده تهران خطاب به پلیس فرانسه:
باتوم بر سر دانش‌آموزان؟ مگر پاسخ مطالبات نوجوانان و جوانان از راه چماق و سرکوب و زندانی کردن ۵۰۰۰ دانش آموز است؟ چرا به‌جای سرکوب، بستر گفت‌وگوی مدنی و شنیدن صدای معترضان را فراهم نمی‌کنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/151496" target="_blank">📅 20:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
عبدالله سرحدی، یکی از مقامات جبهه پایداری افغانستان (طالبان): "زنان بی فکر هستند، عقلشان کم است، چیزی نمی دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/151495" target="_blank">📅 20:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN6wkiznErFylw0-pKUROBdBpIYyigAzZM2MHme2PrYdcjiufpdJWuqi9-pSWxSj7GmEovg7nUBtvjHLX3GK2wKl5o44gRMjmFoN74r5nw_i5rcnlmlxa8heJBTpT1EgkEeWWN1OyFP5Kz1UNUSm8bQ2m2g3YyMftMBmcjayQkA2qIZjNRv6pM-AMIv7g0yAyoIfqiea8SUfPRu4Q2O1S0XPqkOYxkKq3UZwSveskFm0U9RUMI2cVrthy-Pvpfz22BPW_36dnxsPEveLIkSjs1GNKeIqCoAWgV1OY1974VFcnahd8q9NztjdJF62_S6O76r4WhkIaO64-2BWoxS-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد بدون سرنشین مدل "گرن-4" با موتور جت، امروز بر فراز کی‌یف پرواز کرد و تصویری از ولادیمیر پوتین بر روی قسمت زیرین آن نقاشی شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/151494" target="_blank">📅 20:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حدود ۱۰روز از اعتراضات فرانسه گذشته و در کمال تعجب تاکنون کسی کشته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151493" target="_blank">📅 20:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9LsvwBQv6-l5fQGMJSc5NS761-ro4Em77PKvDvVcBwyTTzDaIwBygqR0cnA3BMAWYvfL4_BU9eEKk7gQY-VzLXoc-ysbabYhrdNMJlBrXmZNfk6ZSojGUYsdCAUq3qp8F9_gvtopEigEbBys4USPb5k-sob3fSop_MtR6yeD6GQ04uV84UdEKF4jIVgN6_Gns3Qldz_W3sZbd7bgGIjU6kTsqSm-DB2HAdg00mc5bwIucLd_kcI83xSZbLM_IGN2gLjaYnCAR6bfJRF5hK_nLKN4MAe2PoPIWW0ZkJMeZdOM1P-so6n4uOezRaVsF7ssRcYZZ48Jkh3X0zHiKIsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ پرواز پهپاد های آمریکایی در آسمان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/151492" target="_blank">📅 20:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/151491" target="_blank">📅 20:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151489">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: بر اساس آمار منابع امنیت دریانوردی، حملات به نفتکش‌های عبوری از تنگه هرمز در به بالاترین میزان هفتگی خود از زمان آغاز جنگ ضد ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/151489" target="_blank">📅 20:32 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

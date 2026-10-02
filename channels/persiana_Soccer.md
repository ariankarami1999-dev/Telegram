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
<img src="https://cdn4.telesco.pe/file/YmTo2vbAPHUs7Ewjf6wBukuQeCaUV89NJIeYhmJUo--oOPAQcqZE_bHEkq9N95BfLo7oihm35V4OW9a1IsQ7qFTV9uLyk-gXgEucPMxjD63iAnUaTUlZ_SvUpVCoGLhNdY3yYLZ6FZep7Cfry18RsksyP8OnT__4BdTIcjlrlTPufg_F2MEmx4QLjSuDUHg7L_yz-ZQfpY14wgtHZHDQKd71is4YrEusYhgT4QeZa2CAavrrEVu13NAaM1CGPSPQVGWTLXAhaastMlCQ8n2KVJIdcyt2vl6N91GKVu4zbXrDTHUcDesjA2j3oaC2lE3KmAKbA9vY0HaS7s60wPy6Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od6EOn7qrtrKhcBf6majQCDXtMthA9lFGaRMchgZT7mUt2EdyfFcE35oXvDXNxwu8Mm52wlzZIFKjTiiBIfYZ80sRIbeldAxw1MdCnRA7kSFKtrYu7S0jVBSDdLBkgmDeNSZTYtAyjHx6vrhspED4iC8aj1JUD_B3YBf2iX0LB4zO5eDrovNw8IdIxcEY8mmwp_OFJeIrINFvYsAJx2HFfF6heVWAm_Uz_A7qymvF2MzUDUWeoiTR8lCgq-1tUbO8zHCeleDyGkt7_Q51Ch6uQ8svgE7ZosZAgq-zNHl90HibOmfUATuae6ZCcCO293HPAExBqQFBTN6B94tgQ9ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=ld-P9f7aC0I6-a6MKm0Kp9C3SInoJom-_aw0IkuFgzf4PLfhyjoH5uy1M8tV6s8tZc3iej0TsyKrs6WJ7NivU6a295Jl9n68yVFYcV6Wn1NmIYQDuRgOw-4lgP-bzB_U2oizLKoTWOPEjKfZ-B2mpbhS4ZBJcAEiZQ4N2SalUTm7eh10H675-f4n4YOodKUCxx_Hc69zFUcXjIAyNuwE2zHiirFSAOEsuB18w34yFmYl3BZjXOx1imckl4-BD93KQpASJJvctJ__mPBCCXTeXAXyy4ciqcJEDvLxehx324dbzX-lFN6QydyHPw_aURsTBxr2c58O3EDpG-3X1K2DQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=ld-P9f7aC0I6-a6MKm0Kp9C3SInoJom-_aw0IkuFgzf4PLfhyjoH5uy1M8tV6s8tZc3iej0TsyKrs6WJ7NivU6a295Jl9n68yVFYcV6Wn1NmIYQDuRgOw-4lgP-bzB_U2oizLKoTWOPEjKfZ-B2mpbhS4ZBJcAEiZQ4N2SalUTm7eh10H675-f4n4YOodKUCxx_Hc69zFUcXjIAyNuwE2zHiirFSAOEsuB18w34yFmYl3BZjXOx1imckl4-BD93KQpASJJvctJ__mPBCCXTeXAXyy4ciqcJEDvLxehx324dbzX-lFN6QydyHPw_aURsTBxr2c58O3EDpG-3X1K2DQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=jPwK9zcDUbtB1ZhBbwmXIC5w8Cyd7np6Qhtx0qyEb4P2juV0HXVv_ACoQa1fdEUvT0dY0X4DccGRlen3BXFeXoDvlWiE5iEVb-dNY-RdSZiI52jQ_wrZzqwGy_6w9JajF3Ls6TumppM52vJhl-jUSR9CMvc3iBF8IB1kj6n7S9es-ryLzrWC9qy4SPUCfgATl7W8ip1nM0m2tSyqCI_PzCzXLfBKfFfh2hOm7eQa_ldizQ4WCXGVN7Hix_A1QyYkYS772WwCaBHrfBv01qKEB8wZE6XB_osAjFm6_8dysrxNUa29Fv1jS757Da72w7nHwU5jfJacnW7K-_tLnP1ArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=jPwK9zcDUbtB1ZhBbwmXIC5w8Cyd7np6Qhtx0qyEb4P2juV0HXVv_ACoQa1fdEUvT0dY0X4DccGRlen3BXFeXoDvlWiE5iEVb-dNY-RdSZiI52jQ_wrZzqwGy_6w9JajF3Ls6TumppM52vJhl-jUSR9CMvc3iBF8IB1kj6n7S9es-ryLzrWC9qy4SPUCfgATl7W8ip1nM0m2tSyqCI_PzCzXLfBKfFfh2hOm7eQa_ldizQ4WCXGVN7Hix_A1QyYkYS772WwCaBHrfBv01qKEB8wZE6XB_osAjFm6_8dysrxNUa29Fv1jS757Da72w7nHwU5jfJacnW7K-_tLnP1ArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDkhm-ykVvd1REEPrGqLGMsqLjvkoBibnZI_kVWRTM8sDTSu6OLQMotH7a5e1zninX1-K-XJEqQupND-9sQ8gUJwL7ahO5uKGIMikT2l-7uqi-gvFOpDlGhb1rRKgzY6JgOBPYSbvaE0Ng1M38wJHsXfBdUlBok2sTlFlp5cttdbObdLx3kTuZVBsNPyaOEcIJlAH8v9d4WFkrS94_BqciVjoVHFjVoGsqdSxAFw-GTY5saG7hFx_441xfaGeJJECRtCRjxuoaJnqtMNr3itGuu4cMuV0J-fqvDbL9kjxKx3kW9Sq_1fJXwhF3xgSDmZmkYltilqzRX_suKhVpKcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPXIxDl4k1QE5n6qo06iQzUZ0XfWHGodtlnlF1dIGBprhIuc2WZyXV30XKQVKn4LVwyKzHMUwhRD7YbNP1NeIfV_ZM7Q1eP6y_CSVXmFB9eEhEPBRL1LKzDpYFQ12fQyV2xdvuU7ArKzL-dsLMLwztGUj2tEKwMSEoTt3P09uwKXYGZqzky5Rvzd2KFnFplx72R7iiAhDMAOWbKSGz7K8cWPR4_O6yfQL8jeg4VVgRyDwgmorBJJg6pSgyugXIxtowUD0dQ6NjSOvglugmaQiDn79C2Mpepomx_AFTmUAzgKFxwltwHvJ5rie4qERo6cYI7F9VAlseaHRiVOJYvpyvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPXIxDl4k1QE5n6qo06iQzUZ0XfWHGodtlnlF1dIGBprhIuc2WZyXV30XKQVKn4LVwyKzHMUwhRD7YbNP1NeIfV_ZM7Q1eP6y_CSVXmFB9eEhEPBRL1LKzDpYFQ12fQyV2xdvuU7ArKzL-dsLMLwztGUj2tEKwMSEoTt3P09uwKXYGZqzky5Rvzd2KFnFplx72R7iiAhDMAOWbKSGz7K8cWPR4_O6yfQL8jeg4VVgRyDwgmorBJJg6pSgyugXIxtowUD0dQ6NjSOvglugmaQiDn79C2Mpepomx_AFTmUAzgKFxwltwHvJ5rie4qERo6cYI7F9VAlseaHRiVOJYvpyvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJUCNty5cruubkTaGqsaKq-WtOQM9-T-cjG2XLqcRQv46WmjGbs548eQLtPUFY9Wu855ZmY-xpvRkl2KjdNgec8iNYBGjaYvTAikzkc9WTuufrdp5j6Tu7xOBVoWg17mb2zrjChD_8s_EbM8EmXEFrNEVfssmkDqNkgFxUr7CXVIVYACTqzS2UpfWmBDsEi8CNek-uJDjfDm2OUS-ht1aFJBpkoF3UOG4lVA6VZ5RV6APAYJhsl46hH85Kz_hTUAuYpjruRdF6pgsGC6q18t1GxzENZUz6niI6oNxVUkzb24sy9RpYzcI7PGYrNcRvZmD_mbudzjVTtJ8chYiPCwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFWbiRVZLG3ksodUdNnCMwT1nHir1BfNmS14hg1JiZNj06nd_DuyFUEjbarOO4BkyT5cknCRGMudommTJGQmo30pjjyGQLLoE3aocgtfDZPWWfU-4BxhMMQszaBHBXsGjNjDnJSXQH4gSvVdy9g_7sW0FoZD6aONojExHzQ5nf2fVvLZ8FXY-bNuusRzbXQWP1TYvAwoNu7nP--3357nCCS8fcKUOlzN6cR6f8IjgKgt2pBP6FL1llmrNM3hx-hsdnAzwc7p9CM63yZJWAT14XiVt-e8WLkSrOhMaivk0PwVDe3oEd0bwRnTNEqCrA1l5ZoQ9cMd2wEesey9kd3l9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx1QKKhw3I4tiyscfjg6AXmX8LjSIH-l1VMqoLTvlrjKjEVFBf4LFnAim6lyOxjWHkUMXjAprrK7G7WxR-1S2QjSw_iKgwHO_nQJe-SaUnaCAoCqC5ADiJiB1ZaQkE-46pOUi5_P4hG0yGpXHAmfohbBS9WZt7lK_6g-hb8I-FVltxKVPjwNnQpa7VGDu_gHVSM--ofV6E7bLcm6QRtIbHa7I92gkTFlHlsdGSQROY4x3kKZxRQVjDE5mPj1Ll_zu4MER7HMJ7-Bp9fnd-p4sUxdbpWwqYnP5OzqlGEv1SBnLjX1BpgFObtjt3Ba5weXhgCapaEKQidyw0zNIRY0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlUwWO_QksTWywRTypCFYSxakbPMNh4-bMAsh-tICsH9LZ38jIdR3i07zNe3TFOwkE-r5_t_vcz7RJSDMp8OP2IdA_5A2GM5pcYRUcWfXN-fFPyYfPHYRv4lMn4pse1NphhPCshBDMMwUl8HdgPpYpXe4vXXv39q5CwA0F_GU7y2eitcAceZhoQrgfmLJWeD_CXCI1xOJIQZWIxSsRcP5epu6ScOGov6g0HblIdaKn21H0Qt_yxNLw4ohgO4WXRZQjHRFmjrCfEoXKYL7fXAogrRJa9gMMcvKJFS_IDpnAPrEkbjs8rTsKd8anrPGFokA7hRfigwsmQtZkvRTKx5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5PlrlXyN8EEjk0txR272gSHAJml2Y8sHFhpgRRh47_YeMLLeJ3R9-LLaltH_aDHwiPaP_0UhH1X12p5M3VOl5eDsN5r5u6BSOrl7aH-17SACTN0Odl9TOn8nXm2iIuSwg0-e8cOEVxgYP2ddbIdFz3qhrsTDsP_qZbRacnnYu7AvganAN8JHVBWxMZavvGWmOQOTcxsQOafP_w6-P_sE43-1P9IFCRal1c7a_2f-R4oQhCgf5pcgdgTkVJO6BX1niio0ve8CKKB2sfcSNVYhj-G0Pz45C-700aw21C1cIU7c5veLjt1B40pRNngw2mojtzLsF0pPFb0v1k2VMWGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر! P9
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30825" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnD0kc6Fx4Y-pcgm-4rTE6hZZDVp9BunkftdIhL0LpXEgMILBR2xOwzLidc8tkLHqvvP5d9GbZ2xKchPuZQ2-2cbSQkUKQd1UYOmOWi20KgQIALoLtxulmXZFWr7I8tme4QAB2Rkn4Pex6v-8G7RE8e4Mq7mQ78UkDH_YYta6qDxxC2Ukhs4CBuCta9ff3oarJl_rmgSRq-_1Y6mAEJHD3_tXVh3qHgbZ4hx1WseWHpBpz1YLQe9sh4rA6517lWm5MqeDQB9EcEZ-feW6jRJvqTMy5V7kNy1FC81CbGqs6iX-cwr5IrclC6SvnLAqPCeYfD8wKO8mYH133I7uEZxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9oHcWuJs89u4LZt_R8cL0g3H6qzk0d4V5UO90RhQ3J6vepu7-P5xnzppRAz_GVSjC3fMU4K5iSGlqQUWD1yLjytPcDzN_3UiiuvO7iR8zHDu3mSYrOQcXCPwc3QtdCDAgSYF5sOPgy6mAQOAJ24UP97Rc4uC-L89mxzFrHSnv9XSn3P6xT3JezFsaOdTEw_FpXPRzUfwB9JDqhUBi7v_sX1AQFTmDkVPmSyJDMY5r07gBYx4DkA0qXzOlvxR5zrmWrlo17_lbJJ5oUAb23p58-o6GB0YdWmGBFu7d_ndH8tHqyHMJG-YDJvgUGzfmu4jj1WCdneHuVNPvWR5ohH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE5RuICEUjhd-UCxW7Pm3fGf_7jglpO7AiKMHPcz818GgGgt0SLFeavtgXJohDHZRWm8sacwcKB0rLEyjb3KsyNnd9epPUegaKsPbbgtyB068pcZQvw-9HCNNhtVvituLuLouNmsdNZIJ0Jg7UVDiD9bdYDc4G48fzzL23h-rQQ1z4WafxQKz1D7nPf_Xt3Fk9HlLhvq8St34aVJHnTzzXYBBqbNUMy2cL_fcsvh4HqXmyjmcvAeNKNAdQOXLZ66k2tjb67SMWyWOSBSCaWkhl-HmMOBZmQxAtUR57zTSuu9jikuhjKvv_U_bj9mnHpaplv58P1wr6-HvVrLknTeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYDKH55BrxcH2Y69hib4AMiPcvh3u20FTLs50eRoQ7YVIN2_JTcY2iArClGbafWiGxYzOVPofAr6YUlcEnXL5mD8urm14LMg05DJsO9vq5NLVN9olVf3A_ZtcfhcbZr94JjpqckVzRZ9oAp3R_fx4kvjtBuEdjn51F9hIBlcEV32ysVohKh7Ks2Ctx7d3S8BSbRdyXKsU0SDU0Rx4Fc_IiV9-HMHgAZrHW4Ma5H4_UuZ0_3jxRzD48GGqhdRUeNQwxbc3nU8bzcXuUflCpxxDiGbp7WzprJzdqkKJWOnBZeMUT9PgV5C5ixlG8kw5N7esmVVEJJndLURXIRnf7KSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXK6dlOocevOCbPTaIcbUxOR-OF2gr2KME7qcu90QESWVZzE_hkY5SlZoIRL2lRbNow5wWCbmsXk-lPly_VOxiTDCA1m35Rej2cM3cak7m0PaZ3mXmIlzy5o-wKsO-CUK2abJWZJ5myX_9dwGvl_4i_szZoafc3NJlZ-H903PXGWyLLNCJEWmfnFab-jxbx_YRgAzGQjyr18MW8eIMXU7TI5YSz17DxY5BTqPBh5vpRvma7LajdZPA4CzbLAJlnXpHFB-scjURSGGmTNrdM5kXw7F5KjgKwOJAvQ7KbIAgp9hJ48h7UIneIyLVg88zADLBuiZ7UJ30BltqsZiklNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbiNRh5uVFDeLw3255WJ60wVWJkXseiCx5303JgxBn4UMMX1_30UhczQs6GtibYB1lUe4Fivq3aWiuxZ3ckomnfccSCvJIMo95Sp2ypA2wBZaGgu-lUFm1roZ95k37OxYVuFlBpfoR7DJ73JknBI9Ozo3PCB1ZowWsOsEhToMsRaE63OssJrRKXvW4syQieygXVz4kqc_XRzovemifSKOYjPRs5vnHBQ6lL1aZ4u3u1PS4IqIDg8HzW_QPv8DU0YgLHYM14YwwfzZSRJlZFGJeiw1FVQcnW3Tcmag8qo_Wf-VtUIe_mXfkXgSYQbrfa7x4b5VBf9xMqu115nSCZ-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKM98PjB6UdMBYevP_RenyjHHVbHeekst0_qSZFck5XLVCQklZDR_Z6MvRz3dYRizr2qOvKzGG_hkqYDqkoa28NkfZLQH8vBNDzjcf8WwhWd4b03k5WPoZDuPpmfEEIKggP8_9GdcztJWvx1GUfdSzBU9iMGq4IYzhMN5AT_IeCP0gUgyyEZ1xtsd1hMfOUbB62OWolbuObD0g2jHhHwdPeBaPJ6ld4UizVS5AGxqx-XvOvOnfTak0MkNQNidIHBB-0XVT5kK8fZcCzN_stHyPWsk5N37XJ2gIENQz5p5LHlT5u0lF4v6E2FEuU2D2ajCtTEOI2veX4bMtZ1OEfzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7HefQD2XLeBXW5UauNOTr-6cNsRmI1gedOno72u6wYACeGV5ktMn1mY7DiNGXPbjEOt198kyOdtVRxGvVgu5TQ_rhGBoY8MPAic3_Hck3ktbvRnfoBR9Plzl-P7NfuM913bz49ZT1H0u8YVb-Gkfbkr6Ut8xERWcISjTbmiD5kgBjPpXTaMQ5lvFNCS1_ww5rZxxxg_QpgEjd1IIWeSvD_qtPz9Y36qDE2O8_PvK3GojbUCEbFE2zTvXeMh1oFcyKaiySdp6XQ9rxazVB8_xh98dw16Zd6qqQftsuDPEWLby8R8dhCNIqahXw0pTwCID-4EpZ4I5MKCy1tLsF8qUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9fF1B2HsEGx65UyV0kT-m6hB9IQpx-EsJ0Ncqsc2L78WkSzlNJ-qoFTh64yJpOz6ks6UYkzoT36oZD9uFfn-PL-BMh70MZLAcMFd3OVYzDZz78Mm7O-88DsqTLo-kUhM9ILlaxYmN9-oQFXENAfjCXuRXp2hZ4ZEuj4g57zS-VbZGGBCjSghrFMO6d775WOMgsPBBgZZvMQ4apsLG3wRyd8xYbrBlK3jRkPvzMCdROVVFQLY-qaummTbKAxmuAzQwzakYelAxx-BfoibtoAxFM2RbKg9WnWnchnEoIvxC71e3QgkhG8AfiVnDJDiuDYJlNlK7sZcYThu0-Ua1SXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5QEdCuxOxXlJTsOaBSwNlUZxg_ku7YiCqqsYrxMLhx0kO4d1916elhqXLwTQltAxuvm6MGgLvc2s9CAi84wPfO5PyR7d72iCnHfCVwYQkezQ8vxyeN-_pk28NnpumKGjJGamdMblOMjVM4LmGRRSfUnFoMtaT9fo8jeZWH8c8vz_lvBurIVKvyWgCJ6ITk3HnggbEFKa3DOL05zowrCjB_gbLs6CHs5ESTeKTVPDfci1CWiRco33GD4XyUvJD8bg2puVbyVOWJwUInxOILQVzqLdzknDn3fg_FkQr2EHoSAkBdbGihRH-3FXJCmpwhdeYzMcmHFL49vz_CADKr1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEKDSmWumwp9KnlaJJNwv7Cl0Pj-aea2QKTjGv2drBRv1ac1vca1j4GUWgT1vjsLNCOacsAP4M5_If_X0VSkrun0s39FreU6tOD6On2rl32SkN7eDKz4K8ndQ_6dJirWhrl7g9Zx6jr9wNiHpFkHecnHR_8gN1WbEn_CO3sljhioSa7Rm_XmPpN5gH85eFRNKd5dX37Wp1q60W2La5bn3u4nG0XNYVXRFtqT7YY8liM3Lhgd3qwLu6sk0AmT2ypHljYhcMJHR7G2zjuCjIu8MqONgkzxjaE7WoMviU9wE491_gTi3znulg_0snb7qgB3dzRBPue74z-iRxbGCASkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=bm8U2NPocKl5q0s6zriAQ_b3B6Bq9x_WD597QfBrVDWHspqC1ZEphfUJ5G7OM5g-Di-7MXzu8KwYuL_WN6MO6JhVzOcCW-k4oS36EU3j02Fgl5RAVEaqosxey5U6Bp2ZPxkP8VJp0N2MwBKUpsUG2jGH3JTaV4l2YpKou_J-VVdPABLSJIckBLLQ3qYem8iiG9ITh6ncalqexzC4Oxk0qm-qbeBya82F7p92rH7yPzoXZjjwMnDTJfaIt5FLcrGG9U3NoEmorIWclV0zlzqoQU8-HGjLZhjPUeRiDvGM14iY-MBXmLyRWmR0w0-7ay9D7HHF0EOlj1Sq0T1kAQDTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=bm8U2NPocKl5q0s6zriAQ_b3B6Bq9x_WD597QfBrVDWHspqC1ZEphfUJ5G7OM5g-Di-7MXzu8KwYuL_WN6MO6JhVzOcCW-k4oS36EU3j02Fgl5RAVEaqosxey5U6Bp2ZPxkP8VJp0N2MwBKUpsUG2jGH3JTaV4l2YpKou_J-VVdPABLSJIckBLLQ3qYem8iiG9ITh6ncalqexzC4Oxk0qm-qbeBya82F7p92rH7yPzoXZjjwMnDTJfaIt5FLcrGG9U3NoEmorIWclV0zlzqoQU8-HGjLZhjPUeRiDvGM14iY-MBXmLyRWmR0w0-7ay9D7HHF0EOlj1Sq0T1kAQDTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4e9xgBFj67-Hv5-JB_Nm4qjzPirMlasXCfXfSu45cLN196eSzw9X5zCbGqGQqjpL1KUVC4JO5PGdtWZjmntsnzT4dIVcCYInrf9xmOY6tiWFv6mIeuWlTfMTyIC7XWPTbr84GWN28Mm89ojruIU2i_alydIJmfB_ccPYaCcIOly7LGmg5knVUTARS2cOlBYr1X_elKl7ECu81fNI7g5-dt-oyXktt2kDD_mdvBQCaonWeAhrGALZ0lZOvxwVZRfED2U_ZuxQ1XkXVOFnl4mDn3pcRYjaTwcagDrd_wBTxz9ZVstrgzxmi6UL9MufycB80F557UZtkJG3DEk2okd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiYBz5Vd4-9_FQ2IvoW2sotTvBEtZTQqX_COdqdm5-rMER6CNno7IsmM2mupwKZ8hqR3BuT5b-_eT4X0nfY37C_mwvZGBGcCj2P9ZuE7k0O4k7d4arZQKDHyEilcQefMfzg2Y17EaNNWYM11TKfSivFBE_CSP8AkzYDFg4LpXnk05XELrWMjvKaKTPNPogl7fyF7uVSscdKaU66lFXfdmx6Kca-atva-NbZLRKXUAm1KDUlHfvKZStbi9Ym9gyESuSgP8roRcRTlKgXpKSqseg0lNdocMndTYr4fSY7jDqKd4EH6h6ynAaQRpGrIgbJSIXe7IZIIrN0eSalEfH8Y9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBhCDyLec8ISPlh8FRa3JOOKsU8QyfA0DhF9yqj-EGRVx7M42JNc3WT39qd0RN4eFCa5Rb9pa_ljViyr18uaKNh4m3qTwXzKn3RnWwCPeScLjvdD3crWjWaXwFY_Z__t3YMbC55Gx5pCdqYrsElRjEN1rnP4-mQ9Me9nBxJbMAuWnH_sZ0qLWZYJzc-0mNpr-Yyb2Vz4UNzDwek7pv-XF9TH45dcJopxBbnbm0udPojprZFc0iKe2YcY8LiGjtCwdZhKq7gf7w4JkqvIolwZ_MdJc0AvOWkMe5XpvJQFET4bUI9vwn3E6VtVxrCbFj7CfaJpQw1y8SRQXvVXXdTx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jlv-TAxKOo3ivetRP31kYwqronvaSgB1H65EF5GLG-aF1rm84y1LKH0tYRVWyWkosR2kkdlya7SmO63rOndKWcsMwyeK1fQasU1HgvGm7LtMtuylmyRfar-valm5jlx_5GnDqeA45kVwDA4Bn1mTunwnGi-k4FqFP85BjTSzkflldESB65IdHU6f1ATzhbKOGvxAjlzrAbUr9ms9_5TwNMv1S3KNqDvNvPo2-l6RFMNiMnnnD3Y58L5kPv8HVjScs6V8n_gxiKftG1Rt-QdUxf_atYc8EgRyGWmynkTvpZxxLXTE1Xpg8d8bevMXqeCGikWYZXJLUpDnD-BNMFRKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0x2B-V0sJ9a7AsAiS3hyfkAgIuTG8Sj1ypLTYUeQ4_mdUf2A0Dv5zoKiwIhFeXsago7JeEwk-SX0WXHkvrZwA2tIgOK8U3W-6XDbBGLi2bt8RZZeTNu-oKu6a8v-GfYgQmWdqJX3kaGA5nBuloXVxZXSUIaxJpVUoGZtSy2A_rQ2rIA860ESxcKNf2AhvO5S3KnbJ1nR3PhVpcw_vZ8yn3reAHJqZFvsF3-6dwUr19lwFyJRwWGSQohqRJAv4F_yx-bIYQnBAz56pK5qJ7eQ8P3qbWMpIdmlLFCRl2njhxL2GkO9FN1xCP8eDnBNIC0-EkIOjS4m023SUUZBR8m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0nThgzQeOGNndP8qgPmTAXLobJDXZ56p3S66IEpx4Sp9cGR-6H-5BRvA6U0AJpiym9HkXmm2J0dRyNMSnmDd4-ErDJB65WZRAeAFgMVIxRZMQqfrYaINCVZ-0qR1oozzhS5Kiq6Jbje_UdV4b_pKNEwPT2HqR6X9_gYI7DpvxksSVQyeBVoTkMM9y-du6V59fPOzMXP4xz6WsuiGW3XWa-N6h9kIborZd4yW0-xBhAEurzpoP_Bxl7lHEGYdR4Hz58Pg6f5aHGwp7psiWVLbMSWqO_pcQemwENWd0llowySRnWtMQ6mrjFEpRIwInFTUblutRzkfvRk4KgVr1osIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlXUa4DqZwySCCj9_CdSy2Pe4SHGATE6wHRVzHvezql_l68h5-Frev__7_0wZHq1Ty9BcCHV-SrqfaLIPedDay-pjZozSOg3CEdHaae9l3_IHmlsfpSrglZuz7fnj9bF9AjFTYK6chjhVS-MxjZWnfPsPT7eZSbjk3_S1BanT19uDFsTtmlYQuf2hYljniEqKH7oOscnvCN2pF4Fo65NULcxs4DWsOsQWfiBV1U5aUr-CAMAEuWbUawhOqvYg-pHj4AY1OgoRO_indQDiacw1vg2wTn9ORmX0X4aXaGDf6twNfkoOpOhtdE7_8ommZIz8ldqjb6lESaXiuxucC3dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR4QHnuAc3yZwTz7rXGCFosQkeZq0GLkd-P_BAXggCnKG4_2EDr9S8oR_3bPhTMXlBp0C2s9zm_QSZc-Rt_TgP-NF2Av6-FArcIqf251_Ku_PHgwrs88fzRwggtExDJ26EPlE0xFgYs2aQ1R-YL_KLaKHQiTBPppuWsbFumDfM-bzdbZyQGsTY4xxEj8HWLYxyI3FXlKRXwtBOoLyF4s7rbYpd3_xnoA9LBfXXh3q2EmQ1OfU9bn6TwCSWlZMmyjZRy5cw11hr6sVyXlsfMPT0OzOpgRwVWC7zrsB0j9bZHj4U-P65DZ4veJ1m9SnammwocQBPMftFKStpneIWr04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAPza1lCNWEVqOhYMrPb5ILmSnjkTSi_3BRhlXLdslc_zs1tUOu9JJZjoCd1kdTnL9se4DHiBo1svl5Y_K-XYsmlkiqZCl7M1DzjbSf0E6-aP7FwF9vaPB195u5pV3xfekIutOJsE0c2bqFtdh1FV32JSndZqyZCIv12AZu5wRzc443ZsQiktU4XN-5X2uyWfA_Z74tGRrceNrGzJHSO-OsQ8UC8mbnpCe-Ni7HaYJXd13qKYVQfJ0ZNEt1WFzQP7CNRkmsOrLSDgaxItNn_7VsqGcWtg8pJzeCjQ5bk9xj2SlSi1Blzb57bRAUAn_TE2H3sgi5-V-hTxC9PbZuYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k56JjoZoNyyZpZn11-WJ4hOEivZqZ18HfIUSmAqX-Zl-OzgXXdr6mZBtcM-WexaFCAO8xnesspiM4egWZ4SC0Pk9vQvMkUNrFnVKtbEPFnUQgdA1_IsFkSwbNONC_imWRKsRx0VGPtnlep6GYmuHpQa5tixyPmNURnfgH6xOj9nTePMsdTi1zARMMJQSRBzHH4aGEqw_XHhN3MvyUE1m5ZLT40FOqt-2BrUH_WQxTLOCwDBuZUf4HrKGb3rTkNt_5hYh24bpUX3NTUW0Mm8I5QRNsQrCWyyG3Irle7hxIoIfE1rCRmoc8PSi5oC4tLZFSAZZ3E2vfauZMcHebQo1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEEPNpkK-Zrx6Vk9sncDSJWQ2Dfzwy3g6ZcTUr86g2I7tUWR4OZ7rFuBb1Tgh-J9nVQJjfGKL-pqcaoX2NLDwH2GAGqGcPgUsCJ75D4i8IHenlhuXKb2qQx_SpWnZ_s65PdTRSYhlTYzdL1TIVJkV4czoDB3GiBCYf1wb48cmzjKpiEPvQwTXUftvACGab--S8lOOf55weRKkhW0ZOADXwJ9eZS1FyNuILLHDgVqK4J6qJ-Dc87TBB7t-Po7GHJaRU8e4PBYuEstCkjbi3Wr8T_3chHW_zeuOPkWVEL4hDHgsnGfjMv61ncjam6yif54taExcFDvaRIiLvQC5wKEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQicb6ZtKhYnDcPR5pv2ibq62WzUox6fwJdsI9v0GJvCGbg0f13jJbXaodOgvDaEjTZLN2gPgdYc3pAWs0UKO5Cl5BTqiNyK2nRRqMOX7-P-nlFPi4TvS5JaPOcpvLMzLaNr5CO0VPb7IAL4yNdl4N10rYYFrTxguuqeUIktnnZYx0UFoBwxxY0yZKRzQfMer2lRhlmhFSE4Wrq0HwBw1bBKDxEPQoq-DQa9Y5IXJY65K0MYvZv-T--Qs-SDFXPgjJ81W8DD7zTWiUPPMb9yQzY4h6yJk3oOrrlwkhTFWOAptzBWSWMPQuWlcJ3NqDjD99wEmJF5En-wDJos5SekoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WunEvIBemd181lipVlNgwcJJHJzTzsnprUxgDuTfA5knC_7ghOqgqHu2Hh3NWJkAQJlvKHjFpSmLkTtWiZUCltoR3QU6FZXMX1jhD1uaUPXogQ7KpUhIij2VPCbXZZ81ErKqik481p1Y7lZ-nRX5IN5qLFfXkjuD1x2NaQ-j3mcek8ZEoPeNQlE3KaujD8GIbBI6OStpsck6A0pJwr1eVU7rsYCBg0g9qDDMqJh264SLMuuJE3Z9F6hssvbxBUJnjfBjChVGMxNehHKKvVrqIpbO1XcwPf2VpblwXdcxKZZxHkS4x_wBBdVTymoDsYIb817E3bZU9OVvhlKZIZdtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsSBZWckAQoy4bxlAjTuSkQO26U2Iypni2SwK2VaXA1KDTCc76_RBPFUz98JZjLt0LudpiM-fS43ov78Twuqnfmv22f5YKqQ-0ufhm5LpjneWymwhqGk5l8WKR6zP4S42CWrX4BTnex9D-3zWiB8XEVlRqxnHjuH1uYcJvZKtCSU_2UyoJGkO_1hYyfLon29JxtlapjZUTDHsuhQT50FVruQcUIfiGWWy9wF1qdLFwTq19vfbSnwQdBXB6iJ1ey-Htop6SlDqlHqhAmd4bQbhpUYyoRmlJni4tDiTgqer-HJcCE1fLtNMyHfwct-8GVO90WQzb9aP4qQbgzYDpDqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=Ic3JjANhBRxaZH80q_jlISG1CponJAHn7NPKDKKMjHAX0lhMLwR_m-EpiwBLnp9OIG-v-UVBh5bm4uDnRX_AYVHbYJ3p0miP4mDLzIa8t1T3swec_r9aYWCtneaA_7B8gUTD5wHAUSCFjqFPBKSsiUmlxdgztcsCz2qBQ74twC4bGzCy3C3VoGxVEPWQ09WkDKGsiWbm9pg9HfjphSrBWr1R0eV1RL7oupi3ehq1vL1MFzRMEKFAB6JBjLv0WMIC9ZfgDquCqWYIKICTimiZskYM0xq-fpTK8UNXQZNrM9jvuenDx4X3fwAk1kClmMrMt8EZ6x9yLxyJd-DSh96fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gva4kFMpr4wXMvJlgbqvv8hxo4_7Utbq7hQTwC8badnCLT9-RkC34EQClnTbz3XXVGWy-RpIgM8U10K0WqPwmlSeYFVgnW-6gjwPkUdOjYdcT7WPZ6UeKIvaqCf9XseuU87gAtiI23ccwMsr_6aDj0f4B-O-2bsstHCnviHJJmOPF_wMg11wsSnBmTMmTjtOx9AolA3ycWlxQUrvHaKFsCxkmjeTsSqW_nRjCvAC4G286CCjtkZSMHLRBFKB42rDizaGNXcbiILQVmmDqjxGhjJmVhUyRLIBqXf29WRfDUhb0qBOklOGBgV6LZi3wvz3pseoN3TwwR-JbLxkuXzSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKO1SqkRmJrwxmSRyqmjqwD9CDXgmowoB3dDrjkjJWeC0goELFsIUhA1XzRvtGjp37hXUBYNIcJpknlljs3X8WL5uBAoHpBTvvMZ6pjiiudt4LdSwP4D0Ye3lESoYiYe6xM1eV1MRhsXWZUUxp9obM2j_EWhPCnc295z1zEciLgvQmpzSYbCNQ1jBqUG1J_H8130hL96ZELhx-jUizP3rJpslbsyP8aImlIRue1V3ia-YYicImSW4b9PQSFVs-bij7gJx4qzMjd0qWWFFJgOAjbVrY5T9l-vZc07QsilLZ6YTI1Snq2CIst80KOdgxFal0mYHTpf4HbfLLKWEn95Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUz-10UgH5KO7qlmmWlslmHB6bYyClI4VWaC1Gl9hOAvfI0S67szrAHnZYHHvO4hoejE9ZnybF8H8dFD89EgclWa5yG2BWhzVZTi9IAnHWwtKT5lO9xWPzd3TO-YU7QWDbqsfVfaR0AQWaQBZ5e4V13mRaQgftv35ban404YAwCZzcU770xSzWMzTuvCErZU5WsplIfXJ8f2rySnOhZVXL60cH61EnY3lX51Cw4xXEKLEFuXeGus4BsQZ66pXHxx_XST_zV24cLIg6RBbhoIUIk0OmiF5T_viT7-bdw80IZ6q1Q3msghCOoC-__3Jd8W60kxkDbo57NUoI-vy1_tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=lXBFG6ihujt69Qwv7ZCKVShdJ2nvHbduui6gvLRrLh6xFYu0zKsiLvfktd_9H60JFyJUsLqHKuAfpMz4-D1BA7snwv_kPeHyLACxFfkqkZOPRMZ1q20EoFzVNSGkcB4VUI2QBmPEZksVLA8g6QBUHuOXzfeO-msVWzLz8nAY-tO0sa2bMY4UD6qOR6r_WM9Q8zL8vUFeRamDqpsoMMU8wBopPop__9rExSu2iz9GUCECq63ruF2H-Tl9sNaM-k_iMpBkfdTT5GRkDP_sMA6oLMVj6-jC277As0p50347YyHgsBl9kYVNQ1ZuZDbHxlbD6w7sojtbX8Mn7rOJitvn5TMjcKIcXkoFeyczaX8d4AE31JQtz2Tp9-f9wXQQIFqqFJ0FAaM0DdII2RxmYrWzyhResoYRRa4fN0rVYB6_B3GxGQy9P4C6K9osm3zpRP6LHY7enrD7cWfmg19Q2efV98EkJu68gmvx4cCn3l3X7I9aQp_tDiAgEOLQURHck4gBUto0mVvPxcMw0p7qNMtzb-SUnsDsIAzk74kA47gsoeOOxPIdvtxJDHqgFfqm86gTXmIsBG3GmqNvpkPQbj211qfPVaXK91S90Eh1yZZXckvCj0FsAgznaO6NpTZaPOBHWmxNdWKNQv7HMDki9m02fOJ1QQfn8l_7SjcWiDNDHp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH3gDiHxm8PnxNGwts_IukvJh-TC7BZ0ZNYFiGkGvzXneInKKfuh3BGpXn5-ee6yfuVlTOeBVNgcBbJuNIGry04nWN91zWHRy9dLx3fMXQmC_fFU_j1ijfr3WQXB0WV_nMZNVA6s_6NySkSTtaGQCKdlf0MCjJ1hAKaXMX8LN-AM_YA3wuubEvvLgH4-t2x20rfEAZB-9CoRob4fJwNsV8jYuFe7OiO0voF3aJkQGfbeLUmlTj12dVw4zjhHzf3KSMqJsZg2JAl_aY7ZZYwfBnAxya7_onRJONPyM3uPaOWEIoBeu2rrZM5FBdKHxWpSP2l7cqYpMkVUP1V7zxpJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKOlyOksXnznVd5XXbTVRr9v_v7JYHEYAVEU1WvUWo6rRTTwzeof2SdGVufwUs1U-JCXY_sRNVTIEsCckrZbbOHuya04_jnKOi1u1x0DruyQQnN2uk8d2-YOwZnt0c3YJJv6VCFv6Y7dn8qRJcLgFVQ-Bh5HpmMYGVRcP1hFzyc8MeKmTVV7-2-umluw9g2XBVdCHrDQPmiaoiocD4hkhMUKUxdf68RFgqoKb-i0lSmAQd_zXbAA8_U4vvVjz5FmrzfjHP4YPpJ4lPPn9Qu7X9vRjmXdSSnM8qbktVyzRBCVWIbW-fn5eU6A9Y1-HS2bZF2tOOyeYFDxzA9am3GpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_JTN9UoyXGWm7Zp_GVg-q5LKz2dv-PeusHqsZQb68ll0SxNK7XhLPqubALeZUinsDArRpwRFRdJlFyQbzk3qN8IIWWyLC7jk6Q3-QRyjzRgBJyNvA-P0VmQWU-GYPae20-ihtZgytDjNbKqB-6W5EazzR_gsz_MyC1YgS2q_IcX1aFJ9NWmCToynI_tK80QluKIeOzAZo1rKlnHSrccoiv_BRiMvSBREWuPM3r9SVVkIDmN9kAR595CILg-ZICxDDK9W7KDM45gfo9r1s6Rjtos0qgTwS_6HJjf7mDKYWXbIYyQMdTCedCssfXHBFSEJBxBRGK8dBn5Llqpuz-Gwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFCpDS2avMvcxOmKPLEm-aHEC28ztrZDKb5lhYDW6GT3CH_oNOWno3o6N65vHrOoDUU6T544_MuPr9nB1UbaembuDyGJt7K6E_eQAJiI4XAQY5mj5UgVutZz27Izag3aCFo724L694R1TOlG05Vi1onJL_nT_x-UhFYyQrDeg_9mnv3mwSlR0qoaCyXP8JmO9hrwlcKn9REiswcMR0glYO99xDZo91KYzbrkxejpgvGmI2uqrFR6U_94CU4rmC2toBJJ3QdEwGtgMgMNKWezzytrZ5MUp61Z-iBx-Dyg3FxIWi6F9gh-Kbol60sc-Tko0u5p8MOOtP81WxL0uzSt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAgNKKx7G-fAYUIINrZVJRvcZa2lzI_vcxCZ9Bf71jNuhLxxyAzb9sik2_zSmmWZB-2zrT-p3ZTOGhSwpc6FVU1EpCQavnF82MmW59ncl0Qf8PU4cRCXAcKGTZp14W8ITyLQADaR9h-Gyz9YuKYdwBmtT5_IKTjn0PRb8LOVRFReeayUcaJW6eAjqV9n2zuQbqZVbXTpNYFXecx3W6G8d8D-tRPh4MyjLZcImnBrssne9dC7d55pOSTN7beMbwaGW50dAbHRpJ-2gJW-_814xSPdLQeU7pVPD7HMoKRA5OYDo_nQP4-YKBIXC_JgdAgEcOelnVpMipnETXHjtoAkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXTXG2Tpld3lCleVKeWuzlyW28lye7D-o3QMVV2Hw5ke6YdU4YozXnyBtHqLXtord_IGE4VRTNaq16g9Wa61cqLrVs_i1Uj05d9MqEyKJyMySD8bvz4Uy012FWnKeLghQzC115Zr3SQ42xuhaPRS8CaHuo15-OHAuXWiFnUdl4ogHsvDk1iV1AlJnTSlb9ncUWscit7mEvmjJqyh5jHwSQYJ--u_xV7llIHNQw1FHn45DD9EyhYn88Zrs6MXQy367uBQfWWa5dcBZLjmwaQ09YFF3L9bBzVlqU-Rqb6On0m9_Ca9YeOLPxvxjpPRkGbkaJtOF-f4ONaEE90A1rYNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcI3lDpCgPtDe1nz8nxygtob7KHyG_4FT7iOb007541Pxucpn0Pg_2IZKw31mPddA_MEsh1wdWjTbsEvQDSSEZ7xWlLbvSqmpz14um5eU1vVrl3_AMi99Y4p78VMp20s4251NHm7DVLFXCPchtP1MQg8nO6ulEXZk3q4n7zZJCRaeRzq51OS1ksITmaZcLgxROm7n1FE1GcNNPbl36liAZMEH0oJOfo8x9sgmpG0OoljljXQDdf69A1vXBYpmtHBof2IRJhmvLGr36YkxyUMAJkWpyCTvVpUic3yP7rRLri50I7s8w6WydromyMQRcKus08RZyYkuEwJ2uuwn6USgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5VDFBB9sdOxJA1GEsRpyFe4FHnUNMVl8favZcSMfI7FZmAfQpelsl_VSPrxMuzk0yBTdxBL_ckhdSVa46QV_tFwhwV_ogpvo7SHu_wcUgOCpTk-SNVpUgb7f0K3vLAO0iRu8yK1m41G7FV7aW1kt3pVkxXLsPndZr0gUYnh5xyK7ncPbxI3mceeifbyQ__yKXxY9Z6TU9IYiV0DkIeRpbIQZByXtgwdGmtUgTm-C26KPR4MfInPETqWxMwgQHfGWJ9oWdlE_EWbMfqU2bPFna3T6mPIOFdNh9qibapLaw5KP_wz-ROhpW7MwfhiGA7ON2PWQeqe71TshJfzzde6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=hP2onnLrAdVefAJ2wTMT4vYfCcXKMSO86avZQimwz1VXr7_vMYjNBMLy3GwMORqQuom1HXd5nNbtUCaUypaScFP18qNt1uC4pbHWQ_A7rdLLy4TLCKjkl_D7zg0Kt2M5Jczjcm2ReF1BBn_c5QDN4cLzTlkTwVyTd-c_yvyMdS7hiOvfmmWDAu3pPok3iJjPogbbP2RB0EhcX76e8XIjAIuX0vBBD0tFXPUZEsr8L-l9Gfoq1AFRk_JBzBp2c_UP3ZVhS3HLse6oNJS55JfuRNwrMsU7h3mC5nBYpFmdP5EzmAF92BL7jE3Zlr-II2rkg8gZSABqHhjtmKCfgtFBNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=hP2onnLrAdVefAJ2wTMT4vYfCcXKMSO86avZQimwz1VXr7_vMYjNBMLy3GwMORqQuom1HXd5nNbtUCaUypaScFP18qNt1uC4pbHWQ_A7rdLLy4TLCKjkl_D7zg0Kt2M5Jczjcm2ReF1BBn_c5QDN4cLzTlkTwVyTd-c_yvyMdS7hiOvfmmWDAu3pPok3iJjPogbbP2RB0EhcX76e8XIjAIuX0vBBD0tFXPUZEsr8L-l9Gfoq1AFRk_JBzBp2c_UP3ZVhS3HLse6oNJS55JfuRNwrMsU7h3mC5nBYpFmdP5EzmAF92BL7jE3Zlr-II2rkg8gZSABqHhjtmKCfgtFBNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=qxs-RBhKSdCu8XbvakYugr5DMZldQAJQuFqNdsSkCMHi3PTJ4M-_T2qrlMi00rffgv-An7fqHDodl0Rk9YgDG84fsg5mHd47jnZg9MiEtg5n5GyCGO8c5bx8vk8KYXFoISqLzGVBiugXNFPRTHvhebr2yeaEHbjOdN6Z_zdo5GukAsFc6DRyL4lIfgEXJveIERI2jgfJTtisjdKJp0Y7qzifAEH29Bt8K5tR652m3chk9IU74XTv9c2ouy_UQQ-koWS_nOdxArtPQ0wqXCpnf-blPBrFcLCsZOWPTy3qDlk_1atEuoNnGaR7ZqQR5J-ZqADqXreZ52gEAyZrYspZFAOn2lLt69GwxBv-RwY5SiyrGYAq9L218sAoOmkTYCGrfuC7mkCPAXXMv0xuPdrny7tuLsKiFo3A_tsqffelXSFYGXo81aHdED0GMO_j7LyiRHG8nezTsu7qtYx7JW1YAJPv-hP5T_XwDwEz2xUZUBwG3ZByyEdUiViJ-JdHnLtDSF7H50aORMltlBjVlR7cUxo_W5RgcH4YvrsJsnlHx7W5tAMgVi0KP04jkW2r7lJ7XhO2U9VreeKFYLuzbOoAkd4gIn3RPOro57abZi67FHO8OuRdS8yRSUBJqjScX51t9jBGVCEWC-hEHkW6TBieW0_QP6xthVHK9CkSeLs1cHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=qxs-RBhKSdCu8XbvakYugr5DMZldQAJQuFqNdsSkCMHi3PTJ4M-_T2qrlMi00rffgv-An7fqHDodl0Rk9YgDG84fsg5mHd47jnZg9MiEtg5n5GyCGO8c5bx8vk8KYXFoISqLzGVBiugXNFPRTHvhebr2yeaEHbjOdN6Z_zdo5GukAsFc6DRyL4lIfgEXJveIERI2jgfJTtisjdKJp0Y7qzifAEH29Bt8K5tR652m3chk9IU74XTv9c2ouy_UQQ-koWS_nOdxArtPQ0wqXCpnf-blPBrFcLCsZOWPTy3qDlk_1atEuoNnGaR7ZqQR5J-ZqADqXreZ52gEAyZrYspZFAOn2lLt69GwxBv-RwY5SiyrGYAq9L218sAoOmkTYCGrfuC7mkCPAXXMv0xuPdrny7tuLsKiFo3A_tsqffelXSFYGXo81aHdED0GMO_j7LyiRHG8nezTsu7qtYx7JW1YAJPv-hP5T_XwDwEz2xUZUBwG3ZByyEdUiViJ-JdHnLtDSF7H50aORMltlBjVlR7cUxo_W5RgcH4YvrsJsnlHx7W5tAMgVi0KP04jkW2r7lJ7XhO2U9VreeKFYLuzbOoAkd4gIn3RPOro57abZi67FHO8OuRdS8yRSUBJqjScX51t9jBGVCEWC-hEHkW6TBieW0_QP6xthVHK9CkSeLs1cHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpvtCGyQ3FtWgZaA6bunLAexhf8iqGuqjKeTfAevpCzcwVbR-BJr7gJvqC1inupneUHbGDr7qOQ0on4hI6z7D94mQkB51dZjI5J181G08dqUCSJu1oWFD4cGrDbLk1DXEPZSjUrIJMv8DXCazZr72p6Bw6oEWtpYB5VHcMKC2rnWaZBQbZ-NaPEBAL9zRvSLQ75BU8T8jpQY8E7kZsIM9QF6P_JERR1phWsxT5D4i5sPJp6NsOPgpNaluHZHuqciCM2Hvrs0n1pxCqS0V12z-sCqyPH3sRIDOQlkyTpTfK9MdBHfjw0yrFfpCz0USDhFd3ASXlpFLfNzZVtq-9ghNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQxiPorS4Szaia5hbKRDly_9YXVyiDNzy2rYQJV53VLNOfpakBdMndypn7lamrjKwAVJBde-ilp5lCP5_qIeTo8Zt-xe8iH3eHUoiYo0Wn9sTYyvViIY7LcfBOgMXGMpW5xJwOuP6Mpcffhexu6Y99gZ32MdJbMM11_iIxJuXrIyrnm2tnTxIhQlQH5ewpQReeJR3FTOm6TWdnW9_AP-QLF0EvztvYFXVBJTgcQeLBq2hNngEO91AeeV7fhDztUrd9GcHIOud3M1V7cnVJZ6Zokq6DWeSnulYm2SWwnDd4EqQXQoT7PoaPfsgLnotvZGZV50Wre5JCD9WxYo8Qc8v_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQxiPorS4Szaia5hbKRDly_9YXVyiDNzy2rYQJV53VLNOfpakBdMndypn7lamrjKwAVJBde-ilp5lCP5_qIeTo8Zt-xe8iH3eHUoiYo0Wn9sTYyvViIY7LcfBOgMXGMpW5xJwOuP6Mpcffhexu6Y99gZ32MdJbMM11_iIxJuXrIyrnm2tnTxIhQlQH5ewpQReeJR3FTOm6TWdnW9_AP-QLF0EvztvYFXVBJTgcQeLBq2hNngEO91AeeV7fhDztUrd9GcHIOud3M1V7cnVJZ6Zokq6DWeSnulYm2SWwnDd4EqQXQoT7PoaPfsgLnotvZGZV50Wre5JCD9WxYo8Qc8v_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiT5-8KTZ6Uh2CF2wwG-NyOP0rO-R2PGx9v-qbjEJa8ZnJ0m4dLDfElT2IfOb9REb1z_Tt3GTsxfNuWA0puOdNWZ6MdWbvESuw3huvGp9plyEWqTJ4hxrRRL4CWlFavqU7m1koP27Lpc7sZhJDC56N5Wwz-5hf31pR2vR_NRn2X5hNRhLmtofOoUEs8ITleLYPx4eJbRJ60Td7ObbYNy_0UfcL6uWlkKoy-YmAxHzzj1phaCYs9KgfJylAWujvd-9U-VHLsZ8X32qclQhenuhAs9UIdqi0ovNB7igMpByaIT_otSiwMJ92vHiDinjAfUYJwImyotBsN37fyQ_um2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ06G94ZQ_KioIDm_SkKQlQMnUQh7Wtz8LVoMuynlJJO7U3q6KemulMxh9VnZ_we5ZLHs2OSQFAniNS9EGwad3gxxlsy-ZtNJ8j-c63CPscVkae7ys2v21J-ykWypHvbs6Jwoy7s8KXlVjE09PhNUN1ZbooCZTYrIwgxcY8UQoxfPyJwLEmqH3spJIKB4ptvsalSXPeBxnQ1qS3n2UZ6C6q2IXla9sfxjUEN1x3tTIsDTKNTQwREQTIevIUmRVCUAlssoNZLsOHIKTr5O2Yp7Wa6Oqru8eMBlD1hOiz8JaAefUCx86d5rQZUZT7e-22Iu1dveH2TAKEUl19BEhliLbMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=Tv2RGnzPCvOSMXdTX4Z23BR8r6MbeuK3YgOJZ02qN58ZIpHJFpFhonCWh-4qWQ--LmKjDKo0_6kXwJ0niDuYWeCIp2Hy68qd2FncbARV6Zn_4LeEvnUtyNCi4JN3EzDFrgen8irfdT6RJjPfvars4R0C9VjUt3PwgudqOcgEoj0zlYrmZ8tX9RNboMk-cgLN77dzDVktP5TTxRpKqaFrFxj8b5axfGPXNVmCJPj5WGq6Nvr7q-HdM98iBlE1RdST9PO0Ed97_doGwNEdlzCYmEbBDy_YqjHaUNasuKb807c2e7xxfkeAumN3uoyuhK6om1dadlm1UGjVeT3HH-0VQ06G94ZQ_KioIDm_SkKQlQMnUQh7Wtz8LVoMuynlJJO7U3q6KemulMxh9VnZ_we5ZLHs2OSQFAniNS9EGwad3gxxlsy-ZtNJ8j-c63CPscVkae7ys2v21J-ykWypHvbs6Jwoy7s8KXlVjE09PhNUN1ZbooCZTYrIwgxcY8UQoxfPyJwLEmqH3spJIKB4ptvsalSXPeBxnQ1qS3n2UZ6C6q2IXla9sfxjUEN1x3tTIsDTKNTQwREQTIevIUmRVCUAlssoNZLsOHIKTr5O2Yp7Wa6Oqru8eMBlD1hOiz8JaAefUCx86d5rQZUZT7e-22Iu1dveH2TAKEUl19BEhliLbMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTmn6q_TcaHkxvdlUOmYODBZ0Viq-DhIczP_oMxdQB998g1iwANOQvRwC7iFJC3Q_YxKFz-pXktSTFIzx9bOmfK2hqBOYZsCJxW3N5rfQBns_8R5LELj6phBIwQLGcoijoVrZJCPWRdUQoF5Fq8zs5IglDBe1PTj9FC5TWe7mtYntR3Y8PgqFzCh8sNqteHD50OtAhXYkM2Ik15JEwBafK-GQCuFRDpACF-lswm7pQls2pseGYx9R5eldim8Ki-8OGa-RHHRYUQZwgD_6-UTrVRKTcmWo7bzmyTWM7ECMZwt8f_J6QdMOlHYqEQ8GI2cWse4nCptGEpfjmr8DT9uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP9bfR1zGaw2qJC5yHSXAR2kSHE18WawldSKvzofk2WaLyJLsMm9rUv1RQSKIriVgjTO9GOKhkMh3dJqtQRFFeaq9Z7RfrVmb-Y_QvyS3wZFKA-2wBTADEhjczVeyv7XfSOpI8sXAcbtEq6EGo572Pv4tt-vX-O1STBuRkagEEQC4vTUcWJxN8PD5m5dmaWFLlVFoMf6ozI6aRAfShUwG_-K6Evwvm77A6yCT1d46qITAhiGtYV9m_w2F6HQTNa_8tXlXO-CyhJ6KgY79z_jG4qS-jQaHQ5XF95fuQ0-kuMYdpJCYbGo8mf3pTbOkTZnMWF5-P7JsZbom1gHX53Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_8Bpqb0MRaS3qW4hAtVaNdlQOHriTT9M9DyYW67N7ekGThlQbokYFyW8PIba2zi5Rqz8kMKS3WhustSprcFmwEuKxJPdRlcNGrRjlZYTxyLTtXsY6ALuhrXW3Qbn-xZuYvoMD3phCWIcB1IZtLYVM_Hv3bCDA-pZItNQM6lGm-0XkrmmyqH3kJPLqUMmZFEEKo0Ynk8d9YCENvAI0MZpWAWAcZdavw4Qoo2aoVKH9YQUB6baFkfIaex274O40ONwWCK-hnM7ND9QmXRGFty3z4KL_XazPCOhv-88uBp-yWzfxxDIgJVf2u35MPHd6u0EVv5QGo0WMbZCNRQMSf7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-YRzrBLxCSaUslP9XxC5Qs6YQoxyBhejukbxqY-uLJym-EWPrvogIuE4ypqadQ7A0dvkD3pQph1NHmyoUtP7h4yIQyI-cux44ezUHLZv4mA_iNC0wCcBj5ivRSY3klBx-GEIj4-Kb90SVsIi4C6fkuDW5rdxPE4enn5f70-tCND9TKDZwZe7HZKD_RjFz8L2WMqf2vIHsPuZ1AlwyB3EoXPpq_dh9hm0M2BY7NmzFylSbHDz5fjlfgQRfDSWYdKrgLBMqV78h8ImB-odDsyE1Lvt8w9fKajNe8QVFqMvpNjZtLI1qsRBTMR077YXDjbZUbI7CNK2NwdqCTbnlWqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsPft_VjlnzxSB-USi1hwNPp7bC50KTirOYbKcPIlygZzyapi_q9EO4XuzfwyPHPzIhNKrWBi8R0t3vGnEw6oavkz2u7pxkVYqMU6ohvFM7QWpJ1b63MvkrfSBkKn91DvpDaAuvNwB6ov84n6sLZtJEh-cbtvwg5ZhMwOhCNLudjjr6bh8gCC_dNJae6T4e_wtSeaTKof-GkDmDVBrjDOOMP-3M97pH2Cf1j0mJYO2qcYW6r_tVp0BYWLhvlefs9grMwq9V74yHxh_rSqP6s0yYfQyZfeiP1BUSuinwZefJE7ySNeEgWXa3S2-fXQBxqX39KXd6jR7nO8hGRcHiiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhtCogE2U9QEtculRTko74NYaMUqsSLlJ9c_kpp5jaS9SYENHfnPA3Y9JgIBEwakgjplZMOL_HCqVqmanCPR_H8XSTv0p--9MuwDU3m4uJSLqNhP3Ni2XnTFwe_mP_KpFQS9AtQQzvn50nTW9X1CWrmST5K2_KJxV33MFhSs3RiXMEwOTwpYuEiV8l1XaveCXJ-_CJnmVRpemDMsYsDZsiJ9mXohtBARuytxwrPhVaFvMvLNTaCypPs2b_wgT2EOed8bGLTvMsBoTEqVXjVKxTNNiB21AHELownCKtRIiFCvNZBGpHZwNxZrks7wT3ph5JYvv-C7TXkxX--ruQrHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSiDPgAGXmjs2dyoV7hkc1Bg_ag5AindNA7VaGl1jFouXZfIuD18oAlOLRRA8tae2xqEp7OjBp37CXyJYkSD2XpdiEaVQy2INc69fBX3WUTnJFu2cUgqjFIC0-2OstkozyhZH1X6F5ZV00-us6Dl5jUzfOMHqRn-iIAZA3h4SP6BxgycuQPi_2Lx7RMoeY7grWFnwJkFNcHUVNWOWDWXkx9wSjYWn8Hg_tc9A3HDTIEHq74BBIUIiDFOlXGLKKkcivG3a1-iQYu1Et0I09DhOsjt5tog0SQdl8thD7enpJJdaxrGF80eg4o2V817anD1xdKUBk0hK4krbqjH-HLGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG6Y4Idh_7Wk0GJJtc2HTBBJ0YsqwTTguaqYb6Im8HPQ-UvHLjJFGX35N1GlgBDzEfAqfa75pY5kLMXY3ctpVup8ae4Hqs4SB7QSlbY2w3jfQ00KLtxCLvQUqXmgN9_RB7y_6FIcFBsoCZihMkS-BkIYXsYZa0ucILULFgBDzukURMBgFnLNCJ6iUwTFrEKpxQsnKD-WMx2bLsF08TZAcp2y-_mh8ZYm51Ve-xV2ySpMo8mnLZaIHeGx1Gttd-EbaifMz1YdKdZQY2H7PiiZ7eAJ-RCNtZDtA9tA_db2oYOVm20hw3vjd-P8Ae3yhjTC9fsmMNDOIMr211U1B4BdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VafQ8yg0a4efWL_cavXNDjJ1xhAkigOS7ap7pyeMVU-U6gduyPkJaTPgq6wHVEJr5bXc8KsPJ1vBVZnr4jZ1A7Ik5jHwrJzU-TTprpNUHMac30SF-rehgrteFavuTN53_SsMpJAFYAy80DjMvr1LGdwlMB2RbmHARppr8xleqiu73AqBxu_knK4ovogNu1j6WH3PboSc2TKFL3axxeb4V-zTAlXbcA19RFTxS3GjrcmXcpRWgdZG55ICR0RH7kMZFYsmlLKgPfIytC1ppseSO4zNKYhtKgIO6tD6tINtk2TjXVQ89xYs3KG47iqvojwaooLmx54dpn7diBTywLJqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=hevbtgTHd8DXjpcFbqXDOIi42r-7XFGTzIHHDv03DD6zb3OIfXqrogeP2zC_hEkiQvHe3w9XO6yE4FNBbtl9-M3wEux_7Ey5H5SckMpqVvF987SRyA7C6UBORh8x5r-_X-KBOPcWlNEg63wXdmlqwoJixsu_66AIPLgvu_nXyLFbdNoAkrjBGOif6gnvCR_tQhg_mx-H-61OKAPK4g-9xWUELvaPU-cduIgbtMIYH34qAcARcHzUtx7cAAxmnIsHg4aO_s_COCsUd_rY2RIWT-3XWgqcVQUxMxsB7xlCQrxiI1Lh4Hll29qpxpAf6jjanDpbFt6YV4s9R9aoNnzEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=hevbtgTHd8DXjpcFbqXDOIi42r-7XFGTzIHHDv03DD6zb3OIfXqrogeP2zC_hEkiQvHe3w9XO6yE4FNBbtl9-M3wEux_7Ey5H5SckMpqVvF987SRyA7C6UBORh8x5r-_X-KBOPcWlNEg63wXdmlqwoJixsu_66AIPLgvu_nXyLFbdNoAkrjBGOif6gnvCR_tQhg_mx-H-61OKAPK4g-9xWUELvaPU-cduIgbtMIYH34qAcARcHzUtx7cAAxmnIsHg4aO_s_COCsUd_rY2RIWT-3XWgqcVQUxMxsB7xlCQrxiI1Lh4Hll29qpxpAf6jjanDpbFt6YV4s9R9aoNnzEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYGKzV3FrzoqmzaBAm3d_GvGKvNCYsrr1-zAOaJyHG-mLlnsIuoUeMITyK5WQMeJuchOZd0qjweMVFqB2nG-4CdUzZv8gWEXI7oJiq6dnnDUGX-GDo9_u1vOv_wnlHXE_oEU4G_IHgF5TvAC8R92ZCNnjD0H8n_4iwqbgW0ROLo4YwN-XxvT_tJeYB_M7Cr_7zmDylh-Qa4SUDeq87S6-mEsWgezM1pt8kNIYlsgIUsC2V1pPQSy0YRiepLRMsjRTkae14l_0vLOjJ6SvjA6ojrxFzIC0ksouPNh_cthRAB8HZ3vW9swLOlunJZDiaZzv3iWNn6wGJYfkYziGl3tDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=b_Tm9ve0nMwMk4UO0tQBBPgq02kcG8TDPKkIcgeeu0HfmGhariuubBcNNIC4NiARhNy4Qa2_54ll3CxD8xYdGiX1_IQ5XE0EwDdVg-N3J8J3uCpnspQzMWI9BYvjDit0lnlJDYZA4IcLlIFMZF7h4yZLXMmHENYI5Oz_WjHO0cWOoB-WjpuRps9RYYb8DwbQemHM7OS0n6FbQpi99yyDG0Uh5bRVnm-DuBAl-d7VehlKzrlA3qexQ17pFpKxTLoQ6pyITz_ZRfJlmlwaMWVTvtccozjtmWxXPRWZJdZwnxJffY3jShCyj6TiZd1P50uOjGaeElQ8mtYsi3zsgcIGRVXt-EnSLJtLyU9Pp0C1ZDjijqMtEKiqAWP9ZRA7nGarbYe7r5KmlxeOU0UfKTzTzQbyabPUC4s0feb5RbOjhHc50UD65rorVs_mtQT1eVXu0y3BKYdp0WPpODPMIMX30vQ7-GUhTsMtzs8Sedg27V2XWnXnl-zVxfOqFhKgKVNrMzZvTTP-RaQEanfjF5RPJxQgekCvuFjKgrRcCkuMFbGNOHcjN2KozZHq0h-UQAUycTTXoI7Qz5-WC7lE6FrvnGHAdrf64kJvHQzGyMzvHw0E6xiIqfJMcfINpU04p_jBUy6eB1FXlBBWyGCA4WEphpUmrQpXhebbYlOCuQvkZpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=b_Tm9ve0nMwMk4UO0tQBBPgq02kcG8TDPKkIcgeeu0HfmGhariuubBcNNIC4NiARhNy4Qa2_54ll3CxD8xYdGiX1_IQ5XE0EwDdVg-N3J8J3uCpnspQzMWI9BYvjDit0lnlJDYZA4IcLlIFMZF7h4yZLXMmHENYI5Oz_WjHO0cWOoB-WjpuRps9RYYb8DwbQemHM7OS0n6FbQpi99yyDG0Uh5bRVnm-DuBAl-d7VehlKzrlA3qexQ17pFpKxTLoQ6pyITz_ZRfJlmlwaMWVTvtccozjtmWxXPRWZJdZwnxJffY3jShCyj6TiZd1P50uOjGaeElQ8mtYsi3zsgcIGRVXt-EnSLJtLyU9Pp0C1ZDjijqMtEKiqAWP9ZRA7nGarbYe7r5KmlxeOU0UfKTzTzQbyabPUC4s0feb5RbOjhHc50UD65rorVs_mtQT1eVXu0y3BKYdp0WPpODPMIMX30vQ7-GUhTsMtzs8Sedg27V2XWnXnl-zVxfOqFhKgKVNrMzZvTTP-RaQEanfjF5RPJxQgekCvuFjKgrRcCkuMFbGNOHcjN2KozZHq0h-UQAUycTTXoI7Qz5-WC7lE6FrvnGHAdrf64kJvHQzGyMzvHw0E6xiIqfJMcfINpU04p_jBUy6eB1FXlBBWyGCA4WEphpUmrQpXhebbYlOCuQvkZpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuJ7coRxcEFIdt0f0MNYAgimMTpQMwbmrTM_SxCgsKN6uJDNebL0osc5xcoB8QcLDRJ0Jx12nB7CAvenhgRlzEFeG5XGvkFwGnt3_v1Lwr8ca_24f1HQ_9ZEZrpOgmF-DefweHoGr6whTOixmDxQXSK65dos3IEoESWtlBdzXL1K-EwQVv9C8yzTNL_NeRAxb5fntBrwiMS7h5IXqqTAwlyX2Rc8v5RgibkDLGNgQSo9ku84nG5NPjEe77Y6C4qtAO1r1iGp5ySE_aMSG7u4H_rnDpC7a45QBpGgW2OqbjoHU-xdUbMu_SWjcc_MsXCOCA4msu8ZZ7GiwACt8XhgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLfWPMIe0Lh1pZPANvn4Twvb7RD9Ej2-aVPLrIEu5W7WlO9pqdYBJL-VW9uMvrCXB3RIp4Y9hx6YOs34XOIDToTG0ZO7bSJXYIzFA2Yk7FyyhomR9IlZKDLTgBR6dLQ6d6l7wrxNWm2FWVdOfJ7NqS5IE5npotgzmD69eZUSFS6mNykKWFIO3pUuHJQtys_si5908XWGGWvdMGT3rVAGjd-DdM_lvAqsrbFwiMp3KeRPT3zKJIa1F57Y0Yeev2vpiD24lUc0zlt-nrjPWZdhH_lum080XL2EwtZT8m8nHeHROlTVh9GWudMkr5Q-I9tvuMPjZ3_116rb_TL5JRBcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxchPt-I2IwCWJWLV_kQOoLQFVdZFmNmKcsYJXw1EVeRk7fYse9VZ0AnSycp8j-lpjyabRYjtlQlaUeQ_Yn5JJtq5Vkt-BdPgp2rYUv1nmeyL-6qowMoq4PTz2jXky6vsIJ7fRIbW5aNND_uIiuo9UibzqD8uEIboVVWt9MrhJtah24AdtnAYuT4WvQZZHJzpjx5HppIYzqpUNz1VbuELt3pfTVgCgAV_4E44txUd8TXQGRpGwOUZ0HziZ8p26UeatO-O4aO1RhqC57kbOaJzGtXv7USe4pgnwPG5cW9E1F_wATRbvRS-ck85L99l2mFTnQw8oJPMjrPGBcydNRyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dziwlbeJ2sMY-2TluZTPKQMiR6Z_-dsqabyS3yfnhrEVwlhdHxU7ho3TS79CxeiZsp5GUu-ydSiWDJj0gvlFE4oGaKGL8GhdiZs5R2M5QlbRJhEA0rSVCx-1otvYmIkxlzzSgAkoVClKdyp4n81WLecx3c7rqLK5Ks-8W3k6SU-JtUPb34Ao0nPOCNkoJRhmuxVoRx7OJMmE8hDkS78xx8_-vUe6dVGe14rKButQ9-C5l0h7JHrKwHJDnsyQj5fG_aIPe_P-G318j9JVk-u1QcNubNqoTsWEScJPVXH8gHVYpr3FmmDPC2WBGYbMokMsoEtebbvEhHGuY1dNJWiW2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH3VP73XKqx_DZpz_h7z_nOUaaVJFjVMhrrxhppVA94RxaEP-FqzeBkXbXeE0eFuzxCXk9C4UI55x465R8rbShhrZqhawll5D2p1BVD8qY13s6yy8ZTTPO0nBnWtGJr6kCcN32k6T7D6YnTgop8-8_ftG27irajt2WF97OUT9RqFswlUMjk50E8SmwBj-6apucact9YdgTfB8BT0Z_g46NIhWasinWwXbhBAuSYfk2FnpuUVOTD1gBQfeCHmtXBA3iMnPpqTQeQOvWilmjB-30wIoAwqYm1hEN8F_T6QHBtX1El1CD410_aDUopUePv1aMnWzrwBybfwUz7C_9qwZu2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH3VP73XKqx_DZpz_h7z_nOUaaVJFjVMhrrxhppVA94RxaEP-FqzeBkXbXeE0eFuzxCXk9C4UI55x465R8rbShhrZqhawll5D2p1BVD8qY13s6yy8ZTTPO0nBnWtGJr6kCcN32k6T7D6YnTgop8-8_ftG27irajt2WF97OUT9RqFswlUMjk50E8SmwBj-6apucact9YdgTfB8BT0Z_g46NIhWasinWwXbhBAuSYfk2FnpuUVOTD1gBQfeCHmtXBA3iMnPpqTQeQOvWilmjB-30wIoAwqYm1hEN8F_T6QHBtX1El1CD410_aDUopUePv1aMnWzrwBybfwUz7C_9qwZu2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcOORUdh9nw_hG4dHBZ7S7NZmxEGcm0jEZ2EiOv_VN4oaEIyUCmgR6wUf3yz5kPWxsFc87Bo4EAmqc84YFchAVUIhTivb0sixfiYw4MzPDWr2pEJeiwXb3-4lFjQyvSoBdD9sq32FXW3T7oNK2kvX5jiakvoD-kiU3C9py_8n7qY_biiNVJNwBXA7Y9MTPsAQ-VUh58yv0386EXkgNRuzSmbTbataj59W3dEDjDwncJKF4pCznZKN2-J0895LRcZJWT2xkwE2LBhqzOPxcXgDy5UKDKsbHDyhuulQ2XYrSRoqRy-9VYQElaBNFlL-Jcve_oCy5-ODTLrBkkoKwAD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5NuRZZjuJGBxqaKKwBXG3hGsCvrxLz9WOg7HGr8u4W_vDLfGiZycLpcNlFlCDnd5Gj15c54KqwA5Zrk8zWS0dThVaPxWSe6tsqESfB7JhECJtG8TTjxlhh9mYprBWKKWZ_ws8U4VXGPlAyXAAOHAILpmoKCAueJ7aaEqNuy8kUg8vvlSK_-ZStV_f_iGPrOIIxek6iBVqir4YDHAqWctu85b9kmh72-23JgFs_cM89hd0ScYI5OiyEpynVYEiQCobRvJIuZnsnTMSwY_vTbi7v-x4oALn4a4UYfvSfSUxV0yc6MO1qU32_O9XuWwLGDPuQ-KAyvPVGtUmebhn9VgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwY3fxVgjsSvvWhPTPdg6eXa4dHBZ5qem7-b770tFgFsNQIA5Yt26gq1aqISE8cVVlZtmheRvtDDnYYvLFMepZU9KxHzCAZ6sxmfGUb1pbKSqYwOwb1wS0Wf3j6tMCXwcM9F4hnV8vZ-xPuBu7cChlhyB6d2Eoe_Pi9nPy0EAqUtqZ0NB33fO-A16UNm-XSx_Q7mpJ3DydNKL2bW_-18xbCtPVubEkedr46OJ09YhqPcBei4qQL-5Nf2EA-klPuvpMSF-4liOevnJN1p7Xu6ykz5MwKHrNkVwwyBQBxzMzwC-gCqMOVZNJ21jMhl-I96q1AHapE9vD2Q0TmbpDwaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=tM5fqZ6Vhy-FAJDyV-I_fuDtDD-jYEv_wTPHl3brfGuKn1SbIo-8w5E9LtdgtpXZ4xgDxQi6O0v4aI_kdct2q1JDRX7FQhBQ7JDi0_yz8WgVonLulTcmETP0c6ggRYsdR4L64wooDqFm4FWPV5iNVgTQ8EiGQ9J2FJLeVf4RA_sgRKGenMb7R_s9zTi-PGv349t8WH2m5KO6L9CXffT30uZtPoHiCceXIfPImqlD1NuKLhYHv0BvoQl-BAXoO0XZ6kRmmxRRmpQ0vEY_2yhXozZSIVi6DL7cC7cvrTy_L4oEUwrRS0ceAMvgS9uU0h_YHGEHeHU7eakofrF5HHwvUqnOnSmBT-Hvyr9Su0iMRz8ClQwGWOR7bAiGBVRGlc3yAaP91okOtWas5Ku_mq7L8VR0oP1rPiqt30vZCLT9qK-5UndII72ott7aYoiDe1c2TYU6jPi9ddREubXZCj0JKwvH1ahMZwIE-izT-wVSDJ9ONvD_OgNRkNSP2HbpK9P_nPOesP5GaKqndM8kJqAzQrM3Ye1AvYk5_YZrMuPGdYyKWlozMDXUpxSjyxBZyfgvjiHfe07S6J2xSEVVIWSdrqMasqNEbqbYrnQT78Cs2H5YLwY6ZM6opWEvlLt6RLZ61z6Q-neuAqv9BiR_aB-EJlWUkyVF9oNPK_jzKD2_qNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=tM5fqZ6Vhy-FAJDyV-I_fuDtDD-jYEv_wTPHl3brfGuKn1SbIo-8w5E9LtdgtpXZ4xgDxQi6O0v4aI_kdct2q1JDRX7FQhBQ7JDi0_yz8WgVonLulTcmETP0c6ggRYsdR4L64wooDqFm4FWPV5iNVgTQ8EiGQ9J2FJLeVf4RA_sgRKGenMb7R_s9zTi-PGv349t8WH2m5KO6L9CXffT30uZtPoHiCceXIfPImqlD1NuKLhYHv0BvoQl-BAXoO0XZ6kRmmxRRmpQ0vEY_2yhXozZSIVi6DL7cC7cvrTy_L4oEUwrRS0ceAMvgS9uU0h_YHGEHeHU7eakofrF5HHwvUqnOnSmBT-Hvyr9Su0iMRz8ClQwGWOR7bAiGBVRGlc3yAaP91okOtWas5Ku_mq7L8VR0oP1rPiqt30vZCLT9qK-5UndII72ott7aYoiDe1c2TYU6jPi9ddREubXZCj0JKwvH1ahMZwIE-izT-wVSDJ9ONvD_OgNRkNSP2HbpK9P_nPOesP5GaKqndM8kJqAzQrM3Ye1AvYk5_YZrMuPGdYyKWlozMDXUpxSjyxBZyfgvjiHfe07S6J2xSEVVIWSdrqMasqNEbqbYrnQT78Cs2H5YLwY6ZM6opWEvlLt6RLZ61z6Q-neuAqv9BiR_aB-EJlWUkyVF9oNPK_jzKD2_qNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKSTbvHBpCqsRWxA7r8Mvz0b1i2tPJ6em5Wc81IgndU-2sMaOOSRViNaKXka_53CGK1VLRuOxZgnjPCdyguPlWmDuEjKKrlkZe276hiLFuFWFRuNI859ComUa3JdZoc7EmEbp-oS5Tb1EflhuAzNLU3vcmIZO6WyIRseJnFiHeXLmzgPtr6UAdLcP3X6rRiKXND9CZ7vBoFgrAHPun1-UyeK03szW5tfyV0K2Bvr_Z08Y2YTB-zrGFR95ZpYekQgMq5Xz1mB4Ca6AfWojTsvl-bHePSybWVZc8i6Mw0Dt1y840eliUvp1IwAf4Ut3oBZu-wflvCyzewIAfr-AcFTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=qEBZTh14ZqYCJxAFTBXBH0LLipRfymWpULoDFB7qLgvI_mw9PpxnjQPJ6W0Sss-uXO3SQtySom9YAvzr5jsRkAb-BBsY0SutgWgLSqzZw26uXl4sKmLKQe1RH8Vb053N8hblUk8YrRSBMA22IeEe0xmiv4v2uxzY_E2gyWPoT-5UaBA5cPSPcZ31KFxdpQc1BfLoB-xzRs-iPwoS860RPtrBCeqSbRFuuCzdz8bRgDf6nucAbXyUKNKp60xLCjXuGxrVLPW_-tdO5dPlCZW26AHB-yEvFfADdtxxo4K3D7EWsmr49vKvqPYyZZf1MO07Xy3iF9phUa4O0rOlXADQwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=qEBZTh14ZqYCJxAFTBXBH0LLipRfymWpULoDFB7qLgvI_mw9PpxnjQPJ6W0Sss-uXO3SQtySom9YAvzr5jsRkAb-BBsY0SutgWgLSqzZw26uXl4sKmLKQe1RH8Vb053N8hblUk8YrRSBMA22IeEe0xmiv4v2uxzY_E2gyWPoT-5UaBA5cPSPcZ31KFxdpQc1BfLoB-xzRs-iPwoS860RPtrBCeqSbRFuuCzdz8bRgDf6nucAbXyUKNKp60xLCjXuGxrVLPW_-tdO5dPlCZW26AHB-yEvFfADdtxxo4K3D7EWsmr49vKvqPYyZZf1MO07Xy3iF9phUa4O0rOlXADQwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmgTS1hYZBc2GAXCCqtCOkS3C8zRD7GPg9fRtTZvIdpWjizfU4Ocf-v0m2mxnw_aCAgKZsqdBSTiDupdqiosEg7YhdQWfG68FUlcE0QCFQiO-6GwG3H5KkNVgphRQHAGqBWg3WQkQJheG_ITVSyUnXXB-hdk894z_z7b_brfkWDl40Mb5GKYHNpYW99d7g1rwPf22PSsXj_HZ_FPNT_d2iK4DCb0-umRklNYYylXv4mR0IMFVLdyYuQY76zGiZ9uMR6VzEuJv1dqzsTMtLqf3G-NKlkH0XraImPCduTWc054XVz3xijb_KWoM9MLQWblMLQChYdgmK67yGJrs3H4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=qTR6goOOktvuB-7TTKFzO587eS1iq3G-qwlPbVEmILWKndyBxNFKwN_4u5ylNhejPLhHUNLIRl83LB0fDcC_XDSq08ZH-DH9RpYq4wGIrLjJAIcxkN7GdjTMKvOgaMdR6JwGdKEYx7KZsygiwXgejcYaSD30AwhBdtHhyvIfeNp3OAu-z88rbfDUbn0FEjuMhvVm428lQJwVWrVnfEpU7Do8caqglP63-rv1xFJsY8d8KUSU7kX1XtiaoDrcXL8vLWb8jZZnF__SCE-cpwtO5tC4fuw9KdT0_HQl7UQd_GE486KuPUUPUuUEV2Jyod2qvJ9HuN4spzYvfTBGs_OoUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=qTR6goOOktvuB-7TTKFzO587eS1iq3G-qwlPbVEmILWKndyBxNFKwN_4u5ylNhejPLhHUNLIRl83LB0fDcC_XDSq08ZH-DH9RpYq4wGIrLjJAIcxkN7GdjTMKvOgaMdR6JwGdKEYx7KZsygiwXgejcYaSD30AwhBdtHhyvIfeNp3OAu-z88rbfDUbn0FEjuMhvVm428lQJwVWrVnfEpU7Do8caqglP63-rv1xFJsY8d8KUSU7kX1XtiaoDrcXL8vLWb8jZZnF__SCE-cpwtO5tC4fuw9KdT0_HQl7UQd_GE486KuPUUPUuUEV2Jyod2qvJ9HuN4spzYvfTBGs_OoUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3xYxt2J-ObGKBzurulL5trhjNfK7XF1UB8KANeoHIuRk76dm-PMhaj4Y3BFGRKs5t6dkyzY_Ud_Y74reM-ubAmm1syLUtmm0kjDyVQcFAVNXqPRoaUtrY2-tiKR7o_pUBzOtncS6kyfVYvlagHjTRUTiMF0_L27FFRPCXTWVxETuW0rUeyuXuCKgixaFRsPxOe3ZXAvRA-gfwTLIekUXSf6UJEK04OZV-PM1sSm6FE5cGYZRxJTdpXW-n_StKKpe2tNMj42t3kyvFQCdRTogOC8uUXQ7W_cAz4TLkWnzUMoZQtfrdcLRg6kCTZ976xy1foujOlKgLTeFKgtF-efrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30746">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZYt_02yQxFX2dhLSjYLKaAmbyRDsn8FoODROJndPnp9duuCiyKduZn1EYNog9YFDMuPgl-KRFrEk401n43Y9MuUaRRJ2vfkJ8nJEz6Y48Pnqh6a65twuOGZ8syV_8v7XOi0y-nQT8eXOPEKiAwbZCIVRpH1UTZjWP5Pmc8-kBzTav4UQmQnmfnf1zUv1txEVgs1r8y2iAvCx_bsvKnFJ0ql9lFwuHk00hjEnecG0-NVUwgnS6IWmF_7l7KSSb8Ij7vQzlOZXwLuDTVE18IzDku6DoPcGHwnLHDXsZF-AxBsUnA25FVXrYoh34hvo_GUne0oKAobk6bvi7gHsr7l7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛ ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30746" target="_blank">📅 18:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILW_m4buz7Fp7AdkuGz5E45d3_r4zAEWYCLpF0cp205pS67Z9pSWWi0LQQ2FR5YBYZJFa6B98PUv7-Dgj52tpBjAHK4Qld9SyAhqzFvJCY1ESTO_3IWAv1H423oZvhZ7RjXd9rOlk1WLswFQ2GlfLjb_ueFncZA9gF13puYcQJytR9bfWqJMm9yourLZroizt7v-g2lw84sAyHTk9Tacs1Hwagh6p-TKMmM6v8guUMHsDFUUHLn48gyUMix4X3c7E_lYyX-MYLGb6pMxa1quha3yICNM0A6rKcRwMrE_PZRbZ_zoIExumIyZxsI0B4NQYM943S6EKbpI3fI4QXQD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیلی‌قلی‌زاده‌جدیدآبی‌ها؛
ابوالفضل نوروزی وینگر 19 ساله سابق تراکتور که در لیگ جوانان آقای گل شده بود با عقد قراردادی سه ساله به استقلال پیوست و امروز در تمرین آبی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30745" target="_blank">📅 18:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAvQMjUJY9kqDQLtUkjdHe71yy_eJ-QIGsGVM07gTTTOhYU0d7jjzJIzUoteeRzSB_d24DZBOXSHLr01hPlZD0wOThBy2dpJynNDglZsciXGRaTkGHRAu2W2wIBncmDuGmtniHk9obgroJc2rsRJrWy6OoDLIGTeQ-YZdcMi9nk0VMhx4xDLLyWiXIlXocRFZYKtPv0iNjpR935EQ_I1gNCfJ-PnXg0Qqyy2cvv7kHdcF9hAw1yb4UoAnX99oPLS4QA0yeuXJ-1Nuzlcge2DqOuxn8lBelKunQJ7yxVTBbnHz_US3gea0veIfmtvq8icjauJd4wOPDBsIVwg9px0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انتقاد دوباره پیروزقربانی از کادرفنی تیم ملی: من با تیم آلومینیوم تیم ملی ازبکستان رو میبردم. با احترام به کادر فنی اگه سرمربی تیم عوض نشود در جام‌ملت‌هانهایتا ازمرحله گروهی صعود خواهند کرد و دراولین‌مسابقه مرحله‌حذفی حذف خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30744" target="_blank">📅 17:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2vjAUpf47-WceJLIeknKRkU1nvNSU0Y3JwWJJsxHiFTJFY07hNC-R1flSoCDIElqlykQ_Dtqmiyvw97qSTEJITb-cIMRZ3_xJ41Oo2iDZTjIhXcRnv87QkLmbJ8x4rc4djSrVhxBzEMc6oCBZ0-5JhyR5yTQ0yzUu0SM_eH6jf7t_fm6BaFglRsg0fYeaiOM32Ys21aLgxHJ1dZlkI0JR5owitvx2GIU_U5Kdzh8g7AjzrkCQY0hs64VWBPT4LPH5EfGUuI1mbgm63ez4IP-VhLHro4V1BktAqBAxw8QZNofxwaTH7Mo-PsvGgny-OX_EoaTw3dpPe31oWikWotlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داوید نرس ستاره ناپولی:
وقتی خیلی جوون بودم تو زادگاهم 2 تا دختر بودن مسخره‌ام میکردن. پنج سال بعدش وقتی به چیزی که الان هستم تبدیل شدم برگشتم زادگاهم و هردوتاشون‌روبردم‌یه‌اتاق تو هتل 5 ستاره. بهشون گفتم باید برم دستشویی، بعد کلید ماشینمو برداشتم و بدون اینکه پول اتاق‌ها رو بدم سریعات برگشتم خونه تا کونشون پاره شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30743" target="_blank">📅 17:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIFYiowKSZt9YmzxN-c4gdGL-vPJAY7ISfnRQeD49sYqPIlc090p-zhLjCLsEXha2vI7-9YqK621wNfmB9GxyBIQF7qyUv7dN6YNzdZtAtHHvgWlnloFSwX9VDCE1Br7rk_-yNJtlUswU9qOr6ZT4zyMYYcGaEva3V07RobMDmVvs8iENEKsGYauXPE2eXW5nW_lZQQpra5bUnjKNI5nFvdwqaxgTfOHNvXDzYoyKICcwK8CyLTVYkrYm3Rja270eo9ZFIv5Ix-gGt8wT2oYZiwJEKMzEmvdyXm6VhZTdgBDsotuQ_OuQSZk55dm3dzv6w4bFVSEt11gwO8poifwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علاوه بر مهدی‌ترابی؛
مهدی هاشم نژاد ستاره جوان تراکتور نیز به‌دلیل‌مصدومیت دیدار هفته آینده با استقلال در هفته هشتم لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30742" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHz9ZOCuxJW2Tm65FT7SFg-giUb3WK4-8wX_bnmlHvGwIxUi_BkWZqlw2NMheOD9Ry5iPZOXL-okvHH47mG0EnJqeScJHFQOix9Uit7hxIkPzDS9t18XhzTA_7ZBhPSDp39tprhvtuHq7SQSp7AkydvIuMOFQ0RbISC9GyfzCs6ESa21katTruIqljGjJ1XjdmqZvb3MSHWvl1m5ipUl6G_s6tz_UTvbW5TB5YNikBX2V4c282JmXIW3RmB6krOq4fLf8sHwxXAO4NB1IA8vrReUmyK15erbT-Sim7CMD2ez0Wsh0LV28QzpV3mPBoUhsTkKoWM7KADmDONIoqHGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
لیگ‌جزیره هم ازباشگاه‌منچسترسیتی بابت تخلفاتی‌که انجام داده شکایت کرده و احتمال گرفتن جام‌ها از باشگاه منچستر سیتی و سقوط این تیم به دسته‌های پایین تر بشدت قوت گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30741" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwC23DDLoigsvR6UDlf9eEu8mZ3kyWpha4rk6gHxGmDZ52x5QkHD8nVbBC4n973GT-bQVK0G3Ob5hjWlnQWH3YqV1rOznrDwmpz_35NT3Uwe813djVCKzdFLMP9xG_RZjqEKV8WMg6Wn8rkhchcALmRVzwrVLopOfQM7719N1NbpWRVMpdYgwoSuVxJU9rlLdCd0iFeOoBIIzOMR-yUkiBgZjpPY71VFMTAgxynOIYUA_FbX9_OgcVtpzycP5_jdLyo6lrsFy5MM8qyt_qWWSdOsHuXag_-cP9TZFrqmDNsE8K6Or3W0W461OUPdJf4gS7424P1rEtk9JngKiTWSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30739" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
#تکمیلی؛ طعنه عادل فردوسی پور به بالا رفتن عجیب و غریب قیمت دلار به عدد 245 هزار تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30738" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpF677ooa01TSYaCqOFeZk7YSKgpGOhUExl_-M4dzGW7AuTW8z_JzZAaYTxkl1HQRj6SOHmJd7H5Vl29CrBQfF9YbFBaiaJB2KQan92Hh2-xmLXqiCORmEu92w0m7hI9GFu3q__CYMbxryxDn3SoFI6wvX9jrg-E84utEyktewfUtxu7XEIZPZy4BB1pyMxtHcJxyHzmjWicvl3F7pwC1HuLBV9F18m-Ulq1BzZ69iPD-MuvyjEKFKSuP4yBD5HjS7zrrGaZNzfCz6sYKMllhBIYIN_Y2PYe1pSyTv0diQ1epFTJAEs0kY_pq77lU9S3Rsg4zTVFG9mr2bGeqdIkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
نشریه‌مارکا:رائول‌آسنسیو مدافع رئال مادرید ساق پای راست مصدوم خود را به تیغ جراحان سپرد و حدود سه ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30737" target="_blank">📅 16:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
کی فکرش رو میکرد که نکات فنی مهدی طارمی دررختکن تیم‌ملی یه‌روز به مدال قایقرانی ختم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30736" target="_blank">📅 15:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30734">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOd7ZuCxmyQlHmYPK96ulk6t9_7ozYLJU8P6Xti4uKpWoSZccP580WsZ6MvJ8zDH1bmjB5e5_yHiRlUqooLu8YA7qtk_pM7sjEUYKXJo6o5cwLhiHPsezTSIIeNPcxePck0i4exEJ5-ict3I53Nc9W9K1SBHKNMmmVpzv_EZ0TDK5tTQwPDkrvEvEbH4JZhI8k9h0TsAvIwjOChQS6TorinIkPDA8cbENEqFEgWMJ3HrG0imB4FAKiPVLsqKnJNKwOMRYcR3HLbKAvn_B7S3n2EBskedPqS6wAT_x2OOiUYdw1QBpE2BDURbLDL9rHgfd7YitbY5ZXGb48lYEnYaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhVFv2Qwt6TXXIhlFQtbO0gKow95LgM1t29pSLbbu4V12-OdomN38j2XtPU-yvZb_KI5kRP1gm5lW00RCdSFA9VL2Fhx0ii8Aw6We_qyqwItw-uTmiGYTvsUCU0zYxmXAIRHJEd3V-pikbpS_3dS8pAbaAKuewdMv43UKW4dQ_kBcR738PcfImbtgxIvjEV9_u-RLYpHiO0SbTkVdqZXhWi2R4VGl21kjka3sKt_reoQJQrv6AFyBv04KrhMJJoQniIRJfiwX-ixuV9HPhkXIZKJSAmy3LFRoCPuo59YVibWw_NCuSlY9MxVkfb3JhKhlRhsHCAnUhiwSx3K2uhO8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز ستاره تیم ملی برزیل برای درمان مصدومیت‌اش اردوی تیم‌ملی برزیل رو ترک کرد و به بارسلون برگشت. مصدومیت رافینیا حاد نیست و بعد از فیفادی به تمرینات بارسلونا بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30734" target="_blank">📅 15:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30733">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETBu9gZfpk33O5ktEhC35XtxVz8g4Irwmhah1tUVqJdA3mTC37hysjge2WhzFOxb3rIzp_u45s7-CPM4pq02Odlzm9z1oCRW9DtUp03tu2y3xbFqKGBBXFTMU8ujbtcp7J40DTPynFoVN6fggttCh7zcfzHrAsg-cxcEHdDm1iDd2gDsEoQ1hTg8kkq9ja2BtRG7xXM3LoIcoR4rjjUfgQhbZSMeFy3jjWye8mVM86uokjnNWfKpIsa6whs2FOd6UUplXorAOI0SQBLdb5uPG7pnD8svGPPUvVC8Jd2BnXocHkpK9d3R1QJDU5LEusdp5qU-aZqbMAbB5QwZjZaaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30733" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30732">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS6q8qGfGSnnuk0ybrqBTuqparYioTe8GTLzWeFW7SB8x05nM3C6eZs3mn996PCeJqRr7TWRcFnzDenEDecJ3fK98v807LvhZf_JGEclf132zDe3zGc84MPyf545Lv0OkT2gi9208OX4UCSD2K6zpiu1uaUwo_cR2v1MNATh0-ydqy9AEaVv20HDMf7V6KekVX78PTYgGdRDSsC5jBl42zFV09QkpC0HHSnUfJPg6fjyFxv5HOUeiW_W4SiACxcqrsiJsaek64NiUQntXsk6UqyQOnSzfSS4GKui9jj2hYY7A9QCmaNa_Y9SiYgaIsJuCU6xXjpAb0481qubyru1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30732" target="_blank">📅 14:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30731">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAChVs8XNuAfj5EQptWUWXZerV0jzL4EbIG_tAR7Vs2KxvMkQWEi5Jja4fNnU10dGFT0HpNmaJXqoMzfziPa0h8eU8nRsmNPujHmKi76H73VsCOYhQTZKj6cuqSgik--iWwwe0yPlzYYbXJ2HFWxb7oNyxdAA8pkVNVUO6GxU9JKNWyco8-3x-GvyX6UpLoXody8pNqTUWnxb-PtHOU-2SFr6CE_pwNDpirXwqmViczzYoVqgdmBQ3R_4XjSBMLPINaEKEKjwialpYFu2cMFIiWpNRX1irvD1tJOHaktO8E12p6VJk_YmuYKzBSSPvyoQhKDO2CRdSq0aQsZQtwYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
کول پالمر ستاره اسپانیایی و انگلیسی بارسا و چلسی در کریرشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30731" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaZxcW8hzZe711lRGEMbC6bQPuRYFXC-neaBxpobiJv1zvXO9kBjD_zv5WM4ntIHgn4GJi8WP6SufWYvfo-ChHxQ5smeMN9bdPfXrdg-cirADKskRV6690-1pX21j0GCuuLm0X1UfPnKPurX9cngPfQDgvymqQJ1vQPpkaJSPlGi0rpXE5X4-YFs8C-LirFW-EIgEJC5ijMDmrn96icaobYSmddtZw5tGitgufliHozdMQSuWkJGjHjlyjNw1_rxBNjYMg4HdUDG33R8FZOILIU8m33zFqY3fUuHfYdCW8Oj1jfVDYOmNOVUhjZ9b01vAkLAjl03YqB2Qd41yCbtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون: در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30730" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30729">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InXwAQA1r_e_LLkgxZgqsDfGVTNeAWsWdUHv3GK0OxDUqP_4GxY7Ogik_dxHRFassZ1NQ1-tQj6yyxhvbSwECgmz7UMngA2-8aP8ZGjYjUASPvJBj_LRCcjd8eAFQ9skNtJkfcZ_ARNXJbxM6GOvy-lBUqFXW_IxS6th7QJltyBczBNreNJLSMalO6Vj8K3nFRtxpxqiM3eNSHJbX1GLxV6N69bICh8vq_IyN15g7Vu-SckECG6bqqyok8LZUL-HganMHoIm7FOPq5J6Oxd2oOrdRlx0ksSMjx-GOoVEqSgwwQB-xtcyw63wy_JbE_YOQ3f78JrS1sgN7olMBVJr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔹
معیارهای تعین قهرمان لیگ برتر در صورت لغو فصل جاری بدلیل جنگ از سوی فدراسیون:
در صورت برگزاری‌حداقل 75 درصد مسابقات رده بندی براساس جدول موجود. برگزاری کمتر از 75 درصد رده‌بندی بر اساس میانگین امتیاز در هر مسابقه. در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30729" target="_blank">📅 13:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJxU8Cj8j3lkpUHZQyH2ruqvp-LrvoReuwE9q5JTx5U3OSVE9XCtvJVMTROriLsnMFw0HsDhNb67tRWqonOc1pKdtTzx4J4z_psWRciaRx1zXmScCh4h7sxreCnEOja1DvqCEO3CszJUPL43sOFLhY4AR1WkeXRdXnKKJT8rva2KSZi39dMvCoetmKWj8dwhpRZ23w3eCf2kyfM1r7eeHOheY5gdiOQUaz71IGb-7JVNJE1jwa3t8_i7O6mBZBC9wSduvc3s9-pu1kztU-B_nBCP7PBiijcNW0zRb9MFmb4SkptkeEbhCB7kxPQVRa9WWUBTnm2iagOe06OLBCNFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIQJ47BHl519sNUm6kWks4L3TTYVRs9FLMHPVTZsT9yU0qIwJm8AAgi3ZzGEl6Nh2hn1f-6uMUXU-TWA6jUYryXEdVmASkHU_g0giX8pujWuDsRM3UHvgW-AA4mgbRZdOjHY7JbjHmFf4jo2PrOZt7ld0flq370DR79GqWdTyGEvX2udPJ62OkQMn7bAgDOF9bDY6Y4Uf6s8e-rN1V7wvuBoEhIWrPL0Iqy1MTddRmz_KAvedguQW-zrTbqy9q5xBxSylQJI29D_UnQdWT9MSU2IPRmIxyI8f7CNmB4H0cQA9wcUlFbvyf5hfp7jUZxEBUCdt7PlMPsCnxtglF5BAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

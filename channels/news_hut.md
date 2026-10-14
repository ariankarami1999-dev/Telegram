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
<img src="https://cdn4.telesco.pe/file/s6aD9SqDNdRDkR3qA5JqmmXyF8OJG6y2yXKnNUp_jzEMu6OY740KbywtNZYcWkeUQn5LGi_aw01EOG0w9R1PFTgCAifmj853bd3xbvWE9jVt-_OW2q7Ct3s5VW39g0v_INM_E1ScXZ_mCJ4b2CWRyrqHcGuxizlABTv4GptcrWgHHuMUaoJpRLDZwuQigjKFI9I7XaefAXcp_0TWFs68ch8o7hf9F9p4h9tgct-PEE7tX7772As_arjkUNNiZIcWDhRRjdTAvHugJb2OFHSRhgSzpy8aijHy4JZjtnFcvwggksX7oiOpbYwvRCIgjN_FHfolGqTtY6ogkkbF4j0M8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-73260">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">استانداری هرمزگان:
دقایقی پیش یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدوده بندر کلاهی برخورد کرد. بر اساس اطلاعات اولیه، در پی این حادثه سه نفر مصدوم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/news_hut/73260" target="_blank">📅 11:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73259">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e01fafb.mp4?token=mkA53g-Z7WuUc9y7iZAkgQO0IacDxOtLOFt_dJt3Pv5qEZTdCZ_2ZlTpgXk1c1NqahEfNtafTBRy3uIQwJ_s5VT4HxBMo9zPkzkTVz7W6eLwFtFx1X5CFwSxoxz7cyARtwnw8UdBcri47HW21a4ozwd-m8baY4rti3EsDgz4X9c6UOnfGasnCbDef5OJ-u4O9D1SmTEeO3E_bW_6DkFEBQHaB4mlyfdKwH0siKUk3h5Z1YHVS0ARN1cSVeOOaHEOOx8CkLTt3AmuPjq-Qn9F0f8MSJuw5Q_KhKGu9SV--QjR6zxLjupTIgjQoIlt02Lh1gFKdScipIMpUwnA6HfG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش تو مکه-عربستان، یه کفتره با گردنی شُل درحال مرگ بود؛
که گروهی از زائران رفتن بالاسرش و گفتن حیوونِ خدا داره نماز ميخونه و حسابی به وجد اومده بودن:
@News_Hut</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/news_hut/73259" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73258">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20d7f23a2.mp4?token=i3SeBbcZFwzBde2iCKrBklKbL5reeKZ6OoTxDmuvpClyndoLM1jegVqNrz4WhubfhGuWr8w3liGX25NOMgEKvCVw21hznW4CX6Bq7aANWKujN1Xy7DvK_xR--ROlBdsPe1uPwBo0IDIsL350OezQWQCpTu1XKDJnaVQFLCknXllTky7ijQON1J-V253C5iM472ocICi1L4U0A-sA4EWhQLqi8vpKuxardp7kjmgFPFAYpRhzMNTch1BviSDMSUmiAGc7Yin9u4TPt2GLp8pnw_jwHJ5peNd-EiPIerVRk_Oit8jx3Y_1eeW_SkIxgdEhOCgYMsUs23q1QIEkuQy_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده:
@News_Hut</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/73258" target="_blank">📅 10:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73257">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPn_ZbvZY5rXdq4fkdKESYLWgMpfaa9VoPCpz3uvteQehWa59b74VoUKwiGaV-43e29o6Mqe3H9sbSqVXyjZECjkEtfYZQW6cnsxA1fKbSPOnSyKD4KrUN-0yaTTrTQ-5b0fDvlgRwWmzNO8nUuS7htzhHnBJ7Jztj73TUFvHEcDFOeG7Ojx_jGmHzwTe8pKkUMN-kI74CMEuximGKCpeW-WfTdLDHs4XhCWxt4gjRraAYySFqp3aL32BUdRx9ISDsKq0U51N4AoXd2s_4ozMN-cIYgh3OavIYo27hJx50sp451WKyozYPfVQidYe-fOc1iAIvkU2Jt1Z_OFHdmreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد ۱۰۵ هواپیمای نظامی در منطقه طی ۲۴ ساعت گذشته
۱۰ هواپیمای ترابری ورودی از خارج منطقه:
فرانسه: ۳ فروند
آمریکا: ۳ فروند
بریتانیا: ۲ فروند
عراق: ۱ فروند
کویت: ۱ فروند
۸ فروند هواپیمای ترابری نظامی منطقه‌ای
۴۵ فروند هواپیمای سوخت‌رسان
۷ فروند هواپیمای جاسوسی و شناسایی
۳۴ فروند هواپیمای ترابری نظامی که در داخل منطقه جابه‌جا شده‌اند
۱ فروند بالگرد نظامی
مجموع: ۱۰۵ هواپیمای نظامی در ۲۴ ساعت گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/73257" target="_blank">📅 09:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73256">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=m10YpRDQxIUJX1_r3EWCqclMNXxqhGmqYIybu_zLDOdGYKICeP9H5Hcu_aLINeWHnNSnTblmWX8DSTdH4WK8HwsAHIxfPjcGO-oEiZPf8RR3LEjZXhYUDyvYGZTL-4cyN3aOVBJZmaakzzQ-8BSpn6s3q5KPjCxpiAncqjTleTbvQWAz36efPM866LzKy0bOECkqpSqTVNXFwjvTBARgrT8Q_h8lWlA7JJYXi2fRjRe8gZv49mLh_2Dl_J2YZJpTT301QTSXZJm79Ba6MXlhM9BeorTD7XNZSpDH67ruMQZ12s1aoYF0drJ2-HNJ5SV2rSvE2cL-GsdaLXJtdq85Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=m10YpRDQxIUJX1_r3EWCqclMNXxqhGmqYIybu_zLDOdGYKICeP9H5Hcu_aLINeWHnNSnTblmWX8DSTdH4WK8HwsAHIxfPjcGO-oEiZPf8RR3LEjZXhYUDyvYGZTL-4cyN3aOVBJZmaakzzQ-8BSpn6s3q5KPjCxpiAncqjTleTbvQWAz36efPM866LzKy0bOECkqpSqTVNXFwjvTBARgrT8Q_h8lWlA7JJYXi2fRjRe8gZv49mLh_2Dl_J2YZJpTT301QTSXZJm79Ba6MXlhM9BeorTD7XNZSpDH67ruMQZ12s1aoYF0drJ2-HNJ5SV2rSvE2cL-GsdaLXJtdq85Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
این رژیمی متعصب است. تا زمانی که پابرجا بماند، برای احیای خود تلاش خواهد کرد.
تلاش خواهد کرد برنامه هسته‌ای‌اش را از سر بگیرد؛ دوباره برای نابودی ما، و بازسازی حزب‌الله و حماس تلاش خواهد کرد.
برای نابودی کامل این تشکیلات، باید این رژیم را سرنگون کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/news_hut/73256" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73255">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_VGv7MgXdxx_hEVCwlCYiDQzqK3GwB4LxB1MM0jp48y8KT3XdqMABSwqDIX0rIQhqEUrDqySIWBKfBbJEXTDe4zL_E0mvRI3o8tpiGgbVtd-BJkxNIcGmAzVi7AH9pUzYefKrKcjQHI4PwFPYJ_0J5BBA9OdZsaFz2maR-fPDxNi8cSg0lkhpFb1IPyyiK06CYZDyUhzcyVig_9aqkvzSq-Kqs41O1ehx6TYYLAHPFGnbDvy6pA76hiPk_ghCFT5Uzw6Xx7c1k8AcVBB8W_iC9t6w3d2xwoNaIzKj-ny7p4WUyxO7GeuBEutv3cYd4XjH-LM-1nbUCkO1q3VtbWxvvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛پرزیدنت ترامپ درباره ایران صبر کنید تا ببینید با ایران چه می‌کنیم. کارشان را خواهیم ساخت؛ صبر کنید تا ببینید. آن‌ها هم فقط منتظرند.
صبر کنید تا ببینید با ایران چه می‌کنیم، چون دیگر کاسه صبرمان لبریز شده است. می‌دانید، دیگر به آخر خط رسیده‌ایم.
اما خب، این‌ها اهمیتی ندارد. مسئله مهم این است که قرار نبود آن‌ها سلاح هسته‌ای داشته باشند و نخواهند داشت؛ این موضوع زیر هزاران تن سنگ دفن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/73255" target="_blank">📅 09:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73254">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=h7PKOfOYoOCCBBcU5fsnUJrSUBvJXwM7nHgy9LvCOMngEzePDIhPQiZe14pJyidfmgsaCs5MRptbx77bCABKcIo-2RoJp5ZA9eNH0IghGnWncovm4tkQO7demWZD4meRH3P8KbtnMjZG-KmRgqBkr0TuqNxy71zk5DDAIIQ2Bj7q93Z3jQend4FngR21KxnkHPuGxrZq5BGcUmFlOggi2-HgJ4e4Wg93xALJEMjVrzdI6zcD-BNW8etvPWyxfBP6-z-OFcXJGI3qoDRkEJpIYSSzwL_qCyzHQfYGljTNjUU5QrIDPnZ9ZB-r6kfKiHj7WC_uFRji1Y6ICjfIdyQCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1adb1098.mp4?token=h7PKOfOYoOCCBBcU5fsnUJrSUBvJXwM7nHgy9LvCOMngEzePDIhPQiZe14pJyidfmgsaCs5MRptbx77bCABKcIo-2RoJp5ZA9eNH0IghGnWncovm4tkQO7demWZD4meRH3P8KbtnMjZG-KmRgqBkr0TuqNxy71zk5DDAIIQ2Bj7q93Z3jQend4FngR21KxnkHPuGxrZq5BGcUmFlOggi2-HgJ4e4Wg93xALJEMjVrzdI6zcD-BNW8etvPWyxfBP6-z-OFcXJGI3qoDRkEJpIYSSzwL_qCyzHQfYGljTNjUU5QrIDPnZ9ZB-r6kfKiHj7WC_uFRji1Y6ICjfIdyQCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تولیت آستان قدس رضوی:
توفیق اقامه نماز با رهبر انقلاب را داشته‌ام؛ حال ایشان بسیار خوب بود
رهبر انقلاب پیش و پس از تدفین رهبر شهید در مشهد حضور داشتند
@News_Hut</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/news_hut/73254" target="_blank">📅 09:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73253" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbZTe0tADKDZHnRz16yGi3KOj9OU73psdbA8gHfEepfo8RJJ7THTVR6TX1gRQagLsA_4LHtjLG7lwuTs9_syJduE3z64lvITtrvDLmoT5JhXdiYeZtxvBO4AWgKfwmOFuuBA5KkLJFrCbjFkwu9bbrPTw8bN9pB5Bas6yhHKVZ4GF6RbtImyUx1e2pSoyQiceZPFg8EXf_wFdV0MEcvADar5nzHa09oUN65w4Z-s-YjInr0SlJliF42rh3NUbgqLTVlfaVOSrNT8MdhZcPDANCIPQPLJ98yJIGozqXQ-hxWPq_Fnmb0JrvdrArJ7WTj6JpDJ6kHNibiMXvQjpV81iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73252" target="_blank">📅 01:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حوثی‌ها به مقر شرکت «آرامکو» عربستان در ظهران حمله کردند؛ این اقدام ساعاتی پس از آن صورت گرفت که آن‌ها به‌طور علنی این مکان را به عنوان هدف تلافی‌جویانه معرفی کرده بودند.
وزارت انرژی عربستان تأیید کرد که یکی از ساختمان‌های اداری در مجتمع آرامکو در ظهران هدف قرار گرفته و منجر به وقوع «آتش‌سوزی محدود» شده است؛ این حادثه تلفات جانی در پی نداشت.
خبرگزاری رویترز از شنیده شدن صدای انفجارهای مهیب در نزدیکی این مقر، وقوع آتش‌سوزی و صدور دستور تخلیه خبر داد و اعلام کرد که به کارکنان گفته شده است روز بعد از خانه کار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/73251" target="_blank">📅 01:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0n2P250A7qHZmTtEIZGzhITZmfYCAnSY1PvAB8V3aMUtwg27scseVixSqihG6nA0z1wCyeMlAsdcGp1wZxJ-ZJG7U0ah8YYz2J1ZQmAzixeBK2Qg7q-5lG1pH_ADATmjU1_jtpK68Izrg_ijw2oWA2hJrLhZAKBr-sQ3FBmem8fpCF_CbAFvgIZAgMyhdlQNdQzO8P6pyBgOACxeKxRDfpR3rN9ci_fAKWVwbw38dtyPBRjcGbCH_zAy9WnD4qBJtX-GDqOoP7bls2iRM2DIZPQczm2Ot14clS54FWwy9uYAvyNzeRwSG1LdxmeBVwSHSGv51lGJ6ExSX4CYyaFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/73250" target="_blank">📅 01:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/73249" target="_blank">📅 01:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7e4aede4.mp4?token=XormlDmSJSk3diuhBT2N7W_441fC8NqClXlH_oph63Uwny8Ghvz2N-rU9yOHkLL6t7GNkZBmqQbqyFt5ziP6wprPLBbhOG15R08-zbm_ggp2u3IifXbv4GGs9NKq2okbNb0-BbySZWvkteLOp1zSICsURByjL_pkHmMvvn_2Vgch6mibaiec6cVcplL5tyyIWftDg5YYHvvkFKHOL-13Dnowh-g_GkU4AsFUe_IIi04onBhEHDA-Q7e_UQGqn5GBa86lCBnzDclEc60oAaACd9LzqOg14jwIt3BF9xdCpA8MjLYxtGOt3-w_RJIACInYVvn_U5Yva6hy2ZAMef93Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خاتمی داشت با عصا به سختی راه میرفت که یهو ملت شروع میکنن به تشویق کردنش که یدفعه شفا پیدا میکنه و عصا رو میذاره کنار و راحت میشینه!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/73248" target="_blank">📅 01:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=ADDQxsYhQorSS3ZX8jnB6KKAoJDX3sKzyh83fop2i5Dz8TEcTtw-3jyEJAW1-qtNp2rEDxdV9cSfbKoo-Z1xIQOGTkmqnqoasXzr9W9iTRUdC5rFaocuWhEAKOyr1sD4cbIbsOT1u-NMhffLV5Actwf8igheocI1vYNFoc_55iKM1bI8jd2y73NZQzgpBIkhwwMgIUwXUFLr1cmO9sNEiVhg2Fe57YnSD9bSVkYXk19G7PLAPqs5rUnsGa9F-ktJm02ky06ZNnyb2uSqJzEHX1lDfUNJo-x1nD7whBOm9V0vJvobGA2dUyga8MxbtrnPv2e-wkl92QDGZzibOYnnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=ADDQxsYhQorSS3ZX8jnB6KKAoJDX3sKzyh83fop2i5Dz8TEcTtw-3jyEJAW1-qtNp2rEDxdV9cSfbKoo-Z1xIQOGTkmqnqoasXzr9W9iTRUdC5rFaocuWhEAKOyr1sD4cbIbsOT1u-NMhffLV5Actwf8igheocI1vYNFoc_55iKM1bI8jd2y73NZQzgpBIkhwwMgIUwXUFLr1cmO9sNEiVhg2Fe57YnSD9bSVkYXk19G7PLAPqs5rUnsGa9F-ktJm02ky06ZNnyb2uSqJzEHX1lDfUNJo-x1nD7whBOm9V0vJvobGA2dUyga8MxbtrnPv2e-wkl92QDGZzibOYnnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/73247" target="_blank">📅 00:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSovd1F_eB7ZnpQqh0mXfTOorg_Pqs9vBVroaYvujPxgdoI7acxHE-6jELr8buwmYOM0_HTBiwFeOVptd69IhldUlpUtdjQoffn5W63VoN0urNok-y28pPtITVaP0G5pCj6yZ3smtKeyhKi6oevUGIQ9s05Vn7jGNKpTElCsnaTKwf2sFu3-4FAqB81mIQBrsjzgwlNLEo0-GxktNC55Py4MpcMtTzUGT3axp-rvtVQX6RA_w3oX_fltwIAZ0BGxaamlyFckbaeEICRNMciWxRQXZsuYTVE94hfXgGfYqhFYaUuJRQpvLOS4p0H-ATxC1X4n5Hju0l_iZuhX9KW5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
اکسیوس به نقل از یک مقام آمریکایی:
به نظر می‌رسد «بی‌بی» (نتانیاهو) می‌خواهد دوباره دست به اقدام بزند. او چند بار در این باره با رئیس‌جمهور صحبت کرده و رئیس‌جمهور هم گفته است: «خب، می‌دانی بی‌بی، برو و آماده شو.»
اما در واقع هیچ تعهد قطعی‌ای وجود ندارد. عبارت «برو و آماده شو» ممکن است به معنای «الان»، «بعداً» یا حتی «هرگز» باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73246" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=NF3vYFjAA7S3xbIGbgLIUm2mHmVSWMvE8EnO-Y8FaZcDBYr_wGDUf06YXyLZInYFEN-VU1trOYtD4ca62sXL88mFadG5y0g5dYfpAM6ElHdv9dWMNUwWPL37RxhWk45Eytj22PI32CRc9LDHiL6FB9WC3NZ-uhV8hss4fmDE73n2FOKJM4t-6tbwUREaSxzj9VhJgAErZ5TYDslsIoq6TGNSkTr5RPtDty7eiCZTLp-mVsfen_GbhVMOIxja3oWXhRlUE5qWvHefwMg2QuBJfmZqYmnCwp4oZF7CM50N0oZb3-OUs6X_TrDD6pmPQmRETNgYPp2SW2lbtBNaDfdE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15a3b1b7fc.mp4?token=NF3vYFjAA7S3xbIGbgLIUm2mHmVSWMvE8EnO-Y8FaZcDBYr_wGDUf06YXyLZInYFEN-VU1trOYtD4ca62sXL88mFadG5y0g5dYfpAM6ElHdv9dWMNUwWPL37RxhWk45Eytj22PI32CRc9LDHiL6FB9WC3NZ-uhV8hss4fmDE73n2FOKJM4t-6tbwUREaSxzj9VhJgAErZ5TYDslsIoq6TGNSkTr5RPtDty7eiCZTLp-mVsfen_GbhVMOIxja3oWXhRlUE5qWvHefwMg2QuBJfmZqYmnCwp4oZF7CM50N0oZb3-OUs6X_TrDD6pmPQmRETNgYPp2SW2lbtBNaDfdE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دستشویی یه کافه تو بالاشهر تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73245" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام آمریکایی به «اکسیوس» درباره ایران:
مذاکرات نه کاملاً مرده‌اند و نه واقعاً زنده؛
ما صرفاً در حال افزایش فشار هستیم و این باور وجود دارد که در نهایت، عقلانیت و تدبیر در آنجا پیروز خواهد شد.
ایرانی‌ها تصور می‌کردند که این رئیس‌جمهور به دلیل فشارها و انتخابات میان‌دوره‌ای عقب‌نشینی خواهد کرد؛ اما او به آن‌ها نشان داد که در اشتباه بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73244" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejO7m5TFQwW1ZTXFIHJdPaAa0shBfyfw2iBuxKUYuTK2LcvUap-qPHLpmmrlJBjDZNzvMq0TChGyFmYlohhd7w7ScZ7QUjnPZc5Q068ePfZLQw82ODHNAqU1bPbV756bXZf2oSgO3_pURS-O158LrnswXibWB9of0hLoDfqOSks_Y3kqHC53ij5iTcLdLclfaBphU6fnDA1scUjogNgCuCFSQqmdT8Amczbi_8cPTdqUAXaIddcs4mI8lR1ezkS_yQvOa3xR9sCrzZw2DcPz8HUsDXr0f_q_XVXWX-xOiFhspo2_se7qAqbjH5xfPle4ofMC_s0qUekKVc2pdgK5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی تجاری بریتانیا (UKMTO) گزارش داد که یک کشتی باری امروز در تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73243" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=v8PLq1ypc_qxzflVqUCYtAnFldiA32t0nrjg1qcTAGSql1qoUvUeL-G3Vk-J7tn95fxWVtQhNhNZDvMZ5EjjGmTiNOha4aYHHZzHPsMuixkP_c-lh1r41Yi2m8w2nwwhg9gidBJmcfeIlxWA-m-TeN-G2zF9v39MqphQHm1tDGZ0HoBjp4oiVagZzeiHOL9qmF43yA2JHZ4AVd2xkGvBOaMx7Bs5iBWxcMOiKav4c8d38a9s0k3x2k-x1lKJZZitOv_5pLHYuDCT8v4xrUt4IuJmvENgNkwmoOanLu8a6LmSxeqifXcuvbiudE1WRADNZPTxC_zrf3b1bo5GcCGt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d007bae0.mp4?token=v8PLq1ypc_qxzflVqUCYtAnFldiA32t0nrjg1qcTAGSql1qoUvUeL-G3Vk-J7tn95fxWVtQhNhNZDvMZ5EjjGmTiNOha4aYHHZzHPsMuixkP_c-lh1r41Yi2m8w2nwwhg9gidBJmcfeIlxWA-m-TeN-G2zF9v39MqphQHm1tDGZ0HoBjp4oiVagZzeiHOL9qmF43yA2JHZ4AVd2xkGvBOaMx7Bs5iBWxcMOiKav4c8d38a9s0k3x2k-x1lKJZZitOv_5pLHYuDCT8v4xrUt4IuJmvENgNkwmoOanLu8a6LmSxeqifXcuvbiudE1WRADNZPTxC_zrf3b1bo5GcCGt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار رکنا از سخنگوی شهرداری تهران پرسید: چرا در تهران در تمام ساعات
روز ترافیک سنگین وجود دارد؟
محمدخانی در پاسخ: «اینطور نیست، مثلا ساعت ۳ نصفه‌شب که ترافیک نیست!»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73242" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26766391a1.mp4?token=dff96swu5RsaYDhLBXUy-8Mdq2drZuOtyixI7NgH8XzUW8nSVHf9sySOiPvMmFehH-Rm2-QWdcou_U-Qg_xeswDujtkU-hlxHiMayq_WYhgnbxL3hj8hjxZ7Hvr-fN2FXgQJB5N6S5KJnKwK7yvZ38GiCI81D3lcOu7Jl4LY_ZosrnJMwtTnVIm2TqE7hUJy_4S8aLOe43ITbm8eieSfd3OwNf_45pdg_ax4HOIcmyfntac4CFKkoz7UHO9fVCddGQ_fl3XwQPdgXQXAer9y35_137ysc6KAKBMtxih-QEoLiB1Ffr61Y9KqQt7Dfjd35BUF9yr392hO4TSMUm9KPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26766391a1.mp4?token=dff96swu5RsaYDhLBXUy-8Mdq2drZuOtyixI7NgH8XzUW8nSVHf9sySOiPvMmFehH-Rm2-QWdcou_U-Qg_xeswDujtkU-hlxHiMayq_WYhgnbxL3hj8hjxZ7Hvr-fN2FXgQJB5N6S5KJnKwK7yvZ38GiCI81D3lcOu7Jl4LY_ZosrnJMwtTnVIm2TqE7hUJy_4S8aLOe43ITbm8eieSfd3OwNf_45pdg_ax4HOIcmyfntac4CFKkoz7UHO9fVCddGQ_fl3XwQPdgXQXAer9y35_137ysc6KAKBMtxih-QEoLiB1Ffr61Y9KqQt7Dfjd35BUF9yr392hO4TSMUm9KPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عرازشه در مقابل منزل حسن روحانی و شعار بر علیه او:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73241" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرویس بهداشتی یه مدرسه پسرونه در تهران!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73240" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbTTAj7biiKOyBVZpQlNm0UyL2YZ0d1anTUtaRsiTWhbHaIrp4xhw9cwhOH2L74uKR4O52ArqEGQb5JqWxtsnm7kSfjDUtnN9_ryL1NmllRIce-4nh8xsduQl9qxtLsUmIgwK0CbHscBG2Zd2538nmJg9aVPs_ch_FdNcrJr_WlAvZd8QEiwS1z_N2ZM_QzvKUZNa5tE-c_Xh6nZQFviEYU-RX9wex07PLjVAGtKxp-3HjWWsgMOH3qpZfQK0fnYc8W6xgt9qQ_ZYcWoeRubeEZLvy0QWG-71fDaXGeQdmAScRcKix4fKrQLes1vsMPL4GXroNk_J-ULgkOV1DfP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، طی دو هفته گذشته گفتگوهای متعددی با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره آغاز یک عملیات نظامی مشترک جدید علیه ایران داشته است؛ عملیاتی که احتمالاً پیش از انتخابات ۲۷ اکتبر اسرائیل و انتخابات میان‌دوره‌ای ۳ نوامبر آمریکا انجام خواهد شد.
نتانیاهو با ابراز نگرانی نسبت به تلاش‌های ایران برای ازسرگیری فعالیت‌ها در تمامی بخش‌های برنامه هسته‌ای خود، این تحولات را توجیه‌کننده‌ی انجام حملات مجدد علیه تأسیسات نظامی و هسته‌ای ایران دانست.
یک مقام آمریکایی اظهار داشت که ترامپ به نتانیاهو گفته است «اقدام کند و آماده شود»، اما تعهد قطعی نداده است؛ در همین حال، مقام دیگری گفت که موضع رئیس‌جمهور همچنان در حال تغییر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73239" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی طی ۲۴ ساعت گذشته ۱۰۴ حمله هوایی و موشکی علیه صنعا و استان‌های ذمار، تعز، عمران، لحج، الجوف، مأرب، صعده و الحدیده انجام داده که منجر به تلفات غیرنظامی شده است.
این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های هوایی «خمیس مشیط» و «طائف» برخاسته بودند، و همچنین با شلیک موشک از «نجران» صورت گرفت؛ امری که مجموع حملات ادعایی ائتلاف به رهبری عربستان را به ۲۲۸۱ مورد می‌رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73238" target="_blank">📅 20:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PPPG7Y70tMK9xIvVhnI1j_Dprc_Aqa6yzKUnOi-Ax8a0zIjvkj_LVA7B_z_TizwG4d3HJT6gVodIAEFZhNKQt6gbcoifS60eyTFS7V4AqqaHB-C76rvqmWOK-t860aenqjtJazy-jFU0fSokOXP7UNv0X7qpDJUJp0sgnr88zGsDyJ-YrLnU6q2X6gN3VTBU-71TDgsiyl48ZKlKNjmPqonEfRMd5tlR4XoZcVIjPxXbGaUmLAx-U-4TIbI-bJdIBtZ0R_CGBWeBzWzHRGeA-J1-6Obo4WNgGAiyCN8nNkwgeCa8UFymM0rmYvpZDIkNoNYXLgrFPKN6JPEy6798TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ترامپ در تروث سوشال:
«حوثی‌ها رفتار خیلی بدی دارن. فکر می‌کردم یه سال پیش، وقتی حسابی بمبارونشون کردیم و به درخواست خودشون حملات رو متوقف کردیم، درسشون رو گرفته باشن.
اونا مدت زیادی سکوت کرده بودن، اما حالا دوباره ظاهر شدن؛ احتمالاً به دستور ایران که یه کشور در حال فروپاشیه، نیروی دریایی نداره، نیروی هوایی نداره، بدترین اقتصاد دنیا رو داره و تورمش به ۳۰۱ درصد رسیده.
اونا به شکل خیلی بدی به عربستان سعودی حمله می‌کنن و عمداً سعی دارن قیمت نفت رو بالا ببرن؛ احتمالاً هم قبل از انتخابات آمریکا. این اصلاً قابل‌قبول نیست!
یکی باید بهشون توضیح بده که من دیگه نامزد انتخابات نیستم؛
من قبلاً با اختلافی بسیار زیاد پیروز شدم!
اما بعد از انتخابات دوباره وارد ماجرا می‌شم و این اتفاق رو هیچ‌وقت فراموش نمی‌کنم!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73237" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خبرنگاری رو که همیشه درباره وضعیت ایران سؤال می‌پرسه، مسخره کرد:
ترامپ:
«ایران؟ باز هم ایران؟ همیشه ایران!»
«ایران یه کشور شکست‌خورده‌ست. هیچ اقتصادی نداره، تورمش ۳۰۰ درصده، پولی نداره و حقوق نیروهاش رو هم نمی‌ده؛ نه به نیروهاش، نه به هیچ‌کس دیگه‌ای پول نمی‌ده.
خیلی زود درباره ایران تصمیم می‌گیریم.
ما تنگه هرمز رو کنترل می‌کنیم و نفت زیادی هم از این تنگه خارج می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73236" target="_blank">📅 19:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=f1BJpx750HC_hQH1EnRb0-mMXtdX3mhHv0tsCl4CkONIh3Pc_jv5exAGqe-FX2XrWVxFdywXJmjqgmOebJwN8c2YeOGes_d--lrjuX_PYMZDb9C_-0Y6wx1gkCPDomRjeCJ6vB7RK1NPEEW4ZWe6pPAq-L6_LQzLai3fNmVFfORj30xxseZBZbO71fvNCLZf2ji13lS60olR0XGMWUGA5jIxHnx8TMq1K8lXvzhuXerxhKkSRo-wXIGNLN-_vYHMGdv1uesTOUgUi7E3XgK3GkoSaMBxVGKIOjJVmM3O2bOFMdpOEdE3UN4YwErlsmfc6w-ZVIivOj45JtNUlmB9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=f1BJpx750HC_hQH1EnRb0-mMXtdX3mhHv0tsCl4CkONIh3Pc_jv5exAGqe-FX2XrWVxFdywXJmjqgmOebJwN8c2YeOGes_d--lrjuX_PYMZDb9C_-0Y6wx1gkCPDomRjeCJ6vB7RK1NPEEW4ZWe6pPAq-L6_LQzLai3fNmVFfORj30xxseZBZbO71fvNCLZf2ji13lS60olR0XGMWUGA5jIxHnx8TMq1K8lXvzhuXerxhKkSRo-wXIGNLN-_vYHMGdv1uesTOUgUi7E3XgK3GkoSaMBxVGKIOjJVmM3O2bOFMdpOEdE3UN4YwErlsmfc6w-ZVIivOj45JtNUlmB9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا از ترکیه می‌خواید که در واکنش به اقدامات یمن ملحق بشه؟
ترامپ: «ممکنه این کار رو بکنم. اردوغان دوست خیلی خوب منه و احترام زیادی براش قائلم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73235" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=Rzh1I5Iyk3frrd5c2_C9evY98CyBBBdv9vyzDliFrSwKy27zhXmGFqCgAuYk_qrPebGzuzHAuRFE82AoO8hgzPmuIkkkG-dB45KtkvHfI3r1u8gD6FhPxmaGe2K5oe1iC_u7mw71JGZAl_R9iXURnSiNPZ0S59X7_7xfFLe7Bc95Mq45vOZ-r__4sOiEyaBe4cmcBNN8nuvSZLLdFL-Rb_YdW4BnzvZNMB0iPGyK90ZFYPO0WG4Tltko9wmV1J3Msh6bVwZUb7ol6TMV3g2FQhQr-2sfVXyWy1OlS4u2yhCVa4X9NOPh9oiQM5WF_C9LVl5ETcmkKIbWLoZRAfc2VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=Rzh1I5Iyk3frrd5c2_C9evY98CyBBBdv9vyzDliFrSwKy27zhXmGFqCgAuYk_qrPebGzuzHAuRFE82AoO8hgzPmuIkkkG-dB45KtkvHfI3r1u8gD6FhPxmaGe2K5oe1iC_u7mw71JGZAl_R9iXURnSiNPZ0S59X7_7xfFLe7Bc95Mq45vOZ-r__4sOiEyaBe4cmcBNN8nuvSZLLdFL-Rb_YdW4BnzvZNMB0iPGyK90ZFYPO0WG4Tltko9wmV1J3Msh6bVwZUb7ol6TMV3g2FQhQr-2sfVXyWy1OlS4u2yhCVa4X9NOPh9oiQM5WF_C9LVl5ETcmkKIbWLoZRAfc2VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا حوثی‌ها رو هدف حمله قرار می‌ده:
ترامپ: «اونا خیلی بد رفتار می‌کنن. اگه بهتون بگم تصمیمم رو گرفتم، اون‌وقت... حوثی‌ها واقعاً خیلی بد رفتار کردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73234" target="_blank">📅 19:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73233">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=RCHAkwL7oOf1onzazwyUCMzyiZmwkFPlCYrc6-zyt4AsAAHLjGsYbRnsIBCJ28Ax5mPz8URCm3azkM-aG_IEB8ZckO_-0EkYVARpT81G7PE_UpfoiponWC0ySJltCxJaR4kJ1EdnLI5AeMYPZmr28SzMmcFKkWyJACY-qVUVMNoHLQ5fYdA5xfRzTLxoDwTkV_7tZgobvZtFshvlH5ih1vgCHthrgjhlph3nSceZjk9vBoxa8x2AjffOx3JLjI3Y5LH3okepCz2eur_UGqb5YgHqYmpkaE-Fs3PAXex9LCW1eV2yxk4q0g8tIyjosX1J4MTnAG7RjoC8Ki3Yhtl3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=RCHAkwL7oOf1onzazwyUCMzyiZmwkFPlCYrc6-zyt4AsAAHLjGsYbRnsIBCJ28Ax5mPz8URCm3azkM-aG_IEB8ZckO_-0EkYVARpT81G7PE_UpfoiponWC0ySJltCxJaR4kJ1EdnLI5AeMYPZmr28SzMmcFKkWyJACY-qVUVMNoHLQ5fYdA5xfRzTLxoDwTkV_7tZgobvZtFshvlH5ih1vgCHthrgjhlph3nSceZjk9vBoxa8x2AjffOx3JLjI3Y5LH3okepCz2eur_UGqb5YgHqYmpkaE-Fs3PAXex9LCW1eV2yxk4q0g8tIyjosX1J4MTnAG7RjoC8Ki3Yhtl3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی، خبرنگار فاکس‌نیوز: «اشتراک‌گذاری اطلاعات و داده‌های اطلاعاتی با اوکراین رو متوقف کردیم؟»
ترامپ: «نه، متوقف نکردیم. ما بهشون کمک می‌کنیم و واقعاً داریم کمک می‌کنیم که به یه نتیجه نهایی برسن. پیتر، ما می‌خوایم جنگ تموم بشه. داریم بهشون کمک می‌کنیم و اطلاعات هم در اختیارشون می‌ذاریم. می‌خوایم جنگ تموم بشه؛ برای همین با اوکراین و روسیه همکاری می‌کنیم تا به این جنگ پایان بدیم.»
این جنگ بی‌فایده‌ست و باید تموم بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73233" target="_blank">📅 19:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73232">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=gnVuFo14Ryz573u2Edc5LS2h8hsiNko63Ngtc1LuqgNh2fa1ujb6LjxKfa7kTj_10qpOUB-fWmwfME6lANCwf_mZFnqbHZvRQNiQh74Nq_eCNdZUNfDK_F0DotEfJi0yF8d2q9g5eIxflzwLYONMQ3cM8uBc85Y0WHobFERdRGjTFFME-4-9l251QFvUjfhFFPWehji9AS-18wYpP2U0awknOULFyNbmq1Q4L6mv21bEuZnorTgViehzQPo51S5-Wov4yOCrnff0DGWZM8I6nf8R16OpR8vSIssjCid0JuERbKIKwFP6_AHS72AXy8zESUhP6DeM0zsEItlvLqcbpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=gnVuFo14Ryz573u2Edc5LS2h8hsiNko63Ngtc1LuqgNh2fa1ujb6LjxKfa7kTj_10qpOUB-fWmwfME6lANCwf_mZFnqbHZvRQNiQh74Nq_eCNdZUNfDK_F0DotEfJi0yF8d2q9g5eIxflzwLYONMQ3cM8uBc85Y0WHobFERdRGjTFFME-4-9l251QFvUjfhFFPWehji9AS-18wYpP2U0awknOULFyNbmq1Q4L6mv21bEuZnorTgViehzQPo51S5-Wov4yOCrnff0DGWZM8I6nf8R16OpR8vSIssjCid0JuERbKIKwFP6_AHS72AXy8zESUhP6DeM0zsEItlvLqcbpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی حملات هوایی نیروی هوایی سلطنتی عربستان سعودی، مخازن سوخت در بندر الحدیده یمن (تحت کنترل انصارالله) دچار آتش‌سوزی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73232" target="_blank">📅 18:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=j4uXEhD5y4_86sUkqqa_uTrcXe60E7alMvpMn2rc4Pr4b-IjMxQqgjAKdAN-rHv-QDrbx6MxaqdqPLYxxqMjfVa1M8ZweSAHVqmMf-hZ91Xg4zrFmGP7vMQYK53C3E4sV3gwffVgn1zxL-kn9bleXVEwP-BYgAl3OjDsXvYi1sJjVmVnQGCfd4zChu_A9lZkXTPjZOsecoxtiNIVKwzMGoSl3Iv9j7hk0RskSANriEoxZ666_OdIH_IyC2VTGBBr1FQcv2Kvvso4x4wCH2-vDkhkmn9D1Z8nbJNAS2Dd9FutSk4huAvFyybEFCMGePvZSsZlH7A7KrF_LlnqBUNIqWZalMOjfhbMwtK1fZgmZFZi79xssv6Mwtx8VYQZtPPnLQCYwPa08ykHmALNr23NYyydJ3b_WHJeyj_ey1vIBAIRSenB0RkaVbYRRUmj31vaFByDkEM8iXz8ORVBy4yMSHzYnqj1K1YIp3mECwIQBYpIJ8yLhOIaWn3Xt0i7uy0-zgIm-51cc4dH06sx7qQnt1BfMCt5FnocC0_ZGWV5GvYWfFFojRpFWsGsng218tXYZhpgt3f1UQvdiwkxMTRrUwAuE7C1nxakoP1_F5hWvYHf-Ech_jAtHUtT8y497rP-mVPw26w3gPJe0twexbug89xzNdepwbf6BFKBxrY44S4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=j4uXEhD5y4_86sUkqqa_uTrcXe60E7alMvpMn2rc4Pr4b-IjMxQqgjAKdAN-rHv-QDrbx6MxaqdqPLYxxqMjfVa1M8ZweSAHVqmMf-hZ91Xg4zrFmGP7vMQYK53C3E4sV3gwffVgn1zxL-kn9bleXVEwP-BYgAl3OjDsXvYi1sJjVmVnQGCfd4zChu_A9lZkXTPjZOsecoxtiNIVKwzMGoSl3Iv9j7hk0RskSANriEoxZ666_OdIH_IyC2VTGBBr1FQcv2Kvvso4x4wCH2-vDkhkmn9D1Z8nbJNAS2Dd9FutSk4huAvFyybEFCMGePvZSsZlH7A7KrF_LlnqBUNIqWZalMOjfhbMwtK1fZgmZFZi79xssv6Mwtx8VYQZtPPnLQCYwPa08ykHmALNr23NYyydJ3b_WHJeyj_ey1vIBAIRSenB0RkaVbYRRUmj31vaFByDkEM8iXz8ORVBy4yMSHzYnqj1K1YIp3mECwIQBYpIJ8yLhOIaWn3Xt0i7uy0-zgIm-51cc4dH06sx7qQnt1BfMCt5FnocC0_ZGWV5GvYWfFFojRpFWsGsng218tXYZhpgt3f1UQvdiwkxMTRrUwAuE7C1nxakoP1_F5hWvYHf-Ech_jAtHUtT8y497rP-mVPw26w3gPJe0twexbug89xzNdepwbf6BFKBxrY44S4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش جمهوری اسلامی تصاویری از یه نفتکش در حال سوختن تو شرق تنگه هرمز منتشر کرد و از اعزام نیروهای جدید به دریای عرب، دریای عمان و شرق تنگه هرمز برای رصد رفت‌وآمد کشتی‌ها خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73230" target="_blank">📅 18:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸۰ تن میوه به علت بسته بودن تنگه هرمز رو دریا خراب شده و داره دور ریخته میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73229" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/73228" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/patPdm-b9qTYQL6oaA276jkPlZ1XdWVexxGiGWnBRXsasEp4XSlMgpmsa_PSThkoB78GIS0-NJdlO3cwgspiLSAw5m3aEuUhj7Bv36BBcIik5iI3rULyPdV8nQ2Sq5XYrFlSZt-es_UaalZUU6cnZN13nnWsvcO3LeFpclRh5EfF7TShFAfrc6o1SUDUNKTuJJU56GVYnivs_jlYy2SXJFsJhCEPriq-4VsNmX6GN5z8VYToaTyx0Z0Fenp2vyvGiF3z75IgqtgSIswx4mjPTxcDmPbgWpOWH2spb-hWQ73wVOXRXvTK34FoNcVYTKfD38CoFz8192EXQayIlrLKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73227" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به صنعا، پایتخت یمن تحت کنترل انصارالله.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73226" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=DVrHIqvezRJ3GRlmrEA64p8i0bAJ-2gczGhElGLSgEQYrW-yRu81YCNcJg32bmt32-w8nBGLq9r3gN4yYg1PtQBKWz9AVUMdvb2Su-Nt5oXVmAj2zaiS6hxSuGBtVz00i2IMxnKkB5MCKg2qaDO3gwCWxbJHVmhIclyGkfKCUwHSDNnHUbeVGU8fhL-vp-ZOynl-arfcErytODLpSJyt2ej2GvMd9ghjUjj0ulITgcm00RSemV6YYfjRqAri3kToBI0pu-dBpi21jc92mpv7NePLQHe5J-clSuya0ltEHXSP9n49ewHT8aXTkAUyppD-m1_MTrGFor7R3_XMDbcWjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=DVrHIqvezRJ3GRlmrEA64p8i0bAJ-2gczGhElGLSgEQYrW-yRu81YCNcJg32bmt32-w8nBGLq9r3gN4yYg1PtQBKWz9AVUMdvb2Su-Nt5oXVmAj2zaiS6hxSuGBtVz00i2IMxnKkB5MCKg2qaDO3gwCWxbJHVmhIclyGkfKCUwHSDNnHUbeVGU8fhL-vp-ZOynl-arfcErytODLpSJyt2ej2GvMd9ghjUjj0ulITgcm00RSemV6YYfjRqAri3kToBI0pu-dBpi21jc92mpv7NePLQHe5J-clSuya0ltEHXSP9n49ewHT8aXTkAUyppD-m1_MTrGFor7R3_XMDbcWjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه شهروندان ایران کرجی‌ان، فقط خودشون خبر ندارن؛ چون بالاخره هر کسی یه فامیل کرجی داره.
آغوش کرج به روی همه بازه، ما هم آماده‌ایم از همه مهمون‌نوازی کنیم.
از پارک‌های زیبا و اماکن دیدنی تا رستوران‌های خوب، همه‌چی مهیاست؛ فقط مونده بیاین کرج.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73225" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#فوری؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73224" target="_blank">📅 16:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حوثی‌های یمن بار دیگر به همه کارکنان تأسیسات نفتی و فرودگاه‌های عربستان سعودی هشدار دادند که محل را ترک کنند و این نشان می‌دهد که حملات بیشتری در پیش است.
حوثی‌ها به همه «کارشناسان، مهندسان و کارگران در تمام تأسیسات نفتی عربستان سعودی» هشدار دادند که مناطقی را که نشان دهنده اهداف هستند، «چه قبلاً مورد حمله قرار گرفته باشند و چه نه»، ترک کنند تا از به خطر انداختن جان خود جلوگیری کنند.
آنها همچنین هشدارها را به خطوط هوایی، فرودگاه‌ها، مسافران و کارکنانی که قبلاً به عنوان مناطق هدف تعیین شده بودند، مجدداً تمدید کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73223" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrMo0aGdw93kGeIEwjG4erevonJ8AoE2uCgfw-olx5QA24kKcVF-XCOdfwp2sIh3cPDm5261xsrfsry4mk4UcB-Djdj7TD3CiGhsEzhT8P88R8azEj-yjpaeU2pFRfILAPoD6EmkqRZUK_6s4ZU4-KJivZsMQ7ebnmzqM7wOXy04I-DRlBhm9K7cHSOv4XtJGNxd5_p7rSDCUYmv0LTO6ZUgJFFeUTLhfZFRI88558fPng9lKs4YHPb7TYEvbL6v9YMjJRr9AENey9z2TbzdKMghPcJPY-Kzg2sW1Vfp6Y4heqfhNU0JWAlKQHSbeeug1YnBeDGmLcYqnZzN1VJ5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73222" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/73221" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kaw2i6qFJUIpTxSK6NQJmYwVDxy5CAN55e7A-dJL4ZElYz28JPzcANUf6JEQpevAGnjjwnDlu2tHlmb59m1h0VP76kG70TjKKwYc1njrlmBna_pU6uJlDpo_-CrtCWhCP-U1p5XWl4Ms6rd1bRZ_fI789klEGU9UYo0DStZNlFXI5xquJPlGWKwv6go_jVJDRCh_pso6kBZlEn0t3zM75P_71FAzAR7w1xXyPLGpYnvD2NZKem04agalv_wADbwGoK8ibTxPlPEAQxlRLICNheNQtU25IdG3_-VMcuGkXvIELu9Wd1PONDo7Uo7Fr5hfr6L82e2FZSzbUK6YSRXc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73220" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N8aCXv_ykFuqV7jA6ZgC0flBsItdKNdV2NKYS22wv-1ROmcLnIu0RnoT-pRW2J16ZPFMEit8pJ0DlSEX2uspbBbeS2hY4-vWndShKaldb_Wda72FTHJbWh61zsAb0-q8QczVJ7GAYM4sOeMWnnadMRa6DDr1qPd6lvC-pFaG0RdWlWN0dPI8TPJJm87x0my6KWgC7MQXhIBS26rGXQVTsY_oRWd2tjUNhIq5Onouh5AhyuTXS5sfGfTWbRDUnklzr7gnIUjVtSZfdKLibtJDFjAXWbmDDqYBLSv82ZwLrF0V9YUXRFCQ2Ksl63Ui-ZLkyLK2FARddsetwojgH7Ivog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش وال‌استریت ژورنال به نقل از منابع مطلع، ایران به کشورهای منطقه هشدار داده که در صورت آغاز دوباره جنگ، ممکنه نیروهای مسلحش حمله زمینی به کشورهای همسایه انجام بدن.
ایران همچنین به مقام‌های عرب هشدار داده که ممکنه تأسیسات نفتی عربستان رو هدف قرار بده؛ در کنار حملات ادامه‌دار انصارالله به تأسیسات نفتی سعودی.
به گفته این منابع، ایران قصد داره در صورت شروع دوباره جنگ، حملاتش به نیروهای آمریکایی رو هم افزایش بده؛ از جمله تلاش برای غرق کردن ناوهای آمریکا در غرب آسیا و کشتن ملوانان حاضر در اون‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73219" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=AsZNbrnoR7B-LgxjB9VFUk40c5sUm-Loy-X_4TkJX1z409plQYbtRgj8riDFwk51vSl0RcQ70pwKAS7wHekGDvhfp8Hv9ldD9dh978ierqDY_DM7r0xVTftG4pUYINv4zCuAc8SYFads0xiBtAMIwjzw67qogq2L_ilMN7MxtDBIONqZkdOQJhQ7xBa1EHSIbQ7_5NCT24IAQ_MJjTQw8sHtpSqJBGptqUkpnsDLhkwx1Z0eE35l85oJiVF8KG8o1sg-MEa-1TrEKN6nlQydCXSM7Yrlt3gPXALjspFmut6GqsttAHHO77F-hwq3c3JBRR7HrSJknhvpFVDJrA5MDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=AsZNbrnoR7B-LgxjB9VFUk40c5sUm-Loy-X_4TkJX1z409plQYbtRgj8riDFwk51vSl0RcQ70pwKAS7wHekGDvhfp8Hv9ldD9dh978ierqDY_DM7r0xVTftG4pUYINv4zCuAc8SYFads0xiBtAMIwjzw67qogq2L_ilMN7MxtDBIONqZkdOQJhQ7xBa1EHSIbQ7_5NCT24IAQ_MJjTQw8sHtpSqJBGptqUkpnsDLhkwx1Z0eE35l85oJiVF8KG8o1sg-MEa-1TrEKN6nlQydCXSM7Yrlt3gPXALjspFmut6GqsttAHHO77F-hwq3c3JBRR7HrSJknhvpFVDJrA5MDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌ها در ارتفاعات چاه‌احمد تفتان، با گذشت بیش از ۷ ساعت، همچنان ادامه دارد.
به گزارش حال‌وش، در حمله افراد مسلح به ستون موتورسواران لشکر فاطمیون، بیش از ۲۰ نفر کشته یا زخمی شده‌اند.
پس از این حمله، بیش از ۴۰ خودروی نظامی و پهپادهای شناسایی و رزمی به منطقه اعزام شده‌اند و نیروهای نظامی همچنان با خمپاره و پهپاد ارتفاعات را هدف قرار می‌دهند.
این در حالی است که رسانه‌های حکومتی پیش‌تر از پایان درگیری و کشته شدن تنها سه فرد مسلح خبر داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73218" target="_blank">📅 15:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrFc8sgK0NZ6rck1eY1rMyOuGsCSMZ0HSuD9bhPuQoegf0kRPSoDMH3TG2ivD3cURbXBcNMU908zTMpEqdYVtmWyoTmBDytBxgSEHs3I3yA8_o2pd8jie7hlJgeBF3RXIjsFlO7TUXO4ZuEgcYM92O3Io5k_QuouJC5m3EJLyHHTiwDOnsaEsLyUdWntArXdcjEOCUaTjKEWsXkNKCsMlMODEMsId6k-1DcWZbPmwotMtPthi4oznvTSr9l4_0U_yXWXfZ9QkansYqg1Zgmcuxs09tFe2hWBngwOd72LbPGa1Bbzn8Tqq1B6FjmSLFZzimLk_FXLO8PZFEEqCE-dWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMXT-cKD0XY_jnefXj7Ad_Wk_kYjWC4Re041goa2znMf-T-P-IMV49FhIKOCXWccRFMbQJzXawprSWHPVk2TQo6AzZOYfYwiDBDLX_VERJEdHabAIZPJ4NDT4vegDX57_S0UbghApaIDWNxBaon_9adpi2YpWJHSwwyq5NS6Y3-8rNun_FFdnQGgmWx5rsOuiSKDjFT5YF9TBBjHF8dA8DS5QQSVTRe-qV2SIwGrZ1j5dcoyPtMk-GmX0YBeHrKqB5jsD2aAZ3rqjYZ6yy6uNceGdmlDi1Sx-4-Xs7QgVU8HyiKGWFP-bCbN_mBv5QIrW-y3pel9gT2HkJaIkWCFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcyieCJV2nHVfUW_ctufEgC7cTy2btKBhaiv01_8uFwNtshtlaHABNi1Hzbqrsu_UNjXjxfE4dWyMYIbdn9Zkd5QW-dV82bPisbKDyQCxN3xbVaNy3T-ldQe70tuK_L54crLSt2hweMr6yM5aVqKLy7PYlDjQ1CKJZk8li9_v1kue0_5DA1YlkywkyjsDx_F5Py_89rqV7cHjgANFfNihNolcqawd8sS7DNeFPIHdZXUMQgwha3ocjdUTaTBnHqd161-4UcAZ1acVx1zzXqakvCyp8RNPeA7XgoC01K3UgXJbicIdMJhjuh0n_E2MAuob2JmbY_xRxbPsMrkfU8cpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=muv5jeQhVI5JkhyFezDqrhgbL6t7FV19ZoQMvZ2ZFE1VsUw2FqWEuxbC_tZnsOD0o4eJ2NFDsIuSdklqI25X2ZNIIx7Ub-hQBx4vsZWlpty2mkY0_CAovCammcQXGO_C57dIBnBZ7eP44g_pAeOL-XZkjNJ6OBI-8u2gRQCXYbX4fBtx4rEnTy8FSKXcGst-nc7wDU-XURPXG0H_FVU61C7EfpSwgImaWOY3IFWusQjSyRkEKBr2-C1rQHFkUN-adn2QmxLG7om4ddXHiy-3Jg-rrltIVrRcHm-Dr6So6T06-jyVdlAlJlw5gx0bkPoy-Xs9QBjLnS8RG4GRuECWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=muv5jeQhVI5JkhyFezDqrhgbL6t7FV19ZoQMvZ2ZFE1VsUw2FqWEuxbC_tZnsOD0o4eJ2NFDsIuSdklqI25X2ZNIIx7Ub-hQBx4vsZWlpty2mkY0_CAovCammcQXGO_C57dIBnBZ7eP44g_pAeOL-XZkjNJ6OBI-8u2gRQCXYbX4fBtx4rEnTy8FSKXcGst-nc7wDU-XURPXG0H_FVU61C7EfpSwgImaWOY3IFWusQjSyRkEKBr2-C1rQHFkUN-adn2QmxLG7om4ddXHiy-3Jg-rrltIVrRcHm-Dr6So6T06-jyVdlAlJlw5gx0bkPoy-Xs9QBjLnS8RG4GRuECWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLfGkh4T74jm9gmKKc3Hg-usW2TeoNxNQBFr8fp4x3MqjvT6rcXZAfiw959c-MRyAkwcgr47_e1mrGXKFfsQfBUWgvHwSgKoldaGbEx7NvSU0wNz2WYdFyIs2stFyVJp_AQ27XInukbUe8m1tDFnBGXxV_sIG_pEe8j8wZgzRRge90ImXjsxF0kIRjgfWQ6CJEi7fAaH5UHzA_I8fNqD1ytQZHEyODdEKNY9sj2yPIOz94o5vfj9jyZPA-GrAL1Qj4BkKz_xrIHSFAU407iCTEJkFa3PUwXgmvOXrmAcPVtK2Fysfrl-bRynskvOMuCuDWZ6wFv9r00BGckWQSo9jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=MYcjdbPunXF7SmbfymagDcLy-GkhpM9FVuVmq0LvvSEGfPaXGtueMF2GLBNsUzqm8Wlfyp4Cjao1JpvBdc9LdaAr9cuGt0lHjs3FV1ZxLjfT9OWW4XrVpO8s_jKaJ9nn6UT0BChbelbA7fSqhFUM91VW-tOrN3zJbkjqI2HMkZdbRxuLsYrTqF3ORqRfBZ7FjUwtp1KUR5dx5YXL9yIjwuOIQ0YhyZ6pYihdcQAIiT44Bq2lf3aQU7hk54a2Fb9yEolain4Wtz7NIEBJ-ftS5n-YDI7_GzHDAGQLhZ9oIlGy9-BfVN82E1jFgPb-cILPOeCEGg_BoCj0fKDlNhFbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=MYcjdbPunXF7SmbfymagDcLy-GkhpM9FVuVmq0LvvSEGfPaXGtueMF2GLBNsUzqm8Wlfyp4Cjao1JpvBdc9LdaAr9cuGt0lHjs3FV1ZxLjfT9OWW4XrVpO8s_jKaJ9nn6UT0BChbelbA7fSqhFUM91VW-tOrN3zJbkjqI2HMkZdbRxuLsYrTqF3ORqRfBZ7FjUwtp1KUR5dx5YXL9yIjwuOIQ0YhyZ6pYihdcQAIiT44Bq2lf3aQU7hk54a2Fb9yEolain4Wtz7NIEBJ-ftS5n-YDI7_GzHDAGQLhZ9oIlGy9-BfVN82E1jFgPb-cILPOeCEGg_BoCj0fKDlNhFbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=Ax5xL1yEGoyX0qZ9jpk5eqhFUkggiI-naSEb2f_T3ui_arMw22Q_uhKCizU1eWECjwk8wHpiLuLxPYEEv5PEP20dJ8vGmXaX92f8483yb1H9qGreLHUBXj5uv1fL-pUAcuqe5JW94MZ0grY7U6fT2JpwW_jchfFY4Vq92477bGRrvvA6yvn0NvWOsvyj-_gYszzBAtdrsXG90yjzQjob51qpVYU2CulCEP4xCubvHFB4W3N5gQwjvjkv1rrCUu89FtJ37BxEKAGNxf1WRxWlH9W6ri8xa2eyr5F6t3RMbHjZw9b7vgKUL93SC2JDf8k9_FzyfGVW4ehT_zNcIYgZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=Ax5xL1yEGoyX0qZ9jpk5eqhFUkggiI-naSEb2f_T3ui_arMw22Q_uhKCizU1eWECjwk8wHpiLuLxPYEEv5PEP20dJ8vGmXaX92f8483yb1H9qGreLHUBXj5uv1fL-pUAcuqe5JW94MZ0grY7U6fT2JpwW_jchfFY4Vq92477bGRrvvA6yvn0NvWOsvyj-_gYszzBAtdrsXG90yjzQjob51qpVYU2CulCEP4xCubvHFB4W3N5gQwjvjkv1rrCUu89FtJ37BxEKAGNxf1WRxWlH9W6ri8xa2eyr5F6t3RMbHjZw9b7vgKUL93SC2JDf8k9_FzyfGVW4ehT_zNcIYgZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=ZCqdj9Txf9OhkeJlIIdfMREh1uGQbJcJChq_UrQKJEYNCOmCKn7OzFW3IbvjurAOvC0Wm69EluIwNfUvK8CU3xbYJQBpzEo-sFUKT8oZwL-bRNL4dOs32ZugpMkwVwDNN7y4GMW6kXNhgFXjlZZzstFB2KIAD_0lUEklA9HOyuWQYmjrxnv63LwF5nCo24Y1htzN3JVHBea_eh1DazjhTqD8t2OeMZkzxOX0g9NXolsIgSO0IIWliNc4kfodBTL2oSTxI-plIDCg1DWBc0-9L3ok5Di6RC00N94lnPcwqkKJCMeTF97VzMvuQkDbMiJuyoNbSZVThdBdtDoyOsIIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=ZCqdj9Txf9OhkeJlIIdfMREh1uGQbJcJChq_UrQKJEYNCOmCKn7OzFW3IbvjurAOvC0Wm69EluIwNfUvK8CU3xbYJQBpzEo-sFUKT8oZwL-bRNL4dOs32ZugpMkwVwDNN7y4GMW6kXNhgFXjlZZzstFB2KIAD_0lUEklA9HOyuWQYmjrxnv63LwF5nCo24Y1htzN3JVHBea_eh1DazjhTqD8t2OeMZkzxOX0g9NXolsIgSO0IIWliNc4kfodBTL2oSTxI-plIDCg1DWBc0-9L3ok5Di6RC00N94lnPcwqkKJCMeTF97VzMvuQkDbMiJuyoNbSZVThdBdtDoyOsIIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=NbWBgQNiecBIc5OlnDI41vWzWUnsLfMUiC1zeSa4WYScIVoh8EUM6z7SCw8aAQv_945Wr-vn-RHWAOrg1JCF7LFeF3Hs3jHaMuPIDr8Rc6yMctoVeAMAxAvfdpcAfj23MtCPOnfbAab_yt2D5d-od7sJjErDJVQb19IULo6HjQrmi54edw2I_t9AbRZVz1uH9ahKcfAToEqhz6yq1g7AxpNMDvJ5jsOEYjK2cazNny0xm4Ftqoz5NXJ93velyYIFodIndvqcWZkeyZAm1LjSo4-I31cy4yEfroX0tn1y1EOPhKgObbc7mn3WuLNNHWfHTjjcjgZuiDklTmftDOxyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=NbWBgQNiecBIc5OlnDI41vWzWUnsLfMUiC1zeSa4WYScIVoh8EUM6z7SCw8aAQv_945Wr-vn-RHWAOrg1JCF7LFeF3Hs3jHaMuPIDr8Rc6yMctoVeAMAxAvfdpcAfj23MtCPOnfbAab_yt2D5d-od7sJjErDJVQb19IULo6HjQrmi54edw2I_t9AbRZVz1uH9ahKcfAToEqhz6yq1g7AxpNMDvJ5jsOEYjK2cazNny0xm4Ftqoz5NXJ93velyYIFodIndvqcWZkeyZAm1LjSo4-I31cy4yEfroX0tn1y1EOPhKgObbc7mn3WuLNNHWfHTjjcjgZuiDklTmftDOxyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcVzDW5cklyqNjleZqk9B3nQHSBqvnTYMtts_5ajDx83vOAOhh7ciO36kVDJDlqBNIXs2lsNsn3eCxRP1LNR_qoLVYD8tQ8lUpiruS7MilJ-3h1ACIXJ06jUb1KryXHeVbz9APO84W93hmm2VJwh-exqoatTdOKE1qcmUNd7_U7oL0FUx8UeTCSw0aFaM1OIN1OxzS9fl8MKArKiR1_MttDduGgKyuL20BMke8Ruc8I6_xf1iZdR1x3Ek-oX9PpjlgGY6_GZG6k_j1SmLF1iKPBdBnIbKYeUVNedcrlrUi3FIlqtPsMUHhKKQObEK9Aldji6VGAhEGjDthWjnw8prajs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcVzDW5cklyqNjleZqk9B3nQHSBqvnTYMtts_5ajDx83vOAOhh7ciO36kVDJDlqBNIXs2lsNsn3eCxRP1LNR_qoLVYD8tQ8lUpiruS7MilJ-3h1ACIXJ06jUb1KryXHeVbz9APO84W93hmm2VJwh-exqoatTdOKE1qcmUNd7_U7oL0FUx8UeTCSw0aFaM1OIN1OxzS9fl8MKArKiR1_MttDduGgKyuL20BMke8Ruc8I6_xf1iZdR1x3Ek-oX9PpjlgGY6_GZG6k_j1SmLF1iKPBdBnIbKYeUVNedcrlrUi3FIlqtPsMUHhKKQObEK9Aldji6VGAhEGjDthWjnw8prajs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=WI8lnpuwm6ei0Gv6DQikSt1E0nXQKpzNg_YKAvbM2fklHSodYTEd80Rng2zsNdq08PVL4f6IdtXb_sqCX3pCZoxwFeKb59nUX7uHrRJ_dpB0PiIUilLigAHqHdUpJMDZOoCeVdPVeCsJ5hqK3S0E1xyIvrLd9SOlDEd_ZcOwWJtnQFZGB5_2_3bmy9liwO5NhVqUdravUAImCTpoJxL3f-KbXrEtRshB8Iavx_T6NgWWqn5NAtDOHj6vzkmze035aaq_2X35fJ0r2vL_aZZoF3FIa7-y0hU73WaxA3vf3UFo7utlURtMeX6mv8tHwKknLCnNkiuTz-0OUlWUvPr1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=WI8lnpuwm6ei0Gv6DQikSt1E0nXQKpzNg_YKAvbM2fklHSodYTEd80Rng2zsNdq08PVL4f6IdtXb_sqCX3pCZoxwFeKb59nUX7uHrRJ_dpB0PiIUilLigAHqHdUpJMDZOoCeVdPVeCsJ5hqK3S0E1xyIvrLd9SOlDEd_ZcOwWJtnQFZGB5_2_3bmy9liwO5NhVqUdravUAImCTpoJxL3f-KbXrEtRshB8Iavx_T6NgWWqn5NAtDOHj6vzkmze035aaq_2X35fJ0r2vL_aZZoF3FIa7-y0hU73WaxA3vf3UFo7utlURtMeX6mv8tHwKknLCnNkiuTz-0OUlWUvPr1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyYsLusbk5YYC5KYO01mHVYA4KlijE3IkvdfGKnJVD1TEWqjNCnQtyLkgEit4NXYTbnWdOzoBenMmHo2osaBTkr0I3kFV8IalMgEYOrrcTPTPh42DBrA-RyL_gg4SUk9q6Qe2ExdHhZ8s9HFWrGqHmam8rKnTo7l4bGu4_xfqtobxpbZHDKvpZ1BWONzs15CFxg3SoSKdmVAXI5LjTQaCkEBGDdS7Oa4XbTa0AOjRCTxXPvoz2gYB-r8fEOMA7orLWDuoxXkR2wD89KIK41qb6VonCDclrfgePy-9LsfUBkMW72oOPMYwWrJ38he-S7NK_ogQBUq6f9-TLOTvg_3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_zgEXEqV6rF9-Orz3NlbeSYKnq9HgAOPa6IqIeIguVfGEKBVOEwIdpP0gNoqkq2Ug8iyP9IM8rlD--CVTvjVFiBtsSgTA1qj2u8CV0F4DOunY3mljt0JyrLvWfKQLczmqz-6UJehg5yAniT33Ua1LsVGOOxGYX8KTtV1hzWJ-a5ltXUV9Ht_A5a5MWHRP1FV0_BUZbUPfLq8IoSMtCO3imuEA1odfjwSmAq2ROs76tL5g3A-qYWyuww1AG1bmfXctdaiFsTAur5EK_PQH_NMFW8HKplqFt5G1HR8dtl0mHb4CokLilFGALdeClFzOPjCJ1oCQrA9w24ZBEtoVJt2SUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_zgEXEqV6rF9-Orz3NlbeSYKnq9HgAOPa6IqIeIguVfGEKBVOEwIdpP0gNoqkq2Ug8iyP9IM8rlD--CVTvjVFiBtsSgTA1qj2u8CV0F4DOunY3mljt0JyrLvWfKQLczmqz-6UJehg5yAniT33Ua1LsVGOOxGYX8KTtV1hzWJ-a5ltXUV9Ht_A5a5MWHRP1FV0_BUZbUPfLq8IoSMtCO3imuEA1odfjwSmAq2ROs76tL5g3A-qYWyuww1AG1bmfXctdaiFsTAur5EK_PQH_NMFW8HKplqFt5G1HR8dtl0mHb4CokLilFGALdeClFzOPjCJ1oCQrA9w24ZBEtoVJt2SUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=IDp7Qfk9kFUpbLVlKWPVPG3dsfPW3bAkYp6tFPi4wczWStag-4lZWISJiLdaO9dia_jgFLF6FUdl_zVKazx1gyjd12pN6z8iDsqA5FHMIibAXuRxltjjkgSr1JmXnaG6xk3NWhIJi-Zzp9BeNXazvIG-WIiZwxedxisTW-96BJRHIrtwleG4JsL5es8rw46eLiJF1h_2yvWDPwL4axXIFBH5Y6EWN7k1HZ-XnYWbLNkCtKLeaSFXAviWw83a_14k5BrQD7HtzXwMzTORE-c3lKlg5dp5eO3DOc0_GtSbSbLW8kwgx6khHvz9lE04O9hP_6p1aLvbuzDn5C5KhD8m5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=IDp7Qfk9kFUpbLVlKWPVPG3dsfPW3bAkYp6tFPi4wczWStag-4lZWISJiLdaO9dia_jgFLF6FUdl_zVKazx1gyjd12pN6z8iDsqA5FHMIibAXuRxltjjkgSr1JmXnaG6xk3NWhIJi-Zzp9BeNXazvIG-WIiZwxedxisTW-96BJRHIrtwleG4JsL5es8rw46eLiJF1h_2yvWDPwL4axXIFBH5Y6EWN7k1HZ-XnYWbLNkCtKLeaSFXAviWw83a_14k5BrQD7HtzXwMzTORE-c3lKlg5dp5eO3DOc0_GtSbSbLW8kwgx6khHvz9lE04O9hP_6p1aLvbuzDn5C5KhD8m5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fXBDRJq6ZNuHNdqSiwELqb5_91YoGRO581oi0F8wNjfJqQ7dSNLeGCCmud2c4IkdraJQzaVz8fI5tjbSfdULfeFTUFvjhTxceu0U_j7vkTU1l7-_-nxD3khT5pp95vvIKggAWynwWhdq6zkbLvYf2aBCxlF37oJiZUibSzDYLJjkgU3vD3NWbkO-5K4U3gOZ7Suq8BKL2a-3D2TE0zcuj3EKYqE_tOQcTqg0a9H3PgPCDg6JkBhsdVAq-VTmCgBtr3WA0N3g2IbrCY5skACXCEyw2hweMj91HA-5BDgfuljwzFA2yst7Sh4a2uNjpzXxjrqeo5E2oCK789lMwT_s6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Oy6iZvgv2lNQ2lQXgMNdnbZR_fz-XocIcARGqJ3tb5EiIFuf6aIV7K0A-YTjVZbPqB_WXJl8AlvM4N2csBY11Cckcg-UmdL5pxPHgEfliT8zDiyZo4XVO77n_y8olC8_RKvvhNCjzpUZyq2C7MTWmVvHc1K0pZTW16J7TK37ZwkjxXs42PVgQW-qjyepVV1w36eFeEGUqtuKWmPaJcZHWg-llU3OclyFKQIXDWgvyIdVnZUhZAehletluExLcDxMzL8s_jsF-u2YGQlTZGIPcpvA4xCr0jBsjDt_UszMUTL5OA8C8z92FBwsqtG384ZdiARGvFRAwgJbzojGDYcblw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=OadTDdPAywPC0yGNr3_rBmNfvxBmSH3k0MpWErDDGjdvt95KJDwjsAXWEFBY6FfeD3RTi-Jg29dRQ-N7i0I6NVFeVlv-3Mk8pixcOQS9ghhbYn58mXU33NKLPYkUTtNI_gSJFyfG7Kz6rtAtTTX2_I41SCvOu_9hXX8H37AqqA8i8IBJn3Hx6FvxiyWbHw7TFhA18aseragXRWEWqHMR2bIdlVEF2uTGTtRuGDwbSsLtOjQa4r9GQjTdF7d4_cahbnkBzpTfU3whGcwLw1KoVik80Xa2BVhbHkczVq3qhjOLr75omLKmmFuP9pBprMuEklcmRep0ht_aFScCn-jvRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=OadTDdPAywPC0yGNr3_rBmNfvxBmSH3k0MpWErDDGjdvt95KJDwjsAXWEFBY6FfeD3RTi-Jg29dRQ-N7i0I6NVFeVlv-3Mk8pixcOQS9ghhbYn58mXU33NKLPYkUTtNI_gSJFyfG7Kz6rtAtTTX2_I41SCvOu_9hXX8H37AqqA8i8IBJn3Hx6FvxiyWbHw7TFhA18aseragXRWEWqHMR2bIdlVEF2uTGTtRuGDwbSsLtOjQa4r9GQjTdF7d4_cahbnkBzpTfU3whGcwLw1KoVik80Xa2BVhbHkczVq3qhjOLr75omLKmmFuP9pBprMuEklcmRep0ht_aFScCn-jvRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=UaFozR7otYlrRMUhXlWLlGEzpQzaYZoMTT5h6dtbinE6JyBu3L-wPJIZRHP6UYdESUO0aPEbOJwcWIXhm7us0m58IFsmZS-laxKnH9SBiq3PG3TdO3tAXa8qozGa9LmMqP2J6SIhv8I346DHsNRKwvn4MdBEyqXQErriSDJdIYJcY7x50NvGQJzl-B6zgBPyzjsGp7m2Jd-ue2GeCb8bn4bzwW2ozzuHFHmzM4u4pCrduAz6YoEdY4rJg8sJf68-Txpb4Kgqwmy4jvLI0QicXTL_iYN-OyNTImUMpsADYgu3iPdSrOlXFfF_f487XyECmT7f4QNifXEP21vCvGa7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=UaFozR7otYlrRMUhXlWLlGEzpQzaYZoMTT5h6dtbinE6JyBu3L-wPJIZRHP6UYdESUO0aPEbOJwcWIXhm7us0m58IFsmZS-laxKnH9SBiq3PG3TdO3tAXa8qozGa9LmMqP2J6SIhv8I346DHsNRKwvn4MdBEyqXQErriSDJdIYJcY7x50NvGQJzl-B6zgBPyzjsGp7m2Jd-ue2GeCb8bn4bzwW2ozzuHFHmzM4u4pCrduAz6YoEdY4rJg8sJf68-Txpb4Kgqwmy4jvLI0QicXTL_iYN-OyNTImUMpsADYgu3iPdSrOlXFfF_f487XyECmT7f4QNifXEP21vCvGa7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73196" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=oNzvl5Oagx9IeBPp__SBfPBtdBHlugIpwYOR8pi9vId8Bu_4E7A5DYPLaponw4G_swV62exNPQoKtjE0W9gmGD8461Gj25hdHY53YZWWNN4wJFWVm78yWp5ZeErsRqF-HWD3nKSdli_y9pX-PpkzB2zyy4uyvhUeaP35EQ0eN6mABHDJOrkXOUt2JIlji2QFtKHZJlw2ncfkVzoooN10DDKv0xYZo1RHcOGXPEq-9JLEwbnTc0Xyfg2cA2-aem-NSCzecTlPga7MHjXZNNX2Eip7HY95SxseT8FaQkvkQofFuVhaV3llF8wKDjv2pPCr9ygIDIPffxP8d0C6CyvYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=oNzvl5Oagx9IeBPp__SBfPBtdBHlugIpwYOR8pi9vId8Bu_4E7A5DYPLaponw4G_swV62exNPQoKtjE0W9gmGD8461Gj25hdHY53YZWWNN4wJFWVm78yWp5ZeErsRqF-HWD3nKSdli_y9pX-PpkzB2zyy4uyvhUeaP35EQ0eN6mABHDJOrkXOUt2JIlji2QFtKHZJlw2ncfkVzoooN10DDKv0xYZo1RHcOGXPEq-9JLEwbnTc0Xyfg2cA2-aem-NSCzecTlPga7MHjXZNNX2Eip7HY95SxseT8FaQkvkQofFuVhaV3llF8wKDjv2pPCr9ygIDIPffxP8d0C6CyvYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/viQOmi6TADQriLrpdL5De3AqwunePn9jWMCsye5v2dnFBi5uzarhTqCGfDrjBthfij8WY9bLobkSUO4IznlmGWORoD7GS4s1_ChIVhgCsG_GSXUeMGbKt4GRKDwLbEb7yO7VWAhjHCiY2SpivbXeoXUWM_e7pLB6hoR-1JmDhrybb31n1uVUkUkvcs6XtZ2o8-jE7AMucbyO7qruX5L1-Y0pwpHJVMjBrFFuCNUDJrxJHO8tG6il0Hfb3U8pqNo9BYjUNoD5IXacVEWdf5IGDonl3FsSYG9SfvsFTe3z4kjWfn05SlAZqpPHAN_2tQiokY78T_2_l7l4gnZXHxiReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VEatvqwDbnt_WdqO8IUlS6Xt-OuEZlL-2_RS-d-R8plUzZCzumASG0I4zuyABE0hbVNOdperL7qcce9b1SXQvsniy6LwteJMkPT9rOuMK6NO1Nanp--_-mkOUmFL1GJe3x2MU5avC1M1gQp3f7QgEN_k2SD4YAq0izNgeCHnJ9y4iycoeLfaq3mQyz9YUSmqLpxUUW5FruCJvZ9rhVqCpFasheGsXBHLMHuu7FH_Cyarh18GGz_lI7szJjzO39ji9Zitd50TPc70C-MTjd6DImY1Vyv_La39A2bLFXNfEXKav-8fAJa6l0hDasTT3A75jQoVotINV09UviHJTGWZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rwd4xSWTMZbRJxEtoMtOLb6CytI-L5ls224B28Q_YOGL1ucfz356L4GVEyes2Npgx2iLXC5mMCFL87dCyZ613wx-AQZvNee_97l3LPVNgmA3wR9oJuT3TQJ6afKT7t_NpFOL139gF3AyuvU0i-VmmZKkpRvRcLckvl9l8SXBn6DOsd51f-wG19uvzJRYydLFTele9pnLejdV0FXoqwE7hLIcC7O3ReYdz8XV8-OIXReIDnql5iKqT4ZeWIFpVNMm2kAcat_59_NNV05lPMKoKsq7-Gy07WbCkzcyE85EGTnXF5g_jWSnksgtscDbFjXn7XcTq31McJ-YJRfnTrrUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RseuLbs0v6FYqIs9iKncB8D5caui5DAK5rLQ6qNJfvH8CDc_oXHviMFH0VVjW5aOtzjnfILKhTfW3r9cwKkM_kRJAYoValotlx3S-PrUnqUsr15qn1kAnxHQaNyTo9j0p-21W_pRfQu2hF08Ts3O878xNieh506fB7-_G0AHZQbrjRWw3RddQHH5edLw9AJpRJ36PUXp0S_y88ZTjnVX5EI9JwswNbqlsBd6iFzsdQ_PsvdJNN4CWwrMoZvuc6hnv7rsOQBHmuLbRVF1-2ONJ0ukx8AfohPGQu-rJkRqmFBznAtfRcue1y-i3z9znqwrBIl9bDKWTLeR0jqnRaVs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cHFmfxegSyoVm-toRsIDXNpWCY32ww_4PNiAD51omgKtvb4bqcKKGH7_0ggsK6UWgv12esKLapQYYnpmmNDeRGoluDpNRtBeZFy-5Bm4NT78NoRP4YVFBqigc7sMQhdtgqwTYqECsyM4ZjqlgLpH9ixhQZY6VxAy7JlyYyrQCcVT3ZYbRNTSQHIvR09f-L20cdAnCCsLVkat2j9T966DF_1maxZ-Ld1F0kj1QgToUEgtrVAQOTM-Kvm-3093V_2iURRoZNWV-y5LfhtBqnDtKFQpGr5_pL28UDX3vv0xIt6pW8Ojzz4RBedDtuy-eK1s68pDhwEM3TZPuj2kpc2Nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CGyULcC34c1YWO0Ji1_cPxs4zme0lq0P7JxD-lfpbYshuv7FGQ4KZCcilBdILeinRJVuCZHwAP-Xbx5akFf8QebyCII8l5PfDYZNZ0gG9YwWyNxSWcQB2OV_-tcM8_H9A4woT3HAgqb2sRk52785UqRfbkJoTftNWtgZv6-Gqtfo7YDLL-77FIkD88CzKCgRUlgIGqQ4wVy1Z9EG_x8SqBmeN0z7pt4J-mLNlA1cHA6vu3hhzOUoeRO9F4yAMsPz6X5iBLPwLL-Y_luHXaStayZ1wF7Qh2uJTCq0FHPdwnJOCbgmj7pmj0Q3e0_sefruu4ZmXdO2Q2jrWxvDXOYDWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=OvXWFFc_MowtRc5bzV8f15DjBv_ar9lRItUZiP133V_jDwgN544OOfS0KpaEskjX2ht3Y1PCYwfrLOcUN1Bjbj1CCYIgInqNoLU_N-liCEjKbAcjOmNv2kJkSwGQ5px-0x6OgndqPjA66GmETAB2gcY0zchT_cdpmT7cevnpy4HYDq5E47-ycHytIjtDQuElZDisIEgY0bK358dK8dccN1j-SyUrpEnRzcLJYxGYWucUZFlQaHCFN_sirPmufPsPIKZSLIujG3uYWjbKoSPQJPD6FDf6C-Zr9VHb55wZdaYiupZ9YQTpnYzwoMwSxe2t69WdCu5kDVuOdzpieHzEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=OvXWFFc_MowtRc5bzV8f15DjBv_ar9lRItUZiP133V_jDwgN544OOfS0KpaEskjX2ht3Y1PCYwfrLOcUN1Bjbj1CCYIgInqNoLU_N-liCEjKbAcjOmNv2kJkSwGQ5px-0x6OgndqPjA66GmETAB2gcY0zchT_cdpmT7cevnpy4HYDq5E47-ycHytIjtDQuElZDisIEgY0bK358dK8dccN1j-SyUrpEnRzcLJYxGYWucUZFlQaHCFN_sirPmufPsPIKZSLIujG3uYWjbKoSPQJPD6FDf6C-Zr9VHb55wZdaYiupZ9YQTpnYzwoMwSxe2t69WdCu5kDVuOdzpieHzEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=EPOIKtvCB6RWeAL521VfDpnsXLEvo8n04U6uJj8G-mlX2o9MUGwA8L8XzliWNUX1oJ7s5WgjbndGrU2tgkwwP8Fyy3RV0Jdq3-xAF7iJuePz_ndEIIYi-8dz9Xa9Xr2AmalNR7k1Lhz647qSOkWiAbMzd8KJoZ6LRj8hD61jfZ0otIJLP0P4_-TCXiikf_Zp67t146RRP0s0MaJk4uLdH7b1QqHLxw8vQu55OCErgQFcByaqXtfv_CP_8wXAZVPHOXEcscdms2gPsJGLzLzejEzI6sfUTVKZKRROk24p4RaV3srQP3FrZTOyke3-H6yV4KVVHQhv_sjnBtWdvifLtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=EPOIKtvCB6RWeAL521VfDpnsXLEvo8n04U6uJj8G-mlX2o9MUGwA8L8XzliWNUX1oJ7s5WgjbndGrU2tgkwwP8Fyy3RV0Jdq3-xAF7iJuePz_ndEIIYi-8dz9Xa9Xr2AmalNR7k1Lhz647qSOkWiAbMzd8KJoZ6LRj8hD61jfZ0otIJLP0P4_-TCXiikf_Zp67t146RRP0s0MaJk4uLdH7b1QqHLxw8vQu55OCErgQFcByaqXtfv_CP_8wXAZVPHOXEcscdms2gPsJGLzLzejEzI6sfUTVKZKRROk24p4RaV3srQP3FrZTOyke3-H6yV4KVVHQhv_sjnBtWdvifLtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=c3x6TJZzMuQxS3x9h6-SYTWgcROIxgf32ELjMw0FKwVK-lQCb3VomenmYPKAV9RgoOZqEc9J0k35pW7klj34pA5yb5ExgcRMKWMf-uoZE6ambDhTRxel_WnH6eNQdYM4qykz3HyGRJD-6WbUwsTE_7YkTMMnkk_oLDKtK3mx9Ki4nEflJVuvZd4811EubgbI0KOVTI3zmHuWj-uVTQQyBo-X-_oZH-1SCYiG3_M6z3wsRev2KSoRRByHkSpXlN72HSdzngquj1mWUUubGf6AMV4xsv9XAiguESBfG0AysKCT2VtGOQvhUhrDs2W4Gm1rNO4YbogPiDmmszUAa-Umlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=c3x6TJZzMuQxS3x9h6-SYTWgcROIxgf32ELjMw0FKwVK-lQCb3VomenmYPKAV9RgoOZqEc9J0k35pW7klj34pA5yb5ExgcRMKWMf-uoZE6ambDhTRxel_WnH6eNQdYM4qykz3HyGRJD-6WbUwsTE_7YkTMMnkk_oLDKtK3mx9Ki4nEflJVuvZd4811EubgbI0KOVTI3zmHuWj-uVTQQyBo-X-_oZH-1SCYiG3_M6z3wsRev2KSoRRByHkSpXlN72HSdzngquj1mWUUubGf6AMV4xsv9XAiguESBfG0AysKCT2VtGOQvhUhrDs2W4Gm1rNO4YbogPiDmmszUAa-Umlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJZRCX8pXOZbjkhvpRMarffujby-hc6TaMtFbVTy_54FUengSLx4KC9ZyEMiMpFXUqTHwMImmE6VaY4SnE8KyDA3G7Wl6I2B3vhklsRwNT1_OH5px7JiiJUUj8oX3krfwYkx3tJ6bB10qpS8FiLC9Ex0yDCy-iZJV6TeH6p8RAWjpiVBh7mS95WvfLry7OSTXv_gwcOhOj9C2KYfJjoSjdaMe-6RUbrHY65UWqHqJOWUnHeHY9qu8yCRH20yw4xkqcAyL1CGJ8HOfeGekrQ7-CChD_ym-nFSY0Eabi4Ob0xfih1I72_kqOckG8KxTXIr5lYnQ99jfVj0GWIgEtXN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a66098169.mp4?token=D-iidd39wzNBzPx4-TiDagqTxH7TMMsHLHoPHp2-dwPnLbIIlZgLSJS7AWydOO7aaxwkLGBJsSSc-fy4ILatjXqNAR9W4sudDYgt90C47N27E3DVpubDv8TuiEk4khsGqc86ZnWXJGv_2f8RuP6BajO3FQvCoagYRlumK82DZH_jeQxFtiRUftcMI4Ag2QJI1vvyyD3gSsKMtS1EYh8H7pCf0hxtpygf3g5bXsHjktjMPfrEuNUpczvKcHN7-BOQHEHiVZRnHhYaLc_3crzBQqb22DZ1gDXYiT_J9MjiyuV8FGf4I0FIIfA7_O5B5w8kVTXy9Im1pPVUyqQ48DIpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a66098169.mp4?token=D-iidd39wzNBzPx4-TiDagqTxH7TMMsHLHoPHp2-dwPnLbIIlZgLSJS7AWydOO7aaxwkLGBJsSSc-fy4ILatjXqNAR9W4sudDYgt90C47N27E3DVpubDv8TuiEk4khsGqc86ZnWXJGv_2f8RuP6BajO3FQvCoagYRlumK82DZH_jeQxFtiRUftcMI4Ag2QJI1vvyyD3gSsKMtS1EYh8H7pCf0hxtpygf3g5bXsHjktjMPfrEuNUpczvKcHN7-BOQHEHiVZRnHhYaLc_3crzBQqb22DZ1gDXYiT_J9MjiyuV8FGf4I0FIIfA7_O5B5w8kVTXy9Im1pPVUyqQ48DIpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالملکی؛ وزیر کار دولت رئیسی و عضو هیئت علمی اقتصاد دانشگاه امام صادق:اگه گرانی رو در نظر نگیریم، هیچ مشکل اقتصادی توی کشور نداریم.
+اگه ۴۷ تیم دیگه رو درنظر نگیریم تیم جمهوری اسلامی تو جام جهانی قهرمان شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73181" target="_blank">📅 00:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بریتانیا دو تبعه ایرانی به نام‌های «روح‌الله بازقندی» و «شهرام علی‌رضا تمرزاده جاکی» را به اتهام دست داشتن در فعالیت‌های اطلاعاتی ایران و توطئه‌هایی با هدف قرار دادن افراد یا دارایی‌ها در بریتانیا و سایر کشورها، تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73180" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxoN7zaPw7i02iymxhpiV0M9nRD8kpyHQdjzI1B6hHFjGVOPznF6CHH4oldobbwDb7zWIOjmzgvmCdE4JNyE6TufuWa10yt8wNeZah0OSnT0PGf_ooeF0T34_h1DZpmlOetxmhU_vekt5f3E1jxWrEO4I7qZBJ18CLHNNo5tAiCvTbygKO3t_SvlZ0pgK2ksmP96ncvFaUCUZxRaywZedbIUU21xaskki_sUojQHB2LqNIr5ARzfJFdZmNprnH18yW4q61TKlCiTGe4H1RidGAN6cHTYdxoZK5qPyKgzNSM7cpTFVyYu4BOjgqKt-FSBug8aqzLzG900xcFmYVKl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو امروز لایو گذاشته بود و خیلی جدی داشت در مورد انتخابات اسرائیل حرف میزد که یه ایرانی این کامنت شاهکار رو گذاشت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73179" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=XsuKjX8uCge2J75SPcdKMCZ0DVhAs6kCi9NQFoE_-rI-0hW_-pLuxA_epQW2jErmkXYm_ps3zqY9BAoaSORS9oP3e2-wKo6Ws3N0H2c3gj2N6M__U68DiBiYDOuUMG56_F-_xhmuRoSgg4j5WGwBKik-VTahvDfBEV8AgxV17Q68V4Sw_UMQUEkf3L6CVVnE7vVU-tn35P8AKuDSchcI30oOcqFWR4FZwkVCutwhLFChNEtAM41rI6oNZmSG92HKi-S3l8eQwtCI6S9MAyAoH7WW-URYd_AaHikKd6P_6bqfYBMGv0p8IjZ_yzCxm64Vh6FFPG3v0hvOuxsHawO9Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=XsuKjX8uCge2J75SPcdKMCZ0DVhAs6kCi9NQFoE_-rI-0hW_-pLuxA_epQW2jErmkXYm_ps3zqY9BAoaSORS9oP3e2-wKo6Ws3N0H2c3gj2N6M__U68DiBiYDOuUMG56_F-_xhmuRoSgg4j5WGwBKik-VTahvDfBEV8AgxV17Q68V4Sw_UMQUEkf3L6CVVnE7vVU-tn35P8AKuDSchcI30oOcqFWR4FZwkVCutwhLFChNEtAM41rI6oNZmSG92HKi-S3l8eQwtCI6S9MAyAoH7WW-URYd_AaHikKd6P_6bqfYBMGv0p8IjZ_yzCxm64Vh6FFPG3v0hvOuxsHawO9Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض به تاخیر افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73178" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cobgba2HkcBiMq0IE_uNhEph9VxjjvGQHU9wbiO6UorWpFZlaznILM-8BPc6luEMD-EVUXFGTqh1Pi6LSlxY7Yi6CLZJHVKFV46qzxvD0VDILqMQSwrFFsPYJ505NiXevpGU232CO4_g_uslxg6JYiydm6XCqz0mEzgTlaEHCyY7mHqWLFDQ9xK1Q2-lKkjEcp6o-JQbZGqNxLD5y83Tl6N20vgtRP54GCHzQzexVa0l4NR-R7wO5bylVY-p602hlXvjF2S0pTTw-xLaItyqSPKuGM3X0wgKGisTl5KwDIsefbXot-LTLdsWnKnNxuRlhXUp5zv-1XPO8pv1V4V8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک نفت‌کشِ حمل فرآورده‌های نفتی، هنگام عبور به سمت خارج از تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73176" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73175">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=CANtTW48juDVQUnxz0dBj7yNWdM7_3Z4sUr1MmYBRyhF3-FWJMxgtDGfw5oFH5g91Aw_ewayksnplXTxTixf-Yc95eubpnFVuO0KgQ2iGGD9hqzsqMJtbrq8hosdOauGynAlsQg9Iy59QlDmVuLnAuyefB6DrS5LvOVqgfNOTFHx7yO2JFkqvyUv-FK7dtB758JXM9XmzOmx8CH1aqsUv4WGSmJpjwvesrPVQCg8dpQs6veSgwF3FHx2wYvoY9L5FJOb9EhnKx9mGcOG2Rc6g1RxUAxmWEn2lb-MI8So1D9TxKI0133nIXXvYoICrHbIG_6f5Xo5dSnahzquU9rZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=CANtTW48juDVQUnxz0dBj7yNWdM7_3Z4sUr1MmYBRyhF3-FWJMxgtDGfw5oFH5g91Aw_ewayksnplXTxTixf-Yc95eubpnFVuO0KgQ2iGGD9hqzsqMJtbrq8hosdOauGynAlsQg9Iy59QlDmVuLnAuyefB6DrS5LvOVqgfNOTFHx7yO2JFkqvyUv-FK7dtB758JXM9XmzOmx8CH1aqsUv4WGSmJpjwvesrPVQCg8dpQs6veSgwF3FHx2wYvoY9L5FJOb9EhnKx9mGcOG2Rc6g1RxUAxmWEn2lb-MI8So1D9TxKI0133nIXXvYoICrHbIG_6f5Xo5dSnahzquU9rZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از یه مدرسه پسرونه!
معلم اون جلو وایساده داره درس میده، دانش آموزا دور هم جمع شدن و کله‌پاچه میزنن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73175" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkIzuLCYV1Q5PsqTFs1FaZlcbYC5CZ70_zGRzFmTYPrQoNan1BbKTFZTTd2IwpsndwKq5dkxH3dVMT6WNuusjyNgQflbuRN9rlsxeDUvd3E87KpLdfBjxNt51mtOX27MCyTd4udiJEU1k7oYwylhthpcQHyLx5N4uGq3twLodGN6vYn9CXYOTAwVLtfJRfgWzSAP1XyAFqOGjltbExVOfJU20MUY9gK1xLzOGXRadQL_GnFQKuR-4dlFQNrrQD1ZnpqEQ6suQIv7ttCOZY0O7kjvWv1AywejyyCP6lstx82HW4wwzeU2-fOV1eHNjF5PuUafyJnYelwgdvC_PaMO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=UpptAfyJfrV6FUTxlur_xQ0FpaonsyLuiHT3dRT1LFCtZqWSC9fQW9gKr7odpATL2cVomHACxLeQ1nJwq2WGtUCSZKP6ZvLzkziLDi2kRoTz523mqYw6uPtrPHvOc36oWyQ19B3yT3WXzniexPHMxcl6sQxB_KliAADgt94xdnG78SCRyUdVtadW9BcAMI7kTzD5wknopPJQGAUF8uZoIpvq2ssHK8AIpr-59c3rXfrUw6N_4nPfeDtC34tc-nRj09zp2V4PsZfMFwF13Ex0k7RRQDxrvgimphw92_f03NekjjWlbGoCKtfouhRB2VVavwlRunfmEM1yfgoHDV4y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=UpptAfyJfrV6FUTxlur_xQ0FpaonsyLuiHT3dRT1LFCtZqWSC9fQW9gKr7odpATL2cVomHACxLeQ1nJwq2WGtUCSZKP6ZvLzkziLDi2kRoTz523mqYw6uPtrPHvOc36oWyQ19B3yT3WXzniexPHMxcl6sQxB_KliAADgt94xdnG78SCRyUdVtadW9BcAMI7kTzD5wknopPJQGAUF8uZoIpvq2ssHK8AIpr-59c3rXfrUw6N_4nPfeDtC34tc-nRj09zp2V4PsZfMFwF13Ex0k7RRQDxrvgimphw92_f03NekjjWlbGoCKtfouhRB2VVavwlRunfmEM1yfgoHDV4y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=VQwip-5HJNWZs_pITp-AUn7pbMs2rJjWpMT4tdwqaU7t2vnFBkx8KMNG6WQ3QHmhMy_KnuVSyKLeleIet9ehl6w6Zf32j1yMQcAhUZpZhhmHnZ6Zy-7Ki15xVonEflVnpMdwskF5bPCPsQDh_ngWnEWcWTxFD06eW77ZrmjXomldlUwkpC-zFjgZS9UJhEG9bb2seWb_2rZBplUna1LEJ_1Ll0JzoFCj0mxSvc-kYB2oFeo0mrwL5jJ0ypkHO_-i2W_JfzN0qdqIaRuq8ceoqeIsFTZp4XnDUjkDcH121sTqCBiBLsr7dclnECwGYUmFTQzuA8lZ69qhwkviGYyiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=VQwip-5HJNWZs_pITp-AUn7pbMs2rJjWpMT4tdwqaU7t2vnFBkx8KMNG6WQ3QHmhMy_KnuVSyKLeleIet9ehl6w6Zf32j1yMQcAhUZpZhhmHnZ6Zy-7Ki15xVonEflVnpMdwskF5bPCPsQDh_ngWnEWcWTxFD06eW77ZrmjXomldlUwkpC-zFjgZS9UJhEG9bb2seWb_2rZBplUna1LEJ_1Ll0JzoFCj0mxSvc-kYB2oFeo0mrwL5jJ0ypkHO_-i2W_JfzN0qdqIaRuq8ceoqeIsFTZp4XnDUjkDcH121sTqCBiBLsr7dclnECwGYUmFTQzuA8lZ69qhwkviGYyiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve0S8h63Z_sAw5gHuA3UAs6UEBrRTIs9hAkloTDEHOLam4RBhFOuLC5uIIgQ1vdG6EcF6n7cahfBNP4qo9y9cZAO6MCl-GxCBIdSKZjUmaC3Qm5EKFuzsQix0saI8RxsynAC5S2isOCPOBtGc-fdlIuexQkH83NyzRnnxTKj-s8On4lg3FG2fAd3EKLqX8CknIg7tJv1Dz6IThL3xh8yHXVXQpE-ktgXLryD8IsyN_va8hIY7mmTRDjBDvYxPPjINAWHUT272OHnviTX44D6nWIMWCTOs9PbWokACS_xYnJC27Ia7fEgwJ7kpwPdGLkUHlFLA-ySuKoduTi2RVNVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=huDVCNe-FQksHkWTEEN3Lagac7jog82Bs8IsGJhyYvtLwY4Q2_p3TVRuH0XwYBMgJqo3Y2w8OjCI0vsR7aw2-ld-ESA2kdCvXRudHAdvCPPlerkOwJfx7pe1stMZ108soFpxwwkRAiAZQOzsVXjfcuMnaa79BvLtE_D6BMm0lrrXJSN1rDZRKEdjlq8x4HHX_uapCWlIpdUz0QX_YNFc_dOFsPHu2Zu_1qei-KWgwr1YNd4H5usioIr7o35EJVjzzqiNLpfDKzmwOcLBqLYhGzipjnM3u5r21FEpztVOAFGBE1a_nEhMTkgD_1PTnK9cSfkRUhjOeKHahXyJ9Vw3VKSTRll4F1Xan6YzbZlPjnhy3kjew5f6KlWKprfhAEZvqiuDE2G0O0KKOQVRGBu0FGsELZiA2IuJ6sjL8Qf093XvC-0zCCthvgFlM8ETlVq03twJCuXJzYiOI-o6MY8p-6pgvUA8vUvdsfFSKTxKLlacq8k_ohWfF4H2iNUd16MvLBZTUC6T0K9WHToKLLlCpzhyaNV9ZMCck7IESxhHcRjq-7_7OQlA709Yxi5LfusFJA2dOAMKpk2_RbcWCw4rfB4S7eXHaumIxCYDw9o61uFlZ0WIkMGI5Eqy_jhNtXiE9nlr9kVPHTe5CeEr7eebqgM9Zvr4ii6jpyyqMJUaMmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=huDVCNe-FQksHkWTEEN3Lagac7jog82Bs8IsGJhyYvtLwY4Q2_p3TVRuH0XwYBMgJqo3Y2w8OjCI0vsR7aw2-ld-ESA2kdCvXRudHAdvCPPlerkOwJfx7pe1stMZ108soFpxwwkRAiAZQOzsVXjfcuMnaa79BvLtE_D6BMm0lrrXJSN1rDZRKEdjlq8x4HHX_uapCWlIpdUz0QX_YNFc_dOFsPHu2Zu_1qei-KWgwr1YNd4H5usioIr7o35EJVjzzqiNLpfDKzmwOcLBqLYhGzipjnM3u5r21FEpztVOAFGBE1a_nEhMTkgD_1PTnK9cSfkRUhjOeKHahXyJ9Vw3VKSTRll4F1Xan6YzbZlPjnhy3kjew5f6KlWKprfhAEZvqiuDE2G0O0KKOQVRGBu0FGsELZiA2IuJ6sjL8Qf093XvC-0zCCthvgFlM8ETlVq03twJCuXJzYiOI-o6MY8p-6pgvUA8vUvdsfFSKTxKLlacq8k_ohWfF4H2iNUd16MvLBZTUC6T0K9WHToKLLlCpzhyaNV9ZMCck7IESxhHcRjq-7_7OQlA709Yxi5LfusFJA2dOAMKpk2_RbcWCw4rfB4S7eXHaumIxCYDw9o61uFlZ0WIkMGI5Eqy_jhNtXiE9nlr9kVPHTe5CeEr7eebqgM9Zvr4ii6jpyyqMJUaMmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=WQirhBGWEtDIFzVXgYpEX20tSNNuxBKd6_LrmsSSlL4nYCuKeET9L0tRen7Gf0ho5YriSfCShCxTU9nCnkFHaNRhLl7ovNiPF7HgunSKJu_Lmmx-rjPiRniSY8vRrNYSp9eqohKoQN2jjTCGyFvtK2MD7BjTXwoxT71QMJIc6WxFFWBCh12r8U3uqYn_3dixtL82HrtsOwwqDAdZXBHYUnAzimFwQt0bXfki3U3DgxdR8d8uQ22vlpJjaZtUJjEwSUAJSHK4ZwRwYPaf40oIWdJR6ePePtc-i7kEPi-tSJ4sYdbcX2NznCP39oLEAhZM6FLgrE5LDNI--JFZgX0k-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=WQirhBGWEtDIFzVXgYpEX20tSNNuxBKd6_LrmsSSlL4nYCuKeET9L0tRen7Gf0ho5YriSfCShCxTU9nCnkFHaNRhLl7ovNiPF7HgunSKJu_Lmmx-rjPiRniSY8vRrNYSp9eqohKoQN2jjTCGyFvtK2MD7BjTXwoxT71QMJIc6WxFFWBCh12r8U3uqYn_3dixtL82HrtsOwwqDAdZXBHYUnAzimFwQt0bXfki3U3DgxdR8d8uQ22vlpJjaZtUJjEwSUAJSHK4ZwRwYPaf40oIWdJR6ePePtc-i7kEPi-tSJ4sYdbcX2NznCP39oLEAhZM6FLgrE5LDNI--JFZgX0k-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAV9BECPAESisPPf0CcL8k20-izoC26q9Cciaux917EQ-6lnWvJZewgyGfc1nA9UaDVEnWhP0EO5d6srmpZUh2txdh8XrJnZR939HdbQu9FFmA5XeKC18XsvvTcyt-7otTMlP1ZFAPqf5rhoOgbdBtItuuVEOmIiCDzBG7-Kn3nqy67OAZi7D8gX3qFn0n3BOkItdKbiiJsj_UvGdw142s8O58t6yWF9uX7UKgZloQCk_0ARDo1Mknm-hEaO12dCT4oZR8Y4A2Cfpw9HLgtm4bq2pPtfJk2ONdIOSxn1YcbirninpKug6lLZ_0oJUJdm7GnLErPlbLhswXPjDr2xrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYlkpA5-JNy6J9L0YNt6auAwd5TErpudtLewFT5oWRUtnty1rOm-dDLie9CYkGyxbVs19RK4e1tMJbRVKnjTulQ35ct9pj7Xx21Zoc6XBov1xDcsyr2kbEyYJ_u7zZs_FTLOcf8KEVJn2PKHfXjYC3pjPvlXrbf2NsQOq00OvUZbKKYA5-e3lqT4pwMmu0AYN1850vj4DX3yd24GCwAyChgwwx4YRqy9X1jrPq6x6d7h7v1J7YAZ29UTPZHTKUBbVOCWdxzv07nrdgMlOTCUs5T1VbuE8SQawDle0fsDlhl-VBSkGBV2rvGsoHT23rzGYFgLfC5rczG6dsxeK0M5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxKIBkYLC4SCaYrs5D7bf-0nBihssNWkcN-8KxplWl0Jj7aWz83hljciy-RXy-qogw7opiZrC1qXrDCpy6B2LgXicbv_hYxFOw9XRIyxHFEH5Gshxdfk4gYw8wYEXNc_L_Er4tDhkzBz-zSkURevnuQNCFbQhAfTWf2Z2PecNA3RM1edl6ALSFK3i3-CaM4Gll0hOcOZjXolXZNB4mYand9giZ63ssdeSqsEAxT95KkXEo8q1EpH_29PXGPEEm6mdvtEVwQ-5RzBVFoTi8jSvbdxqdL5G0GqUIgx7sg0nuxmxTUkOdC-A0ZfhSijtYyjiYNpUj0pE6Muahp0xXKixA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=L43NqVcX1jraYTaGgzn8BAdQEekh8VOLouNI2eptPqyxm1KmlSwIY0smYdvSagXEplakAtXDm5ilE7Y3QA8cutGY8ZWJLfvf46fhDjIyoG5_V0M1vjPucnuA5-nmpBpPAy6H7up9AEYQ2cxbRJFqoyuUzJukqw05Qq5O1-Xxv5WszKATu3CyCexxsCa6opeKwmQMhtThKlNIB5bd1Pc6jo_IZdAy5PmF5HHhEeo9SGoVBUQ1s5ENKLnwfWDBqYFLEC73g3xW-anpf8zx8STwV49pBeLNQoqYiAwYkw45XZOVSuBVwCTqmAiE55wmo4m-811HhIhKx464773HiaTkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=L43NqVcX1jraYTaGgzn8BAdQEekh8VOLouNI2eptPqyxm1KmlSwIY0smYdvSagXEplakAtXDm5ilE7Y3QA8cutGY8ZWJLfvf46fhDjIyoG5_V0M1vjPucnuA5-nmpBpPAy6H7up9AEYQ2cxbRJFqoyuUzJukqw05Qq5O1-Xxv5WszKATu3CyCexxsCa6opeKwmQMhtThKlNIB5bd1Pc6jo_IZdAy5PmF5HHhEeo9SGoVBUQ1s5ENKLnwfWDBqYFLEC73g3xW-anpf8zx8STwV49pBeLNQoqYiAwYkw45XZOVSuBVwCTqmAiE55wmo4m-811HhIhKx464773HiaTkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBhhUEfFTAUdPGJ35GIIvAa9_UDjAycRCCghbAclumazGhvzpq8KFuSAk6HALmYUVgOGhUBdIhpVtYpOyuEYUvuAJfyjvI2Eu_vRwwyqiJSPA_f1xiZfNwLijPrEpr9dMj-4ZvEPvdaf0ueShlclKDjvuumnGuZONWLfjOKuZOn16wn_I1F2Utemi_-bzIXoB1s5cg6_WVXSzxD_GqePt79uCIU_YpAQItDBnWYx6pgujT3cY4Pt4qtBYuRe8sz4NgYi28nUPWlV9xEfvANlomNevHJ0ISMn7rn4k_-DPJYvbvvRzlgbaunIh5P46MaOxVOrd9TRCoKi4GheQl8hjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73161" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارتش اسرائیل در پی وقوع حادثه‌ای در شمال این کشور که منجر به مجروح شدن گروهی از کوه‌پیمایان (که گفته می‌شود معلم و دانش‌آموز هستند) شده، وضعیت «حادثه با شمار بالای تلفات» اعلام کرد.
این حادثه احتمالاً ناشی از برخورد با مهمات عمل‌نکرده بوده است.
گزارش‌ها حاکی از حدود ۲۰ مجروح است که وضعیت برخی از آن‌ها وخیم بوده و یک نفر نیز نیازمند عملیات احیاست.
ارتش در حال انتقال مجروحان با بالگرد است.
نتانیاهو حضور خود در برنامه تلویزیونی «The Patriots» را لغو کرده و در حال عزیمت به محل حادثه است.
فردی که در وضعیت وخیمی به سر می‌برد، اکنون جان باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73160" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=b4noXV1BvLbP6SugaqDLTFZNiPX8JSUvJmzYnzgEDqeC_OYWOUZQJ77mgVY_avHUNM5ggF0xzYcifaM3q_cNYfIFtN4Z3rM4ITZinfk2nAZ3W7FZE68Jnt4PGfyczEgHtYExKawHbAHxwQ6invPCc7man_ZT0j1uASfyCSsZMtE7YMemtu39OoU0Aufcd-0ahe-31hKplrnItb9FWfHJ8ozuFsaSK3Tk1AZHijYkFurBoO8sHfd-fOUxXeOFthPJ6SoCW5VxUhb2bOx9uKonFXl4MeLTFLsg4WAPyANbYxXDKoedXdChhPwSu1DcapWsZsV3XC5ZfDrnMgOrr9SNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=b4noXV1BvLbP6SugaqDLTFZNiPX8JSUvJmzYnzgEDqeC_OYWOUZQJ77mgVY_avHUNM5ggF0xzYcifaM3q_cNYfIFtN4Z3rM4ITZinfk2nAZ3W7FZE68Jnt4PGfyczEgHtYExKawHbAHxwQ6invPCc7man_ZT0j1uASfyCSsZMtE7YMemtu39OoU0Aufcd-0ahe-31hKplrnItb9FWfHJ8ozuFsaSK3Tk1AZHijYkFurBoO8sHfd-fOUxXeOFthPJ6SoCW5VxUhb2bOx9uKonFXl4MeLTFLsg4WAPyANbYxXDKoedXdChhPwSu1DcapWsZsV3XC5ZfDrnMgOrr9SNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو ماه پس از سیل ویرانگر پیشین، نپال بار دیگر گرفتار سیلاب‌های شدید شده است. این حادثه خسارات سنگینی به مناطق سیل‌زده وارد کرده و بار دیگر زندگی ساکنان این کشور را تحت تأثیر قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73159" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=YtFjfyXNN1lqaMcCxnAUTeL-J0dfiCGtPbkRYhFrLZ7EKWTzYHlK5YkOds7VPOIn2TcxDM5HMc9I8XBfc7O_Ukd2McBgyUggan8xRA3s5_k2m2YAK9Xxi0FQFVDZr0yTgq6Vokq7KYvlnXDCSmZA_bg3-QGeK_jimWmhYH0qmR5a1ziLVto0L8GxxqyPNkJtJ0aczjycRKEicDGZS7U7QdjsfdXHRaWxsgSVgf8J1Jz4VbRMbepIkCABAcZy90dkZhnnluyxDwstnNufxZSNRycBSsDQWaxIXvhcvDPM_qxsz8iFpoJlj451qU-T9GOPCo8NIFyLylfcps0OWf24rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=YtFjfyXNN1lqaMcCxnAUTeL-J0dfiCGtPbkRYhFrLZ7EKWTzYHlK5YkOds7VPOIn2TcxDM5HMc9I8XBfc7O_Ukd2McBgyUggan8xRA3s5_k2m2YAK9Xxi0FQFVDZr0yTgq6Vokq7KYvlnXDCSmZA_bg3-QGeK_jimWmhYH0qmR5a1ziLVto0L8GxxqyPNkJtJ0aczjycRKEicDGZS7U7QdjsfdXHRaWxsgSVgf8J1Jz4VbRMbepIkCABAcZy90dkZhnnluyxDwstnNufxZSNRycBSsDQWaxIXvhcvDPM_qxsz8iFpoJlj451qU-T9GOPCo8NIFyLylfcps0OWf24rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی عجیب که از اعتراضات فرانسه وایرال شده؛
مردم تو یه میدونِ بزرگ با جمعیتی زیاد جمع شدن و درحال شعار دادن هستن که تاچشم کار میکنه پرچم فلسطین دست گرفتن و حتی یه پرچم فرانسه هم دیده نمیشه :
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73158" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=NXN4wqnWQDgYx9KDEg9gvrO_1TT4KLZa1qNBbFsajZYYkpOu1N-_kjoYFKwdu-HhVGLqvUPTwZhNIRxirVSNiJad0KRdKNT01nwM0fQVoyDu41EyIoKGUTz36FeFI0BSdjvEiXJtK1Pu5GvUPpR6Rbm6K_5kPGJiMvEoLshts66AO8IXzqj4Oz2ZsFWdVDZ_K4MpNAv2fC3zW1t4iZxaapcNQCF3nBmiVwTjEbO6q5gxLgcmUHvmjLfpOodH0zME6EdQMZeIh-qf2M6ezCg9BcrGcOZZf8hvHN-es2hkt7vEE3KHNmxW80kiioPNeY9w9I2W7Kuzt0Wa4QrmDg4tew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=NXN4wqnWQDgYx9KDEg9gvrO_1TT4KLZa1qNBbFsajZYYkpOu1N-_kjoYFKwdu-HhVGLqvUPTwZhNIRxirVSNiJad0KRdKNT01nwM0fQVoyDu41EyIoKGUTz36FeFI0BSdjvEiXJtK1Pu5GvUPpR6Rbm6K_5kPGJiMvEoLshts66AO8IXzqj4Oz2ZsFWdVDZ_K4MpNAv2fC3zW1t4iZxaapcNQCF3nBmiVwTjEbO6q5gxLgcmUHvmjLfpOodH0zME6EdQMZeIh-qf2M6ezCg9BcrGcOZZf8hvHN-es2hkt7vEE3KHNmxW80kiioPNeY9w9I2W7Kuzt0Wa4QrmDg4tew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "
من میرم بین ببرها، ازم عکس بگیرید!
"
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73155" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e5000591.mp4?token=lOhSmG4qFLUlMrvYdbOlieEK9OUPju_chNxVtrg8gz5w4M33Gnd0erNfxW6-AmWQx3KoVH_kQ0JYWdKdsslpXojv2XoAS0uQ3jS3m1wv3mFvhZ-5a_j3cKBRSgNnU0nJgMKV6TSD4_Ym9leoC3muDpXuqYe9P0h74_rTBqNHIm9xKiMI0IiAnyn7gwHQSvEyaj3-diSTc7eruyeNiLjfoEQsB3bwMNd_VRArPxxfq4lCzgz2YBz2L5MyaqlvYWzZ3gWSU3fuqEH5btVKt1BLNGxbhlN2El1p689lN8Ng10iYugXMqlPM7MlLCBm1WkigzXFfZ8mmDkBg-SvTpeKHIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e5000591.mp4?token=lOhSmG4qFLUlMrvYdbOlieEK9OUPju_chNxVtrg8gz5w4M33Gnd0erNfxW6-AmWQx3KoVH_kQ0JYWdKdsslpXojv2XoAS0uQ3jS3m1wv3mFvhZ-5a_j3cKBRSgNnU0nJgMKV6TSD4_Ym9leoC3muDpXuqYe9P0h74_rTBqNHIm9xKiMI0IiAnyn7gwHQSvEyaj3-diSTc7eruyeNiLjfoEQsB3bwMNd_VRArPxxfq4lCzgz2YBz2L5MyaqlvYWzZ3gWSU3fuqEH5btVKt1BLNGxbhlN2El1p689lN8Ng10iYugXMqlPM7MlLCBm1WkigzXFfZ8mmDkBg-SvTpeKHIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با نیسان از اصفهان راه افتاده و رسیده به پلیس‌راه سیستان‌ و بلوچستان؛ اونجا مأمورا بهش می‌گن می‌خوای کجا بری؟ می‌گه ایرانشهر.
مأمورا بهش می‌گن مسیر خطرناکه و توی جاده احتمال کمین گروهک ها وجود داره؛ بهتره صبر کنی چند نفر دیگه بیان تا باهم حرکت کنید، یا بین دو تا کامیون راه بیفتی تا همراهی‌ات کنن و به ایرانشهر برسی!
+
گنده‌گوز منطقه حتی نمی‌تونه امنیت جاده‌های داخل کشور رو تأمین کنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73154" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uUHKB6_YCbJHO6GSxSCvp3vxrzAO52P7wZbwLmKXBw_f-4ZxROw8wVReSiYy5DLq3HFAsfYelfklOV9hPRlwqYcFZgVLMIAfcVSiMiiP8jEN6AnMppCH5WRR2S8--ppxKKYx4xLyiNuZ_rb5lzu96jQ4g18Xrg7evW_JgSbQvFBDcOoIpjoWX_c9er2IcMaO8ldvkgf8jkVlUf5PprI9TqhPMcShceTRSoJ2tiKgK0690GQ-Ag0QujP8GJAkznWmel_K5A7aq8Q4-xeO5PNQWaZNiVe3eLtLtZcZwI7CziBkkcG7A9TRFEaJBH1z0Gk-Hfduvt5FmstSvJtmyEct8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر به هوش مصنوعی گفته هر چی میگم، در جوابش بگو جمهوری اسلامی.
بعد ازش پرسیده بهترین حکومت تاریخ ایران چیه؟ اونم همچین جواب شاهکاری داده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73153" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=Y31E3LqSml8zjCpHKAJhuNjM2pn46s97jPAA_BG47MOUsgwzYK_1qM5ESU9rC56SHZ4voRbVgM528WwuwrUh6CZcc2bmU7lNLYxjcZuyCbY7ZfW9dAQyI8y2Hwh10vpNbtxfUXthCfdeTelKAzVHfBsUH0PqsgX4zvNn1iFTl02eXdQh5j0Vo-BZrK4Z384lrkMqP2UNcvxZSnUOetIlrbBPw7y9Ug9Tlvfz_kHT2nc5WYtx8kkM3HJZI_xzocUFhXeGpIkcGiNq0uEYNsUWJK57ajzWZI1R4466WMQ-UVY8fL3izSGzjJkj67rCrj9v61_gpeXZyLq67rVQX0q4-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=Y31E3LqSml8zjCpHKAJhuNjM2pn46s97jPAA_BG47MOUsgwzYK_1qM5ESU9rC56SHZ4voRbVgM528WwuwrUh6CZcc2bmU7lNLYxjcZuyCbY7ZfW9dAQyI8y2Hwh10vpNbtxfUXthCfdeTelKAzVHfBsUH0PqsgX4zvNn1iFTl02eXdQh5j0Vo-BZrK4Z384lrkMqP2UNcvxZSnUOetIlrbBPw7y9Ug9Tlvfz_kHT2nc5WYtx8kkM3HJZI_xzocUFhXeGpIkcGiNq0uEYNsUWJK57ajzWZI1R4466WMQ-UVY8fL3izSGzjJkj67rCrj9v61_gpeXZyLq67rVQX0q4-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73152" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=KSxSmILkcwyXrDODrExujH7udd7OhmjWlosCZimUHVqxEY6PX7IQWMmW4LdPCluMxunD_KpDDDqabiZCFby6OiTi-Z8Otf0i6DEpX48PiSSc61Gwk2upZHNO9uE0LqcdkEHJbPI_j2e5FwRoktI3sxA5-wW-xs45KVSxFn_jF57c45EHyJNnSM5kzTtUWIrAXAfM9eZDDnnlR5oQLdsW8IMkDLr-JN1TUUZ45eIrkgdKzHsdhvohclzjy7i8fydVuHvECZTpf8bqxDlPgabAek9K0OJr91LYhMYeIqDAhf2VdFV_3IlexB5pt0biL-ep68KI4SLx5XQjLq-LA7NwCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=KSxSmILkcwyXrDODrExujH7udd7OhmjWlosCZimUHVqxEY6PX7IQWMmW4LdPCluMxunD_KpDDDqabiZCFby6OiTi-Z8Otf0i6DEpX48PiSSc61Gwk2upZHNO9uE0LqcdkEHJbPI_j2e5FwRoktI3sxA5-wW-xs45KVSxFn_jF57c45EHyJNnSM5kzTtUWIrAXAfM9eZDDnnlR5oQLdsW8IMkDLr-JN1TUUZ45eIrkgdKzHsdhvohclzjy7i8fydVuHvECZTpf8bqxDlPgabAek9K0OJr91LYhMYeIqDAhf2VdFV_3IlexB5pt0biL-ep68KI4SLx5XQjLq-LA7NwCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73151" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=Tz_R2sWuJ8aQVajXT-oMnMvNqcBgYUp0H2G5GmZjX-Rf3chEsZAXXvjOiIZM14wnxUP2_6Q1w_RHcOH4nUG63iaxMm5lNLHWeAtxmXswXeT4YkGzUN77Y7NQpVB1jMMbAWuisMwnqx5Ka100DH0_RpUmxYGx2IlgOmeD963azURggLyvRkj4WFTJiCrfTpKfO6IwXFt7RQn0MoINit106hVGYXw_LYbUrpo0YZR3RttmxM_qRA1QufWnnywsPCl4NMDHNZHZ8pGYTh_Bo-BFc0WhYYeSBlUHGauFmPDfQyu3hv-yrFuyLTaWVebCJV3HMBeBR3jUpKsFHPhG27qvWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=Tz_R2sWuJ8aQVajXT-oMnMvNqcBgYUp0H2G5GmZjX-Rf3chEsZAXXvjOiIZM14wnxUP2_6Q1w_RHcOH4nUG63iaxMm5lNLHWeAtxmXswXeT4YkGzUN77Y7NQpVB1jMMbAWuisMwnqx5Ka100DH0_RpUmxYGx2IlgOmeD963azURggLyvRkj4WFTJiCrfTpKfO6IwXFt7RQn0MoINit106hVGYXw_LYbUrpo0YZR3RttmxM_qRA1QufWnnywsPCl4NMDHNZHZ8pGYTh_Bo-BFc0WhYYeSBlUHGauFmPDfQyu3hv-yrFuyLTaWVebCJV3HMBeBR3jUpKsFHPhG27qvWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی:
«بلافاصله بعد از پست ترامپ در تروث سوشال، روسیه حمله‌ای هدفمند به یک نیروگاه در خارکیف انجام داد.
معلومه که پوتین تروث سوشال نمی‌خونه!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73150" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=fRCChhINcm1ieQo4dVDWZRs4iPBYGHU38n8oiXYsSK498ikVx8I4blL6Mh-ECQvEwm4v38cTqVZn2jYdxaA5Rg3LwbHLp6v8etJOJ3Qh7ind4-7M837Rv9I0YuLg45oBC3mSRAnXUAZL5SNPTwG1ydqYMLXdoP1xZicb76JgsNbz2CFXjnhIHtYO76XVadawFsj7QmA5BPYQH94oGagCcmGLr5Gzkz2a20XX6LdHCJqgfpqxloIifP_dgiwt_92XPO0GoCR0RQPtHmzZ8Q6OP5Rz0S_11WoJrQBxpO3rxzK6zPLta0ZA2NKZWLBvayT-XEDTEYWm1yQ5raxyb-jDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=fRCChhINcm1ieQo4dVDWZRs4iPBYGHU38n8oiXYsSK498ikVx8I4blL6Mh-ECQvEwm4v38cTqVZn2jYdxaA5Rg3LwbHLp6v8etJOJ3Qh7ind4-7M837Rv9I0YuLg45oBC3mSRAnXUAZL5SNPTwG1ydqYMLXdoP1xZicb76JgsNbz2CFXjnhIHtYO76XVadawFsj7QmA5BPYQH94oGagCcmGLr5Gzkz2a20XX6LdHCJqgfpqxloIifP_dgiwt_92XPO0GoCR0RQPtHmzZ8Q6OP5Rz0S_11WoJrQBxpO3rxzK6zPLta0ZA2NKZWLBvayT-XEDTEYWm1yQ5raxyb-jDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بیکارِ کنجکاو رفته بازی Resident Evil 4 رو روی نوکیا N95 دکمه‌ای پیاده کرده و همه رو به تعجب وا‌داشته :
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73149" target="_blank">📅 12:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=rHkiwSq0uZ-Gi4cIyeT7K_dKX0iN9D9za_L5fJQpALa1uziXr4SQt9FMQHnEZCyJwmrCynr9Q98t5vuZsQrFkJeVP4kuWLfCW4tvQzUv5yxQTEMBEnznpKwff9xC9EJ1pT09Qp3wNaKpAmSJoxui1hnLHIhgiR17Ynt5L0alhxT5YN0uLCmhk4rfECGueljzfmk3nw7BjnPAmYNPLLDlLdEY1VCjinolvAjh6jJIhBXw42mrptXHlVu4A4dukix1VRjvXhgGlIJLVhG6OmmCaVrWVBFCehHLFTQsEVOtM3IxXUi2HFNx9oByrauoS6QyD_UF89ZfzhiG63zSXSpTtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=rHkiwSq0uZ-Gi4cIyeT7K_dKX0iN9D9za_L5fJQpALa1uziXr4SQt9FMQHnEZCyJwmrCynr9Q98t5vuZsQrFkJeVP4kuWLfCW4tvQzUv5yxQTEMBEnznpKwff9xC9EJ1pT09Qp3wNaKpAmSJoxui1hnLHIhgiR17Ynt5L0alhxT5YN0uLCmhk4rfECGueljzfmk3nw7BjnPAmYNPLLDlLdEY1VCjinolvAjh6jJIhBXw42mrptXHlVu4A4dukix1VRjvXhgGlIJLVhG6OmmCaVrWVBFCehHLFTQsEVOtM3IxXUi2HFNx9oByrauoS6QyD_UF89ZfzhiG63zSXSpTtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیسکو مذهبی هم آنلاک شد و توی تجمعات شبانه یه رپر آوردن و حامیان حکومت دورهم میخونن و میرقصن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73148" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73147" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73147" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyFcjmDYDFRgOHAsjkmwJZOyk8nX1WfXj-YVuX5vkMtU5LN235WEh21SQkpGz7yY87h7N1QZ_MkXCrSWZzOi462FChzfD-SaryxqZRNi1KHimyCf6xtiOSDVaMG-mp7IX7bb3d3mZx-PSbueFAsRB-hLzCnntzFNe4uEaH2doewXBjgE8aJ_cRcC7aMyEylHKEhUAEl1gpqitjuTFHinsx3lYTE2bu3fzKhXGLpd8rKJH929sf_5RgHQhe3JK9Zt57lrerNQmSP9dAdraNTA5scWlGlfJlM2rj1vafEbTXr6P5bLub5cLuH4K8pt2NPrHrTAgakljmWtAViaUQYcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73146" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

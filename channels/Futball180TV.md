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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 668K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-97345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd228c0fbc.mp4?token=rJbHuVkjVwY7XfO0HAxXgm1tFs_EtxA1--CO64GZMn0lxDmbF-wxtJRxnONweN2kvJ0gRZpjymfJ5BAs75kVISIJaX0BmSnyb3VZvT11SPJA7DPJK08T0Xc7gjtH5XYslahdN671LBEYxjZMIisWvCJV_OJYozs5fkbyZkp_AyQZsCOPDcq_2so4CM2_mQGdDQ66qXnjt8rkq7qw-RksLOHNJ1BEdATWhphgKbTcOdLQfsW6EQj5B7zeHkkFAVJFBaVRJIoPtbgYrLA3GZbqW59h2ULJlspX98eMEEcVqugaIAli7bV70Sel9iJaWULcrJMd5FZ3PzvkhTceChwauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👶
🇧🇷
بچه‌رو چرا موقع فوتبال دیدن اذیت میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/97345" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bece496424.mp4?token=U5Of-ySc58pDdFOrLJUuc9Vd549A7cQt6fzQcCwK1l16-rqqR04W5OhO-gZs7gWn9uQykeHd-2TtpNEbpmYAUOJWalnFa0gLmHMzJa-cxO8Biin_ioxVVz_e3Lg3PiLEkDiYtXsA1XZg3SpqR5nRIbljL-t5cIhUQW-IkcsgwAc2hiiqWAjkYvdOuCEa1mvVBrw-Le9j-2F6cLP7-H8c04DLwNEhG-Mf01zoDu6RDdaN9bk8RnsRxNug8JwGz3m6LEMYSyhL4kNPp4cUyB7JYo0WOPriXvYT4wz0-wq187Ts2BXlZIBSN5VbFWV8ANhmjKRiSt-C_9UZ01OdG-X7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
‼️
در سال ۱۹۸۳، ریک چارلز و چهار شیرجه‌زن نخبه از برجی به ارتفاع ۱۷۲ فوت (حدود ۵۲ متر) در سی‌ورلد پریدند و رکورد جهانی شیرجه از ارتفاع را ثبت کردند؛ رکوردی که گفته می‌شود تاکنون شکسته نشده است. چارلز با سرعتی بیش از ۱۱۶ کیلومتر بر ساعت به سمت آب سقوط کرد و پیش از برخورد، یک پشتک سه‌گانه اجرا کرد. بدن او هنگام برخورد با آب نیرویی در حدود ۱۰ جی را تحمل کرد. در حالی که بسیاری از تلاش‌های بعدی برای ثبت رکوردهای مشابه با آسیب‌های شدید همراه بوده‌اند، چارلز به لطف ورودی کاملاً عمودی و بی‌نقص به آب، بدون آسیب جدی از آب بیرون آمد. بیش از ۴۰ سال بعد، هنوز هیچ‌کس به این رکورد نزدیک نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/97344" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceeabbf9a.mp4?token=YLeAHx6wCBuSrfuDGIKwQqUaspK-fch2rWL6-CbDVcpyfmsCx0cDtIS35lhX886m8kRFJ3l6DroobhPyYoeI2OLIvp27gvW8tmVXpOQ5G5ZKwqYWonY8T3_dnSTzhTU7QnhbZpUgDXg0cs7lpyfr5yAVoHowrtstVfTv3jaKLj8aoY9a0ktPff8HMSY3JIT14uh9uwfzyePFUlDH15TTpxHs1hZYguAw_d2ci1W5orZZcR4eJd4WNyT0sszSKtKTE2tDovr0N7BtCINxaUjmXtyU_AioN44UT9zICc-mgwdNqjNpMXLIxXvjJurEEk8MNfmZAKLM0hT4H5KV64fJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌رحمتی: بیشترین ضربه رو از کی‌روش من دیدم ولی واقعیت اینه فوتبال ایران باهاش خیلی پیشرفت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/97343" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgW0yS-qBwLxV2oR83CJiBZOIV-yxTWLm7uqfzdjw723AhnSxOkJo8GlwdImfwm6ydPWYklWuiAmx69sY9mTdUiZP1lbZKJ1PdOIKuGKKDfGmi8uy8Bhb8QNxCmERg4hrPVlwJpHO4ArshAJ5n-G3bwoz5fL-bMuNaOHeWKsZlLrOLX6v74WQcIsE7pZHC4slIdFNxh9Ye4OORUHVXKAek5M-4WMSV5bs_IraqwOWMYdC84mwAFmLfmg6Ptp8WN3oMRKlNC7qcifUUJwIP-Bcw_KV2ov13yWSxhsgv8siHEQ9JLiIAkb-6FcMRmnH3oWykYMWDzL3u2gG4DtEc9-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هوادار نروژ در بازی دیشب مقابل ساحل‌عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/97342" target="_blank">📅 14:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03f28112d.mp4?token=A4kb-NcG5Qja2f0T5xkGlALEgUNYvf5tZerg3QL5sHJJAEFp4PKhlnkB6lHJNPfZn5LqN9PmjdXYNp3kG3ctCGP19uuMowofHxtK8xhjQ7lPAIPcmGwWq17xxCXM-OO0pmBmnD47cM8NIARoLo2nAwOs4ZXej7C86zZM9boV3LENwk2mnyk6sDxox-yNxCnfpPWENImPvJLEWQTJ7Y8OYkLMonM2H_LA0AZq568janjc8Q-R6o7j0E8w673EjJDPzQ6sYHLUJDhUlVDntIPoVf6U_gXLWWY7UV7Sbv2Tv8yNAIEuexahiyuQU_cujNoss0efIEN__O5ygt2BTeZIAWSMzDH2o0ZNJG0vKJQ6iMkEyL-Il2FTm4C62r8Qzdlj0cBL0xlI_8Dsf64BAFfWnMKnGE9gXt0waF3UAKam-IFa4Bo5oDUnDB8sGvGzF_vWGIzOGP6uOTP5ddEXoRjqggFju1qxzdDEAX8yaKS7Jyly04JAox04bf49vSSfkYOBcz6Jcew8DarRec3e1Z6t535XTWVq2spxcyIpoPoMuJDXXntnDDIpMdv0gdkSv6vFpYWw99ISWFDk-XWJ5N8oIXuKPgIikSLVcv0HEBDKxu9U6H8R8hC7w_lB43gDPHHSZ1Jt7z4yTxQXzlbT20OHMSR1a2mH_-Y-TB5koMQ_pIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ادعای مهم و قابل توجه سید مهدی رحمتی درباره وضعیت تیم‌ملی و تصمیمات فدراسیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97341" target="_blank">📅 14:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97340">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiCqJI3zRSFHnpZioiTe4sI1FMB-2-7H_9cbxWqBHToo14ZzdHp2IiZV9tlLd60tNXox3X2U-LCI_NDn9kFcvPE_nZ2u53FWkfWDzQTpymC9Ak8eAEzr1w6C0Fg_pwPUuTv_5RCmI97v1F86MYh90AK5yqBUxoS95gj4Rbb-QdRpTft_yXNGY44O3l1NxvpABU9BL8fkOTVeyaLpCY_tdKWaeVhmZB8Bk3dpuIOO6K89AHdSzSgfeIQfd0ZJv8ohByPeM00df0Eix9lJW-oGD0ozApMfcDMuDUWEzHd2FNsiHepg1pA_6Ko-i9PpR3X1ToaBXzTmGR4XSrrmQ5Wn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🤡
کوکوریا بازیکن رئال‌مادرید:
🗣️
امباپه یا یامال؟ تا اطلاع‌ثانوی یامال اما بعد جام‌جهانی نظرم امباپه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97340" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97339">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLLioSWl-j03ajAZjpCpNZRL4Zj_T9gT5t2VXF01cXgYZM02934vI5-xT6NM4SX8EwmNMq6wmp9jve3Fyuv3ulPVCS6iG04zLTATzsOmtFRzP3Xf-W-WELgdNBjZjL6H3NkrLxuHyh8TlAaZBtr0Blf9rCMB_kO-xO9nIW90sgpLyvQUXbh4GuKYpmJxuUGl_1iyJ-g7eYGaAQfj_JYYjYLiT1pwJSKT_jq-6CWhuMqydX92jPfj3Ol8YylxJ74NQ478ScFTbjwZeRna6STLpsJ4A9y9aUBqOa6Kr902tr1oIiJqoylDdSGYL9-yITBGI7QTTHojKOcBSn_FWmkQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اخراج‌ یا استعفاهای انجام شده پس از حذف برخی تیم‌ها از جام جهانی تاکنون :
❌
🇹🇳
اخراج سرمربی تیم ملی تونس
❌
🇰🇷
استعفای سرمربی کره جنوبی
❌
🏴󠁧󠁢󠁳󠁣󠁴󠁿
استعفای سرمربی اسکاتلند
❌
🇨🇿
استعفای سرمربی چک
❌
🇳🇱
استعفای سرمربی هلند
❌
🇺🇾
استعفای سرمربی اروگوئه
❌
🇸🇦
استعفای رئیس فدراسیون عربستان
‼️
✔️
🇮🇷
در ایران اما امیر قلعه‌نویی و مهدی‌تاج با اقتدار به مسیر ریدنشان ادامه می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97339" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97338">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhdKLwLmAosBShYCL7SLK6qRreyo4YSMwu5tmFRw-Y6gAyauvHYUg8fro5CTbdk26wn_N-4s2KickbOvhpM3lWbUDuAQRmpUOzshlRUNa2ZyHlXRrvlHVkv9K2kOs23SsvNZ_dqeATqy_xyA5xg_ONKmsyzphIKZ47s1alkHalBqv5pJgaNIvaoTKT098QgUOFUpmQCRIVG-ux_qiQAn6e-12dueKg754XfVbb7XxlFqo8eN6nix5FfUi6dUG7r2R6XrSqlgwFLQmAONWFTf8QmkxaK23t9eNHXSK_hjAP_aLIABZ71XndZxn-Eqs5MjubvXWS11WJMcE7-IY1jUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
🇪🇸
#فوووووری
از الچرینگیتو: امباپه در اردوی فرانسه شدیدا با اولیسه درحال صحبت هست تا فشار بر بایرن‌مونیخ رو بیشتر کنه و به رئال بیاد. کاپیتان دیکتاتور فرانسه به اولیسه گفته حداقل میتونیم یک‌دهه تو رئال‌مادرید جام های اروپایی و داخلی زیادی کسب کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97338" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97337">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0e1d128a.mp4?token=jiwGOtq97nESYAyZkkIXsyubr2cWFv7-RzDPeCPLRGTQwrYtcgFIm6iX63C4WS-k0KjccvuT8dyOLBN-cCiXYRaS-t_QOd_Lnb7i6TKKAR7qFKRbQXvMYl0tiWp6lDZKsFe02Q3rmRjcS-um_vcOZAKCQtaX142cQe2EKCc1olWokxzfvtfBIlkxS4thNimA1A_McHQ1D8UlkvO8qJYFSrNF9vGyovAIZ-BlXtYz_xMAmK1wvt_lLi1WQegmQ6gbk6YQBmTqRsME6Cfiq9jG280xuFVkeX4jhXUPAydJUr3JBguxC_dXKyXoVkxhj1-oACAjHsFBrBdqOJ8VFWnJVgh4uYeDM0Gm0itFDa5YqMaLlwvGEcSTThM8MpXF5PuFpm1z9My1hPjZJhxOZCqgtoG7jEAkdXMquTMOAowD4cxn58lxxhvZhIbEhp5s8Cpqsn5it_UUbX66CViC5NtrJsNSyIPa4VP6FAqaEtHYeqIKMIwhNthe3OoBKIol0F40bL-XZkuRzudGbTUL3ABbgOas8K45WAq3Vt2ljDNWmHsS3jad_B1I7THLj7p4YSkc4EV0pWtCVrl98H5yU-nYJnlYZFBY1AIVUcLWowclSSwzlHcMzBwBbuX6z-Tf--aOeNzp9V44hKNP1y79XnoN32FpDhberCYtfXVP96sR5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چرا فوتبال بدترین کسب‌وکار دنیاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97337" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97336">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfacd704b.mp4?token=NEHpsOypSfuUH05Y-mZZIds_Or_aGPut1LQ49FytlXyvRV-PcIkhPfDcvY2gEKcEhzsFq5w9Spt7YJVYe_BNxqWmvwQSW72xLEzYADYsqsum1rukwfF3xU3yknkmFQ2fZP3qCp2Vx6xYoXfMcCa8fz4EatV0YvYhuQclBz_edHMAj0VDhxztOrtndVD1dUyLBahn2LGnnvPp2jzUK92zMUDjzKJ4X6r9mZvxf3hUBsUeBX2vAuPO2on-Unm3B-63DT6Jzhp1llv3LBhf-pM9ympiR11GwxadLEIgcVUgSrl7tpIlRZjZcKjNXNSPUEjjLZs6N7038_cmQ07Jb_rdEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇲🇦
مجری خانم ویژه‌برنامه جام‌جهانی بازم تو معرفی بازیکنای مراکشی سوتی ریز داد
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97336" target="_blank">📅 13:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97335">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdWNPxa8loRTm-_FW-XOB83MJByGe5Nmut4qbdMxtWMB25oRFDwk14IjwVpNJDL3RxiZtgrEGhfZo3zGCDcbgIf87UuKg4vWLstjvR9WPh1EXlvjoEdKzOChc1cKku516gG6DobznE9SZd3BvubLEhlhMVfuSVHejS3lAzYMCVvgJgFKZNHeYzW5FlwGqMbXFwx4ImJdVh0sVhBCW1ucQznvGpqmkLqSZT2AflNDgJnKCA73ZfaJwjOIoh2curA9s1XRS_cpJMlLD1Oqlb8LT7s5DE8ZZMsNog6vQx6avg7b4vsrtp4Jb0i99fsS4xiOJ1sAb4ZhmEjsS17lJOf-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛
در چنین روزی از سال ۲۰۱۶: منچستر یونایتد اعلام کرد که با زلاتان ابراهیموویچ به صورت انتقال آزاد قرارداد بسته است.
📊
ارقام و دستاوردها با منچستر یونایتد:
◉ [53] بازی.
◉ [29] گل.
⚽️
◉ [10] پاس گل.
🪄
🏆
لیگ اروپا [1x].
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام خیریه انگلیس [1x].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97335" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97334">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIP3CzyhT2QBBR9xNHkfZzcmZreHMe5w7DFHzTaAm3FPgWq7V7Vhn1nOYVftp3hvC9gBVTfBt2cv7pQ3_KU1qlJby9xt9YwgU52jd0CLBX-lHNHvIX5OMnFe3K9mWsQ0o2xRsgD8CCrLfbyKWXtOTgh9HydcyDJn3wP18qU6GsvbBV958JyrNWmjj7yeYzZMbPndti0UN6e_CBEwwn52vVOwM8D9NJ-7JAn7tGk9e9pWPxmJWBr3TFR8gVvOf2xg3mdcTGleH66J1csAinvs0BL3RPkCpS12ccPanr2F5tW6qxARzHe9vEkcvaGI_x7Y55cDdeMw4KloYVm1fqLZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ جرمی ژاکه مدافع رن با قراردادی به ارزش 72 میلیون یورو به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97334" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TZSatZ_wxRvxHIHwIWeI-AjUYMQqMS9sNUFsHoI27zrIeSiUfvIGORpqVgWt1zIm6q9xVG6W928rygBGqmyfr9-cR6XPZ8iYhfDuTkO3rFIJI60xFwtcqAVJIAFY1XBK86IfTdcVErvWMZDHChoCHGrLt3gjvIBxxKXJLc5fQg96_1m7dxyaNUC65lcrRVGavE1X3Qz6U_rh-oHGyeOXNs7hGuDlvhCzlgVYK6ppORAmGEh7tGK1hBNzOxEHe6Ca12uvohy9Db7_-buMuSFgYI4cW52iY-Q74BYKAdOWzBT4lJbWefiQnPgP-Omnsq1_p92nS9ZF9DFGOu-piNhjXOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f803ce8f.mp4?token=NRvLkjkrmgSZTDvn0R1ky9RyQuSesaYYCCmaBPA3wOfTgguPr2DaFcZfBvj3WjT26Bk8bxFeirVo102dvMAMhaIxwH0IZAgY9402q10ApxTWKQT1BlAVUm1kTVRw6acBIQkc8uA8u67dYzMepFvIbZPJ9UQ9jOcyw-IoZ9OIwmmcNGOfKtIPEk-3JHPAVlIfwsCTf7NwCb3s7zNmvRqPVMlaHtkR9r7dxSmCW4ZeefA2eJ4ERzlyvvSJfkFVQqc1xMEHEU0zLBaSFqUiw8e2vn6kjPyAbzmCghdVbMRj15hLSZrfStrQr_0aOIkQPt4HWIHL_lK9BjMe0Nbadft-TZSatZ_wxRvxHIHwIWeI-AjUYMQqMS9sNUFsHoI27zrIeSiUfvIGORpqVgWt1zIm6q9xVG6W928rygBGqmyfr9-cR6XPZ8iYhfDuTkO3rFIJI60xFwtcqAVJIAFY1XBK86IfTdcVErvWMZDHChoCHGrLt3gjvIBxxKXJLc5fQg96_1m7dxyaNUC65lcrRVGavE1X3Qz6U_rh-oHGyeOXNs7hGuDlvhCzlgVYK6ppORAmGEh7tGK1hBNzOxEHe6Ca12uvohy9Db7_-buMuSFgYI4cW52iY-Q74BYKAdOWzBT4lJbWefiQnPgP-Omnsq1_p92nS9ZF9DFGOu-piNhjXOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
عادل فردوسی‌پور: از عملکرد تیم‌ملی و قلعه‌نویی اسطوره نسازید. خیلی معمولی بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97333" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=Ffl3453htvF8UEeuBXnXOTMVx-_IVi6yLzyLdxEeBh2kat0codBS6Clq9OkRAcpymtPVzu76ZSim-iyuH8bXEr610d4t9n0hyNnH-ilWg5j2pVYJA3DqSH4BQ3PcudsW5x8d6KcovRzHuEF8gzZJj7SDGnUMoX5IHQLp8dXdNDordAz1rNz5oHDAeXc6j0e8zeuRPqOobjgHkYlHUnN3baQnfv4uP0Dqsgf9_luWYP90EEeDEVBgOmMoFrlcnekYAWmwBV0gl6i1bPMa3MB-dm-vt60umBA7O-djaYoRlWyRUmLlDnXzVuGTfp-GxadB__cJhV-xGCaBP2nTLKumkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d18e2b7.mp4?token=Ffl3453htvF8UEeuBXnXOTMVx-_IVi6yLzyLdxEeBh2kat0codBS6Clq9OkRAcpymtPVzu76ZSim-iyuH8bXEr610d4t9n0hyNnH-ilWg5j2pVYJA3DqSH4BQ3PcudsW5x8d6KcovRzHuEF8gzZJj7SDGnUMoX5IHQLp8dXdNDordAz1rNz5oHDAeXc6j0e8zeuRPqOobjgHkYlHUnN3baQnfv4uP0Dqsgf9_luWYP90EEeDEVBgOmMoFrlcnekYAWmwBV0gl6i1bPMa3MB-dm-vt60umBA7O-djaYoRlWyRUmLlDnXzVuGTfp-GxadB__cJhV-xGCaBP2nTLKumkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
چرت‌زدن پاره‌کننده هوادار مراکشی تو دقایق حساس بازی با هلند که سوژه رسانه‌ها شده
😂
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97332" target="_blank">📅 12:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb04aa687.mp4?token=LbAuyF2CUs98tPtaCQ-V-CVSal_8dX4N7T9q46Szy_7TTUnbO1Xzwj-T249ZcQ-pdCSfY3j82Hyx0J_KziURZXS7sYNNAMreoB5xsj5O-CsSJeL6v26wpMEyPtGA_DWmy7jcOgCRmKsefzU9mcy7X7XeRs4b6njTt3E53Bwy5HPNp_LFBkaLKberQ3W5Mdm-g-QJ2X2mM_xPFLlEhVK5IV5fU8fwMMTh-8rUOlITMYjVezYlDynikMJpQcde9hJdomhzLlQSh0UCcwbBv3elfOKPBqQSZT2mkpJDVYM6AQ3LmmBXT232Ob1_7XtPWBuBLr0wgYBD1D9ReD6hBm4RvpMdg9EruRDhs49YINjNZVfwuX8NLDbLZw2P2nGNxWHJbobO79HjYIMVJYfQ-KNoD01_nLwYPYa3tHgS0GGP1QT6dhhKtNZN0WD2QcUZ9n9fCaAldTAVt2ZRZRg_iuJUiEPENZ5JYiW4COZza9rhOilwB4uj0_1uN1sfNYGczPPEAG9RJF97KsHygfJ9Shs3b7cue8owxeFIu-oJJnHP6OPRzV2-udlT-W9jmTub2rtTypUHn3S_tNYJXiIqLIXowcTxG9Bw_VUAL7TdAtPoWjLhh73MewygnfZ6XRBzawO4RWT-Tp4ImANScMG4rvbIb6_a7nlcaffnx2uxIemiXqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
تفاوت سطح‌فکر سرمربی ژاپن و قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97331" target="_blank">📅 12:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCo68cet0EktP0WCYE_hqC1Vw5eXGnFSegrqJGhQ30Mbka5RJYpcM4Itam5sklFRytIggr_Fw6gCaigzyhPb0KZCFVGFF2NTNW5IIg2yIuWWG5QsDdD3Alr2cXMMANBsW8HQGHx_e23TVoX8aEnZw5YZuNksQTbRlL9UAsN8Bnx83IxwuDh4wECKaceDURE6PRZf4wAdQSP5npdjWUNwb-9wiLPRkqjmI70VXpu0PnB9jwRxG3SKWqPYU8xQz_fPDX9TytnlLIql68CW7K0snwEERBach_xM7m9lwJzqqyFWpFSrYLYljooEw5q43gAH2EmP3CvAaMNMJF_y9acjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🇩🇪
تصویری که آلمانی‌ها از جام‌جهانی میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97330" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD6SQ3q71i0ThZViEW1S_JvIQzr9hYX04KHpSHoMDMbXF-dKKDaCzXAwvHzWXSI-ratwsIV6GGTKKezH1537TuJaEqoNO_H2CabfUq3Up4YSKnPG_uMt9QMW2GWDgVRvxsRQ6v5M4n8dLkNNrRj76hFoILB-AYLvlQTT--OSKE_8kUixD8SSqZzndhx2Jrpis_ogs_Y6WowiynTvq3aXqqhRkfrac-RTLJegL0HfpBr8fvJ-RAqnx1UYO6qEhuWIfU5FCz43Crrxt9A5weXRAeOW0QDZQY9Q3efRs-z36n1_mePR9CGMy0nXSMma0M6u3rOrpg3WmfAPfteSkm3geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قرارداد کریستنسن با بارسلونا تا سال 2028 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97329" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9652808f.mp4?token=CWtLlmwbxRkWcbE5IDtDLdBjaNFocyfVShyGY9-h1hUUoPpKbBNis3titUyO281Q56vVAPp6SPtmhMVmA0xf3qtWayYClRKdtKJ4tP0GuN3TFzn5UUhZ4KIY5l8mgcIebULznkoc5q1TiuNwMVwZP1YGWJiD-we06kszhCQvOwT1jjsg3AroEWL5e2m0rIexzVUGeaNHAz5WuyT9qcCq5lhwkN4HJgifBPMTsABFmROoKR-B1S_-AcdAgoXUoOLkoFFWWTtIzGJiFRJITrysMj5VK_oZZsZCpEWIuGvfUwZOMOTrli2EMSZ2eCZwdv8ROvkaF7NhlRPYNCoD1rFY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇦
وضعیت مراکشی‌ها بعد بازی با هلند؛ خیابونای کازابلانکا رو ساعت ۵ صبح تسخیر کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97328" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_4VJEmkyhB9E7WZH7GE5NAj7JaOjXtujq5ywBOiGgXFUdcMwVBtUOXXtcLa_RqP0GHD4WBUPzVy8rg_G9NTZ011B887J3lznX38EfUAhMu6oN_tG-5wA8A2tbPQeOJ9MyK8Ao2v8LOSO11EyjLlm-IvcZSAbDVVcsvxJkkSdxHmcrOoSE4Qb9gW28XwpuZdopLEydEE3zH9y3ah_flr35iduYpwRiTKs388Alco3B1OBGqai_q87dr0FTj1mLBVao-fkEI-Xj1PsgWRRuhuZXqaol4TWxyMBCWjcyqWMX8IeXJikJQ1CHgHEo9kelMUTebBLAkmNiXApZLbl47wMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی اکوادور پس از حذف از جام جهانی توسط مکزیک از سمت خود استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97327" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd1d74f95.mp4?token=ow1pDiHMXPm2dadUVhgrtUwD-1aRxyPNVS7u6rzMXbBUmd6_X0GxYiwVc6x-ZQAWWtkocuUAi-vkSCyxvKCEYtsRD0dPaDzhlE-LkJJhffaP_fvsxcPzbevapnJNZOqjxP8doosWVKr-nfOVwPNF7FFlv2s6Oyb-hzymDcqoYu16Z-7y7nqGS-uXX4W_Oi5W9K0Yhk4bquEBOY_rr4Iui5t5wE2_Da1p-Agirv374-rsfT23ZH0K04FGVTIMu97-BXBrFVAHcy0po78zHwe0PckdWJmFRdrFThjc6LocxCHCzRrsCxjAqYkEKpXsc2pIiOJMNjRRBVaOTc7pU9Z3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار مراکشی وسط جمعیت هلندی نشسته بود و سر صحنه‌گل اینجوری کون هلندیا رو جر داد
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97326" target="_blank">📅 11:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334dda10f5.mp4?token=Ih7TImayb9pITWsD5D0ghRKoQGyNESXa8W3F6PmB2JL7zutAoR8BFTxlH-c0x1-c6fp230qmFp8B3KvV0cumPB-kAbozf0cw9Usl3VeBQ6y2XyYtLOXeEk6qBlHq4LDZYlqak9Zjqa9Sbee_r5oKB9fvYzxfLPoSAphhJSEvcFmg0MapT5ipU-J-WWtEwQO2WuBs9-Sgeznvxcm2mkD6g8vSiLdP_I_nmETE17VMib3KiQahUrgyzjwowffkpMvK32p_ZzFnzkqlcCw5PR8js2OOj1I2SELSrpju5Bix7VwRpfo0Nx2GaVWZIMMRgTHZM_kH3Lmswd-vQDf31H-G8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
خانواده پاراگوئه‌ای‌ حین‌تماشای بازی آلمان و شادی فوق‌العاده بابت صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97325" target="_blank">📅 10:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc32bb0eb.mp4?token=cMhgNhxJq8qFQAG48AUocZGYgmc4F3iw1T1wGwjx69IXqA4gzsG-hMy-KLn01yF2IecEpiHp7aQuZ3CatEixwwOB4JY24-Wg5l_PKj6-AoypA1Jbxpai2y_BgUVRujQyBf-SiJ6hZQGSj2-5akGCRBo3gwhXr1e6GBDk3zIZ4gV2tQBeICozjmgJuMDBSWLaPJm9gRBoIZCsTfS-Me3j9Q2RYWe06Y6K7yqnmwAQ9MPNWpLmsrnWNYkEOw548hT0IGd6aleDkm5-sq-gl9RL4PDE7eVKhIGQI8dXLVPZJnJHsK2bx1GLXtpjRp2JAiNorULKenBsYmjDv1dWaZGRb54BPsufX4V0AiuVOSFsE-q-ePnGaidp82pkiIIbkb0ADkixtSvSjqTjyKeXgnowW8JcaJsur_IPQG6uPMrhTQqGKxPwkcD5yqXhskAy27dm_SCAzacWOkUcF5r49TeNVwP3pJVZhh3z1SPUJ77-R_Ptlp1xQCCccVElyoUkdKchVaK_2bCWo58_Zzch77Q8TJ2nZhunIKUT60mgzKyaC275vAm49D8KiqibQJM5FTqYkj8L7GPa39QsFBWL8ps-EmpaIQVTJcC_6aI5zhAL22y4TswdD4utxQgJNRZtmzD4n-q9f1s3tk9n1nBlrO3ln6upajoUQEVsp6Mo9BhlHy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇾
هواداران مشتی پاراگوئه بعد شکست آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97324" target="_blank">📅 10:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3264c990e.mp4?token=QveoiIf9dHoZ1ZGND3hYw2FOo9-MEyVVGgkPCwlrUCVS496hOJv7TJpV27jAY-41kHm0snRGkqDaTS3RF_VxAZ33F3k_hbjIufJLXakgRTz8yWbB9cWwksjFWj83b1ef31clIO8S4OMGpxfOO0jByPkg-f_48seFg-L0ODAQV-hvdliWYqHedFEbOIFQaDyOzxrfzkN2xVGbcHHBhIh4aHPfb_gd22f33TBe3H5g3D1rc347T5CkX9hvSqEJd4G89PCMrF9ffKy84eo-R81h5UwVnr9Ni42rt5LJc--ad4kKJ2IVR8_ebmzN6fvkcASrSQuWO0esO77EqPLpflY3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
این‌قاب برای آرژانتین حکم دین داره که حاضرن برای پرستش هرکاری بکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97323" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37351875f0.mp4?token=s3YZzvYOdRVrQ27B90eWDRpRtnlF8E4LcoY7Ukz_3tiYw-KN0MUSw0YYg5qGOZ7ujZs9OhYJf_o-MZ-3NHuwC7a_Yl5mmtPgxiXV1G18dh_3USG7CtPHBGquhBA98GF54O657ew81WEWnLrWsYyUvR0fZxAIJrQAzJJdRwNIedaMSSWgAVBxdZP52X4TJt6PYhdx9X3yd5xE0JK_1_D3Ccilp2ZNtHvWeY5NOdu_lknziPJrTwx15tOTZMu1CT6Pfkqnet-q3f7F_ncD3-cAgtwYzzLCnqynM-kntoSraaWnoLsHgVzrmyUwFG42idFA477N346gQce_OPM-xUcEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37351875f0.mp4?token=s3YZzvYOdRVrQ27B90eWDRpRtnlF8E4LcoY7Ukz_3tiYw-KN0MUSw0YYg5qGOZ7ujZs9OhYJf_o-MZ-3NHuwC7a_Yl5mmtPgxiXV1G18dh_3USG7CtPHBGquhBA98GF54O657ew81WEWnLrWsYyUvR0fZxAIJrQAzJJdRwNIedaMSSWgAVBxdZP52X4TJt6PYhdx9X3yd5xE0JK_1_D3Ccilp2ZNtHvWeY5NOdu_lknziPJrTwx15tOTZMu1CT6Pfkqnet-q3f7F_ncD3-cAgtwYzzLCnqynM-kntoSraaWnoLsHgVzrmyUwFG42idFA477N346gQce_OPM-xUcEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
آزمایش فیفا برای شناخت تکنیک های ناشناخته ژنرال و مقایسه با بهترین مربی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97322" target="_blank">📅 09:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0Pw9MBxl5CL1NzFIcN_SvBV2edwJzgFSIELLohSl-CrPEpbE6AFw_F7sYlf-BF3mxrTuJnLdUuKCyOObo8t3M_nQITNWbR6Q8UlYWvLIdBkEMZQxYCjyrUD-Ejx426_aj80GLK1T1hYBSgL9BIwxVTe9lfX3THLtlmWPWjrYFqkwO5jhqSynzvON5S6YEcZaNfDaG6YgncAMdyw7B6TKOq5jbT7UUZMmpi7h-FgtnAF7DsTYs3BxtfLyvUG8DJdS_wZzJMghN6xWhsZeMCWRs4GicJzSswXeD-vyheGITTID6Urzh2QiJTxQyzCKD_wHTgSg_9GrrwVYR03zqfBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇳🇱
آمار ۱۶ بازی اخیر هلند در جام‌جهانی که شکست‌ناپذیر در وقت‌های عادی بودند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97321" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN0KZgnnnZNnXZda4X8chlYDVHWSrTHkX7G-gtPPXKGq1FWfgrL3nVV48E6Hj_jVQRWuIHyWJ5epPnNVnU9HrU38YbyDFGu3NmVz-OX5z_KERSYVID1CTiRsCTd8RqyKQecz8dg0xfciigQ0C7sRnacce15qTVmdWVP4oRX4cxCSiugPvZj4Lpy7sT97X3TDKuoUCGBu8mX8aCc4HbDsKS2B8LyR5-8qGMczDuIe3otq7NDb_-rRbTs0BQdqrEUCkc31L07L5MbNpLKIC2svIPkr4t3DN-cBx2hXoCysEUz5OHtdWtBGAIKDuTa33EttATVDlk7ZSUz2BdZXBjRvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxzpB6rp9soKAgxLBywPl-c-r08IAnpzZ7MD83A5x19HCSCEXAOk8q4Oi7ukYYfSObl-mQltnkfUHFp5A380mK9Napnd-ra7wfF5fZV_4vqNTQXidfnoPae0fVn9HDoKtVegE0trYCpb-P64QC2L4CfPNHYaFrb0uFYPJyzSuv2vAuc97XaD7YiU4FnFbplhvjPtdM_8FBtUeNt7fmDKV6nUGZCoLcgjTkz3isF8QfftcDXuFTFDsyEwwia0pko43ozGsbUqRG1RqLOUOh5P7qHO8_ytqRPdykr0uNVa00yiI9aXAIAuAETbiGwOn22IE1XI8z50aJIhafKenkR-KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❗️
🇲🇦
وقتی اسماعیل سایباری به دنیا آمد، پزشکان به خانواده‌اش گفتند که به دلیل مشکلی مادرزادی در پاها، در راه رفتن مشکل خواهد داشت.
👍
اما مادرش هرگز دست از مبارزه برای داشتن یک زندگی عادی برنداشت.
⚽️
سال‌ها بعد، سایباری نه تنها راه رفت، بلکه به جام جهانی رسید و پریشب پنالتی تعیین‌کننده را گل زد تا مراکش هلند را حذف کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97319" target="_blank">📅 08:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNKCR0v-GkPOlPiFqvm2sHxIOLv-eOmpPia74T3SuGWEi-r9IFbdPu2EARSZ37gJZ7CkqiL3K_EzHkVPnom5q4ivImbv_2W6ak-1Egm5sm3c6BDE4sD7OaMjV4Vda-S8TfchdsrdFmTat32xlVAij7IjugNXABrRzax1DOB--ipjYIlLIY_s8XtLZObUTzQBNf5Cb_0FFKK6k5pgxB_h_vYlllB_7t8nSTxHRp0uh48plCcpoarIzrrmfbt9u7jqWWyF4_ruCJQxisNUDJ66wCaTXT5a9zeq0L6Z0hsw0f44yommZ9rRH3ZkJGAc1QHB5bl2zEEjOkeKdFz3bbRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
آپدیت نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97318" target="_blank">📅 07:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgUjBcF3QRcs2E6vQo-9f_y69uAwX4Ewx6o7BPIrGd_hhPXNyDv7xxy_4BusEyG1UhNm2vhWciTg4GvTw7X1s4R_x1eCP-4OMThouLFPufZqzg-uLa6LRUtRlezBtoNBQCnbZOxxPEHDBYDNymwDAy4UJF--h2jNPQt5jBWq00chM5Tv-lW-NZiQd4uI8_whMlJaldgzl7YEUQtXWgXr4mQXRYFL-y5LjtHafR8CoRmMD2N9xQpEMgykq2y5TsZyI0RhxCW2zaa1G3ErBKa4OMVmn1E_JJs26CKxJbCRumoF6CBUlVFrmCKHS7oqUdiUmIhDP8vgO4DOTlaqo-A3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:  ۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97317" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZjrUE1bp4-SQfgkckgjMR8GTCekLMUSfUubEQYCnPccTZoS1cHCUZIYWHEuPn2VvFQogzok83UwTctLZU4YSK_Z3qlN2ZEGL9E8kPqZl4pKyE8umnTE1POkTy4lLq9s4gEDH-ovZijmR1FXqc9MO3qzycBelBSPz3jojP0MqSS8IBZVKcie28nJLwBAAq7nFzFm6-BUJFwi8Y9ZF9Z7S1F9wWaBbkJe_elD2k-Yu-sTJLPsha384bKaNz9nc1o5M1Khaxtt7v8RyL0S5EcW5p0Do7eqMBvixUl8pmmmnqnx1xVscr9XIiFiZA4A99YOS2ulz_K7x1Fu4SSBsLpGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طولانی‌ترین پیروزی‌های متوالی در جام جهانی:
۵ پیروزی — مکزیک
🇲🇽
۴ پیروزی — فرانسه
🇫🇷
۳ پیروزی — آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97316" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB3jPCKixOL3FgcEmvc3ffs1rdvrJEQ9A_Tn3qeP_atH4ni5iiMe4fcHs4KqdxkZ5ynUNaprWVGe6Y7zFRFDNlAu2bVN81H4Rd5O9o-2xIH3xJ003eJDD-i9UpugHuuqGu_i6729IVdrkinpJCXqKM6E4DaFIAYED0doFVopNOB6RlL9rTYIYxvblDcQkmk_0ztaYipsE6rYg9qc7v4LJzM2adpvw1GvPGEP3WsdXHenB-nt4dEfeScXZTDV60tPyWzU0FtFOvRpzLrDSBQYH-rWSgN8Lu-MCNCbOPNdP-p1KE7Ymb10kQ-3NmR-aN6Bmj_Xd40MSwbtCuceOL1nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
قانونی وینی(پرستیانی) بازهم قربانی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97315" target="_blank">📅 07:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97314" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkusJuiLzPTcLvQm_bv8sZxvGgD3jbsMNgGugLpEm9tCMkj9lGtYvtMot8ZLcFquGan1ClauHq4kpsb9hG5OuCCegiYGQrhbOxlgHdT5qmeJDkB3p99BtWP2Wb1s49DcAA-LOlqLW8415Lm_HQPP2I_w1wrYZlCHT2Tcf1G6VFo9cLgFXNvxa3nzu7sWYt3XX-1HJhUCOtsWkS-SNHCmMv9HMV_5Oc4aTkZQtbo6JNzhRsiNDBIlW1F2GuL_CMkRqBpdVNLFjk5XL-2vbyrFY9W9b25XYM-dV0dNVsqXKiKEgyrCAoGDzOZL8ulCbemkia0DUO_wcPXxZkYyfsIz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|میزبان همچنان مقتدرانه پیش میرود؛ نماینده آمریکای جنوبی با شکست از دور رقابت‌ها حرف شد
🇲🇽
مکزیک
😀
😏
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97313" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دقیقه 95</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97312" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هینکاپیه اخراج شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97311" target="_blank">📅 07:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=VhjRNbpg_uH5OcZ3OB1FYUQug_3jBQC1px4ixBu_SsGg_gBsDPlOTDwHOf9vsxkE5fmyMcFM-L9v1TyEm7Yjzo-_Yyw-ANyzS4KGE3zSbswARNG1Fdax-d4gIkT5RMLViTF-qLE_UzZW-If9-ynhG192ks6B-2qpIPhG74NdeRPBiOqBxBwA7FV9A3YdDz9m7UjY8iMIfEUNpJAsExJFNq8Enu4V0tJQC2K0e1utOKjUoYyUgQ6W6Ndr2X01JMTHSzU0UvsCVM1GDbLLGW_66PPa7yNy2HGNuc7wOvTHlFVmUDiTzuP6aXg2r5UOyLrmjH_omEIK_GrZX1WuoqdEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59fc7f9397.mp4?token=VhjRNbpg_uH5OcZ3OB1FYUQug_3jBQC1px4ixBu_SsGg_gBsDPlOTDwHOf9vsxkE5fmyMcFM-L9v1TyEm7Yjzo-_Yyw-ANyzS4KGE3zSbswARNG1Fdax-d4gIkT5RMLViTF-qLE_UzZW-If9-ynhG192ks6B-2qpIPhG74NdeRPBiOqBxBwA7FV9A3YdDz9m7UjY8iMIfEUNpJAsExJFNq8Enu4V0tJQC2K0e1utOKjUoYyUgQ6W6Ndr2X01JMTHSzU0UvsCVM1GDbLLGW_66PPa7yNy2HGNuc7wOvTHlFVmUDiTzuP6aXg2r5UOyLrmjH_omEIK_GrZX1WuoqdEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
مانوئل نویر در ۴۰ سالگی، پس از حذف آلمان از جام جهانی ۲۰۲۶، برای همیشه با پیراهن تیم ملی خداحافظی کرد. او که پیش‌تر بعد از یورو ۲۰۲۴ بازنشسته شده بود، برای آخرین بار به درخواست کادر فنی بازگشت و آخرین فصل از یکی از پرافتخارترین دوران‌های تاریخ دروازه‌بانی را رقم زد.
◀️
۱۲۸ بازی ملی، قهرمانی جهان در سال ۲۰۱۴ و سال‌ها الهام‌بخش میلیون‌ها هوادار؛ بعضی اسطوره‌ها از فوتبال می‌روند، اما هرگز از قلب هواداران پاک نمی‌شوند...
Farewell Legend
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97310" target="_blank">📅 06:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شروع نیمه دوم بازی</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97309" target="_blank">📅 06:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏆
پایان نیمه اول | مکزیک 2-0 اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97308" target="_blank">📅 06:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مکزیک هم هوادارای خوبی داره هم تیمش زیبا فوتبال بازی میکنه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97307" target="_blank">📅 06:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آلمان چقدر لوزر بود که به این اکوادور باخت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97306" target="_blank">📅 06:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=p1oSv1SqDFJL2tyTPA7DVdjyyO7aeHZ4E4TalA1Hp5Wupj_MadKuItyCGtOrrBdT5662Xw3oz2joUM-nxWB7LBD_pwpq46SqPbRKEDBXAEwUUiSodnbRmepBb1mkg4ktPk0IiPOWhy6aRUJY4gzBBKygLJ8Mnh5dQHED0Twtx2Vwu_tlnqklKs8wKLGgse99wdX9_65FSut_6e3C8KseUj7SOCb5-H6LyZcEI0T8uMTxOOK_eJjTg49NzJjouqoglwi_5Gd-fdTD5Ejky3_J9cNnFS53tkVoLTUwW78jF2IRVqR-apsOL6AFfp53gvvt-s8XBSui2hEF-HigFG4C0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e871bcbc.mp4?token=p1oSv1SqDFJL2tyTPA7DVdjyyO7aeHZ4E4TalA1Hp5Wupj_MadKuItyCGtOrrBdT5662Xw3oz2joUM-nxWB7LBD_pwpq46SqPbRKEDBXAEwUUiSodnbRmepBb1mkg4ktPk0IiPOWhy6aRUJY4gzBBKygLJ8Mnh5dQHED0Twtx2Vwu_tlnqklKs8wKLGgse99wdX9_65FSut_6e3C8KseUj7SOCb5-H6LyZcEI0T8uMTxOOK_eJjTg49NzJjouqoglwi_5Gd-fdTD5Ejky3_J9cNnFS53tkVoLTUwW78jF2IRVqR-apsOL6AFfp53gvvt-s8XBSui2hEF-HigFG4C0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مکزیک توسط رائول خیمنز
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97305" target="_blank">📅 06:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رائول خیمنز
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97304" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مکزیک دومیییی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97303" target="_blank">📅 06:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMHALJ0-JWtsTc__D-sqsbgwR2c5xZ5tbh7a1m2KFDptBIV_xKBfEfzggn1vA32BJDMgZGuuOM4ayW-7qXBlUzrVHmBcqbwR-g8bd-xlWyQmylBT7CHWVNKvFBTSWECEvEc5EsJz0V5aOTE8ZPyfFNA8K5bJbTJ82jguJq7kAfd_EtZhjwA1tIBo_tlfl6UZUmsKRADjdRxlRQesDuyxcrY2L1hsSTS6ewiv9fPkj8WDzhVPQ4WEVP2vwqBYXxTJ2RMfp6wmzgaQsaDE8XHj_X1_nbJeslpPb8C-QDInIRjbzX4gGEecgKC2T99fg2iPRJ9ge1tMKDVbv7jnSayOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq3mSmhshCPWYeQQICqZ203RmklwNd90kKgnhpDSocMYN4EUo_nP62aPH0vlT1ZccY6lqNmoNTKtBRwuScugMlGAmI0amS8AerY6vRtdZ23RiGNW4DrlDuqRLIfT9fKo9el_UPe5tU4aEUtJmrZnNfHv2xyIi4REeog1W2j_uzYq-8o9gA1Y8SqgFxqfqfhrQ_xj87MH50GxZfaJF4ARHhrz5pYJDiDEpScW0aQKJzYevyGe9EuEo0AnroG876Ud-DHxzRwWCVYKSh8awzKRBLOCVmkbEweD3Klb7BIdF0p8_HxP0JuhSfjBaOK3sxHFCfySaBjAbnWZHRAglO0f6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97301" target="_blank">📅 06:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97300">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=L05xzDPW8IrWMwq58uQm10B1xwFAFOyyNmzmrkHaaZy3-LsOCmmedCDnIm0iS6gXLnrC3cl3y597Uir3Fm9h8pbNl7Cps2fRIVUObznI38ay41FG3B18ook3WV9p6TIdyLn3ZWMVA_4JBdX-Bqpzv0qXpU2-BezdaVeE0zo9DZAYQmHp8vhLCzFo44TgQCCCgS_pjOAcTLlb861zJUUiIze0Eu5BEftR0JhorfG8XGAU3lUkA8XG_07l0yf_Ev8QlK3rghMFrJFBT-LbfTepPYUF4eav-jzWsVsDoH7rzhYQmvoqfHKPbv2KS9KYBNuBX_SWXXR2h4E3TV0mHyQRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a754997a6a.mp4?token=L05xzDPW8IrWMwq58uQm10B1xwFAFOyyNmzmrkHaaZy3-LsOCmmedCDnIm0iS6gXLnrC3cl3y597Uir3Fm9h8pbNl7Cps2fRIVUObznI38ay41FG3B18ook3WV9p6TIdyLn3ZWMVA_4JBdX-Bqpzv0qXpU2-BezdaVeE0zo9DZAYQmHp8vhLCzFo44TgQCCCgS_pjOAcTLlb861zJUUiIze0Eu5BEftR0JhorfG8XGAU3lUkA8XG_07l0yf_Ev8QlK3rghMFrJFBT-LbfTepPYUF4eav-jzWsVsDoH7rzhYQmvoqfHKPbv2KS9KYBNuBX_SWXXR2h4E3TV0mHyQRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مکزیک به اکوادور
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97300" target="_blank">📅 05:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX5wDwM8u_TbvlmsVJbm_ykYK4tzzntqx7zGj7Cg-Th3JZ_etDOL85l00a23uA0zVCkjoEFX0FNIQuzSd7NXC0kskXdSmMN1rxEdkNBwaBb8vpgJ-deD6Br1Mxve8uR8XaENct3DPKjdghL67DbLYb3ZsKpzz3-gxQpdBsWvsA_sziTgcmCQiO5LcJkPF9ydTitdyWbWbTKetcaXd2tXtovlGRk2SiOQB2MODGtacM4oo0jwZMF7pe08ZPgJE-_rxZIIDsJ7YQKWtZ_KPowQFMLY3c7c1cACzkIB673fXkzz-ZABOwfWNdfiGuR-ozY_JP46_aNnYGXpk7Wm_mzeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خب خب یه شخص کاملا جدید اومده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97299" target="_blank">📅 05:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بریم برا شروع بازی اکوادور - مکزیک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97298" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv1ioFm2z32CYV5f6xnHZ03cqBzs8AILTa9zynOJ0IougAp1oI2yy7m0VcDf66-AfzwjEXMbtHoecIoaryOWLjERKOn-kjqoevmAJAjxDwmxnCIGj-EcKQ5IZU3UIze2UDfej5VZYEp1Z5fQHMsytRl2Oj20uo4bdTQsmDg0R20fB-vjpAPko_GyW0b4R2cziKNMepXr95REDWuxmzzcryUyuJzFBamHFZ5G08L2gxSgNEat_8tvk1xDF43LxsvlqXiDfc_qAwSYyB025tPXUwjrs-b12R5RPbPPELDI3zCCj9sh6Ww3-Dp01GhxUI1wgmWBRagHIxJKRlEwewCknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
امروز قرارداد محمد صلاح با لیورپول به پایان رسید و او رسماً بازیکن آزاد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97297" target="_blank">📅 05:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01873d097.mp4?token=VHP6cizFq2B4VryO4NSPdUDbocMLSgLSAStYTZ11VQlB0ktELxA_avYYPr2rWIM7lFOVHplJaA65mNoQLu0lT-5ZnTo7ZccJDw9-0KtM4q-ezb-rWenGeVtntQBx2erC6Rlxsu8qfeg8OwcybOvzBtFJyxk83jkfZ0Bi3yMvqp7bIxwOAxMsNc5-o5YnUmAwQgSvM_LkkWQMfS1XYRFOB_jfqd7xPB_tVS71qlLgZCpOMsFIi0SLEOZ9d1wIbQwO_yU6gPtHqGjq3kiSO3h36PNiyRIgeEtuUozYV01z4-4_0FLphLmrJzw8MJ1NvTAFDFq_h3vZH-174bQ3s8zwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01873d097.mp4?token=VHP6cizFq2B4VryO4NSPdUDbocMLSgLSAStYTZ11VQlB0ktELxA_avYYPr2rWIM7lFOVHplJaA65mNoQLu0lT-5ZnTo7ZccJDw9-0KtM4q-ezb-rWenGeVtntQBx2erC6Rlxsu8qfeg8OwcybOvzBtFJyxk83jkfZ0Bi3yMvqp7bIxwOAxMsNc5-o5YnUmAwQgSvM_LkkWQMfS1XYRFOB_jfqd7xPB_tVS71qlLgZCpOMsFIi0SLEOZ9d1wIbQwO_yU6gPtHqGjq3kiSO3h36PNiyRIgeEtuUozYV01z4-4_0FLphLmrJzw8MJ1NvTAFDFq_h3vZH-174bQ3s8zwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه‌نویی: خوشحالم که بزرگان دنیا یعنی آقای مورینیو و تریلی هانری از تیمی که من ساختم تعریف کردن.
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97296" target="_blank">📅 05:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA8tOyQoE21la2EzI-fE39KZLWSUhMt9deaB1ed4XgbwaEjObqwt6ErnhljFdYH0JwZ2AvTgHEmeCElKPGQ1yspem-OA_8Fiv-nsUyBgDMubLfs2G00kOuzW7-2k_suKh8y7NnpQwON1ILRPaDalL6rqvsJEwBCBWNW0Fp5MWmif5QvGHG78WxlrC_xDBjwhhVjdXY5g6_qNLmPQTMBggdex8YtFofY8Hf_3rK9QIC8AF0iaYZJpYjomnMA8752xL9_FcTIg67hc--o8RAwcXDBTrFnHpGu6RKanRWhKfth3s6WOxnpfndIT_r-untLr8jh9U3WdD6poo43YbbeCgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه حاجی رعد و برقو
⚡️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97295" target="_blank">📅 04:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97294">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx4j9213fk8Xomev3ox0JNQy3kP0ektcT87qE87MUl_aEMIOiZEwUHGdPsv1doVgLBn2ixT7CVzMvmjP8sQS-qy1-CbGcR4y3yk99xZ6k2ifYqqXVjqJVjqt0f2-c3Xaljq5WAOSqJ1uIbtl6j3uYWdSQWEK4W1sy7WIY_ZFtpo3nvc5PC6isCmLx8P91wPtY9prYk9Qx0gGUDi7Jkv88OJiuOmcZz4KtvDHdvrfa2QKQbThyNPgLRi24EdmmX1JuzVvD2pMRT-Znu7Y9NLdw15nSGX86hqnFO9xKbIs08Jt6_NRh6G7p-is7DNHcW4QBpkT0XF0_phFNXoV3zH0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
| از زمان اولین حضور امباپه در جام جهانی، تعداد گل های امباپه در مراحل حذفی جام‌جهانی برابر یا بیشتر از مجموع گل‌های تیم‌های ملی انگلستان، پرتغال، اسپانیا، آلمان، هلند، بلژیک، اروگوئه، سوئیس و برزیل در جام‌جهانی است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97294" target="_blank">📅 04:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97293">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=EKSXT8v-3f91elU68ALgBnrP-ZvO8m19Uc9C0-cPH1-oBzhi6cLTAZLYqn2xdO-xyqajCXounHMm98UdB2MgModgXWxf_Lsrx7a74DWdWtOeXGtw5ptHunIVoM2pb20L56f207TrvJH5lgGW1OuNfZjpmo2OAyysm84x4HW9pNnfLk8wNi5owNu1P0LfxNuVXze_qkibIyYTSsOnyoEYZeRjqctx18Ay627ePymjVnMkCgvZxS2Eh5ph1XZs4sPvRhq4Kk1t8nZ_xU8moMNMVmrSRFF1Vng5tPiJ3lgqcmNx5ED9QAlmFvQCDRupTtpYuowktqTs7bP-auRaNukEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18350dd6f.mp4?token=EKSXT8v-3f91elU68ALgBnrP-ZvO8m19Uc9C0-cPH1-oBzhi6cLTAZLYqn2xdO-xyqajCXounHMm98UdB2MgModgXWxf_Lsrx7a74DWdWtOeXGtw5ptHunIVoM2pb20L56f207TrvJH5lgGW1OuNfZjpmo2OAyysm84x4HW9pNnfLk8wNi5owNu1P0LfxNuVXze_qkibIyYTSsOnyoEYZeRjqctx18Ay627ePymjVnMkCgvZxS2Eh5ph1XZs4sPvRhq4Kk1t8nZ_xU8moMNMVmrSRFF1Vng5tPiJ3lgqcmNx5ED9QAlmFvQCDRupTtpYuowktqTs7bP-auRaNukEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی دنبال دلیل درخشش امباپه تو بازی با سوئد میگشت؟
🙈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97293" target="_blank">📅 04:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97292">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwiJDhS_EukIjiDhedmNdtvAJt6WI80h_7bD0Ep4mmaCeRpVApHtip5oK7Rg34aOGBIf0AAlgHtfV4-w0ulbI18ioOBzy-XuxobwawLfVCQluZEel_h2GK5o6uRrcJ21cxXorM5z3tTZg5Uc8Ogk4U5J_55mlLE2Ucs_dNe0BSABMLqxQGh_ZOKH_w95sukw568pqyteod9FNp4psh14OTotoByO_yenacyHccT2z6iXsWq4liyLyksDXq_-DVqpDiYGDGNIN4wMrAgqRsUO6fVHl5uKAHE3k62Zz6sr4tLH-p_qPJdGhvXDR86hjpzo0GzrJLXDOdHZZ30Lh1dq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به دلیل شرایط جوی، بازی اکوادور و مکزیک نیم ساعت به تعویق افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97292" target="_blank">📅 04:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6j4g-C70pNw6k5oIVP9nZRNSy8xw_hWM5taFXP1bHWzqyKlC9F7uzdV7gZ6ddu4DBztZVISHvG8hQ0dlohIaF3ozi7-EkqhYFJItFzI6pwECyZAli3RtqNsLJAV5CBoJ4JqLvqRXpYukceKTXatiaqsNDi3ky1Q-9OBhxelkMZiDKTETwjMfqK0cu8ILJJOgDp0L1m4l6ggTk6MhCJO2Ksd0eOaStWvUaN1z1H1GiXW6I5-M2PffgWCJRIjgtWJKN-ZZNeHFAcv1AQNFopGYQvQJ5lFuaedUbISHYRxPf2_6r9UFw_eWParttqgmJUbUJQEyxfcsKPctNz2xE6bJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egYKT5VvnuG1sI5QQsTj7YkboyjjKO4dUNXf9Zzm4SGLvdpRz9l2UCVT-5UmSlu242cEQHfHtk96CyA5ubhom9jbP2OAu0XmhTSYCMSskZivBELOzebNGnKVSlH7SRK8xQBq7HtNumg2Wda7H2HwHYSKbBVrhFf1_j_bBcWOYsNVeM6x2YR9baIp6kyW_JXlf5Ej_WW_df9-RDNs83_aYjfudvhndiAsB8ekvCF9dRkJtIsrh3ytO0A6yqsYy-4ty8NLDbh7OKlYdt8uEfVkOirxdCuI2v81NUMpZNf9QXwRXHSQlc6P8KvuIgIckBn7WsmIN7NfT7vUjSer_VYc2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇨
🇲🇽
ترکیب مکزیک و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97290" target="_blank">📅 03:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4L_WL-qpHUC78ZL6GJAhtP9_Q4BszZGBDpLzSAjCB3U_agcY5a_WNiOhB-WMF0hARgm67Vli-z8sX9zh-ijo5cQXjfNEv5MuVwi7_TDC5ij2kXF5jpN5jsbFvmG37vmSchK9CKgpBSy1mlvRAY0-Q60JiGYiOUaYBZ0I9n7bnxlWrrmH3WZXzaE0xm98bivv_SetrAYBWuHv7h48QCfxW8LFjAXBQ0DM82Uqk2vdhwC_kLQ8qjJxkcTorFhkJUk2EHXerDJ73eqXmFJ8i-sKFqlGu_hZDwIRnawSFqcXQptiFz3ZkbYlBsbYC4fKorJWR2X5SDU46E0b9hUnAx4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWL2yZMWSbp3HRIQFKboQuyiCG5Boq6hJx9od_NZDS8dZQ_LQY0OpTVlUstcPlH9c6sdoCywNeZ6fErzT-bKs7Edwczi0R5xsGTS1qTBFi9N7KcbwkTWsnCaUiJTdOouUVTcaalB-cs7lE3sZdmRPM8su-FlCjcH_icRrHT-Xvl6gBw4W7txNc4gRZzXHddmNJERvsOTYh2XBQaboMo0fdRi6ijP_o5StpYm_hd7sJQZlVDpc0TOnIg5K8JgePWcD-nvaBSAxoM8ufsRXR7-h4xRB9tq_WYLncQBwqkdyUyonXYGhvsQhuEyJh32Ont6FwI2zNjwAwhapYZ0yQVBkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رایان شرکی که حسابی کلش از نیمکت نشینی کیری شده اینجوری دشان رو بعد بازی به تخمش گرفت و باهاش دست نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97288" target="_blank">📅 03:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97287">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7o-XOu3liVrw0U5qxKM61UHEwGFf4FL0R9FS6Ywwz2WCPJfAbvHNC1dolwx25WNI4umzjCUOLACDXDL6jq6ri9N8H_JmJYBEUtVi5y_ydLjtGjsuspOGjiJjv9u8H2p1EIXkdeh_IkxAMyIngsdFrrQIoX3jfzTVSjhhwdIl5SQVwx7BDNqKZQ5MA48jBvYlqMeu3hQXaG2SHnK0TqRb8djDhWhdBjVEV-fLqikXyicOpxq4nKRhq43SQ_DgT9dTKmhlmoAFDufDipL94fKfaXMP6mSa3XzeIDtYf0-sQWh4WKHdxdGTCO3QF22osbUIvRUeyCNepopYCPU2cHqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97287" target="_blank">📅 02:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97286">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BameMFDLfYu6xkZ-9AZZl8CkQ9A9vXeMRwb2mxRx8mTGGB2wbR-wFEFD-jfWxZb1rZHS46MsI9lFidDE7AhwD30_m7Ms_JbianMQKrrU_V6v4MPP1Pircc6B6Znj8RbMLe98CNI4ng8i9qphyXFYPreSTpn6IIDKRpr19PZKlSyR9FLzJZnQ1vkJI9fWD-3MpkZbPlDXJ0nzGz0MHRbzSoz52pieLwdtsK6FNZOLw-0w8nioPdagKIC4n3h0-k6tu79qpxTIMKqMU1pAoQmJiVc-_U_gQjY2Wi3jJ9dGBPyjOd_237rSORrjT19IS7cPkKWcy_YDYXECwO8vfy5C0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه:
🔺
پاراگوئه؟ من در واقع دارم به رختکن و کولر فکر می‌کنم چون هوا گرم است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97286" target="_blank">📅 02:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97285">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCvrZCZp2Adj0N720GHi24pTj4dzMHq2T9zmP_0jGWKQz9Pbryu4qY6Di24Lt6AcWELVqau89AlkHLuozDam6OltZ11fZqZLZawvl25KQUlnsi9YPSQd0jercrHtXhjDrQlSXM5nMh9edHk1eS7uIbvhSEPtEDdYAmdfiV0NBFgWk183tiThU2wQDzPTtmZtE5kD_4e8oMEEsEKkVCxkptugAVSLr4UbVn63iJ6SyjX65D5VzM6T6p8WvHklq5B_-8TXOwaENp5vPw7kTpQ7Qt5a9tQ3kyAyBxuMLmsUIvzJ436Ea9K6yDYZ2EklfNZwY2jjL0TU45gtfSuX8mE_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امباپه با ادامه این روند موقع خداحافظی تموم رکوردهای فوتبال جهان رو در اختیار خواهد داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97285" target="_blank">📅 02:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97284">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Accw-7eByeydRlgjzbn6wOD8JYm7JXOI_Qtt2ZiiDO6p6Koijv2AqE5q5OsJQ9ls08JtDOzHbFoljErGbYWktsCHht3nw63tisJDOFVAYh-vq2N-QCVl0NLzok_uFw3H2HQte31CDybSyhC1SJ6dB0utNzX4vjTLYVWGS2b1ReaGYw_VB_512Hdl5EsO8DQYy_wnaxmr062Yw90PrtaT2PctMSaCeiYGf4SYR-xobCiAzkakz4QR0-1ulECXNSUVOosgxYaBRRZymZ5zItgK3nf2i0-LXWwZ_CNCcloLG_HJrAzdPJyLsjkPng1cJbW-0BUrbD06_fIabVZURIefGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های اسپانیایی با بیشترین گل در یک دوره جام جهانی :
🥇
بارسلونا در ۱۹۹۴: ۱۶ گل
🥈
رئال مادرید در ۲۰۲۶: ۱۳ گل
🥉
رئال مادرید در ۱۹۹۸: ۱۲ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97284" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97283">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97283" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97282">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qw3NMJSseyxIQA9hO9ZGwGv_xX0l9KEZV9iUHltaePrEwQBng227j-CmLvFb2Kz_5gVRp2wOp32GZvxp_gED4vE4_ArzDVuIdKoU9Lv5mAh5UqnW48gDkQTFj_eUdFtIsNrast5ayNrPDlMUsjc7k3T8H-P-d5eaz-reOkBXYsC54z6judwUnZ69aO3byPMLXXjLIUZb4smj3xHhbcFYZ03s-2BgOnSl-5XORGm5Uw9HA6Melh8vm106xCe7mM5gUsEiEmoXzWaMl2qqHcoI9qmpfyvyyS3PZ6GHK_wMDtc9LAo7Kj4XXfeP5SySpErzzeClExLv7bZ6JCx5Mbv0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97282" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97281">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqTS2qwYptO6aV_m5nOQSkMccgjBKo5_-C_AuAh5veE2fZE9kVinYTEupUb-329xSHz0YnYIsX0PyAmW2rhB2QP9cu7wWEx4eq61tYJIEeJ-jifHGe0onzR804cpisFnBPEEjk_P_lzDDIdeWPQC_uUX413uSIjNwTBcYX7XKDc7CEb9oN7hG8cTmgdmVe27TdEpbpPoMvKOQmLaYCLhP3UhNIeg3HNki8E0lDGA5lpZPrBnMXmyAzKiAGApndSN4ctpxbCMOB54pgAgEI3UyAq3SnHDb8D-PWqj8RaiKVhFjBvtcJUEEgrrMAiV9yoqmRAx_FDv3BIBj6-p-vaP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97281" target="_blank">📅 02:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97280">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4Uno2ISxNOjTvgMiLWBpi4tuiHAWPtvwHvJTSct5M42qm3ByIzD3d22yTX3j7zSHApHXcUxhHr2qEdCIKsml4_E5UnAdDpiL83hpBkE3V_rb5zLEqt7PaoJNSI5KR6x4ZworKDZ3U0WW4c0TSHpoYG7OCcfPyDyOTFf4IXWAWHXjraDBA1_ZoG85a3iJpYh9Uft0EP8LpFUkYJLYgwBNOOPWhInZhqtus3Q5V0OCkAhmwgl5afr4Qw9QxUTv110VZBfDpJYP-T-TLsBFaJ0u4DZ-_irn_IkL2pRrGnldBALqxJY0RDzMGCLbSuUuqA4G4EEjhi3GyzzfU6F8QXDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازبان سوئد با وجود 3 گلی که خورد نمره 8.6 رو گرفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97280" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsC0povgGg46lmLCcRxRHFaat0-1BkNv8ZYrEOE5eSCs8d9m8CcmHM7ICLAN4kiRp-GTEqFaUCbicDYF0Uouu8qZ3q5LZ8qxXZ-A16wH_xoXpBqwzpvSgdRCfSGXDQC18bZNh_dycQMpNPi6KmkrCDCJCeUhNIR53umkQXopcLQz1RqPpQEPbsQFL5ePs9MXZjfLEqeb4vRpc4W2Z3_2eT5eKVdDZDHc1awMDDnDQmeyKmOmJOPu-tyGO7uK2kvl7eg-d6eW3E7hrB6ZMOmYk8Jb_DoS4nR_-EGmhrTSSRHcYFqf6RutYkMuBU5l-wVlLtEz0Z_A5VLjhlLFeUn0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97279" target="_blank">📅 02:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97278">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9ah4KnAAEIJvksTio480-4fgZJ9fKf2RJlU32ZZ_RqLPu8eOHkUdO9dCB9GwUqbrrkVoU2FuevzvDaRVU2WY2LK-F1PQmZ_X_8C4LP4_3mw-vTxYaLZrGrwnTNbR_Nvzi6tYMJmqPx20zrV19UPyN56dRnLlHDg3OCuJSYLzNzToVHKV_n-VtFdIkuLqR9lCvLWhX4RafR5x9LVHdFeqawMvE8DvYZdf9utV8UcvWpeuHqU62fr6ktffBTifgYszxKFQjOH1MhhXjoY9MDHIddIip2pg9D3w3RfPTR3GbasOw8WdlVjiQIIxoz5rcdqq4DcdZFwRlMNLPDKfxl5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
برای اولین بار پس از جام جهانی 1958، تیم ملی فرانسه موفق شد در 4 بازی اول خود در جام جهانی 13 گل به ثمر برساند!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97278" target="_blank">📅 02:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvAbWu7pf-60rHf2ajzpZdFVp4Nzx1TznevQYiNL1UjnDx5Ift2dlkBeDdgR9WhTau5WoKbqNc9a-YdwOqwkHGh2S7zH82Bclhq6rI3Zjl1XrB4OHi2bFGEAGpGAk2VUexETRzELssnTdZUBAfrSNQ7Kd_9ch96mu4R6WrOjcn1rSEoQ_SV24wjc2Dwyw8WuxfIfO_4WtGTUfdG2namXKxf4tjcfOTNddn3NFoLm-5j1MO2hP46loZCPQdlcp3x_AUyaU2ni8fYJGVD3F380M-cwznHjpIkSwy7epZqI4CMLZm5EH7gLXflfuAkYsxWS9vEylaP65RthN5NIK_3_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها با درخشش امباپه به مرحله بعد صعود کردند
🇫🇷
فرانسه 3 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97277" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDz4tMiIN9Xg25JrvP1EHEfdHG6lFPt9XfnMzXi7zw6DHJGlzPQ2fWO_oaW-kAgiwWIg-dc_vXHhf4GjOgc08C1bq1O43jSBCUzxJYA-Alrz4JDeLhGt4eZAREnUopFFOS2WW1fmmY86oBAZhV04N9-FEChj9H3EdJODGvwHmk_CTlhPpLg7n7nxNK28sz4Nuh3zVr4uvSyKPZTOfhxgAV5w7gtorVjXFKrUIIkiXCiGTlJQ1gyVA6XOCAFetD9w1vBKoKcRhAavxAIopwL0tcCxvS30Wh9m__CcFsy7NwYq6SjHOHTvmAGMslFBaZVjjV8c_9lanX4iTso_4PHebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WynlDmYWKB9d1_fs42Lbt6QmIT1NCjTg6osOuy2NYBu7B-IXazdZ9k4cEZCXTAVVVy5nfpJZM57o4mJtRLAOv0d886irYSrImjlj5fQetCDbrWig4D3Rq50Kghc6F8TtdJaj54t_6ie-UMHPoI7ookGmNUBnSkD8WBbUONb5y4GBnGg3MbtlJmaPMm3vQvml3qqYYjDufGi4LqEIXWAyNtPrsPKDJ2AQVgTLA2Na1w19PUKk3sYd2fclqmNQKfzmQ7rRnPm8gl_HyZjiG2In9ZWq4fB6Popp9Z0d-jA_nyx69jZoeotpmi7mE6scVH_J3Iec4ZUYdVWJaI0PBR2uJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🔻
لامین یامال :
🔹
راستش اگه مسی نبود بازی های آرژانتین رو نمی دیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97275" target="_blank">📅 02:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnYKfGYH5nxiruPir_OFgvlmQWUTbtd47S1YyTQ5tfultejRk1DwS845KHx-jVxSMmWYCke43ZmXCAgMmvIq0GwV90LVzSlzTXI1erttz1CGfTPbn-n3YA009eU4zSb0zO20Ej5kmkp9L4_fYZZq71b60op3zLr8IfhrLyoVF-FgFfsgRT3NtZSpA2iJBHm5ZCKzXNCD_B7tz4J17zgaPouzs3RqX2h_sTru_cWUSC8ENIfxlEo-6D8E2MliVZN7cCbINEe6wbLhb8C8LSnDUPWPcnJrpJ2obh4jyonG_pewLvcYo301McdwQ-JCK7Rgty_qPntGKLVjD67vb1BbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعظیم دشان به امباپه وقتی تعویض شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97274" target="_blank">📅 02:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFfctcnID1cJHw5v2zPEeXRTJ4sRfPmZEZwXkN1AQzroHZBEOPBgmx0d_NyGmzhUOOuID14AnPsF_gwcpjeDfZIkj1xqz4ZWAFcEV1m6xPnpvmg_QqT1Ukk_doAXDshUoaDAF_1VLCZeqpcBQHQ9gGaoq4QPBSFCJwT53Oh8QS7foV035QMqHbWl_jxx5i8feQ1L2qGAegAqIubi4KZES4BEYnTliU5f_OJ4gChZ8rzVqnI-Jj4UL8IeOaY4xMzzfEhI4bhKrfIU14t00lGabBMGwCHyW-aeuejxqNU7DQ4VL_gm9NbwHS-NfaX05lvyqx4TJpVoej54-fQTq4k3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 تا اینجا 5 میلیون تماشاگر داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97273" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoZx_LA6g_lcsPuYcpaucT5XE_sjFZSEakSSuwYBkIxZOiaBXbjlWUdFIQ2XINhJNJIhnExVhNv5oz43gfmJp2T04mzmx5xZWVag_abs3exnTclDzACt1K2Wi89L7RNRr7bwTyfOL2JhW9tsDYGG9G7X_yZIwE-LlNjnlEwBEC-ZnY5yXQoHKJBl2tPGqaObQaQIPOo9auDulR_djQlbIwPbCufp3PilKXpdH-at1Yh3C3SqgfMNjsJPuD-S5B1oSmfyU2vTxKL_TBD2gT67X5pHl8ltBwPMYKRQ-0ahFK5t1R6gQcmNN2vJsrEM4f_FDHAlH9i_bit-UBwVzMddcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97272" target="_blank">📅 02:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrOSjoL8GvZbyR07R0cYmc8FxcUs3bJqltNiCkb6vOTnllQCE_txq8unOH2qT12A-lcLVQoYWdoy_zo2w4jdFpCEYkovFnL5XvpCshs74muHm1QQ_pF8EYPBd-BX_BOyxxEewjXeDU9SdsDqUHhIcoWt5YbOgrQZsObXoNOK3JN4IaRPWNWuizz__QzfjbZe42NSz3Jfj1qluiK6lNDAjrXyScoT2eBHHT_ZKNahjIvnZA9pKj_vsPOJoYt3WJMHj1R8zDrB54HGTxMRwZ4bvMUNyBbF9GLT0708_el9BX2ZwungG-GiKuAO101Cbxm_JC3p9nrfs_WAkhC0kCWZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR14MIxyDusl-jkzVbZU33n7wUq5YTrhRE6AuceaKp3fHfGNDhtsec0DclC7x4Fg6AexQ7gTrD9Q6Qq503oCoUI7AUSrAGm5MhV6yqetzt3O3HXRfvxN2EvhJaEII9weS3w1tMPXruH-2rqkArZKIJ7-YJZKVhUFoX2_IvnWvs50La9_YXUGOl00isCALuZ0kaK9pCk9QQuKydWQMxev5qHwyxxCuhth_E9RoQy50nhM0T1Q32ySxXOu2LvnarzvNJrbdjT6GJwdhme-XNoINu89Efux7GCg7yvZjGHP-Mh_FslJJCFfdC0kWH79dvPy7Y_lIez3B-sNpC1EIxdx3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🌎
برترین گلزنان جام جهانی 2026
:
🔻
لیونل مسی : 6
🔻
کیلیان امباپه : 6
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97270" target="_blank">📅 02:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Bpqgb08IWRJykjEPM_auQMeNSdxc9lKgif8E2RFYPSD_nHbVWXLpiPyGgf1JQekbyUOY_9TkKiHRw8ahSeS7a-_YDYmCgbd_cG6B07MKCsQFcTuZAAIn_qzrRSZ5-uAhATpiQDhLwUKMogYayqfQply669rL6yqa5SMEKJMZCSUM2ZGPwPkrl66_h9ajKrM03tPcggrW9RIi63S7mYiyGLo7KWlsRASJf00hRSikevnD2K_H1dXfvY6OdUMRrsTrZmeRTcl1b-GnqPd8H6oZAsxfJihCKsa4lcnhenbEICo-DgrMglyFB-R-fepZSV3BSEVxt2EY4q8Z1SGpyiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانسه به اولین تیم تاریخ جام جهانی تبدیل شد که در 5 بازی متوالی 3 گل یا بیشتر به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97269" target="_blank">📅 02:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=c7Bhqd-GaqPT3B9iK4By21gFSE19v0n2KcG7LYQNUVHDgtwRStDQmnN-6Ze2haTgmE_n6pai81IWGUHlUCq7HmFcXzzCnc_jakt6pue3id7r6aomPi6drgWpD7FIp7cnW4mI6z6qGjj0J8IBY18hv7VDTgwpr6fCGCIw5Q5ifErzxvqIJZZZklSnAFE9WZ40B-kgJUxJI5NzSOb6TIFUzbLSExA8TjxGS1nVqYQZ21ep4Jk2a4iW2ISJWEL98LP9fKBotoDSB1yHMNUoaJuZEOt0572ROzh11MrZlduiXbBWYnh6GhkRk6sATIvAGtYQ2gqBLEgRtFUxEBeYNmkCtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c55785b7.mp4?token=c7Bhqd-GaqPT3B9iK4By21gFSE19v0n2KcG7LYQNUVHDgtwRStDQmnN-6Ze2haTgmE_n6pai81IWGUHlUCq7HmFcXzzCnc_jakt6pue3id7r6aomPi6drgWpD7FIp7cnW4mI6z6qGjj0J8IBY18hv7VDTgwpr6fCGCIw5Q5ifErzxvqIJZZZklSnAFE9WZ40B-kgJUxJI5NzSOb6TIFUzbLSExA8TjxGS1nVqYQZ21ep4Jk2a4iW2ISJWEL98LP9fKBotoDSB1yHMNUoaJuZEOt0572ROzh11MrZlduiXbBWYnh6GhkRk6sATIvAGtYQ2gqBLEgRtFUxEBeYNmkCtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم فرانسه به سوئد روی دبل امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97268" target="_blank">📅 02:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دبل لاکییییی با پاس اولیسه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97267" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلللللللللللل سوم فرانسه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97265" target="_blank">📅 02:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب اولیسه تو گلزنی طلسم شده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97264" target="_blank">📅 02:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ks0seNiKaVQX5wV_kgQGnaSWBfADwBsVgi91WQ18cxJ5iB7g-3qKe-ZGoxrithhclQGdYhojD_-z6LZKHplWFDMv6erCG0ZKU8jvab_YVAiRvcM3pIkz9ijIximrrXMjB2lrJrKmyM0a7ZtdAbxK-x4wjLa0xsohWdLIFaTJt1j0uRn62cy3DnaZxHdN1CAXu2enBA7C7djJnHOJPvREcoepmaQ84tQeKx_lXkX1tjJMMcFUfSPH6kA1xBtXR0I-IBEKElYs3DjJ9nu0LbYftXjdAuiDN7jbXeXcGTKzY-hHQGyO9zKgAuoSiMA0e_ry6PXSYlpfmoH6sQ02bQB4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrBo5iH9FLSQzDKoZlqcyKF43TRSef7NljYv9XJxLHIAz1SPKxONRuqZzYkc4XOBRuUXzwdFe-HdM-8LxpMz8YEqtworuW99jhP1GO-GTJRps05tq-vg5cb69EjIwTdW-KpbkFumwYUTLIP1mowcNlF18O3bgT__AANfBcGPZccjXjbLd7FGYOHpsbIoNsO8xqwGSavaAB3utjS_WtYeUPKVriWPP6sPfXyMoGn_Qm4WaXuhvsfzKuWZmPE-gjp8_WyNUZ0ci1F5ti3xwbKTjF3sw2tysBm888Tu-2KbvvRCtqJL8vlApCsxHiSGx1_zNC08wr_r-HVfLlYl3wusYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htmarO3nt98G8vjQibozQ2iJ1GF5AXOQ0FjqMmrH0WHKAizmmiddAc4Sjtyw7eE6rSYMBe9fYYZ-Uc3uRYx_ncp2nvinKn0UERJaXpl8lkoNaw5_6n9tuR2IFfzCK4B4z6mr6v_T2PTIrzSMQ6-6uqx9lL-J3VOhQWg6A2mllAigyNvOgMDWrmqKek0pZuOxLyMrsOf64UlUCXmj0tZ3QTa4GsQEcenOij0Dh6jeG_U5YWA3SDE06Ok9EqXNwcR4DvPy6UfsYvpyrbHmiZc1oATuyjnwI5HQx39w71Gklr8Kle76fdgogqDEVllZeoFu3ShVhXJnN5jr49aBqCXLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMJFckahQKVwJjWukjXaqA2C6D1p40w_ha8R_fa2RTTUgaIBNuTgT_60IfnxeQkhUYbrWcABx9xiW4HCcJaA9pEY7iMXZdNNljF4RDNjq2poTWzgVLalADQgyHuILuy9Wju_SGYF5tg9DtKkf6A3gmFUjv-Dq73tY_OfuJ8Bo5rzrZPoD0JQOGGvuT3etI8J-om8E-Plaob5peQf7rG8qKz1CbJKgw4Ht4htlF-vrBwTrBnECcnqzNikqgn2ij8pwv3Zr6VoBXb3WjBEWDGKI1y8KjbgN33m47-XEobNOJt6d_uccfHVF5RJzoxuW4VjBu1Z1pz-v_Gd7Wiz45eQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CK_yJndvwWSyuDRh_G1LrOSL4e6w4T6ZZuX-wpUpQAwTVg0-lWLqCn-Zdz8PwQcGCfTHzmbiwzyOXERjZHF--fH_GJDQi5NSgBEf7EDBmgms78y1ZV4jiN1vPnjqWJLaFAIjvP3_4FLC18ei7jIO8oVBw0wppH4uV0D_yakx5m4MQym-mDy89uxpslCcKPx6WT1oZJizMR2psc-0x3weXWuCDmZKoPapAHpYxXpywdZ2YMn3wSOXDMtqiI9tM00-oY981VXJ0_sE1DZMgBYneDGxKJKtBYzcg7A5j7YzwRIE8HNPDI0vsFk1peM5MnF7gV91q0OJ-C79oiAjoKYPjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای سوئد و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97259" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ngCz2yzsAZn5c6bAOY6f30gtwrPLqIBgXzTRB3Ei6lmUZcMlXWINUCt4TifE7jES6fe4qoQiZsGNZ6wQDv48O4r_qGKxqzqZCerVJtze28R-5O3jGOgJeLRmgyW4_oqSOWGkh6ZvB6HE3yPh8x-1fkCfB15goqK4fK52Iu-SC2YjACt0l7Dlyv_XEP1ardZPrZQfd1P4AXWTsrkkz4Oj33BCTyGRZjywXqd2g2EGr8PmHYYgozT2DABDLbLdw5TxJWIxJemXspwLsQSS-QzsLGnsE-59G594R7KyIUF-9FabiJLujVhczBzOByNZJd7Mue89hxB4NFJwTARLYWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97258" target="_blank">📅 01:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گل دوم فرانسه به سوئد توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97257" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97256" target="_blank">📅 01:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBO2CUUxBqJCoS7v-NqFI0dyZ4Gvv9QJ02bvMuwPAX27JdByF-2uWxh7EWVBQ50f7Zz8wmkdiF0lZ3T7A0v7ioOF8yHJrbe-0yRU8aJ3vGQfttUp6Hn9gqa-cZpeRC-8O4Yv1z65lz9gYrUGw6S3NdS_1rJ-XgYk7feXrTDutnrPQ_te7-ROB-8xt3DRSSq9eeGCYvXuYp-0LEbfM8C-KKTt6sse6kbPAu4vQ9UKxSusFCIPhBmpwZgWnuh6CCApAhz9QTTwEt1hHYNeG2Fbdkt5FeW1vl1SWkGizWKDsSVT9v9hatwmZ2_p7Qyt7WFtKo9uYKbpgBhIuCq2TlAy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه تیمی توان مقابله با این خط حمله رو داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97255" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بارکولااااا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97254" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلللللللللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97253" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و سوئد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97252" target="_blank">📅 01:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjd4YKKz9_9jyWgORz4DkwfztxGSSRWHTOhB-f6bI0bGnBHiOu_D1-kvGGiBz9ECPpxfRiq61QRDo2QkcqJbcs7ZPWoAeQibTwYiFswCHNpJT8cBOh22jS9F9xSAB-v_yYcBOYBa4PvZNfnSn6tUCI-gwBTY1shnyFP4Tw-wvVP5INIn0_zcU6K5JMjeirn8p56e12XTVMzokrIeKq8YnwNMqxAxVgA0PSDE5R-3doYe0w-uQu6Vp7T-n-c83HigBqfI2quWhf48aUmBSK_4ougqgBzPq0ichGXbj4_KccS-myjBMpUmwtcCS4l_vSmOmFlL_i5LMaD_3p77LK03yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
امباپه جوان‌ترین بازیکنی شد که بیش از ۱۷ گل در تاریخ جام جهانی به ثمر رسانده است:
کیلیان امباپه در سن ۲۷ سالگی به گل هفدهم خود رسید.
👑
افسانه لیونل‌مسی در سن ۳۸ سالگی به گل هفدهم خود رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97251" target="_blank">📅 01:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97250" target="_blank">📅 01:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4KpSPNU5VPTA3CT-85K3mrQOdA9wXAw2B8Q8Yxgk-K3enzArWWoEwTscoGdP1jsENCLL7JCc_P_M7l-bZWuWIUm0DR6bXvfFQdoVaMtMt6on_EP5EQE0DSEP5uWOWfq10gfkdi1ThngeR-ohVN1azLAUkM1jrMQ33vXQ-Cu2gQzMCd25RmvsoQXzyibYwKXl-H6dsjqVOUjPNRKVUDDElfsCAuvyRTph2u260a05F5YjZvYvDWpFj0JSIF-1p7AauLCMuzH6Ov-Ty8FpqQVwAeUSwsdsPwsW_WJGG5QYAcun-xSJeAew9R-yhKZxX9QaoD9boP9ILpjlC-iC62WKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
📊
اولیسه اولین بازیکنی می‌شود که در یک دوره جام جهانی برای فرانسه بیش از ۴ پاس گل می‌دهد، از زمان ریموند کوپا در سال ۱۹۵۸ (۸ پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97249" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbtVeITuDy15uMffbw_j98bAGgPRqVGaqrKI93_iGABVaXKnC3ju6Fq3p2ZOR4HVlHmgZgI_zMhrD_HZ66v4h-LRl3S2Wt7CZ1q-DCdy--v5on_cOQ8qgsKs8QEuBQ0sOWbpIozwsxiiiiVoFeRbqxtSc6OeF288b1vQc81xpMih6GfgtUArrKSq5BDdoMM5W4jryC0xWhqipKJ0ZQIj8vBzgZHZgPlGvFPFspaGqNbZGzAkJu_lklRCmaS5PQ5v6_QTAh2lS-OM1s3YoTTX0WKxMBCFEDzMB6HakNKSqg4zUwCSEfjW5HekYbDs6VN7Ga7xkilY7OjDfLJ3BE4sQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🚨
عملکرد دمبله و امباپه در جام‌جهانی ۲۰۲۶
🏆
🇫🇷
۷ مشارکت (۵ گل + ۲ پاس گل)
🏆
🇫🇷
۶ مشارکت (۴ گل + ۲ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97248" target="_blank">📅 01:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:  ‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97247" target="_blank">📅 01:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOaFI9xt0d0gIya9Ec5B8-IlQI_JLGlNkXD5SmSAccnpbfLApqcn5-KjF4p_0s75R1laHh1avpWY0JfUSIc5hPXdBWJcnA-DCReRybAYO53uydS4YmosX7Am2RKQ8PEBxxzQV7PXx7-ekHays_uW_8TvitUBBT_CwfOKxaBpdNJWMgPcSZHSXvdDLKbqIc5nAIJqdqTFv2iLEa91UyP4qT8CFxr0G-l_ysT8T_UnEVB7TylLQQPrSq_p1Cdjb1sFtmXC4Ysadgq2UFuVggPYb5enFGgGnnMzrn0T8ij3n4Vbq2GmHxWBat_IJxOlCH3oElfCXHtN6osgV3nxIhYtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
دیکتاتور کیلیان امباپه برای اولین بار در دوران حرفه‌ای خود در جام جهانی در ۵ بازی متوالی مشارکت مستقیم داشته است:
‏
⚽️
گل مقابل سوئد
🇸🇪
‏
🅰️
🅰️
پاس گل مقابل نروژ
🇳🇴
⚽️
⚽️
دو گل مقابل عراق
🇮🇶
⚽️
⚽️
دو گل مقابل سنگال
🇸🇳
⚽️
⚽️
⚽️
هت‌تریک مقابل آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97246" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU7sI-CLT4W1n57k-2gcoKSX84JASeHEyVYuzpjUpiLGAnz2LerI6NmY9uDCxK17RhPCfMR7RjaADBcivohKQL1HLFK8gD6q9WRFStE-Lp9xHR12T88uHQGCegejRjw0w_78HP8vyocr5P65eNdO1_gXJdvGnFwflIXUuYv7ufFt22P0v5bUY2DYgXMe__uNk8VQlNCOGhdOfHN13Yx7LtbpGrq5T3pYDaa2PuzDkyClZpfCrrrD15onLfwtoq060UoqYziCkyVZzdSu0SJQm0CDnRXdjsrj82QU2yIrxacIor-yxA0nOXZegIycQNjlohgTD-DFgE19AatmGviBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🤯
امباپه با ۹ گل زده رکوردار بیشترین گل‌زده مراحل حذفی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97245" target="_blank">📅 01:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97243" target="_blank">📅 01:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=uTZTlu2Leguhkwi1h_JXKf9kLcMu9PXTm3lWxe1qn-q8ElwNtS044pWCFOG7Ekgv_xkfKwIOc8U_Nj8IeIJm-ndzBVfWm8fMZ3P92zMDvUK5-CVNN_XVARVYRqT-Ppb20F2qHEfFGMiQfVajIKiSRa8POyVuYGv_DXRPJggwgYudMZXBFGb12FcSHiPuEnv4E1Q3On5-fNBaaxfffbZLPr2Cr6xYFV4ppOxzzNmuJFFCgzs5a73UT4eoISkWJ8lEjQPtkv22aAKcYRqn0QReCnKOi8GgY22csOGqdzomPi7-tCUu7w2GMvBQ3mNHn09KRMh-ahruK_Ebm-J4m9UIlKbmLYMwH5jhSKbvJZMfx80S6h1zCZPsoxPDUoijyxWeAYkhHmpT_BzdkaqKTk7SvYPN7ON9FsW8Pd44-UBzyN-SW8mWwYQFpxJOmoxaJpDnIVv9Oez8qy8_-3n84p9TgoH--pZdn303Rrg9rf4KqzWR6cmVeLCT7ek4D_XK_T1t665ZrMUqhv36OWgHTauKqKev5TnWmwpwR5dlIFhbptCgUqDKZHMPTcf0Szqb8eYsczHdgFz6XlhcUXYQ5334ibY8L3keM9Xhc3BrcLx_iO7Sn_1MexTzP-PlzRf1W7blsJWSWcak2HhoQapn77K0Y2klVtiHWHd9EjEUgNjLQVM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49dea00f2b.mp4?token=uTZTlu2Leguhkwi1h_JXKf9kLcMu9PXTm3lWxe1qn-q8ElwNtS044pWCFOG7Ekgv_xkfKwIOc8U_Nj8IeIJm-ndzBVfWm8fMZ3P92zMDvUK5-CVNN_XVARVYRqT-Ppb20F2qHEfFGMiQfVajIKiSRa8POyVuYGv_DXRPJggwgYudMZXBFGb12FcSHiPuEnv4E1Q3On5-fNBaaxfffbZLPr2Cr6xYFV4ppOxzzNmuJFFCgzs5a73UT4eoISkWJ8lEjQPtkv22aAKcYRqn0QReCnKOi8GgY22csOGqdzomPi7-tCUu7w2GMvBQ3mNHn09KRMh-ahruK_Ebm-J4m9UIlKbmLYMwH5jhSKbvJZMfx80S6h1zCZPsoxPDUoijyxWeAYkhHmpT_BzdkaqKTk7SvYPN7ON9FsW8Pd44-UBzyN-SW8mWwYQFpxJOmoxaJpDnIVv9Oez8qy8_-3n84p9TgoH--pZdn303Rrg9rf4KqzWR6cmVeLCT7ek4D_XK_T1t665ZrMUqhv36OWgHTauKqKev5TnWmwpwR5dlIFhbptCgUqDKZHMPTcf0Szqb8eYsczHdgFz6XlhcUXYQ5334ibY8L3keM9Xhc3BrcLx_iO7Sn_1MexTzP-PlzRf1W7blsJWSWcak2HhoQapn77K0Y2klVtiHWHd9EjEUgNjLQVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سوئد توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97242" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیکتاتور امباپه زد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97240" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرانسه اولی رو زددد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97239" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97238" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91457d579.mp4?token=Eh-q3YYzuynUiAQBazzo2vkORorgOmA2hd4sGu71Uo7YjKji0aAXGFScKBibxjtoVQqa41aQ0yPq4-f_06BjG6czEzk05RCtYYnvdqdsgLXnn2gTVzLGoHhTHmWtw7ly5qqEuzV5PZd-BkC0HVKNEWKpj2LmmwHEHUTAhBbStDRqFqnZ2CBt-vajTc4Ao2JKBnQnDUNd1qMMANSQctoTyZ1_bRR2R2A2p1amV5WsldX1j1cYhTS4DegcoeZ0wiWBdnNsxidP9G4v9EMQZ0hAzO4sl_NkKbKzE6P1N4qXhYRB_jOXlPTFzs7nfPzaMmlr5wCkqdHqWs4q98pYGimayQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91457d579.mp4?token=Eh-q3YYzuynUiAQBazzo2vkORorgOmA2hd4sGu71Uo7YjKji0aAXGFScKBibxjtoVQqa41aQ0yPq4-f_06BjG6czEzk05RCtYYnvdqdsgLXnn2gTVzLGoHhTHmWtw7ly5qqEuzV5PZd-BkC0HVKNEWKpj2LmmwHEHUTAhBbStDRqFqnZ2CBt-vajTc4Ao2JKBnQnDUNd1qMMANSQctoTyZ1_bRR2R2A2p1amV5WsldX1j1cYhTS4DegcoeZ0wiWBdnNsxidP9G4v9EMQZ0hAzO4sl_NkKbKzE6P1N4qXhYRB_jOXlPTFzs7nfPzaMmlr5wCkqdHqWs4q98pYGimayQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل میشد قشنگ ترین گل جام شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97237" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3G57ag3qeAgmOvJO0zGvgocLZRN6W9KVPl86a0ho66D9doMZ5dJjjS3aYD1vwAF-q9o3Q1Mghj4L45_K-xow5KvF3-iVO6KSx-WIL1gNW3CVNYxIZFu71jiLypytC5W2Yf5Xxp7Tf8Hx0X1tUBIicB8g4_2fgnk5jRF-G07Txh3zGy3Vn4W61ux2kp4aCkkBQK6vLhiy0YEGSYmaweK5qtXqVvr06vGzH2I6kart_ai_xsG3E8BkJ2e8RB2DkpTb_rA6_ig9fee4qjwXC0DWyxmxoKxizWFYMirUJGTLHw8QKnDtexFv6Iw4G13r2shj3xbnniiy__veEFtJdoWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام ریخته این اولیسه عجب چیزیه حیف گل نشد این برگردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97236" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پشمام چجوری گل نشد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97235" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs5to1JG04eZzksyJue9KcWvSJ7JbTvfg1NvQdFq3wCqMAlQa6F4t4JOWMgBWMYTtwycxPfnBksxySJZ-RlFWVapZu7wy7n3pyxAVGNoAgj10s7csWtEqjGy8-bKq_3ho3gAKlc39G2Se7Z0G8uH5QiEXDm_GkFYcE4EWT1seZ6P7ckBefSRurkJ7gPyFOMr5LXUWKmPN9LnJHXZaYZcSN5mOfK6ri7bjDJcz024ADUmkDiEddrD955PPPaNvRc-1rKWN3F9X81I2WduxtMTNdARTGeBSZ6OcofpHkdW6MewL1J5AVNbco0cbeXNYb3X62gwJ8HyKT6tCxpedAX1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارسلو بیلسا سرمربی اروگوئه رسما استعفا داد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97234" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyUghlIttccwyc_IKGoru0sh8eO_iikbDoguGmcHfml7s13pz73Uxg7dxfe9hWiaNA7LC6PfYacAr782BGVrE5t6fKyP8X1YeLaWGNKrMs_b_dAFhfCGr4x9enuU6r6LszUGexSa8tHOogVfvc2HV9hNaW02PgK0iA2agMO9HoSvU2WlivZODwC9jyHRg6XzVQ6czGiHnv3xWCE953E1mtIHL9c446rsiE8Gq90lMkY-wjpMiOWmg93M2Y0NnT4vVw_5dRKgCqd6WKUbdbU6dbaFs6g1AIIuUtv787KNJcq-YT-lCzkB7mKT-K1ZRH-BcaLHFSbNIff-pFB-jDb8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFREYm6VAUUKWCRPd4AjW8YD4npi3QORKhJUn7nN24UB9n6WGcpIuNm9G8uRaYF-OPQlSVc36dbeoR_I8aoiknjsRtUeUv9CHUtpaATaNdIh3bCppto-E8rPcaOltoF9YIi4I-D-O88Jgp0fBBnrjLvd-31iwn_h9OR-9WdGDen9qbO1IF1xL6-pITZXi6uOTIAqynDXdIVmYeZ_KLrUSHbrhvSqExKLBS31n_opnkLgixX12aj8GicF01cdbAO-SfOU4YHxvteDLPb1scmz9C436daY6h1tW8oXX6S2zx-Wum4JlmfSxx-ah5I8rI4FVm1uqdSbg4XGS4mAHU9wHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97232" target="_blank">📅 00:54 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

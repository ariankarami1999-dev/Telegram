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
<img src="https://cdn4.telesco.pe/file/p6iFxKZHhHVoicqoie31qkuMWQpjjkTmwkkZHJPC3hCuKoKCak21uaCZkRa6vMC8VpQpieJHWq6JDZ2kLSZR1Vp228qkHmfmG2R5f5_ghKIizRvEyXhv-x1QU-9-qXBJO16AcBeUR9ISY895C0_Im-6xGUNI-3MmdXX3NOp086FzkdaE-oljZwZT3HYuSm0s_8WgtBPTspzynNlJv5ONM7-dLDyA_LqdowOgkamMQujMx_kOrAyE0O_aRmE_q78jtg3dYen9tsNFpB6sE_mzc9Hz-mos7eA_hdQsFFLC2PrqOw73ZL_K7wrOzNmjB55wAHgx6cgYp3kWDRzN5amwJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 121 · <a href="https://t.me/SorkhTimes/133268" target="_blank">📅 19:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
گفت و گو با محسن خلیلی در حاشیه تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 724 · <a href="https://t.me/SorkhTimes/133267" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
اوسمار فردا راهی ایران می‌شود
❤️
❤️
محسن خلیلی:
🔴
باشگاه پرسپولیس بلیط پرواز اوسمار ویرا برای حضور در ایران را برای او فرستاده و قرار است او فردا جمعه عازم ایران شود.
🔴
او به همراه کادر خود عازم ایران خواهد شد تا تمرینات پرسپولیس را زیر نظر بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/SorkhTimes/133266" target="_blank">📅 18:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❤️
❤️
محسن خلیلی:
🔴
برنامه فوری فیفا همواره اعلام کرده باید بازی ها برابر باشد و عدالت رعایت شود
🔴
در لیگ ما بازی ها برابر نبوده و این عدالت نیست
🔴
اینکه بگوییم شرایط برای برگزاری بازی ها بود بماند
🔴
انتخاباتی باید صورت گیرد که شرایط همه با هم باید در نظر گرفته شود
🔴
دیروز جدول ای اف سی اسم گل گهر را گذاشته بود و ما اعتراض کردیم
🔴
ما دنبال عدالتیم و می خواهیم بازی ها داخل زمین انجام شود
🔴
چطور این قدر سریع سه نماینده به آسیا معرفی شدند؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/SorkhTimes/133265" target="_blank">📅 18:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd56fa69a.mp4?token=utZSJLe_UeewHIFBDntgAkTHLSzxOaAIBlGQd9vfV9CBxPR7ZbmwBuNrxkivYTLqtxWzpR4a17bjpb3izah1CI9Oe4N13pLcdsiSwTOvkp3M2AZkmj6YrD26pjHGlIGwOw2Op1GJg3MTmtpdrm0Xnpty1w-K8pY2p0dKvYimotmYFEVC6Xxy3ycrICWN2cFL43mb-Lvi1Ys2ar7OW3Pri0nibEMnewRc8p_2MAyOr_QD9wpk8_vFkeUT1-h75zkO8mqdCXmMdWeZyrowL8AmS0i9S_eOmwUeRqE01_iQ-yqmlJU4tmj_FT10eIeUPDg9Q8bk2Ok5LSYt-qwwLuE1ZUVncg-TcLIPn7eGy-6PacWDfqUMg92-YMq8VFf7V9bn2Ly8xmctLvWDk8fFTG5Qa4VmoMs2F66GGgqFKWIL7N9CkakM6vGh6a9sxkf2syWWkxE55DDoE4bRqrCurIRz0AHMKc3iMYFd7T88tU5pE6DwSCUvuUStsPXdf0turiLGaLaHAMJWJ30W0lJI5BcHrqBMAaVvr7tuUGhfVH-h4AVA-mReZUzP5fDMQJY78bu8mTliJO6LCmZLN6zKFTUGMmlyRhnjgI9qvrFbAKNuwQqNHCD9VKSYPAKn0TH0QjD9WiW54dOMoFP5_5mpBIguJAxgXwIf_STRr_lJs-dOUlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاپیتان عالیشاه: بدترین کار ممکن الان انجام میشود مثلا ما تمرین میکنیم اما یکسری تمرین نمیکنند
🔴
ما نمی‌خواهیم سهمیه آسیا را گدایی کنیم این نوع سهمیه اختصاص دادن خوب نیست و باید در زمین مشخص شود زمان برگزاری بازی‌ها بود و راحت‌ترین کار ممکن برگزار نشدن بازی‌ها بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/SorkhTimes/133264" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b0d9daf7.mp4?token=nYVo1Mk_WsyJOyymrdVS55Ph4MnL9Tn-JkegMgSaXtSDSDL4csdXQGuCYlmjbf1AVTEd4bvKsNhoj_XpTvq4Vpjw3b2UDGI-D6wZGJDyv7NJtPrps3CR8KsMnz6TKvGBPCuyM8CMvN7eilnn-j7YUg5GY9Oyl-SMJ3Gkv0yikDCFEdd8KgWnxwJraKAzAJTM5tkhAuIYbhwxaM_o9VzMvUDRY1n9WIW-OGEIYhsMpBf3KFVrshluel-wzo8Rps1GXRm_XDrcAqpV5IOfFpqECNTNftQrXYKF3M0gdzX1PINQ2sTTqNAJefKg7bUds6e7j-V1FhMr42JtU02_zNY1nLShUxT2d1ZzGDsdDzFtSsomlPLEiRjQcFTcIdkZ4lZZ8MlYdvMpF7amz6MMtHX1e_Wu8gZlr9GYYkzQqlR9S7kkqDmpQZcG_xX_nirUyjQT_Posp1m5WyqOapaDpTJnS5C2lBTdGfpVQKqjqKEloLVWH4H8Jidk53KiFG6W1nqaghojdVaJhqn9nBufyaNdFnGKeOwSUJ1dZPs74EEq5hTvHLr2z9ZrnalTjmyJqjD-fw-PUtsmZ-4trnXczBl1i71FgB3vX-f9QWrakeIaXy_eAmEdGUObwM1lXkQP8r6ExlakgIVY3x_RIDkit_Go14FjnVo65qafpLttlAMEppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
رضا شکاری: باشگاه پرسپولیس هیچ وقت سهمیه را گدایی نکرده است؛ما مطمئن هستیم با برگزاری بازی‌ها می‌توانیم به آسیا برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/133263" target="_blank">📅 18:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf92abe2e.mp4?token=f6MsJynYG898-Wjs9EZBoWT_xRjDsHHMCHSufcKjp-eUYpOINzlFZCQunVW8aMAEggfy7GVox4kRtQNy3zXCN9qNH4LApApczVQnJD79_9GLr5fSusmEy-PFEKrJDJL4dG23iitPyL5UU8V0xPFF_leG0WcCM5wi6H1gu50L3KUBz7392SO0YK2t3Mr3k2EbzqwSCs2P3kQEPmqiRFNESCj71qy8o6uF2VzJxZrD5eHEw69c8tnMrGQj_h-_PtnuwxyIiQNoZdNopd2yhLTjj9U664IwNPBVkG0CcONWROK5AfvuqRW4PQfVK6_VMSQNHhTjag9Xs_0yp6ifJXxLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور باکیچ و گرا در تمرینات پرسپولیس
✅
تمرین تیم زیر نظر کریم باقری در حال پیگیری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/SorkhTimes/133262" target="_blank">📅 18:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
اینطوری که فرهیختگان گفته باشگاه به علیپور گفته فصل بعد کاپیتان اصلی هستی این یعنی جدایی سروش و امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/133261" target="_blank">📅 18:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a69b9d7d1.mp4?token=DCs-sg80zm8MyF1naGtwVu4Jaq2vctWysyEQbZnmtdZjAYCzDPzb1rEVD6kcALFtOrX9-3InjD_gaNbS9rmV5orwh8qlpYIBenLCV0E9k0Aji_66I20Fq9cwxjecH78HoYUa0BdF9uJBrRGGaWj5iTvMfJ92MgraP66wLL7UpqU7KO15KvqP_rsIqrpCubrc1zq6TCg9ARdzeU7MgJetgSIopzPnjWTlukI2ecLcHkE7T3Z6kd-XHDoFszLnRgxYysqhXkGwAiSMWVoanY014i_Ox7ywt44jmVi7iRijzdhHM8G9or_gh11TJJi8yr3WwFuJO3aUPTgKZoCRxTlZZil_ZpL1_lrzzPPFJMnBk7b-z_d3nIw5lRcbnDuHrQDGjsNfxRK_67bCAFZOD3R_snP7UJLMOvUEN51_FVmF6s0lhtUKgxMVr4qqlp_n51AdrkRInTikNqb9iYbzBI5qqjtqNrU2DA87iUcYcSmullEjgZ7OqujNrAOWhpegUhXVbbO442a-AmLJpLtTuzYMlnZNRtU5PrmLHgDInwdmZe5xYL9a6Hs9s2ph_1V4QG-4Yp06LUdR5CZN9bvdl4VDVeUMPEDDMmRHqzhTKwzgfD6xf0ye-ghQbf2FF-_MNoJj9uTnYA0TNKLN1z3OXZNaZkn4Sl2yNAxNkwn2DdAmJyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
مرتضی پورعلی گنجی، مدافع پرسپولیس: پرسپولیس در یکی دو سال اخیر با چالش هایی روبرو شد
⏺
بازی نکردن در ورزشگاه آزادی به ما ضربه زد. از وقتی آزادی را از پرسپولیس گرفتند به مشکل خوردیم. هر وقت در ورزشگاه آزادی برگزار کردیم به سمت قهرمانی رفتیم. بازی های فصل قبل دست به دست هم داد عواملی که نتیجه نگیریم
⏺
هواداران همه چیز را کنار هم بگذارند و بدانند چرا نتیجه گرفته نشد. باید تصمیمات درست تری برای تیم هایی مثل ما گرفته شود. تیم ملی؟ از سوال در این مورد باید بگذرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/133260" target="_blank">📅 18:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133259">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 50 · <a href="https://t.me/SorkhTimes/133259" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBqokCg7jlJAvjQ0XcjcFhKqhwkBQVq1L1q1_hqJEmg7KBuD91SU4-KKvIQd_VGqg2deZiZQaQaMjwXYMNL7o03C1ZFvPMlC13Jibz5Aci-4s9yMRcHxbZeTyUjXXOfqRCMBv7DUGGoPUc6SjtHkXWImTgz4cDdbAhAGNF2_VuePAaW-p67GjZoQiNtVwMoFbEwRibR7RxCARn147VS4BeOeP9V3K1edliMODTvvTeSul8IkJIkjd-Ed4gjr9mevTQ7PthCtiz1pA00nhojIsYV7YMy7FgGgLVfUJVjZ3Owu5XHVpue5S9-PJMLIPQNAZbEMI5NvkDniDwRRMyGyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
رای دادگاه صادرشد؛ حبس ۲ دوومیدانی‌کار ایران در کره‌جنوبی و تبرئه ۲ نفر دیگر
🔻
حکم دو دوومیدانی‌کار ایران که در پرونده اتهام تجاوز به دختر کره‌ای در این کشور زندانی شده‌اند، پس از بررسی در دادگاه تجدید نظر، تایید شد.
🔻
دادگاه تجدید روز گذشته برگزار شد وبر اساس آن حبس ۴ ساله دو نفر از ورزشکاران تایید شد.
🔻
دو نفر دیگر هم تبرئه شدند و می‌توانند به کشور برگردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/133257" target="_blank">📅 18:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
لحظاتی از تمرین عصر روز گذشته پرسپولیس؛ پرسپولیسی‌ها با تمرکز و انگیزه، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SorkhTimes/133256" target="_blank">📅 17:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/133255" target="_blank">📅 17:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
فوری/ ترامپ: اگر ایران نتواند توافقی را امضا کند، به شدت بمباران خواهم کرد‌‌. هواپیماهایمان را بر فراز قلب تهران پرواز می‌دهیم. آن‌ها ۴۷ سال قلدری کردند.   پ.ن امشب میاد سراغ تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/133254" target="_blank">📅 16:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
فوری| ترامپ: آمریکا امشب هم به ایران حمله سخت می‌کند  پ.ن خسته شدیم دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/133253" target="_blank">📅 16:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
دیشب شب سختی بود .آمریکا تقریبا همه جارو زد ...امیدوارم حالتون خوب باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/133252" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
سردار آزمون: حقم بود که در جام جهانی باشم.  من ایرانی ام و کشورم را دوست دارم و بخاطر همین ناراحت هستم. می‌توانستم کمک کنم اما دعوت نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133250" target="_blank">📅 16:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
مجتبی پوربخش از تدریس در دانشگاه آزاد منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/133249" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
اوسمار ویرا جمعه در تهران؛ شنبه در تمرین
🔖
بلیط اوسمار ویرا امروز رزو و صادر شد و او روز جمعه ساعت ۱۱ صبح به استانبول می رسد و روز شنبه هم در تمرین خواهد بود
🔖
اینکه اوسمار برای بازگشت مردد است از سوی نزدیکان سرمربی پرسپولیس تکذیب شد.برخی رسانه ها هم مدعی…</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/133248" target="_blank">📅 15:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
سوشا مکانی دروازه‌بان سابق تیم های پرسپولیس، صنعت نفت آبادان، فولاد و... به اسگاردستراند در لیگ دسته سوم نروژ پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133247" target="_blank">📅 14:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
رویترز:
✅
با اینکه ایران و آمریکا هر شب دارن همو میزنن ولی بازم درحال مذاکره برای یک توافق اولیه هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133246" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🔴
رضا کرمانشاهی از باشگاه پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133245" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSs6KjLfSK6J_Fq5ldfx3CtpK0qDPMUj6M1S8VDbzs-H0Iay6l8bnHNYrfkKY_9uDev-aT5-38EOJ-NpLrVLoFxx1vGxxKEPTp0NRwX7sZxIryzlnG8j61sJ7ykV3JZ1RExeR2Kv8xSjQ_ptf_fkgkcvY0Tl1mEvnu6Z6JKMhAePmDZB5qXeRmEq8G6-QEf4IWuaLWhcioXDF9dTYHa0Fy6-FrikgOZAl4w9Ek6bFIuv7RTN8hwagDg6qVKizGv5Wk4RduIvcxdngQOuyKn5o_D8ZXrmyWv5pyzXBw43ULDuOckpVJYipJPL1y70UKAOKAhBPGAiD_BWjhV28DwGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
امشب با دیدار افتتاحیه بین دوتیم
مکزیک
🇲🇽
و
آفریقای‌جنوبی
🇿🇦
رقابت‌های جام‌جهانی ۲۰۲۶ آغاز میشود، همین حالا وارد سایت شو و
دیدارهای جام‌جهانی رو با بیشترین آپشن و بالاترین ضرایب در اسپورت‌نود پیش‌‌بینی کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133244" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
ممبینی، دبیر کل فدراسیون مصوبه تورنومنت سه‌جانبه هیات رئیسه فدراسیون رو به AFC ارسال نکرده و برای همین AFC بدون اطلاع از این موضوع گل‌گهر رو بعنوان نماینده سوم معرفی کرده///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133242" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
ترامپ: اگر ایران توافقنامه رو امضا نکنه، امشب هم به بمباران آنها برمیگردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133241" target="_blank">📅 12:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133240" target="_blank">📅 12:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
هافبک پرسپولیس به استانبول رسید؛
✅
باکیچ امشب در تهران
🔻
باشگاه پرسپولیس برای بازیکنان و مربیان خود بلیت برگشت تهیه کرد تا آنها یکی یکی راهی تهران شده و در تمرینات سرخپوشان برای تورنمنت سه جانبه‌ای که در پیش است، شرکت کنند.
🔻
در همین راستا مارکو باکیچ امروز…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133239" target="_blank">📅 12:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133238">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
فرهیختگان: آریا یوسفی، علیجانوف و صادق محرمی گزینه‌های پرسپولیس برای دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133238" target="_blank">📅 12:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133237">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
🔴
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔴
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133237" target="_blank">📅 12:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133236">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-CTeeUWNrd93NdfyKfSXdcfpxdmyR0c6O27DRlDiYpjPu7gb2m-17ZYvEjrM3NyQiFtKJqF-DjatDde2cj2sdrKBruxsXaCZnuU3CPOxUF0fp0pe6Sv0kgbVM1-BClHxfWC5MjN_zGgs3sQiiXRd94QT2dyScEN2scX1Kr-BRZtAiIJNXFo1McOm7B4SAFOCio5yILQq7lPPtM5JGi8fymiD80i-i4LCRJdap4ZmnAkHITr9NyYgFiTQnlEUoiIyXuLfbmq7990u0XTUWmL-tywYOcSWrCEtgA7xRikQkPYSFX763m2pv6yHQVX214PtrE3jNCGH21_V5syFNi0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
منهای ورزش
⏺
یه زن ۲۷ ساله که معتقد بود با خوردن فقط میوه میتونه یه زندگی سالم داشته باشه امروز فوت کرد.
😞
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133236" target="_blank">📅 12:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133235">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
🔴
وحید امیری پس از پشت سر گذاشتن مصدومیت طولانی، به بازگشت نزدیک شده و می‌خواهد با حضور در تمرینات پرسپولیس به شرایط مسابقه برسد. او در تمرین اخیر حاضر شد اما به احترام کادر فنی، جداگانه تمرین کرد. امیری برای شرکت در تمرینات گروهی منتظر موافقت اوسمار ویرا…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133235" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚡️
23 ساعت و 55 دقیقه دیگه جام جهانی 2026 رسما و شرعا آغاز میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133234" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133233">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133233" target="_blank">📅 09:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133232" target="_blank">📅 09:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF8zutx2ZQsp0ojsUrUg_cGl54sI5zQRdqrE6belxHmn-i13JhF6P7gctAdzobKoaB1149D33G43cSO3fBf7IrFKtHsQu7obZdlC2Niy6ncaYOSZgcLCQIfIylEq2cF4-otrzLmYNpBTMIVjF9woBlTot0uEbDqgddN_R9pzfMJ8c4Uv2hg2Hf2vlG9gHuPgzcmf7eY7sSRhp0KCGOguhBTKnymOwtcgheuXGVeLsWOeU-k7yBVAiWys2wrBEkcv6XUlvVKYmw401A6qEdgipV8cBecoGxkB05QPnFSXqBff-06db-tu6EBamGzAn0adrGvQOwAaX3O2VqCl5QYC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین محمودی امروز صبح برای تیم ملی مقابل تیم جوانان تیخوانا به میدون رفت و موفق شد یک پاس گل بده
🔴
علی علیپور هم موفق شده دبل کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133230" target="_blank">📅 08:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
ترامپ در گفتگو با فاکس نیوز:
🔴
آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133229" target="_blank">📅 08:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABISBTNwaDRV7gAn_Mfc89mpNP8SsGvTFbPPtOlz6suhHucRxj1THa2dlunM3Sf6qdweV5S4pVX97K79eg75dtaNzRcVbGXMKAyS4PZx517BYCy9EnIsl4r10Jy3igwb3Sz8BpKHvVrNUt2PfSAogxxX5-nrx8aLwXUwnwa5Bw5hSuCTQ74cfunZg7U9yL9VEIKV_hBbUHdOLGIEp_xMdwY3857M8xbg6BCqPVOq1ZnHwfUDZfgpwFxJtG3b10eOdenHnKXrEkOJRHtzXQLjtOjcHAyNvSkLa38Dyn19lruHpXQB_tyBzGj04zTkxj5tw087xU4etwxu4xQkfcqiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیگ ملت‌های والیبال / استارت شاگردان جوان پیاتزا با شکست مقابل برزیل میزبان
🏐
برزیل
3️⃣
➖
1️⃣
ایران
🇧🇷
25|23|25|25
🇮🇷
21|25|15|23
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133228" target="_blank">📅 08:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
آمریکا حملات شدیدی رو به سراسر کشور لحظاتی پیش آغاز کرد  مراقب خودتون باشید
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133227" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚡️
⚡️
سلام به همگی صبح زیبای شما بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133226" target="_blank">📅 08:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡️
⚡️
سلام به همگی صبح زیبای شما بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133225" target="_blank">📅 08:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALtGgU1rvUzYqee1Qbo8hgVN_Wr5dKxmI2acha58Y8c7q25hlnAsoGNaHIkf30q8DTXDBJc5bHU1vqGCFUHSwD1eta3aYxX94-5Uftok_KT9kQR7DtBkCuWpIBe5pKlIfCB7hlf-83ByUqUb9hKDOTaSsRKgKLV9KpKK7LCJXPhmPjdueRHHPhQQOXMhrm7FAG_GAVOoVdW5n-0X502nbKBKIJurMBWLpxCXnOUkObQuIYDYvL9KroEHAgtIaBcn1PQVEnVZNZejOXAU5qPGsKVWCdmPYqWP9-rT4kKjZl1NmAU7U7zqI8Uh8Z_bs0XlNQz968qLzLlKJ5WoO8nWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار چهارم از فینال ان‌بی‌ای رو بین دوتیم سن‌آنتونیو اسپرز
📀
و نیویورک نیکس
⚔
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133224" target="_blank">📅 02:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⁉️
💢
صداوسیما: برخلاف اخبار منتشره، تاکنون خبر هدف قرار گرفتن منطقه پالایشگاهی عسلویه تایید نمی‌شود
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133223" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=K5XvjnWzRI9ndOn6nwuhMTYgXQseXZ0RLXeRC2eVFx8ZnoOggtN78coF2Eih7ScZWvFQ1aRiQJK4CLYzH4FcCkqyLEsAIex_U8G73dt_TuDHfQYcWyGmw-3NLCL9p0DsBEoaUb7vUaYObFDuLSnrFHgeTV_J11GrJdBeW6MXsGlIMr59t7IcM2KT5EiBGd5AqVlAkJHCMgYxNKuhU5lbrjJNhvrL4pQlUM_UQJbx4xaJ9gmKfEXATGPEcsocSUZC123cZ5sZEez2P3CpJY8U-Y3Pq7_wybq-cL1Mu7tIsuC2FSQSx9xzWmFx7jzD3TSjz0CGVv3yL3UsoxfmH-9aeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfda20aaf1.webm?token=K5XvjnWzRI9ndOn6nwuhMTYgXQseXZ0RLXeRC2eVFx8ZnoOggtN78coF2Eih7ScZWvFQ1aRiQJK4CLYzH4FcCkqyLEsAIex_U8G73dt_TuDHfQYcWyGmw-3NLCL9p0DsBEoaUb7vUaYObFDuLSnrFHgeTV_J11GrJdBeW6MXsGlIMr59t7IcM2KT5EiBGd5AqVlAkJHCMgYxNKuhU5lbrjJNhvrL4pQlUM_UQJbx4xaJ9gmKfEXATGPEcsocSUZC123cZ5sZEez2P3CpJY8U-Y3Pq7_wybq-cL1Mu7tIsuC2FSQSx9xzWmFx7jzD3TSjz0CGVv3yL3UsoxfmH-9aeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز: هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133222" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133221">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حمله آمریکا به جزیره هنگام
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/133221" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133220">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
✅
🇺🇸
فوری به نقل از صابرین‌نیوز:
هم‌اکنون درگیری شدید سپاه با نیروهای ارتش آمریکا در تنگه هرمز
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133220" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133217">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133217" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133216">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
⁉️
خب مثل اینکه شروع شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133216" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133215">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| منابع عبری: تحرکات موشکی در ایران رصد شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133215" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133214">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
پیت هگست
: امشب شب شلوغی خواهد بود،
سنتکام تاسیسات ایران را بمباران خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133214" target="_blank">📅 00:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133212">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
🔹
سردار آزمون: نامردی در رسم رفاقت من نیست، من با این بچه‌ها نون و نمک خوردم. دوست دارم اگر روزی مُردم با عزت بمیرم افتخار می‌کنم ایرانی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133212" target="_blank">📅 23:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133211">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
سردار آزمون از لیست بلند مدت ایران هم خط خورد و رسما دیگه به جام جهانی دعوت نمیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133211" target="_blank">📅 23:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133210">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
#فوری | ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133210" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133209">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/049d690382.mp4?token=jS7H3xZl2Vfp63BabfityQ5PNH8cW3s-_WweAqYrdCzJCuAn9snsg7dJ8OGb85mBVQ4EXh-vOtSrkigILak5gCxwaLT4Z7iqKvZTXGy_WRHACIuBzb6Zx3n-ppjg1jHzuSUvYeJWSWDFjNZYmxkfu6tqOUXdf8V5WUT5qxvQ_QCiCEvfLVI2CEgAMYaqj34GF5t__oJW-nMeZhNSOpM2xtqljkZLa7giOey3kDx9mZ5-CcRy-O-GRL5GI3TBSA80Xa8b6QxkQTDbDUYVhESxDvFH1ogxDzD8f1yTHL6funlkd5NKhKJhqfgFzDitScdg8t-sY_Ov3wYq5ooH5YUnwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/049d690382.mp4?token=jS7H3xZl2Vfp63BabfityQ5PNH8cW3s-_WweAqYrdCzJCuAn9snsg7dJ8OGb85mBVQ4EXh-vOtSrkigILak5gCxwaLT4Z7iqKvZTXGy_WRHACIuBzb6Zx3n-ppjg1jHzuSUvYeJWSWDFjNZYmxkfu6tqOUXdf8V5WUT5qxvQ_QCiCEvfLVI2CEgAMYaqj34GF5t__oJW-nMeZhNSOpM2xtqljkZLa7giOey3kDx9mZ5-CcRy-O-GRL5GI3TBSA80Xa8b6QxkQTDbDUYVhESxDvFH1ogxDzD8f1yTHL6funlkd5NKhKJhqfgFzDitScdg8t-sY_Ov3wYq5ooH5YUnwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ترامپ :
🔻
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133209" target="_blank">📅 23:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوتبالی: مذاکرات پرسپولیس و هوادار برای انتقال امتیاز به مراحل نهایی رسیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133208" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_5IqqEgRVtC8hbfO-tpUk1O7-x1DObf4gkG84SVScs2pT9ltnsssBmv4yZ04o7LrGRZTbwbkFQTF9VKvpWqA3vPlGB0L2t6KRbNZ6egTEBOFseoFDB8Yl7ZSsBHxjaejZrH0ujrXwHi-rq5NTNBIsmXBQkvziL1UJKFjhKjT8IIuKr9WPyBRTHNYI81vSUykOoKt3-xUqoXctXAvDBZX9MImUBUwM4thmi_EqbrlI1sildlbhOsziWD_ibqRgwpfgCuG2fRaxZJiPwc61lQewI2eE2RtSI4gUW_WV2ujB0_T6aFG0rhGHRfRScgwBvLReRu9MwIR8QvOHr8J2aFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امید فهمی، وینگر سابق پرسپولیس و فعلی نساجی: در ۲۰ سالگی به پرسپولیس رفتم و قهرمان هم شدم. واقعیت این است که چیزی که در ذهنم باقی مانده، بازی کردن برای پرسپولیس است و هنوز حسرتش را دارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133207" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
قول ویژه به علیپور برای ماندن در پرسپولیس:   امسال کاپیتانی!
🔴
#فرهیختگان:  مسئولان باشگاه پرسپولیس برای اینکه علیپور را راحت از دست ندهند در تماس با او پیشنهاد مالی خوبی را برای تمدید قرارداد مطرح کرده‌اند و حتی به علیپور قول بستن بازوبند کاپیتانی هم داده…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133206" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
اوسمار دو سه روز از باشگاه زمان خواسته تا بتونه خانوادش رو برای برگشت قانع کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133205" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
اوسمار بامداد شنبه به تهران میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133204" target="_blank">📅 22:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚽️
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133203" target="_blank">📅 22:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb3041a14.mp4?token=qU7odVBrl_Nm1II0yt0FWXCd_bozNbWPjDXK-BkR4Nva6qIgRrBIpzhi5DFJahn_Vm1_Dovfw52icoy_V_3ozj8dRCnqkhBBklpS06QaOp6PpBRfzg1T1mJp91e-48vh84a2_Hv8yo5stER9oI--kLyNWcKId9dDbGMtkbZax5NJGKQ5nZO1ZCXH1TOzoj_juRzF_G81IDRRoKN089BSTbwB5V-VvAfI_erVSEZoh_q6jYaA2Cw2oi9Jj_VzpqOthzZTRZVl6TR2POx4LO_oM-AB6RaO2f0DMAb51qaqBxSNRuPHa2lXHpt6aD3egQnrkQBj_DqL30H_HNMiqR3QrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb3041a14.mp4?token=qU7odVBrl_Nm1II0yt0FWXCd_bozNbWPjDXK-BkR4Nva6qIgRrBIpzhi5DFJahn_Vm1_Dovfw52icoy_V_3ozj8dRCnqkhBBklpS06QaOp6PpBRfzg1T1mJp91e-48vh84a2_Hv8yo5stER9oI--kLyNWcKId9dDbGMtkbZax5NJGKQ5nZO1ZCXH1TOzoj_juRzF_G81IDRRoKN089BSTbwB5V-VvAfI_erVSEZoh_q6jYaA2Cw2oi9Jj_VzpqOthzZTRZVl6TR2POx4LO_oM-AB6RaO2f0DMAb51qaqBxSNRuPHa2lXHpt6aD3egQnrkQBj_DqL30H_HNMiqR3QrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
🎙
امیر قلعه نویی سرمربی تیم ملی: برخی بدون مطالعه می گویند جام جهانی با ۴۸ تیم آسان تر شده است اما به نظر من اتفاقا سخت تر هم شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133202" target="_blank">📅 22:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiJvdde999Pnb_QH-SfB7LXYqC6RyBk7kNPHG2YwMnipBSuJ59_Ek7J1yFGM9WnvWcflUFtG3twLZX9P0i6pmA5YlYILPvl2d4rjCkQIoCuGEthaHIyNE8jIF0QCGasjTfCH8_COUM_gcVpf4MP9MRogzfuds4WOrCpSWXny4zYjLJADRcMUuo_eeuHH-vmV0iANyTt4cw7RCH3swgavk88Hhp2kNbW635xp3TQTelTleSZZxjo2D6eZGwzJtF420mIUZFZq913yBQKs6guJ8z6zLxQQCUgiv_5xhCGEPkOvg2bqxGrZjY2FotL3tzKXBuA0YlLKxOofAjOkvvdkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جواد خیابانی از صدا و سیما خداحافظی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133201" target="_blank">📅 21:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13HU14EUlamKefoC0LiP9hUn4GnX7KH_CdB28noUk8dY1Pt9cq8Yqh0YcYwO314IQIKu9rAaYlxrRO6DoIQaiZOYy1o2jhqOLxPrDyzhLk_GLWgPEuZPJMy--N03i81-N_kZ7qy2mVCb4BvzwIj-rrqOzVePC0bmKI2AgH_Rwkk0RhAo_p223Faql6sksTFiiHHAIY97g6_tM-Kq4VKeTZYSHBqStxIIHOaok8FM4zGNgHc7naizkZUHrSSE6YWIRtSwW4FNv29YOpI4HVuanghpKom4ucL62b4hYoKcUJs8EWOCRa6V8UDtbKzX7e-AWZUjoAhmtXWVrTEz-Qglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇺🇸
دونالد ترامپ: "جام جهانی ۲۰۲۶ موفق‌ترین جام جهانی در تاریخ خواهد بود."
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133200" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133198">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
ترامپ: ما با بمب‌افکن‌های B-۲ به ایران حمله می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133198" target="_blank">📅 20:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133197">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133197" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133196">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
🔴
غایبان پرسپولیس در تورنمنت کسب سهمیه آسیا، پیام نیازمند، حسین کنعانی، میلاد محمدی، امیرحسین محمودی، علی علیپور، سرگیف و اورونوف هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/133196" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133195">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
ترامپ به فاکس نیوز : فرصت اینو داشتند توافق رو امضا کنند و زنده بمونن
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133195" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133194">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
شایعات؛ به باشگاه گفتن رای بازی گلگهر و چادرملو برمیگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133194" target="_blank">📅 20:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
دنیل گرا به ایران بازگشت  این بازیکن خارجی پس از حضور در تهران، خود را به کادر فنی پرسپولیس معرفی خواهد کرد و عصر امروز با حضور در محل تمرین، در اختیار کریم باقری قرار می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133193" target="_blank">📅 18:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133192">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
مراسم معارفه رضا جباری امروز در ورزشگاه درفشی فر تهران برگزار شد و او رسماً کارش را به عنوان استعداد یاب شروع کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133192" target="_blank">📅 18:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAFl-oyfex8IahkmRZSKNciQ9WUSkKMRLRYXti2r4mz74_0KbuAPvayNm_DsKt0ntclNdA0xqhuc6Bk5Ph4rO0DimnZlXEp4pUhHYMonuevkui4iLkmIJLAT4x2DBRGD-ztV2nkeFs4YRYqvGtd1E2foPo4YvC_UkS4rqXIiDNTz4zZH7wyLPRZqY7NJQLyGlk1ZJPSmAtIQUhFr4FxrUIDm9oxbS4XzJCccvqyelJldUe2C7b6Ck7Ek7vndmTPai6ss8rO9szDVJAGmHcJfvOaO5npkAJEiQNMs_OCCd83Sj0FYlm5WXddcTyED98wZfM53dvhFW9HXrmPCeEoA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل از ایران به خاطر استفاده از نمادهای سیاسی تو فوتبال شکایت کرد.
❗️
168 تعداد شهادی مدرسه مینابه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133191" target="_blank">📅 18:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
دستیار اوسمار به تهران رسید
◽️
جولیانو والیم، مربی بدنساز اهل برزیل که قصد داشت راهی تهران شود و روز گذشته از عمان برای پرواز به تهران اقدام کرده بود در نهایت امروز وارد تهران شد.
◽️
این مربی از فردا در تمرینات سرخپوشان شرکت می کند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133190" target="_blank">📅 18:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvZ-XsaB_UlBESyo3bXGczcmbDbH6fnnXZ9EXe3bCz8_FWS3WPN1es0ybPOW6qo99NMFWT58RjY9V3mk0SfS4pvBTP1uNAJNSava5FgBIE9Hx1tKZHkXjFtZnRT0uqXxEbdB8PSAk7veIlOEQElSKMXsJCNLNVdCLgazb8ppqDbzw5y0Xn7lJ1n7JyXePBA8cq0ROpK4H5pJKlY7KuzKyp6ep8Z3qtWos-iRdPrx-adoYaXEgwRaeGZQDkvgYQ0K6fmxIb8la8WvLqHdhvIB-0uP_KNXjt4cU-ZRRdMHcjdMmAVBP4dSlmkCPen-EIQYCXdbQod-mLbegeO10IY7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
💙
وکیل یاسر آسانی اعلام کرد در صورتی که باشگاه استقلال تا ۷ روز آینده مطالبات این بازیکن را پرداخت نکند، قرارداد فسخ خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133189" target="_blank">📅 18:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
فرهیختگان: پرسپولیس دنبال درخشش اورونوف برای فروشش با رقم سنگین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133188" target="_blank">📅 17:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133187" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
🚨
اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده!
🚫
ترامپ بعد از سقوط بالگرد و حملات دیشب ایران بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133185" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133184" target="_blank">📅 16:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚡️
⚡️
حدادی: دفاع راست اولویت علیجانوف بود صحبت کردیم گفتن 800 هزار تا 650 هزار دلار پایین آوردیم یه سری اتفاقات افتاد بنده قرار بود برم ازبکستان گفتن تردید داریم باشگاه بتونه کل پول رو برا همین خواستم برم ازبکستان که پولو بهشون بدم قبول کردن پاختاکور گفت چون…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133183" target="_blank">📅 15:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
#فوری | به ادعاهای رسانه های عبری تصمیم ترامپ برای حمله به پل ها و زیرساخت ایران قطعی است./انصار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133182" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133181" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPS24ZOB-JJnKfWWfS6C2JXto21COUv2Xm5TyzCdVbNpD1gIu2XHd0fol9LODoX1KMZ8QN3n_lkkCd4Evdr5W6jD3blnGz46yfpGL1SI6-jTWHA4iBduWG8q79UgoOKBpRVA2eT0C5XdvAwBinO0pTbf1aZgO7-H_KHbovfofVhVRou3lbChp8Hbh4LHP_OrePmAhqPpYo1PWKwyb8AqrMbvDetKIjWg89d61AkohYczB7BogRxxyJm9Er2Oy0QiD9Q0ekm1j8S2iPnl9VX-E7vQFXDJJ24Cku3DwHm_VXEJosxBk_WULXb1nKb6oGN8o0pEWULSo-QP-6QRQKJmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133180" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
فرشید حقیری: اورونوف و می‌خوان بفروشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133179" target="_blank">📅 14:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
اسمار ویرا سرمربی پرسپولیس بامداد شنبه به ایران می‌رسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133178" target="_blank">📅 14:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeD2nvvod1jwI5huLV7TnM6jnBmNXpDh9B58kG2LW_7KEUaHzMtBEol3ZeRtMBV3CeITqOzDitBrv-0_uHTawQYxKMf_0xc3TkQAG1yBKJg0gDiBZyfFj2G3IlSH9JLBbPyQS6ojmmBSOC6JUsY0QbM661l2CmKCEr7AF_hEyoPN9bcl0hcotCJGrJ-xKT4Iy0JS_-BCKjaKnXXuVCT_gLvxwmfvfIcoLMMbIW2mKdwcl-GYl4MGQWoJvJuKtIhFyIPOZ-_rKlPS99ofv8IoRkbcaIZHYgz-7P4gJexxi07nHx1QGjJna2n3h7ysAFx0Rc9wpOHo0uI2yAbykxf6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/133177" target="_blank">📅 13:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133176" target="_blank">📅 13:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133175">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
وجود اعلام AFC، پرسپولیس، چادرملو و گل گهر برای آسیایی شدن همچنان شانس دارند/ معرفی سومین نماینده ایران تا ۹ تیرماه
⚪️
در شرایطی که کنفدراسیون فوتبال آسیا دقایقی پیش اعلام کرد که تیم فوتبال گل گهر سیرجان سویمن نماینده ایران در فصل اینده مسابقات آسیایی  است…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133175" target="_blank">📅 13:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133174">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/133174" target="_blank">📅 12:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133173">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neEjVlKf_agU6-A7SkJ1OBVjV3_nFxfVxtJjZT98bgk5njrWbpGjTy1cry87hM_cRWK_lJrSZ-wTY4pa7SSVq8b6kGy3SmEWdd2TNPKif5GPxaQgo4IFj35hxAP7qxYH84Hydf89cnO62f9o-lFYPFThplwRyxxyAP6HF31EjpHMj5fWrWNnz-pLZzzTjcZ6bPu68PoITeNe5aQ3tLrt7q5BEhfj5StfJu2flffhvKYrDnni4TZIlp8bI1c5AVpkv9hnVYS3mS5giLGcZTGR_IkiN8hH8yw8r0JrvrH38bjMiamK7hD_EcMWyx4CoBsotBygDx7_RHmLyf3newIbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خاورمیانه واقعا عجیبه
‼️
🔴
افغانستان و پاکستان که دیشب باهم جنگ داشتن، امروز بازی دوستانه دارن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133173" target="_blank">📅 11:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL1L7Z94EXh24ORz35frdYC0DViHCO5TQQaRJG_MKOwazHi8pRIOSYhJTPdd-cyHWt1BNSWTQZSGkLOKjzj1qUdyDSHVK4Sdpt556TyQlpfLTDEUFHCj1jBKjTHmXHkP2tGfqvSO22u_RUfRhO6tesEPMvBprsDPR8ofJe8MLpO9tDcOOg16LKQlIZJ4BwGxzEs5ES8Ws7rlHUWViu0_H21mPD_musKZX3zuITrkodsuhb990eer9Q05n_uTIpbAJcKvcs0riRtuqeGeenug7vYzr2smsvs2HRL49feYcg8Dvzs0x8TmCrXh_NK5z0ibUhh-D7m9qBdpOgUmaIhfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133172" target="_blank">📅 11:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133171">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فوووری ، پرسپولیس آسیایی نشد
🔴
کنفدراسیون فوتبال آسیا AFC، نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد!!
🔴
استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا 2 شرکت می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133171" target="_blank">📅 11:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133170" target="_blank">📅 11:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
اینترنت بین الملل در آستانه بازگشت به وضعیت پیش از جنگ؟
❗️
رشیدی کوچی: اینترنت این هفته به حالت قبل بر می‌گردد، یا ۴۸ ساعت آینده یا تا پایان هفته!
🔴
جلال رشیدی کوچی در واکنش به زمزمه های اتصال دوباره اینترنت بین‌الملل طی ساعت‌های آینده:
🔹
من فکر می‌کنم در…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133169" target="_blank">📅 11:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133168" target="_blank">📅 11:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133167" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNbEFKTXwB8iMEqtVSZmv0sOndi1FHF7HaWO42Ya_MMIJ9v0UXGWcWnb7up0okEHW3mrcrh4muhjmjac6Fsmp3iFEbBy7kb81ERpe0YseQDmg3zpQQiTFn1br6EU2bEbxNh33I3wuX9cyFDy9Xstp4UrAiWbixV18NJgQIxzYW5AS8CuTBV6dAVPc_7oFBQhXWr65dsRbCkBoCy6QWr_Yq9hGCw0VoxFpYACvwxroXTprJUFVuHHFy6XCe63blxHjG-fI39_5EkjHX-AEOyS_Tds71g6up2BcgoPEVBZpRtY2VnGL1bPEOung6ahmaa4hD5oLLvvqlO5YCRWqJhiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووری؛ پیام صادقیان بازیکن سابق پرسپولیس که به ترکیه پناهنده شده بود به ایران بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133166" target="_blank">📅 10:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133165" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133164" target="_blank">📅 10:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfxbpe4O7uP0tzytmEjMpg0GF5tz5YnAFWO_c3eXPNcfkTTB2lhXOAyfv4_5eRjUXBthqnXUSznKE6XBtdF-0ZDjUBtStOzQWHMNeBzZKUKH_bkgrJNg_N6xbdADeSRlrazambF4CwOF7REcMbwZY1VwfA8Q21vfVRzziLrpw6wdOqyS6Bc3xvR8T-3R6mxoQBQ1dBKRAauBrmHPTWnYG1gbmGXMM0h2vkT4rdfOoOPGUgHct-ocDuWD7eIwybNtMsfUV2o6mzmI2vnlZmpaNdaR-joKXEth2uM8hI_t5zbqQTvwTs8ys8KbfOrFGtICOft6HWZwNHqv-jylVKr_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهروز رهبری‌فرد: درست است که همسن و سال‌های من به تیم ملی دعوت شدند ولی با ۷ امتیاز صعود می‌کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133163" target="_blank">📅 10:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
#فوری؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133162" target="_blank">📅 09:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMsdxdM0U9B6H9A830h-FH19bL_UaZSc1XzieHXGubzzNwtQkTHiRvG9yo7T1juC_06BqR9TuHptMFqwoMfgC461Hc7p7TvtKHy1WjpX3SUhD0fR0AGa7siDha6nMLxMz1x5VNERx7goE6Fb2-h3_pQrUUKAyqYGsvS0M5rDRRGaKSfmgPnuIuUm99dKR98ccjY3XDAF2fSv6QemD-cjBHfwcHGR0AzNReEKVqDlHsKZfugpL9RCSiDJMvUn8WJvQR4M8NxAF0qM-BeGtu7rVAPaemVS0YLZQP3YjdRj0n9KPh-pAFjRLQdJduKO-_CjtEcGqYgv0V1yF9RRQDB7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133161" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIRX5Q5__jkFePu1KXlKc280xuw4I650A9-83Evs9Yf7yWi-AFLFfDnKL-D6eTZMyXLZ7HpzsiFC3jVSpn9TPwpM1hlIS7Vom_gwcVY60lw7_0le2MQ2ljcD-1r5EX_7NAFQ8VgbiKEmqF-JtwTP_-oDfYEUo33fHU-BydMa8xMMD70u7XeOzv0lAsWNj4-iOVrEUUNzNeQBmv8SAgZqAHZvNl0wEAOhCtNoCby8E7z3CgP_6yQgWNELjh-IpyAqDXvic_H3n-U98Q5f0i1ISrBIrGODGv5w3sGSpmz3BY4CmrXDrUESNICa3lUDGSXELjQh9K1akAck65jknG3M_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133160" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

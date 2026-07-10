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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 187K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjnpsJ5xnsaeMh8VZUga0qPWjna1lZNgCGA3KteIt383c0K0UIJ468YE6bjuCi1sxV8-wuhe-W3IJRSSZTuJl8WDExrcaY7UKQf7W4vkzzyFW1PUsg3z3kQvGjxDd5hjvzDwLkHbgzH3uDvkQO8DIgnCithsrwpjxtDQFfW0R9YxpHw8AZRKcERDYm-pJmnVZQktNmF_Pgt7wOReHdPCZxplea_ppnICoSUYWQICK_DYCt3CLz750uNc0kkDgWnm6ckugaSxhDsgDWLAe7NJjKtJBQ7EmtIb9FcZS87aGVxpGC3VkW9VFj3q5SrjHsA9FkTWYQTizxlrcLuV_AjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU9Sctj167KWL5BeATIl-nk7KxxONOc1wIu5Oev-J3wArbgw7XHrar8bg4kzNYUhKFRV5onWtVYYJcfMlAx-CZiHdA3ty9P_rsZKU2rq8sUbA1wUPzg-TN66JvCOCfnyhIXq4Hwby9Bcnf9S6Jg1-PTZVn9yWa3LF1k7Cac94n8kmuEv4YxX6E8uRN1DfhaJyFkMcKnrGO_lH98agkztuaZ1FvXMconYlpgYLAAnfkmzUnEIabPM3eKTEU0h6wvKRAGwd3wPfqPCyjlFg2SPz3gqaUfARiTnkXfB8z3QoH7v3IncCX8vtvyD9TlYbH2tBGB4yISCul1ayCwzmY_oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LobtDc_3YShnkjUz0Zp-1Hz_gxTikobKfg8bpdfkdlkzwhHaBF-2S7SlU0Ci8Xbjmld_PzsFTSVmewOXBBqsoTtHulgZrMQwmJEzdbau8VHuYC-Nx0-KOeEfvWdOJZ8tZtJ6CT2ybk3tPNh92pVl-eWLaaBeem9V8NbpyzeJHPIUa7Jyedj0keEesKNd3Obxg8Kj3If5jDjwhiC6JM88GQqnJ4pr-boWAqBwMcI5hBL5MqdliBcW82sbkuTTmhFOnxbn03amBg4iVQq5Pv-eTphJY5PSUG6tZearYQjaV3IE8pmAhi9ZMiKKBR0gH6EIHmcLLmjj-rryi589k4ArKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiFDIx6SIWVbqqTWdPlEuWDK1EgV9eIIKw5LqkDp1l4UoE0vmb06414c4JIwNcqYOzEu0IEtEiZKyISeI0Ti6qwoDzlI7XhN6Hh_UfrHmGofkqYsVcHdCtSjfAl1fVGZNZ1vxq88BKbDiXhPOmoOfStHm2TIILRtvYOB3GVD7dQuVcfknJf6DoCrZJQ7jFOauv9dfuTFlX6ktm-9nA8QecvsVzVHn9ywBmpZIsRw3ryjUH8ZFlncEG01Hh3JMyvP5fR8G2RVFhryBqtrpe4o7iihLeCjKFOsNuFcUVPGKBNxhPEgHo-a7qVy6f9GczmB5CGuiMQu1dHgX36v63GHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4niFslqZE0AoBZJ-dmltWAWiO_SCAmrBELRcjebG9bGaF0oA6OXrYPFo-CNaN78SNNUV8c84axNMDp8PdUqqIlUpaq8INLezNLXwJBFw_ohvxcsTnpeaq6l2ptEIG-ZbSrZR73fovMYw0TDb-GdIFxLbqSwgCbhhmAsgVqglFUT6790J0kwhS7nakj9QQRevpdvLWmogh4_W-q3xJ4A6w-ztFWjF6_wXWv72lcE4Vcf15UfRetSzPWYzfXMFGGyq46nRXJL2CRNxgyxv6-1o-L5LPE-v0CcmASgrQfFaRTihQ2NK36FSRRW6SJ9tBCNyCrsOBxqew5BX8wrwnWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwga0J5qoQpDy7fdgNWSFyD6jtgsob4p1o6RLRVe_bbKM2Yv986DG5qn9jPz61nvjgCrHM93CyIQx2qqrhFeA3kHuDdkVgCzoq6W_P4PoIdkr3IDxS2oEf9C1_Qvtl04ut-OvLpHEztSWGRp5B4Z-aGQ1nO_GOh8VSWOARsj-j-qQ4m3YKHAX-w4x56IOvL4Z32lxOjEuWvW5y4SlGng_3C52VGaUc2oNK7pmtaqkiRFqNGTKUfGL6o8bZ1U9WEcXUYlgJReQgjS_RNNMcz0OnVd7i8tF-3dtDgT-glPY03ouPHyzYp-dYH0JNPHU-vDfGBpsOsNnj_BKk5DW-GtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=eo6EHCRmN1aCW6hrHQuwpwe5PQGgLnZt1qedw3S7oT0ojz5kq7zhprrW1HLRQ1oF2Xa_tvWNF5BnKInO-MMqTiwChd3PKyHlJBApW6sJ9QZ02LEctNPRpFI6QoXrZKXZsG3oXJJK90OnVZvcuArkXQgiOPhcNtJajaUAkymVYFOSPkOTDeMef0YLAG3agRhCUm5mQZKdfkgHvLtqkmhbWYRXcjPXNKQqht_vO_2zlTNO1eWodMe0rZ4xrOgIWTFYbU_FFMfQNDnu9pFuq5W6wIb6m9S7hBoYCvLkqGZXwHx6glWlVEdVlvrTHHithv0znOBoVE0ZpztRmbVnY-AJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kq3T_2CavGcuAVoxUfplfubHnE7OTK24HASaEC8iwpuFC_esIer8aLaXW_7jmxjo5JKMrUz4phhOGo53KOwJUj_wcJVJYwrHnE1hEyokspFho86RoYZRXSv7y6vdMDI_oMj4D6t9-nl9JfXl9u-wyl_e3sVcsGMdAuvmGKwZHA2_uLNzUBTDy0530nxB493NfUxN4I4eP24UmRQhj6y-hdUNnnIfJMA6XsmMwsZOeZCOG2daM0FRde-Dc35HVZQBwe_5r4SOvQytdlO-RdwZ2hO2KWECNYPp66U1ypJmhI9VkAmUf8t9AAxKeEMizMfH3BSeGDQll1J1ZwROVEYF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmFOMTM5g9RP4M1hg-JuNg-mRtQBtk8IcKNERE1jr3sHd3hQi7TtQ8OJrf5v-6kZb7Zd20S4JblJKy2_ZcXIEPlzkJ53q_i28lpQ6QHaHy4jderSpM6l0EAU78TLUcEHdBIX0KhpEh23l5IunTbIR2axqGtfrJox7fB2ZR1tgUqiBtFV_g40fg4RJXiniDSTASgjMxVLIM5pFZ2y7vGupPvxcgni4PQZi6iCvXgPAhpUs-5dQLPzgvmhWiddAlP0h3lUFkL5ZKettFkte9bXGd3HL8__gIdqQP3cDvLBn2u-B4gzokejN4xRki6G70Vt4MJHn-WP4G3I52OkXAgyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_SCRTXIZ3SnESPG_wvKLm7eAk5tTQrH-orNFDMkurHTpU_u1G3kin7aokjf8YmViDpBkhlO2bC_HPKmoWgv4kJ53PYBF8krzyLKhP2EtlSagyLyRIg_cb7RBWrL0Y1JsXJIzxYRyuSVy6RgGOFbf-6PBxw2dd6rFBgtQ0BgSxwscMp7mYbscfO0K-sfmdD5PeZS1xw3Rs3bGXYIS0VpaKW9pj6roKFBMNCRhJufaMlOihs36iTzJiEt4kd9OV4BuvRc5ZcsvYrrFMInNiJVo5TUTivMECtYrDOOrvJbzjghHxpvbSfcE7_DQ3_7yLRYe83pWfmjX6I9euk324Rv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUFiVTUam7j5aNgBAQeVcLSkDDv5dPSnxrv7k-IW7soSFuzz7lmFn0A7RJRXGpzKbUTeoLNTA-wpVtsizUm0ZLuUtBmxlv8TBdiG4QZSGAJXk-TSFEtsYQquVU3OgtyjSwAaIr9csu4XGxusL2xCRz6_1Uh73jv0arctYkqj2zwPqGJy0-RNjFvch3TgqL64gMrQkCOS0kfHw8YRSteBSRENsqMFUeT2a8Q6vbfXIzVVStwzRWRLX3c_-Sv7CfZhiS8t-HTmWwVw0LPwUglGVosEpQfqQlLtp6b5SrW7x2u-VQKiR4-2XtKEEjjfCdU9B5K147QtFk2yvXQBfEsTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ3EGvs7BLdKgnBhD-wVJV4fZYOc3DT-MSs-8F3aDcMtUjevgoTFZx5GijSbU2X7d4K8uCcfHhqZK-Np-7-o49WhYwBpuRcd6aASn4_qY2UIrsBzKTjFE3CbOocgPUEEDfcpnsGIUK3Lv0N1yrYVX143xtitYCCgXwgHNLicAM0LymJj1goQKq2SoM_cQb35m_nEpfpUe0LUCR3TaMDMTek_2p_RQe6JX7cdrrAQuDoBjGD220FIfwFCv8HbhT-Sgc1s2pZrGxO1VyAjcgKdOh4NY8w4cR_4LVaI43Ak4-NfmrYVldApuvDXk0tKtZ8yJJLcps4iF_hlqA8k8Of-Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=GYvBereNyG8gYKbVUuhFC4y7Dv8MW5m8Jjet3HvxlWIjtBpB4oVHL5GTB-eesv3p4GFJM-VwniOA9x17_z1Jc9Cxc6Mshx3Oz3PVgjdmyTvdLvFj1k28AmqMYQg1n26Xqe8hSB2IyrpnrEAmzIsWpBBm1ipdb8HX2UKTQJUbyWq6oCGTIFwDNVcBfkRMONSJqvXxPoiiv9OnN4oAX8ZHrbpUx_AKp-oQS7YhSayvw61gL4sXki0nHOR60x8_zvVds1--bauEUTUnWMsqJdi_m_Da9FmdDRiusYwETBVwp72PuR625v5_wu5dy0C1rChtdMEZZSxq90O1RnYfEdAiSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=GYvBereNyG8gYKbVUuhFC4y7Dv8MW5m8Jjet3HvxlWIjtBpB4oVHL5GTB-eesv3p4GFJM-VwniOA9x17_z1Jc9Cxc6Mshx3Oz3PVgjdmyTvdLvFj1k28AmqMYQg1n26Xqe8hSB2IyrpnrEAmzIsWpBBm1ipdb8HX2UKTQJUbyWq6oCGTIFwDNVcBfkRMONSJqvXxPoiiv9OnN4oAX8ZHrbpUx_AKp-oQS7YhSayvw61gL4sXki0nHOR60x8_zvVds1--bauEUTUnWMsqJdi_m_Da9FmdDRiusYwETBVwp72PuR625v5_wu5dy0C1rChtdMEZZSxq90O1RnYfEdAiSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTa4ciEXZNtsS-9mIYaFZ-8C8QNW0ALDMuHiKGSN_H5s3JktzrFcsOwc9H4bStkKyzP0_Cvir2lNycIx1q8A1K-XOpwSKyh_NHU5YQYhrid9SZbwgb6NaerJrILEWp4IaxqTRX9m-rFudCRlNt8m8ka-TZ1Hhj1sdw36o2NF5PakfcJ-dwKMxFvFgbgwd-9V4VGv4F2zzvDmD2yOfMWuK-mAysCS0NGKkwOtb3UG9B3wmofl8jBaRScx7Ry0c-cqJCAX4Ooc0_4D-tgY6YqYxRDRTXG1BC_UbltKKIRdqt5N4nVdlzOV8fVh8j8MPlXGLlWHVhIg_VYjHWJ8DdZOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkP4ROuvyg0LuAzH2vC0x4_hfpk2AusRvLjmkPQyfCu43k6xCdLFfnKDleAm_9dZvckmOFyJwRvbiHJxxqw6j0V-QokwCBbZPM3wERnKVau0I1WkIy_yl3OxPD5GTA1Sx3e-9DcM1Rncbqx0QjOWigWCER8MssGGKicPhY3YJaqr0gcMkhr9R9sHAGvyTnR3hFaqCGPPtf_TradY_UzszujMqSnEg71CkIKcQdMi6aNIE0D0nn9RvP2uMlkbygBrxAaCVQvlFHiRCODZ7jFT6KvdzMPAAczX5A0ZUZl5YYfH1M7voQFXXeWNk9dOKFoe18oUQQqmIE_TfVzv12B_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpgXvKjchU0ZSKmXoJ352BssOw6Mxnuu9XSdSNzfYyNwgbYGcmCBgowSiNHyYxLMKWCM2ck3MudTgxirNWiE8pibuW2aWaRiXtE3gMLnlTzrMCirhcgAAtYIEIXG72JlRaeRKb25gGP50q5JhYd9TV9loMFQ68n4I-1gvKGV6jXKXEhhN7eO_Er4UhRS3MhbKP5E36W0Nwdu-Wk-8mLVpObw_SxtitdD9DQlLGtT4hN1a5F7iaNVcbbSYb8xt-SPTIplGDEzuidodksOzOxkjzOm1WFcd-1pDTn5tDHqdsFUDKapIMQ4t2Pq1LprdI9NRd7mFSdPBoOEys5FF0huxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhNerOyW-Q9VCLj1Nrx2m0BBFIHi1BLk8VD4JrJ0Cct0-VAIbI9Dm08QVQY0JDPJH-_1qGkA95f9eIkghaYCsvQdqBSmg2wVBbigpdDDTH-zcIE2-fLE1hD-STFrYvFWf2Q6MTL-yH9lY9aU50jOnOkEWnx1ZEAS4kAtUfDaJ3b2Rt0H74kugA03DMyg83f0yDAOhwkIrODi9Oa10kuJhU0lWa__ZpOKTAzRjWv09c44ngwNTzrdpWeol5gwtFu6clK6YeKSoTo8gLNbNwhHhiZL56j77USsbPXNtitJvRD-uEKd0457JO1wc2swZGYGMRVu-N4OTNZAjEm7CBLopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=jewZEsHY8R1tgGXBmk92AXxWRwpe7vkgUkP0gTpIffrMIRUuvZItWRPdGXGpeRFYzc1Z7snMjUM3sKQDOYBQkrpjaWaMrxlEY55qpKaDrn5rV0CeI44TRTNHibF60vlz20t-QFa_ErhPx85tsGSFtqPCQXZH7ORMENrnxvouESZJHev3V3GKElXT4UzceIlUFMHwxbRmfMPwnbhNYhA4EeVuuOiFwR1DyzTiTwWyDf1-LQkgZdYFgRWlush6Q39eI0i1gLVJphH39h2T76myl3r6oDslqK6_z61Nqd0qokJQbbKd43kFMQ8_gDUFhTzaXocAXf4PUV5vjIlW7_dvWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=jewZEsHY8R1tgGXBmk92AXxWRwpe7vkgUkP0gTpIffrMIRUuvZItWRPdGXGpeRFYzc1Z7snMjUM3sKQDOYBQkrpjaWaMrxlEY55qpKaDrn5rV0CeI44TRTNHibF60vlz20t-QFa_ErhPx85tsGSFtqPCQXZH7ORMENrnxvouESZJHev3V3GKElXT4UzceIlUFMHwxbRmfMPwnbhNYhA4EeVuuOiFwR1DyzTiTwWyDf1-LQkgZdYFgRWlush6Q39eI0i1gLVJphH39h2T76myl3r6oDslqK6_z61Nqd0qokJQbbKd43kFMQ8_gDUFhTzaXocAXf4PUV5vjIlW7_dvWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=iyMGurckNK1Sz0NTZVPmFj1t5IurgGIEbCrqrOOUA6yahAP37zX54LwgMPewJEOPNywkKW7OBB6Or5amF_qMJA5e0Id0knTThLYXoqbKO5oLH4GT8p56v2EeDxff1qwP_sOWtaBdef2ILt7BHd-gqAcjIGi6v4oCuvPdLbD_xGJHC55dxNCCtLqU5NEFIJ7y4gAlPddPGwgK0q0EZYueCrArAAB2tjo7OOcHdZEAsGaQVbDrUMh6UCwSxe318hNUt6Vyfg4BlnSsxPQbzEVAk7Tb-sE-xdFxEMBf6K0H0KVEG6JCyfNv1EOnt1Wxb6hztYKh9zigNFJxDi_oHIPB9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=iyMGurckNK1Sz0NTZVPmFj1t5IurgGIEbCrqrOOUA6yahAP37zX54LwgMPewJEOPNywkKW7OBB6Or5amF_qMJA5e0Id0knTThLYXoqbKO5oLH4GT8p56v2EeDxff1qwP_sOWtaBdef2ILt7BHd-gqAcjIGi6v4oCuvPdLbD_xGJHC55dxNCCtLqU5NEFIJ7y4gAlPddPGwgK0q0EZYueCrArAAB2tjo7OOcHdZEAsGaQVbDrUMh6UCwSxe318hNUt6Vyfg4BlnSsxPQbzEVAk7Tb-sE-xdFxEMBf6K0H0KVEG6JCyfNv1EOnt1Wxb6hztYKh9zigNFJxDi_oHIPB9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=GLxjRw_TXqWnPhdQi8BgyyE3KLQ4dztHlHIXGI7c2qFyW5W27HC-4mCKfg6r0cW5Qqz54fIdYulHuq68yYu3TIVx2NJSJXMLN2c_fpODFQatuh_E6C0AFNmfG_-JO7Jx2Z281Q8eRj0tkrzb8CbtTyBATv6I2A6Qiw1cbMKlYgn390NahwXiIIujw_O0X46O3UMKzkrliVKrXHcjT5H45q9J_Bl70ODLBXfLN9DXHRTLUuzSrtZ6Zc53a4zHl2agwzcIKJKcWii3Bqigav3u0Mrnj84pdg6A5T4JN73JKL3fZGs1RSFTcbrYFfUje5S6aEarZiXg2bMMvqkp_F_Dzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=GLxjRw_TXqWnPhdQi8BgyyE3KLQ4dztHlHIXGI7c2qFyW5W27HC-4mCKfg6r0cW5Qqz54fIdYulHuq68yYu3TIVx2NJSJXMLN2c_fpODFQatuh_E6C0AFNmfG_-JO7Jx2Z281Q8eRj0tkrzb8CbtTyBATv6I2A6Qiw1cbMKlYgn390NahwXiIIujw_O0X46O3UMKzkrliVKrXHcjT5H45q9J_Bl70ODLBXfLN9DXHRTLUuzSrtZ6Zc53a4zHl2agwzcIKJKcWii3Bqigav3u0Mrnj84pdg6A5T4JN73JKL3fZGs1RSFTcbrYFfUje5S6aEarZiXg2bMMvqkp_F_Dzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j14_y4mN4RXkJJlMBijcU4cNydGqo_rSzpYL-tLsmOsZ_8e3zbS9yqAXbEAeH8jjyldy96OVmhtfhEDFYDbg1fbA3dFGp0k7PgXw7JHB_eQoIi9f93vCQMYkTyw7USVYXxNzqWxYJ_t4nn4f8EIv1WJlfXR-B65HAuJOEbrOLzA0L9DaCHS31aFF8AM6uj6iuotMGmYTb_g4ERKra-S6pfubisyGsrGzrELCaxJO7yfF1kIT0k9USLbG4nSBmCOoR_1_NLaG0AV9GHJSSOZoDJUsOhkt126CcOiX6i07enVsHSTajuybRX39ZYV92C2K4O_kabyzUJwU_v3V0tzOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onn_jH4vu02SNDKZX74WZVAlztQ_o65Dc4MdC61etvhYcRVsbiqKaYfWmSVqdS_g0EwOEaOHy7po3PBfB6ISPEwbl7G1506mrnFYRDq4zAYuf1vRbUGmeF2CZfh6EQL1PWRojApOyhx1XWJpMVEZ93mVD_OouWMI74evhEkNj4mhtij4McHELY32HKyn3uq8_u3_cXsMD6FSGbFX3-4Zjyo1xXbhS3XARdAD8LDYan7CRDYHVHamBbHjtIFaMhvrp2VrQgT4_qfr-Qms6wvsVjE0OENnYiErN85Mx-sSm14AMaLeqO_tUnre1nvDrYQOsDvCMprPpAkaH_-E2P_S5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=l6KIWpdSx8xxogpR2BiB2OYkHgoHKsrksGF9NABQqnsyqwNJUmOHOFaxzIaaedXvTjOFgrYNPzvN-eg_GXMtQvkr1oqfl-I7fnmF9L326lhyQoHsJWwMobYDd_UnZplWp21oTE6ws3qDKPlBcvzuKLWRnDB0c1z3KpNWboQyNWGMInU8t_VyvOhUYAyJMVwMt5qkceebwMmg6mij-ggQKeUTffLaLte52qEABpPY4kSOFOLSOvOgAbZ3OepS86W8bUIBaEybQGC2GYrlry1W22iiUO_W0c0NDjfyQxunIC2qGHuFAYRWPe2ndPu1bR13XmV6gftbeT9neBkhI8g-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=l6KIWpdSx8xxogpR2BiB2OYkHgoHKsrksGF9NABQqnsyqwNJUmOHOFaxzIaaedXvTjOFgrYNPzvN-eg_GXMtQvkr1oqfl-I7fnmF9L326lhyQoHsJWwMobYDd_UnZplWp21oTE6ws3qDKPlBcvzuKLWRnDB0c1z3KpNWboQyNWGMInU8t_VyvOhUYAyJMVwMt5qkceebwMmg6mij-ggQKeUTffLaLte52qEABpPY4kSOFOLSOvOgAbZ3OepS86W8bUIBaEybQGC2GYrlry1W22iiUO_W0c0NDjfyQxunIC2qGHuFAYRWPe2ndPu1bR13XmV6gftbeT9neBkhI8g-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=cQ6_kz5CD7BvMREy2bYgCBEUoeZIjx3wahYAnaF4mGnMds9DUT2TrdHpY2tN2ylgD2I8Ri-9baKM13h9nLVzXcnLk-Thm4LIfgbnZ8kXjPJz-oJyB0kZhnzU-CC5yJ24h4gEcAPkp_dBkrkqnDmBhePkIaym6Vlc5L-KP6E0f3qdnp83X9OBnG58zuAEimH8H2H9WhlqgmhpMLW326L1GoFYslgyg-kCoOJ7is1FQR5VuL92SP3OEdlWTy8QKzm2xYC-wjR6Lpy45-azYVSIbe7jEofaGaJRLiDM-LnRBpavhyJ30qaamKS_BwpujJaCr363ZpJvFy-_3dLKtZRyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=cQ6_kz5CD7BvMREy2bYgCBEUoeZIjx3wahYAnaF4mGnMds9DUT2TrdHpY2tN2ylgD2I8Ri-9baKM13h9nLVzXcnLk-Thm4LIfgbnZ8kXjPJz-oJyB0kZhnzU-CC5yJ24h4gEcAPkp_dBkrkqnDmBhePkIaym6Vlc5L-KP6E0f3qdnp83X9OBnG58zuAEimH8H2H9WhlqgmhpMLW326L1GoFYslgyg-kCoOJ7is1FQR5VuL92SP3OEdlWTy8QKzm2xYC-wjR6Lpy45-azYVSIbe7jEofaGaJRLiDM-LnRBpavhyJ30qaamKS_BwpujJaCr363ZpJvFy-_3dLKtZRyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd1p9dBCG-c6VAzDzjiIziuonlDlorAS6E4476N74RE_mRFchvokm7FJWo6T3faPTGHXqqZPGtuQfJmcugvDao8ZTAAG4ei-pCXpi2kxOuYdak0NTENgjFKWjs_1btbA-rR6fQ0ULn1V3J9Ppx9KrV-xF3knRG3NH04CqrOmjI44l2v_QIKGuR2yYKbDnY6RDBb_ll6Ac4cXPspzJBicBJc2rUaeSegRFZ7UyGXAMnqahIBsLNRoKydnHEa62DKtuXjA1LisSJdspVJAJGkaq-cFge7_aFoanRz5JZMFWl_CHWWGVPAYYCTVvQivdAjclbUkM91wq0DxdRluncXLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaftFJj6TndvO0Hiae1fgpIuuvuc31Jt8XaSpO4ILmnHLguIA0wGfpl1txMd2hnpmQWxJDTx4BSrQkBTxYv-OQXoQpvuR0b8S6H60X9UjK-VuHtPmZyLUy_SntWtpjNcKuKMwQukxe5n9t6jLKR1cXF9BvbFB_qZqz6r7yt5JFOGoqJzmSG6-bHU17LeOW2aMNKGSDrtTmIuqhxXzx7YIs6L8BHGxosJt-Gpzvk5glKuuZeuXqtMHv_ZK8ntehPj9zPQ0jSSjXp-euhVYpPymPnUkSVN39iRUXMpNESTySD1Bs8PhHuHTSqIbSzbqmnVFycz5pkVZYqMHwvTsrc6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7GK-e46sE89GO_Mv9szckyDWd1CtOqdAxruJp1etNnTXJhjRVLvScYzIt4ogvEMpyMKherAINJLr6begQaO6-VvjOvwrnn6xghwGfvHEspQ20amOInywnH8UaVBlA35Jm-ZTsJI6oE2BdDGLdoy5lNKPfvelRaaDhxYTJrDEb9Agy8AuRjsHJ31JvTq6tLu3NEmpV0f8Sj8DdDXtLaM9Cw8NNTvI52kry5T7823bcC8sOtfJigckRnbe93n0R2btv2_4r98C1ICMQKlvTV0ghxl9a1pOBmtob38HfI8r1kl4RLpw-kd5WM1HBc9ju2Gv0nSxmP1_Iox0Y-Bi028VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=n6qYm8RyvJOSqyG1CMeP8REvSpnvLSvukOI46xZYbri6fq1WHlqmPY0C1s_AyVyFdKlyztMrHoO5uKMMmq68k1OE_1F4oqzrA3QYp0cJQ2_C32bavgAOszd1NMD3mIZ3WeNQWxJ_46AmqtzdCmcgs4qYDqBtqivYKjlvdOYA3y8nRzh4_61a6OXGlVV4A3HEJAunVD1RGKIp-Wl55DSTUMu9eBRR7iYC2KKxn-ucETiR44d92IRmUKq3JXbFpBtPn943wXj1iT8O8O-WHTkpu58RLyrAuQTGS003txeevsStnt8DmVr_7jl4d3Sll0qxhhE38XudRR1qBw-rSX8_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=n6qYm8RyvJOSqyG1CMeP8REvSpnvLSvukOI46xZYbri6fq1WHlqmPY0C1s_AyVyFdKlyztMrHoO5uKMMmq68k1OE_1F4oqzrA3QYp0cJQ2_C32bavgAOszd1NMD3mIZ3WeNQWxJ_46AmqtzdCmcgs4qYDqBtqivYKjlvdOYA3y8nRzh4_61a6OXGlVV4A3HEJAunVD1RGKIp-Wl55DSTUMu9eBRR7iYC2KKxn-ucETiR44d92IRmUKq3JXbFpBtPn943wXj1iT8O8O-WHTkpu58RLyrAuQTGS003txeevsStnt8DmVr_7jl4d3Sll0qxhhE38XudRR1qBw-rSX8_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=g-MjpiDuqX5RrYs1ky8NTzTNNaDCMJR1AqEgcF_Sig2M5FJQwdRMFMFgZhR_1If9lwHr064WUGyLXcs8zpcv_4xySF9d3uL8UEGN6dLmlCqEYFBGI9v3ZdKOM7-AR3qIcrT5p8dcx_hePfoWTzIGiElbSJzekZRw7AElyGQmHuF2F2NPbS89Q0pxGRNnzMrrL7lpv3iJmUxbPUqkOJgBr3UCQNCc7rHXUxqhPkZYfBEuBT6YQiBZ61QE42impJ6KHP-LTW-fgNL1uGUWXotE0fLz7UBm-Gl-JKjUNfdAo8P4j6sb3wV3ydq_lNJQedDSrHL4vjBbJf2lhTa7mJLoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=g-MjpiDuqX5RrYs1ky8NTzTNNaDCMJR1AqEgcF_Sig2M5FJQwdRMFMFgZhR_1If9lwHr064WUGyLXcs8zpcv_4xySF9d3uL8UEGN6dLmlCqEYFBGI9v3ZdKOM7-AR3qIcrT5p8dcx_hePfoWTzIGiElbSJzekZRw7AElyGQmHuF2F2NPbS89Q0pxGRNnzMrrL7lpv3iJmUxbPUqkOJgBr3UCQNCc7rHXUxqhPkZYfBEuBT6YQiBZ61QE42impJ6KHP-LTW-fgNL1uGUWXotE0fLz7UBm-Gl-JKjUNfdAo8P4j6sb3wV3ydq_lNJQedDSrHL4vjBbJf2lhTa7mJLoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=t4WPPQw5JYtuJuzpQLNyjOHbZRVlloLUF9n5XJkwxT3FonBtN91mmECH40hEduCWVK8cSJNx9h7Df8wxoMq27B1qug_satD7_M_4ftWOWTkPRdBQbyO1Xh4luvN9oDFzLVBjyNRnzk827T3v1D_14Hx8_QhJ4XeZrHjXtNLljyRzoo6X2CFhpAFQQ2toOh-Pb5b70AlmURxqdCBplk2Ku9ApVyLlNhsLuiZS2XmWe5TeOIckiYpdl9bFdWLoXIPreHhVsOTg77mvF6kEig2UKjTDijltU6QFpDDTxBU8slpyLD-D1O5z3xvZeYTBom62_TWCLoAqJi-FDeWLaOgDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=t4WPPQw5JYtuJuzpQLNyjOHbZRVlloLUF9n5XJkwxT3FonBtN91mmECH40hEduCWVK8cSJNx9h7Df8wxoMq27B1qug_satD7_M_4ftWOWTkPRdBQbyO1Xh4luvN9oDFzLVBjyNRnzk827T3v1D_14Hx8_QhJ4XeZrHjXtNLljyRzoo6X2CFhpAFQQ2toOh-Pb5b70AlmURxqdCBplk2Ku9ApVyLlNhsLuiZS2XmWe5TeOIckiYpdl9bFdWLoXIPreHhVsOTg77mvF6kEig2UKjTDijltU6QFpDDTxBU8slpyLD-D1O5z3xvZeYTBom62_TWCLoAqJi-FDeWLaOgDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=T-3oTDJ6NDmZkheoIIKn18Wf5qg6maRlXUQT0j-0Ft-hSxsmn0NtDvx0nKaWXx_itTcurOQIYMGVj7ZkFIG9YNwtoh-PIqjhPQfoi4GtcbgDpoLoyt6HfOSPGrlEEx27ZyZjURmIu60osfTIS6QD9ylfJM_qmlwfsGsnFBj36Es5xMa6e_kJ22ZNKr6ZefcV6_KjfcC3Vxhqh4xjYFHBphUwNADqhMbiEAmW1MBX5oZpAbOeRcgESPSpeesEk8NBnKBXp0ENf57swibenQnJAulc6BtfSNwBsPYC9REB4LD9oclRnCnxv0JsUrLzkYFONOGmh-o-I74TCfkXydgHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=T-3oTDJ6NDmZkheoIIKn18Wf5qg6maRlXUQT0j-0Ft-hSxsmn0NtDvx0nKaWXx_itTcurOQIYMGVj7ZkFIG9YNwtoh-PIqjhPQfoi4GtcbgDpoLoyt6HfOSPGrlEEx27ZyZjURmIu60osfTIS6QD9ylfJM_qmlwfsGsnFBj36Es5xMa6e_kJ22ZNKr6ZefcV6_KjfcC3Vxhqh4xjYFHBphUwNADqhMbiEAmW1MBX5oZpAbOeRcgESPSpeesEk8NBnKBXp0ENf57swibenQnJAulc6BtfSNwBsPYC9REB4LD9oclRnCnxv0JsUrLzkYFONOGmh-o-I74TCfkXydgHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpQPomESaPa0wowGXHVYQEvyLaCrazYX_VFP9EhdN_VMbX5-CcSiGI-MeDYrTykiTKF76l4Ttnr-EMpWlaizbliSxsZcxI4TklFztWoDP10TbdpScLeEhPB8qgHnxiedoD9Qg134brvXm9YeowNPG6Nvdi0eust_FEiG8B1vxff9HPwD-i9Ishlxb7RTW2nBLXfaTRmRZDPC59mTZKcpx6jfz1syJ9rIsYrNoaxHNvA_0BTMq2H6up3q1d5qjXpy-OB6RvXpl0fmzD_KgUkgJS3MXRIvbhidMFVCPriLv4OUyBu4kwr1C6jtX6T2oshxxsLLMm478GYyxl4-_9NsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=kIYz0wCxvhCew-KA7M_lERTLKRw5fj_aCZULWAr3kRVlg62Ztr5ZPVwTF6F-ANM0POkjYULx3wEZWLiMmTMhP8Sq3uCAleIzvqABhD0WiLxr_qIi3fe03Dhd7A2mIdUz7rQ89j6EP2rh0leH2sTzfeKBtru6K6xgtQ99_Bmlk1MrnZ94sKuqHBS3o5UO9LfDFCb9dYNGnzr2tFy-7rq9VULwhu8dQpAIrynlC2LXt6pvbpOKzGPYA4sOntr8E_FT_JxklP4RE3IQm-79LxIcENoz42aKbr5R8LJNq9MtcCV2Z-NK3NgdBk2Upmvmmwl860jnBDQg0KDgH7mvcshNI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=kIYz0wCxvhCew-KA7M_lERTLKRw5fj_aCZULWAr3kRVlg62Ztr5ZPVwTF6F-ANM0POkjYULx3wEZWLiMmTMhP8Sq3uCAleIzvqABhD0WiLxr_qIi3fe03Dhd7A2mIdUz7rQ89j6EP2rh0leH2sTzfeKBtru6K6xgtQ99_Bmlk1MrnZ94sKuqHBS3o5UO9LfDFCb9dYNGnzr2tFy-7rq9VULwhu8dQpAIrynlC2LXt6pvbpOKzGPYA4sOntr8E_FT_JxklP4RE3IQm-79LxIcENoz42aKbr5R8LJNq9MtcCV2Z-NK3NgdBk2Upmvmmwl860jnBDQg0KDgH7mvcshNI4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFomM4sgcm1DXSKzj0PX_eKE4LoaB7Wmv9fM35elRmnQLASYlWBFaECF_Kc3Ut0H9Jfb2biBS2kl6jSbcATwt-dzshqfAEgBad8Uv89xKGAcYGP8ERyhQqb3T3cSvLNH6QYD7m9uzMg0sYgNf_TD1XRIkJm4E_5LSl57j7-iueWJTkem9TmZB_f7bTQjA4VJ9s2wIkQLrKQ4tusVniHhBLXQ-ihHM11zBpyZzmWqzZkdtFlEhUQZOmW8mNcTJ-yFKg-KN635ESRPIJ8t8W7g-oKe_m1m3jdm54rjciCfYMlNhD2IO5qG3c3wPQWCRzgBvcmgWsIexhlqI8NXcRLZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2_HEgLXeketkYbsDiRJX8NX-dHL6JKS9bpbYVfnDLLkwFD9knQGg5EJUD2W8sQ5CYa6AWTpoBLsEeAuMXk990OoCyT0srE1T-U4eUV4l8gTbkLS35dE63pYzxmkInCd06rWM0on1I6-NuMDZlu84DrN_b0xD8G5mPNuRtClKaQgaXLodAGyvw4MlmqOULiGXQXwuy-yfkU_Tm-keOGPZEdA4hEmkJaUubOSNKmCOxywNEdalunOCs36MpaomXz3KSYKctuUMABdtGpQ43jQyP_VKIVkBnjnlgNtqi0pwmmyUtZoJfGxM0m_7lhAbkdGqrEwblbkgExgvibn8urkWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBXQ44jQ3gWSp-cYdnNivkJtghQQdejtN0MZQXN3mo6FjBx0C9Nhk-8htyeTYJckkMRWRItTCdCFp-UY231_g42sSxBb2FbZEW-ndQ4Ffy6WXAbM5X4MtIM2_UtbmeNXC2y5ENAZ1nXDIBPP78wjT3tLKtQsRcEAyPJij9QkBceu9_3VrOTfZlIYexor9iuQJ96huTboG0YR0GbrrZNe0Vv4VlG5dti_DS0NQczv0ddHyZOZWaC-Yr-pzRIpfZ8mimf1_zhrXPQUb4dF6wFip2CXS3aZLykHBryDUo3O962Ig6c5ipIV2ZFM3lKSLne7LnmeZAeZlhuUebdZTUm4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4PEWMzbJivkvow4xWcwdUlWyDexiHuhNRt4mXzy9kjqvVcziZpbGM4v-dDIytjbOMtg6oomR-tWRwxs94bN0eyncHWjrA9dNIrhayyDpPl_-D_1bpkc25dWhXANeZv_lVoVJpXwM-05rU0fyuAkaghNfklezxfODt9WYE88w2m8H1HjAz1tVThx2dyGK6E6jdcbP1ayd8LJFq4N21mj60m1BV2ecuLc88EQl_Zovisa02PpgUtCQ66Eu76Avio5wedkqkJ3hJCjW8ZjitewclxSKno37HBOQTJbR2_aOeSGq617258ebsG1hPhGRR1vlfeZQr41S_MyqGzNCUj0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=ry8hdYgG1ZnrTLY50kd6L9r60R2BzUebb1zXNy6RuctrkuVjrblFPWNcZYUjs2m-dmcUxuyF3-l0e477vixnG35trTDmvxq8V15ROxCGkgokj7b7WCb94DUOZWDNZo5pjJGnt3G3Sxmgr7P7NhTTd2jJg08wURVTRtGtfxfQNdKBFuogS6GDX1PJPPjM9wL7DCanOYbZGauUtlfo68FUe8rgv5hQQ74xAAtLJsLiSOaLYUpcjlfpRglxuCgaz6UkHXT62zQcE49LxrQPbluSCPtq00jTfvpoAafteEns43yroJ2W6MoCJKgXEYcRzCL_Y4zqVxNkYEkMLc1ScMeYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=ry8hdYgG1ZnrTLY50kd6L9r60R2BzUebb1zXNy6RuctrkuVjrblFPWNcZYUjs2m-dmcUxuyF3-l0e477vixnG35trTDmvxq8V15ROxCGkgokj7b7WCb94DUOZWDNZo5pjJGnt3G3Sxmgr7P7NhTTd2jJg08wURVTRtGtfxfQNdKBFuogS6GDX1PJPPjM9wL7DCanOYbZGauUtlfo68FUe8rgv5hQQ74xAAtLJsLiSOaLYUpcjlfpRglxuCgaz6UkHXT62zQcE49LxrQPbluSCPtq00jTfvpoAafteEns43yroJ2W6MoCJKgXEYcRzCL_Y4zqVxNkYEkMLc1ScMeYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=NsrTLvXubd9iNDZtF33HGKgTv5U4WgU2S8mNTpGXLFwqCtjkFFyGPvb3FdNcTGP-DPYHB-ftP39c4o5F6pAtuktZ_Gj3S5VNpzB0hO9CDS60xxgDYn7OozkT-A9VTbg9LQSxrVQWNY552WIeIgpootujNZxJPtmrtSjdbHJeaYGUzsotvljf1h4UPJnT4Ntk3rVFocsrm3PropMmbhUwqwU12kU66Hg6PKsrQMNOFfSeGU5FBVu0c5cDKH7-CKdkVdpOMASVEV_-AemW-DeWd8KSInh9W7Tl_8jI_Z28sdMHhe2Vo2AWa1f69u9081wxcA5E0vCZwAahfuL0N9SfnTTC76l-eLJgLOwIMMpCm8JEqyjQURCn4pdIMrgrYYppuVV3zDKmjbk06WmjUANYIbKYYgTOsnOrc5YZH6oKOR3c0O72dvSyd5JxaEJZrfm-iaPQOx8kSCokVe2GZP7kpCvobmrEezg4-VA3Ry8NGAxyoJScvaKDsVHvCLhmgOlJ5Ob9mGQm25C1JnSmyLinb4hXTkJncE_AF_ZxhANbflpZE8TqtQlm_vFLvAgJRQtc3KsN0qDeLvx1fCNN_RI37SQEQkcS2_QEK-ifl4jpiA3Rxmec8eIWeRX1mtg4JxVy5xLhLI3vSW3fJ35OsHx0u-dnx_k_gwSI1nP4WEpY8FU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=NsrTLvXubd9iNDZtF33HGKgTv5U4WgU2S8mNTpGXLFwqCtjkFFyGPvb3FdNcTGP-DPYHB-ftP39c4o5F6pAtuktZ_Gj3S5VNpzB0hO9CDS60xxgDYn7OozkT-A9VTbg9LQSxrVQWNY552WIeIgpootujNZxJPtmrtSjdbHJeaYGUzsotvljf1h4UPJnT4Ntk3rVFocsrm3PropMmbhUwqwU12kU66Hg6PKsrQMNOFfSeGU5FBVu0c5cDKH7-CKdkVdpOMASVEV_-AemW-DeWd8KSInh9W7Tl_8jI_Z28sdMHhe2Vo2AWa1f69u9081wxcA5E0vCZwAahfuL0N9SfnTTC76l-eLJgLOwIMMpCm8JEqyjQURCn4pdIMrgrYYppuVV3zDKmjbk06WmjUANYIbKYYgTOsnOrc5YZH6oKOR3c0O72dvSyd5JxaEJZrfm-iaPQOx8kSCokVe2GZP7kpCvobmrEezg4-VA3Ry8NGAxyoJScvaKDsVHvCLhmgOlJ5Ob9mGQm25C1JnSmyLinb4hXTkJncE_AF_ZxhANbflpZE8TqtQlm_vFLvAgJRQtc3KsN0qDeLvx1fCNN_RI37SQEQkcS2_QEK-ifl4jpiA3Rxmec8eIWeRX1mtg4JxVy5xLhLI3vSW3fJ35OsHx0u-dnx_k_gwSI1nP4WEpY8FU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=kN2xFxJetVPOZhiqcW9_7aI84CwkJNM3ULA4YBcw11Hof41wEh2yViSU1L1tM1hsaDUC7cwZ31peFGi7OpmE62-80Wsd3ACU0Ef2LDz7PhGXjg7ZQ37KPASTnvkptlxUHfYcaWhTeqkkueFAITJ_9eFke5xfFRrWef_SxhIP2oRbGwnTsrw_QaQP_hkQipwdAt4-Ze_39ObYACPzIptlz_t6f0Jzjoo6C0DFWGNq2L9tiIeQjGz1oqAe2UVvs6nemaZ3m4GWiJqf67aPiwR-qHSCBA4O2PFb0qrZvrSgt-ORq7kW6lfs5ISH7SmVK-SPMRSsElQjC--jn5KP4vaXiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=kN2xFxJetVPOZhiqcW9_7aI84CwkJNM3ULA4YBcw11Hof41wEh2yViSU1L1tM1hsaDUC7cwZ31peFGi7OpmE62-80Wsd3ACU0Ef2LDz7PhGXjg7ZQ37KPASTnvkptlxUHfYcaWhTeqkkueFAITJ_9eFke5xfFRrWef_SxhIP2oRbGwnTsrw_QaQP_hkQipwdAt4-Ze_39ObYACPzIptlz_t6f0Jzjoo6C0DFWGNq2L9tiIeQjGz1oqAe2UVvs6nemaZ3m4GWiJqf67aPiwR-qHSCBA4O2PFb0qrZvrSgt-ORq7kW6lfs5ISH7SmVK-SPMRSsElQjC--jn5KP4vaXiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=rMDm4YTvwNr9YcvoufzAQRq3GmNzBwDbit2OdX0IjfsiPwAYitVuL-Ui8BujHDwFA54uQxKzf60-7DpPpJQAAuwaFrsgXxNdJPnXqqZVKJj6J0WR77-EKaN5DCHUPk_4C73CgIjb2yIAe0x2--dJDpguCe6lKWx0DapVRPAlhZeq-TWtHP_W4FqcOxhdQef20WKK_ffHpOw9WJqAgLcZsDeiLD-g_DogtVNyVBXee1t--kPBQaXWF77QeRL-GM8P_m68aJ-6NMY_w5-L1eER2BMiZMnGuvsic9NXqqfPnQwE2YLNvWnOWLkjED-C8Hulcz9wrY-KjsbWtZlga4udFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=rMDm4YTvwNr9YcvoufzAQRq3GmNzBwDbit2OdX0IjfsiPwAYitVuL-Ui8BujHDwFA54uQxKzf60-7DpPpJQAAuwaFrsgXxNdJPnXqqZVKJj6J0WR77-EKaN5DCHUPk_4C73CgIjb2yIAe0x2--dJDpguCe6lKWx0DapVRPAlhZeq-TWtHP_W4FqcOxhdQef20WKK_ffHpOw9WJqAgLcZsDeiLD-g_DogtVNyVBXee1t--kPBQaXWF77QeRL-GM8P_m68aJ-6NMY_w5-L1eER2BMiZMnGuvsic9NXqqfPnQwE2YLNvWnOWLkjED-C8Hulcz9wrY-KjsbWtZlga4udFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJMh-FeRFX0SoJPPwcqcUhAYyY_b1ohm2JDWxtmWgNKGHm8gDsRnM5wiNSQs3JNw8AT8bdVuvpasvWn3vYrgh7c6AJxmBHNrDq1itJRbQYAodGfPNyeLud5Ee1v-_kv_dpuQKggLHC1Szut3wPvnT0ZSIka6MlP3vTGXPPSioDYKGXTu7CgG0ixGO0B-X6LuOL6VXov-duDSUP_NocsItylmzVXjS7VUTCqdCFnBHv0xDVS2efuaRyXPmVQlnjS6XIQ_m2KB-TbutExrsgSEVwvGUL1ot8jCAN6qPxj-UhuVCkPHxwB00G6q5hSPH2Rsu89bFJ4b0GxAZ0kFjYDhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVUknZRoDOUpO7SMnG9MBWOzqiBTEcSIfkdct9KgYgbc9b5L5G8Gf2UEnPln2fI3AtyirrJ28pKHj9J7L-2OOfcM3r4DNSJVT4FZIOTPwNWa7kv67gQcfEPFkJZuwUtsegLeBarX8kkAB6lt_tgpPdZZHLfcwTeGJhxzvGREuvcdXZv2zjqFxNjeOQGL_WpHBLxuk93wXntO7Op4zLN9zCLyufKX1SBHwQgzF_pBSsvCWx8JHq7talNkC8JVt9peQ_H9D0cCNtmWqJU9ub4IzPWugKRXN5A9iD9zRrC1Mc-5WcGnhcRJQt7gJ-RcN-ts5lU5hAGtctC4sgPwsKDr-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXzaxJFooeADkQMUw1f4hRV9cLtqnvRr_lmsaxcNxT8PX-Rra40ElAnfjRYRjeJURN6xI30Z8LyT2PUalrEllm1kB8iu2o6V012G1Eg-UoglBAAPPwh9x3Bmzh6LPGMMoA_ZseMFHubCAGmGQiL2V5P6XUkAj39QLg_zdh6d-4yYdbmlCiVL4f2k5F-FHMkfOiixMe7NUUXDi17V-m91Pkbaphj1qU4gnKREgAW0g1fe5xcG56t4J9QJoMxxhqQI2a0BPMXkmwGG42EQ0XGhz6hG6TJOIdGMq1KGVmbFeydYjY7msHFaIx9Isv6VLk-YDDUs7IEJmyrLgWBPfpNGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tw8emig_v-9L-NJu_xey01pl2_t-ev67M4XgUJlJ7W4bDikhBlGdHw1Hdm4hRx0Pzx-50d3c2Q9rQaZRYsE9JZRrraaN-i8oXNFotRb3VD_27loES-_jDbKbrxIWERtXRmBf4U38ErQ0MegVL3EdTj9SVKTi3jXYPpi0nxiZ4b7FdRhBkk5kRpW0gRCICVh2bJ0mdVycuzbt9R2RhMvhDupO2s11l9Nwz_fYz2rWPWHxP6r8yuDmj7LqVmBKnOzqBMTqR-6XNyJ76Gvybylq6ODoPD_6tA6URt3vCrEKGK-RXrz1FPDaF38rgNtwpOZ5FqZ07Lyx7YzJME-xFYwu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbSFerYa6iSxBGarWipIpkvB8blJdiqEXyUY13MjQYwIIAmtzeQj5YDt6kdU6f-5M-5rtZJ2ID2KMMN-43OkBuzLIdRAri76NuPSqOY6S3ydB_hbL-FHnEtk-mcNw-2Zx-QteOB-Nvzd6O8AWtdPef4kC1Wm3FmbzJ5_kFJXUcFwv4XXSDuD-Tkwh8CD-lN5YD4AVijmMG0giptT-qN7vaxyXNMxf9YE8wIPqsvRlRxabHUKYjNELIJ-kahYzmiKdD7PiUjceD1tOPCOSBa8BfRFhq80pKhKqCyZZKN5ywdQm1HnoPFsqy24cquPKha0tSnzcRcVNJfOH2cLSLJvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqEm9AcFQF2P6tZ23LThJbRWKM_7XM0jtyJy8n2DngN6aLwolAo5jLJQgzEhqg-S-2nXUxLgh2S6QeDdafRDflWoBYVUNallybNmRwxrZ2KoXoucFIqZbEKWrhmWxWf1O_GL6Dsyv6raGcL03lfYAz-iH1LZmDI_deXHK7BoUMiQiJNuGcIoFSKQ_7DwJc10i0bliqzgsbuyhXnu5Be-tD0zJF3i7QNruMyS4FVn9DkV9pDKcM08I7_t6VYpFsnK_eLZsFNPkCh9EtnOihcPBbG-Xsj_CxrLIcT77KMcWmxfVHYUnY_EV2DG-6wKPjlVqU2IIfYB6gB9PX2MPNky9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4OyATj35S0wNt5gKiGXJeSCkU_HP4U8mn-d4N25UeJEMWfFzC4f-5hKLc9IC-k6owj5cz1WfPw5iPHI9TzYGIYPovJG5rz3GVYHm8S7M67hM3bWlE1WcEIe0Os-FAz8Md-y9DzDJYPiQe2IM99t4CMeYkFw9i0Ab6ubEghqwLBL_yH349jgKbt6kqKkUh3yp8FwsdOkqDx0JyJLPhURK9wMPA6gFGfcYF36tejrR7afY0srSACMrT4An7ncpYQDo1n4frsB-KqNnZBmtvY-uusppNpoC7KIyFTP-vR53HCG4w4y_Ukgluljo_fK5UzBxhZz9_RjU2MQOaUwSPnQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPHptOB4xE4K-YegYkdo8Z4_Bocv6JQY79gE2zNJ6D77quwesT_kosLbIga4QDExoIoyLxhq08gtI0ZFYMm2yyGWnOtlgnMMzHR7QKNGVIVROCsGCs7k4zFpqSNVxT5osndwQWoVU8XXJUV8Bz5CjLbQutwvvGFu460Id9_xHXxUhN87Yh9UfZ-s5uxmYQjRGN3V8UeKguiyRfENGK8xaZSIQTp7V94oTUq9YgS9zgLKS9SripVOdiqVHaND7MIsjTFwHnZ5-e2p3RHeW_kBxLYEDJiaDahqWvf4A0HOgCuVlqbLnuxIGmBmird6TlcAcU1pf2IN3SIwIw3hm3BHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=QZnzmbMu6oqlo7Bds_T-464gdyYfYJjT5XbjEWgKod7KAqvaPvs0Ixg2Mh2Nx9QcWXQ_R1PvexmX3rnATjDRPnoNXhCIoGq_NSHPRO96EujkH-SGLQDAVpdmo3GUDPoM4MlM-8UFOfvzHpRwsQ0wZtozHTwzG2iDQdo7b2g355L94KoodHlc7EVWizY7p6LUmYdE_v6FrzXblWnfNJDPOdy58e514BsTpUCsvUAfTdZ98pX9vl6g79izzvMptGPIqLLHYekBZx3TWLUSetk7lVllK3yiPufbKrlKFwOQ_B-9gbQzsLiVLI3QfvPxGh5QCN2_AU7wWKo-c3vlMnXrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=QZnzmbMu6oqlo7Bds_T-464gdyYfYJjT5XbjEWgKod7KAqvaPvs0Ixg2Mh2Nx9QcWXQ_R1PvexmX3rnATjDRPnoNXhCIoGq_NSHPRO96EujkH-SGLQDAVpdmo3GUDPoM4MlM-8UFOfvzHpRwsQ0wZtozHTwzG2iDQdo7b2g355L94KoodHlc7EVWizY7p6LUmYdE_v6FrzXblWnfNJDPOdy58e514BsTpUCsvUAfTdZ98pX9vl6g79izzvMptGPIqLLHYekBZx3TWLUSetk7lVllK3yiPufbKrlKFwOQ_B-9gbQzsLiVLI3QfvPxGh5QCN2_AU7wWKo-c3vlMnXrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=A7fmFaYjOmL-TefisKtArAY4T9Zyy4QdF0eUqmkVZNtcT4uEo8hUGzX0FFjjBwFjpE7JfD52IpzTkXrkO84DlHlKiXBmx068BW5QIUu8ZstX_lpRXWdP_DtD7Er6Jd7maA4_6pjh-nDxzGgduGx7EzE8fjWqT67FDf1mepjL-RBg2YC21Hzomr8NPzqnBYJnSe2k-nQfO-CARZ5pxcjhZMJFbiYrnPDWiWwYWWpyxb01bpxyccJY4or9ziDZtR9g3pPEYN67WQmx1g7YC0LRSc99ahGM1lMJxI_lkF1APbice6HRocb6NonWnUu5pCVETxeQ-fk3uQfP2P_uGjaS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=A7fmFaYjOmL-TefisKtArAY4T9Zyy4QdF0eUqmkVZNtcT4uEo8hUGzX0FFjjBwFjpE7JfD52IpzTkXrkO84DlHlKiXBmx068BW5QIUu8ZstX_lpRXWdP_DtD7Er6Jd7maA4_6pjh-nDxzGgduGx7EzE8fjWqT67FDf1mepjL-RBg2YC21Hzomr8NPzqnBYJnSe2k-nQfO-CARZ5pxcjhZMJFbiYrnPDWiWwYWWpyxb01bpxyccJY4or9ziDZtR9g3pPEYN67WQmx1g7YC0LRSc99ahGM1lMJxI_lkF1APbice6HRocb6NonWnUu5pCVETxeQ-fk3uQfP2P_uGjaS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7SDADTf3MgyDN2T5jVhWie-o26H2PK4XyCnO08jqcrvDtRqiFNrwhNbbcSJNvf-oVzXk3VpqASbvX2uceUy69Mkrqha44hthJo4loEiyhJc0dxcm55OMp4KnV8e_Obj_A_kP2iGZ2ee01Bciz5bqxejn5ZbDc0w4aL2IixiWc1shnxK5Y-cG4hvp8FLF_AAxMGh5RVoQAeuJ_NZvuPYdtREHOlWzwKL75X6w-2JrHKD6NhOC4PGRGaUlM8AJk0HBVt8feRjUbd7zQeiDNd2alRmjTTVoHlTJsJIYFAE7lcpWxAAjUq81oZgK1d5KQ6TdX2fPHue11ONVXaRByi28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=OPPFF4qmzNPm6Yx4_XcWNkBuu7Wua48FgnjNYqGx61V3qg12xdaFomzztjCGF8zUm4v1dMs80yuOlPffKiOOzJ7NRAsLM63umTmFB8TKxAdWqMRD7LUcQdLila8hEdT43ihPU5ySBGv7OenWO5FjetOqj5s8wAHpuuPog_xDBbXYLX40iDMSraMms-IzuGx2REkMTIviP83EHkTASRRFSAesYzEMY1pLzxT_FzS9vLrqRIgVsBJMF0uKDPa-hwIKV-sbWfOd_pWoOt40GPe9ZxcSHJ2N7x2Cr4jFTAUKq2OPa0uNCJxGYvSsmJbcOSXMhhCWUPaDe_6UxvaK35NuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=OPPFF4qmzNPm6Yx4_XcWNkBuu7Wua48FgnjNYqGx61V3qg12xdaFomzztjCGF8zUm4v1dMs80yuOlPffKiOOzJ7NRAsLM63umTmFB8TKxAdWqMRD7LUcQdLila8hEdT43ihPU5ySBGv7OenWO5FjetOqj5s8wAHpuuPog_xDBbXYLX40iDMSraMms-IzuGx2REkMTIviP83EHkTASRRFSAesYzEMY1pLzxT_FzS9vLrqRIgVsBJMF0uKDPa-hwIKV-sbWfOd_pWoOt40GPe9ZxcSHJ2N7x2Cr4jFTAUKq2OPa0uNCJxGYvSsmJbcOSXMhhCWUPaDe_6UxvaK35NuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=CuorG64dtRraEVEMjWA3NcYtC7ENU6tEx7O8vVNrVxktMNoJ8uQFoEIs_bFFo0eg7DqrZXu6ZrUUTqJTXdlNZ8DX0dIFfUznfNk_eRvNgJUNC0EzSdeyoOwoA20eb0DDb12ICWcnAwrrXdMYFJLGjkrPfhUXen-5F2DbZyrYZgdudgi9BCBRwB9Ka7JbHCjTb7dMsc4xt0hJfHdQBoKlJD5nRkGunQwRnZI5Vz8zdaKU-JlStGM8ZL3UeEuwjt6tQl7ESmbJ8QkGfR5b4ucmO1Mw6bGaQHq7RnKQ3v4s6h6uTMficpoy0WGOxQoXizpWWvGpOjcYnrBiDozi-4x5ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=CuorG64dtRraEVEMjWA3NcYtC7ENU6tEx7O8vVNrVxktMNoJ8uQFoEIs_bFFo0eg7DqrZXu6ZrUUTqJTXdlNZ8DX0dIFfUznfNk_eRvNgJUNC0EzSdeyoOwoA20eb0DDb12ICWcnAwrrXdMYFJLGjkrPfhUXen-5F2DbZyrYZgdudgi9BCBRwB9Ka7JbHCjTb7dMsc4xt0hJfHdQBoKlJD5nRkGunQwRnZI5Vz8zdaKU-JlStGM8ZL3UeEuwjt6tQl7ESmbJ8QkGfR5b4ucmO1Mw6bGaQHq7RnKQ3v4s6h6uTMficpoy0WGOxQoXizpWWvGpOjcYnrBiDozi-4x5ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JgaZLcPHs_bPsI3L8PNfFHUYtA12n3c9D413bVilLyOsrv8f09lIYgO5DABhHhtd_RyJiI6NJwEy_CJ7qRXhHOKP8chgTzG0n3aHlv-bzOBu1YUOfm-BWIFp35Q2eA9d-8i5S5IzoH1gFWQjyY1D2cHLCoecwC8AjWQ-1Ydf9iVd-LZGF0m_CM2h-6B-upjyPZx3jZonHPFwFxA7bbduAuTiY5-QqjQ0O5L56Wcy6NKPOaCYffSZAT3gpAdiUKpWNMpl0BCzksm7TwKTo7-s8r6zQit8BxkcLKsVTffekRytReUpsWdeY9gayRhCrwoF43NeIF_bhPrvK7oc5V-v5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r22oTB8winRYRph18p0_2f1VPKqXaUkNdryEznzSYtRAfWNMpyFnQGUGTaVpERFmZkfViJeklu2hhPfjuvdqztJaa0DQFBlVoCXGtNfDw3H0lC24umuAnWFOZSyQB4Ouz_F4MAf9lEn2tYD1Xvisq37-oVx_yfdj8Tee2TRDbNVK4JlltgkyAcdJVNj5fVIQU3F7kjXge4MeAk3uNfDUzvhQ8bZKikiXRJPo3cuiFc8GG3VrTckLJQV7Hx8vYUiuOCA2kAE2HfcOrGf15Hp3YzhsTe6Y4q-9tDAFoZncox7voN3jC_sa3MO2azFejpcSkUy16Fuw8nQI0I9lsS19gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP-RiHzsGi_6ISJ7renGaIBQRnTWjySAx1fPYM3OCx5c7AhyH0j6y51x2GCRBlyjctsTpaNGfV0V8xRnXf81XvjJyk5p04WmRrQBemlMwu2Lo9oFCluOw5j0H0nDod4tft0tATjm2dNBiFJLEhktUfJ59A3QKeC280aynticB48oBSepl-VoKpEjD4obK4m0NxAi6pOKc4AYmiJGUW0o9N7bSZ2NBkFOKT6d4LJ0zt1BvwgmncTi0QQVYnsfMXavrD6M2x8d9V7akitwL5v5F9d38La9MOpKzaKlO1c7awfxphIhvzl9wRJhi_hULvrpeUgI-Rzd_L4AsdlQIajIgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=EoZ_DFsFLATtsz8p2IrzFv9bsTSIGZpai3S5hU9HY2Wn6BbdMtRMxwxYwpJdagFrwEmtt1NgO5ubtRLlf4Iorzy4o1t6MEDbpazeLTC0aKBghds8frC7c8cppXETgS-wKANCQvd9InKCW_T5EIeED9wnvQiuupMKsBOsnZXimr4f1_x5YIJgA6hOy3D6aa1Yj3DP_i6YrzhZhY0_GuK5kAEWLgmTrDnv0tdf5jiUEBPYlU3Ld1ZiWG9lM69vhfxJcyfx5imZwWHT50ktMj_iIg2zsA1y9SOFV7bMvfQmyjNQmgs-KXpBGGF1GuLsO9lqdjNpyTqt2NesUzosUaixZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=EoZ_DFsFLATtsz8p2IrzFv9bsTSIGZpai3S5hU9HY2Wn6BbdMtRMxwxYwpJdagFrwEmtt1NgO5ubtRLlf4Iorzy4o1t6MEDbpazeLTC0aKBghds8frC7c8cppXETgS-wKANCQvd9InKCW_T5EIeED9wnvQiuupMKsBOsnZXimr4f1_x5YIJgA6hOy3D6aa1Yj3DP_i6YrzhZhY0_GuK5kAEWLgmTrDnv0tdf5jiUEBPYlU3Ld1ZiWG9lM69vhfxJcyfx5imZwWHT50ktMj_iIg2zsA1y9SOFV7bMvfQmyjNQmgs-KXpBGGF1GuLsO9lqdjNpyTqt2NesUzosUaixZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Se6Yh6GDjeTvIiI6eM8AzpcamHWuIxs_roSXfBcH1mYpQ33B4l6xm_JjJnQfJoxSldmYsj7JhYcbk_QAk_v6lJHzGfsV7wCTtaXrJkKYv40a7usTaHNMQlyJWX8fNwA0wHBJA1HRCWeWTXIQn8MyBZxlJ2nsMmXiuJMSdkUraeK4o9ayOeKZ6fPqFI6D-HQXRyoG1fMKUs459n3cciOpmQMZbssBSvWSVI0RlEyrQR_RbBUQJH53PkZsaFPgvOZZKs3ta-1KdGUoJO9LI-T54kTYbrXaCgA4pCQPDZIrK4SPUH3OeR2tvEVKZxyY-7hLExWiPPUI5mT-t1HtntYQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s310_wYh_4FrVLMBhT1-WeefTB3iQL8Q_H8-qmq0EzJX5Th8-RKdBoNg9cv8yAJYeMpVQ1NRvjuNuGXPaz2_EHy3MGmC_6L_I8s5jj0XP1D_2Z6pRzB2782TVvQOFJNkzczovpbgNvKfvQGgRIeswxgsqwPtrTnEumoT_GaiwJFAEwfF9Gh0AposvXKILbsV7eGfUaxtQh56gSs66dpkSIDM8XqCVt_P0UzNps4kGv7lZZQ5cqClkkoZFw4Ug5M4RiF5Ot6-6LJKwGjT61Nx_DNLw4QmC1_GE10zgizmb9TFYN3GsB_zBMJjBOn4uxvg27txdkXvM3Umv7mTpJGdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odNuZl8wSE0-F8ly4KC-GzFL6z8_kP1yW5FjDOWM6wYqRvhSmcV0Oq8iE83XThaJdbJ1u4vgnLAo9MC5qnqG3XhYzsWwZoSD6oh6GMO-hjYgPx6AVAtb-Ou_0dersFZ6v2gxlcTRkTM1Bb8ixDPw2i_FJ9HUoaE4DdPgDL-8afDzg8e5BwF71CL0qxL6oyKVXLjZmIRkmc9hdaK2x0i2ax5AGk3BSz_FgRFvVXxm6lese5oA_kebjYlnhEridgWTFPW58uvDGI58EiDB3H-7KgUdRYTYlcfn-vGH2AqHNy2_NIM7fjOTYz1OHL-op2N2j1foPNmClvkagqx_dxRMcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=f2qGVnb478peDmbshCb780UzL2XsXYb8rK8dbBAsznLCtLYeuwjV8xrZvYt9GNqHFQUfe0uxlZthEwRIRnW2nq9kAffv46njfgtG4tEBvhWJYVLtdTmcxGeGnYNxIw3jecC9ybtyRzemiPGPLfhSLuogqoohjYWV6JFYaTQ1a9OtzNaWGjNJ8XwhM8r5rCGuwJSzCiIyxIxjzuTyvnR-eGPHgAsKYoY3TTLIp9ytHXmcsoHhTbjzFgkSiHNGotZbCT5gyLqvaiPtrp5Z_OFdtnmu7yOKWfQsfaRvdpQMlaOiMpBJycxl0XrjSw88PWsCqij8z87sVP5V_1YXbXhJwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=f2qGVnb478peDmbshCb780UzL2XsXYb8rK8dbBAsznLCtLYeuwjV8xrZvYt9GNqHFQUfe0uxlZthEwRIRnW2nq9kAffv46njfgtG4tEBvhWJYVLtdTmcxGeGnYNxIw3jecC9ybtyRzemiPGPLfhSLuogqoohjYWV6JFYaTQ1a9OtzNaWGjNJ8XwhM8r5rCGuwJSzCiIyxIxjzuTyvnR-eGPHgAsKYoY3TTLIp9ytHXmcsoHhTbjzFgkSiHNGotZbCT5gyLqvaiPtrp5Z_OFdtnmu7yOKWfQsfaRvdpQMlaOiMpBJycxl0XrjSw88PWsCqij8z87sVP5V_1YXbXhJwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=QpPnlb7W-QZskToEn8hTdnogOgUSB-8HfiqtGTGJLU8YTRNbitl-MS0dwo9WM3I904fSC7KjaGw-CdEBXhBWXCMsV0PRzvR43Io7B_Q2AfegaC-MKXl7HRcjtR2-K0GALPQqSVRVGPqiKSa8_YfhDtCXv3GVQJXMPajto7e5Yi-YxA1F1zV_-53tv98XmkgcDcKdeglEyEJHv4b1JsUrY-D4n_OphfPc0c-nFN0bbsMI8JXFAYCQj5uAejAr8Qx1_AdFsaAFcRQUmrvIWMVwvHZaWVY3l5l469bpbdaZPVGlAKTy7K0oLF7neH2ga2XYpvXkpBK_LetEPA2iENyxQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=QpPnlb7W-QZskToEn8hTdnogOgUSB-8HfiqtGTGJLU8YTRNbitl-MS0dwo9WM3I904fSC7KjaGw-CdEBXhBWXCMsV0PRzvR43Io7B_Q2AfegaC-MKXl7HRcjtR2-K0GALPQqSVRVGPqiKSa8_YfhDtCXv3GVQJXMPajto7e5Yi-YxA1F1zV_-53tv98XmkgcDcKdeglEyEJHv4b1JsUrY-D4n_OphfPc0c-nFN0bbsMI8JXFAYCQj5uAejAr8Qx1_AdFsaAFcRQUmrvIWMVwvHZaWVY3l5l469bpbdaZPVGlAKTy7K0oLF7neH2ga2XYpvXkpBK_LetEPA2iENyxQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

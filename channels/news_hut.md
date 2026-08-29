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
<img src="https://cdn4.telesco.pe/file/W3ciE8AV0pkbirl9eXVsxWBWZUYrlKYbzvSXY8BN7gA6vvKXo1_7qz0Iptan7W2rIWA4Ml5MlP1OclZJlbEc2k5Twkg9me-6N-id8Uds314pf7Ga3SPxhul9-YYvbZ9Yuf5o33lGwlcs__rnTJo5JVNSm3E8RRR4hucBdKo1_LwRhJGIUzx3w3TuDjsoXG__p62I7qzdDw7Pq-wgHenCvfUjmZHUZKAuX8iYYuDsjfDJxB2h6ErpPzUZ9sqpVPVPoxouNqdPZXvZjPTSUPCwM7T49xlLao4KwWb6d_RJMUVS9NWWS_KJi1lI05dOrHExTRSYMZ7guKfqWLUCDkc4Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 115K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 22:31:10</div>
<hr>

<div class="tg-post" id="msg-70770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر رفته دکتر و میگه وسواس شدید دارم و نمیتونم برم دستشویی چون چندشم میشه!
برای همین دستمال کاغذی برمیدارم، تو اتاقم لای دستمال کاغذی پی‌پی میکنم و بعد از یه هفته که جمع شد، میندازم سطل آشغال
😳
@News_Hut</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/news_hut/70770" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سخنرانی یه اخوند در خیابونای قم برای در و دیوار.
@News_Hut</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/news_hut/70769" target="_blank">📅 21:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=iqTDFKqlmegLPIZtC9WI2BCx5dZB4H1-WcdeucyFpuGEbczMwayFhi36F47h2MuTZCLCmDG2Sd8Ltyhn6ywXErHG1_0RGoHrcGk6lFrMPdoPyPNIJc823HUbECCsXov9YaNcDhaGOsLpR0IUnwGwbFi3g-ccCegGjAQ-PCZQEmEZbeWeFpXIqqRDDyU52i-N-2hp-o0t78wgFouAZFVMof3sXNs7GiTVjL8bmXG3N_4fu62sNmKigFW7UuQ_TyTy29KFQKxMqG-rdqqIdmV84qobLm91PBqbGpRUPiaHQlvPBUCf3yPHswcBS30FdwOJPrcOGZM0bAszLXARESdiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=iqTDFKqlmegLPIZtC9WI2BCx5dZB4H1-WcdeucyFpuGEbczMwayFhi36F47h2MuTZCLCmDG2Sd8Ltyhn6ywXErHG1_0RGoHrcGk6lFrMPdoPyPNIJc823HUbECCsXov9YaNcDhaGOsLpR0IUnwGwbFi3g-ccCegGjAQ-PCZQEmEZbeWeFpXIqqRDDyU52i-N-2hp-o0t78wgFouAZFVMof3sXNs7GiTVjL8bmXG3N_4fu62sNmKigFW7UuQ_TyTy29KFQKxMqG-rdqqIdmV84qobLm91PBqbGpRUPiaHQlvPBUCf3yPHswcBS30FdwOJPrcOGZM0bAszLXARESdiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صدا و سیما:
تو رو به خدا تورو به ۱۲۴ هزار پیغمبرتورو به همه اهل بیت باور کنیم که ما تو جنگ پیروز شدیم
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/news_hut/70768" target="_blank">📅 21:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBj865gsflqa4IqXDbyRlwXmzQCEVf4Otd1hUVFf-b5_fAKw_CBo0avl0HXgtmiPckdvPlJ6Ic21Qz94pvY9nzKaXEaVDfcKqnV4OnqbLMLwrjlSyjn-nrOCDUhqV83Rf1duzBFnQ4ykm0Zr1sre0YD4tmr-heMbM_qiJMvrgtMrd2VmADgeFauiluCFFNc3TkG8m7mq8XpkKMxEvKKjeHPi9gcFKbypSwTUfWSle15B88AFSJ5XwN2xl9pcWc3i8JAuCchIWO5dOOvKXwqPjDYeYx1KLU0e2UenOUzDAd9bhrD7i4F0YT6Uagx3OSr1RhNxcCwgyGlsYD74JF6k7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
دیس قالیباف به بسنت:
دروغگو، دروغگو، شلوارش آتش گرفته.
برای ۱۳۰ دلار واقعی، به کارمندتان بگویید که آمار مودیز را که ۱۳۰+ میلیارد دلار هزینه جنگ را نشان می‌دهد، بکشد
از دیگری بپرسید که خیابان جین چقدر از ۱۳۰ میلیون دلار فروش استقراضی نفت را فقط در یک دور معاملات آتی برای شما سوزانده است.
دروغگو، دروغگو، بازده (اوراق خزانه‌داری آمریکا)آتش گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/70767" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
دریاچه آمریکا توسط «اردک های دونالد» محافظت می‌شود
😟
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/70766" target="_blank">📅 19:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
صف ترسناک و طولانی ده کیلومتری یه پمپ بنزین توی سیستان و بلوچستان!
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70765" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/70764" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txCAKV6km2C7FyJYB-5OpAvje1MmPScIX69vIQwsnx05xxTklcUCLdALUK2T2e55JIQHOsugGUhSRfc-Rohj7fyIeLLO1oXU2gjYcmNWP7sSDqVHW7xhHgs7KLU4nj-fhGCi2ksudLmkh5OzW8YKKvzhC-C6MjJupqtvL2xWglAA6p5l360Icx8PTYN4Q3rFC6jmBCyhbtp2Z-dRdDUmq3-98XqfsUrDZuc2cA0oRLjDq_zUCkFmtKyjA4LLoqmt1qmJAAud2Dm4eSO9KXRW0gh_uPsQOUPKB_d4_X2X-TkXdTnjAjIDu5jmWcy64Gm8o0wZ6r2CjV77RNT14__A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/news_hut/70763" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنفرانس خبری علیرضا منصوریان در عراق که سوژه رسانه ها شده
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/70762" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
رقص ایرانیان در شهر وان ترکیه؛
هزاران ایرانی برای خرید، دسترسی به مشروبات الکلی و تجربه تفریحات شبانه مختلط — که در کشور خودشان امکان‌پذیر نیست — به شهر وان در شرق ترکیه سفر می‌کنند؛ شهری که تنها یک‌ونیم ساعت با مرز فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/70761" target="_blank">📅 18:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر داشت چالش ضبط می‌کرد که دو نفری باهم برن غذا بخورن، تا اینکه یه خانم دکتر خورد به تورش و آخرش این شکلی با دعوا تموم شد:
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70759" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:
ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود.
امروز همان پوشک ۸۶۵ هزار تومان است.
باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70758" target="_blank">📅 17:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💀
این ویدیو از سرعت تایپ مسی شدیدا داره تو رسانه ها وایرال میشه
حالا جدا از سرعت تایپش فکرشو بکن لیونل مسی با ثروت تخمینی 1.1 میلیارد دلاری گوشی ای که دستشه آیفون15 هستش
بعد یه‌سری جوونای ایرانی با هزارتا قسط و قرض و بدبختی میرن آیفون17 میخرن و تو چشم همدیگه میکنن
از یه طرف هم بعضی دخترا میان میگن پسری که آیفون17 نداره کنسله و ...
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70757" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار در گفتگو با شاهنشاه آریامهر:
آمریکا و بریتانیا نیز، که احساس می‌کنند رژیم شما غیردموکراتیک است. شما چگونه به آن پاسخ می‌دهید؟
❤️
شاهنشاه آریامهر:
خب، من به آن پاسخ می‌دهم و می‌گویم که رژیم شما دموکراتیک‌تر از ما نیست، زیرا به نام دموکراسی، شما کارهایی را انجام می‌دهید که ما از آن‌ها وحشت داریم.
هیچ برابری بین مردم شما وجود ندارد.
تفاوت بیشتری در سطح زندگی و ثروت بین مردم شما نسبت به مردم ما وجود دارد.
🎙
خبرنگار:
آیا اینطور است؟
❤️
محمدرضا شاه:
فقط ببینید چند میلیاردر دارید و چند فقیر.
در اینجا، ثروت کشور، حداقل ما پنج قلم مواد غذایی را یارانه می‌دهیم
تمام آموزش رایگان است.
در سراسر دانشگاه، ما حتی به دانشجویان پول توجیبی می‌دهیم.
🎙
خبرنگار:
خب، اجازه دهید به شما بگویم که آقای کالاهان (نخست‌وزیر بریتانیا) مانند شما در یک دفتر کار نمی‌کند. شما چگونه به آن پاسخ می‌دهید؟
❤️
محمدرضا شاه:
آقای کالاهان نخست وزیر است.
من شاه شاهان کشوری هستم که دو هزار و پانصد سال سلطنت دارد، اما این کاخ را نمی‌توان با کاخ باکینگهام مقایسه کرد.
قیمت کاخ باکینگهام صد برابر بیشتر از قیمت این یکی است.
در گذشته، شما، بریتانیایی‌ها و دیگران که در اینجا نفوذ داشتید، می‌توانستید نخست وزیران را به دلخواه خود تغییر دهید و در امور داخلی ما دخالت کنید.
آیا برای آن زمان از دست رفته متاسف هستید؟ آیا همان چیز را می‌خواهید، دخالت در امور داخلی ما؟
ما به شما اجازه نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70756" target="_blank">📅 15:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70755">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuA_RttHOxXhFgjgOFTkIWonaPDuzIWYsNTTGp0vaokGpzyBV5gpNUbqinaXR9h7ExK48mYkpKZ28C50B9LgL3bwH3PLE-oPJ9ICIXnXA2qLIF6Qb_7CHQoo_tTE0sRm7Cz-Q-crDWuuvgU010PK-1fZi9phGir4wO9eu-iKDUk0SWYJhQWYGf4aQGLSjUUpIsmKISspuJ4W6dpzSbHYw4zkI3np-z5AceoMAjwvvz8IlQFnAaAv8v3UAp6F-C4uKReXVQb2pK09Wthv-VzBzLmVN4uDLJxJuVG9BZZf0ey24o3PjoiDdMPTzu0kTf173W6rHKcEH50cYg4I8FHxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
اطلاعات ما حاکی از تلاش‌های گسترده برای دستکاری بازارهای انرژی است.
عناصری در دولت آمریکا با بهره‌گیری از رسانه‌های ساده‌لوح، سعی دارند برای منافع شخصی بر قیمت‌ها تأثیر بگذارند و رئیس‌جمهور آمریکا را همچنان درگیر جنگی بازنده نگه دارند.
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه، بر طبل جنگ می‌کوبند.
این مصرف‌کنندگان آمریکایی هستند که پیامدهای واقعی این وضعیت را با تمام وجود حس می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70755" target="_blank">📅 15:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70754">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
مراد ویسی:
۱۵ هزار میلیارد برای شیر مدارس «نبود» — ۱۵۰ هزار میلیارد برای خانه‌سازی حزب‌الله لبنان «بود».
بودجه شیر مدارس بچه‌های ایرانی قطع شد. عددش ۱۵ هزار میلیارد تومان بود؛ گفتند نداریم.
در همان حال، ده برابر آن — ۱۵۰ هزار میلیارد تومان — برای ساختن خانه برای اعضای حزب‌الله لبنان پرداخت شد.
وقتی می‌گوییم اینها ایرانی نیستند، عرق ایرانی ندارند، بعضی‌ها معترض می‌شوند. اما ایرانی بودن به این نیست که در مشهد و تهران و کرمانشاه و اهواز و کرمان به دنیا آمده باشی.
وقتی پول شیر مدرسه را نمی‌دهی و ده برابرش را به بیرون از مرز می‌فرستی، معلوم است که منافع ایران برایت مهم نیست.
بازنشسته معوقه‌اش را نمی‌گیرد.
گندم‌کار طلبش را نمی‌گیرد.
پرستار اضافه‌کارش را نمی‌گیرد.
بچه مدرسه‌ای شیرش را نمی‌گیرد.
اما بودجه هزار حوزه علمیه سر جایش است.
اینها حکومت نکرده‌اند؛ منصب حکومت را اشغال کرده‌اند. اشغالگرند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70754" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDl7C-LJkbnvGt-r4FiAWmycU3aoOxHuoQjHHUCpl24hFvNCAeB_Y0oF1d24fzEnm5G98U2_2oCGArbfqqJJ0MO-UvQ453_C9aUtb6fQFy_P_9pqzc-T7kFNg5cPPLUHImmr9g9Gbbc_Py39Mm3eG5SbrnZdC6ZeGrif9UK0riueeVqU9vRTtnyEnj1CGJW3zn8S0JYuOC1jFpM_Tvoyfcxlpa9T08TNm00-J4La3x-OEZUOH4W5cuZk2tXiYVEyxYDJRGC43AhQlerRkNp8JmXM6K1kMSx2-q8U5ok6RTXz182Cw61Sptwjc85BORPwGSlIiODq6TSn8b1TXUXjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXhG_4bmQI130SoVlqIokrNj0sSmDpQG6yOxQ3C44PMpsB9jVpXW92bUe7wLlun3bh061nIq2bAq5HO8snf1836ZpGJmjIL8uBYd4vo1ctZeeKBPwwRbnBI5s-vjNoy4KfpAdHK022prQEJUWVDSWaYOqIjZuaqiJ-XJ-PaiVcdttC0HzE6SJLHA0WF8oqK0w6JK5ojgXWdqyRLKPjObugR9M0BoEeCkBNYZS09NpRrdUIBX0d35k5VSQkD1FyiePbEX4ssZ-ZPt0w2aaKGD8S_NIDb7eeOy32ZWbSUyYDiGBMPKwte6ymMcSx5jpTVbfJwOPE6hSeGdhsZvVJQ-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9FbQzYNwPvLp6hdzYk0kBbR5zYtNlNsyTI8j0wyGB2KDmZzUdOhibqb519xnwcjNc2yLDyDNvPGL6vgQHuvetkR2CNz9zqxwLvHy8KIDcWiRaNBJKtsEf8MZOcUJkbc-CX1o7HghQHEh7tcL6f8bRXjJNeLPUXp_n-x2L8jvhQxE552lKw_EiXH_cMVXqTM_wloS7RdJtcCjkhcjFzw4XLb-gO6ipFfiejzHuaEXAzxZepbBbmvbAz4hGJ0mPZAvlkSVNc5nbc4_d-nHSjwTOKBS2EPCchajnsY3Iws7sLTLltvX2NGIGGzIr0NGjprSHXSnISI5Y8nTpoOKGa2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALuhG7RHUsoUUxnkdVMNU-5rmfn99FYMAn2AXFYWfJKWnvEcmSVE-c6HcJP4BUdQp4nibvdjB0HLKj9cIBm9dFuMC13ajzoF5i3GUJhREAbOCEVMjSFh-59D7Et_DcNSmAMJX5zAnLn-ymEHkRADJbjYZDjPfJv1mU5GQ_KdrX3aGlyu-onMloRIewr2Kjcs8QMrb9wZ7uw6PzpZcSUvb16YhL1lISO63NLCTf3bz9wZch_YuIbRw33mWAAgjF-lq1zDMCk0ca0MD6meAvMr7cCy6gYlQL_z4iiAIPOSqvtP4AsaFAtkSZQ5_8r9S4wHhLa293TZC5fLBEnjVSfs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8l84jHhem2V1LgwWIUWmgrPZZbV4megoqusE5tfb4Zi8IGms9VaYYyAs3TDvxuedGM8gB2veqOs-dtOP_caUwvBaopZ8W_IP4H6NjlbMbOEaQMz-7V4WkGUuOdb6bayjsKJy2cPihHFFW49aUHmqeo-vyrF_Boytstz81qlbq2c5KxwqGQOenPEtJ3zUtW9xqDbqfvcd5fCaCz4rlwoZMR0EJZa7k8vObyoMMKklvT5a0vH4sb5CajdeoVmvKNl3Hn0jF5m4WfkDQ62gKpy_w8q6AteQm0VDAvWIOSG7GBEPvpqDz1yqBl3VshgMYhgUjGtZue7bbD5mQQ200OFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL6bikRQU5sagSvJ7gkzTMIaEcpmeK6Jg7TIfCG9ThA5lhO3o8KCDz-P2UMVEFUUegA13FBDk7ZvcbtG24H09krURJaZU8Szid_HqlWPxRVaM9nmfgZLderR-3sKv8I9fOnbzkNWaQ3FSJxSMyxKb1-HOFK_1DCRbSefM2hM8FRMYvPSeBt3xK0IeAkqBMHObl0X47wqq6ZAqDpQ6a08kl-Inm3KEz7_tCyfVm7b0tpVtMwE1BSdaj9YakcRBwBCjMl7ayxFf5FRIKmprGgrL1S6SdsipL5mjdb5MHyMx0p1yfENCIazMdySG1CYUgyCGOBDsT4tgllgi5VccieRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRMTPorfJBPYx1kvegtNYB8U6QILwbcO8tsd50exh-jTI5YxcR-5W-YlCdLvtIVwQBYEAvLQv1WdIUiIZGwC3tRviyfO6s8lEHnAmWZcbHUEfNhuxHxE4FcF893ldhTzAUYHFIibJ-KydqZN-66erkpCFUPoSfPF_qSMM3feihFCotMB4JirlS1X-z4H-R8plhh3xW-JuEBk3u9GHd_2LblYxNLVnLLvP7A8SYiRn_oSMOum32Bm6EWpbuXvAcQOyy6z6u26pDDLqudidTLT1_SUiSLPzN0pbxMSfd_Dm6QGc48IBlBETysaa_DURcJaWH0nXaWjVTRlqc0duAX6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYbNatPLoAw2Iv4xQJmPmUDBqJEAy_cPfGKUBzJmjzUotckwRb5MsivU9TUbVp2d0KVR_0PBin9Zk2EeQtWjfOvmHJZF7JjA-WTxxWIXqnAtnZn7JkN0cwr8mxnyadXeNXAfi6qkZD5ihgD8cPDNJHqUjttrB9SXNiIACiFFcm_9zKPxNTxo253g1-HCM1Ue9qQBu5F_Lqk5FSZ16jq2qi5BRMg_ABP6WVjydBqByj1Nlq6Nk6y3vcZ1yLpgDFuzMBW5iIXw0SDO0Jm9c7b-TkWYBgyW-XQcFDD8O1dtmpPd-35cSBw5NnBl9vDp4MkLSZbW8wrryENfKJHySutrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=rrisaKTk2NDKxUIeamDQZhFNBJHpAdfKi01XO1842XmewdmuxAhsmqMcnzk6PJlDNBh0nwJ-iM-SJ6oXvsfBiwmNqOldEsh9vxh0Kbtq5Y0uBLjQ6wBw5iE7cQ_FU0VToeK7uwMyd1kzjbC-ULoZt3x_m142fr1sTZcrvQREPMxAOWn5E0QCEplW5qTaF08ww6I5jsCfX5FHnjHBhl4WrXzVW-l04Hs2360Vxf01Dk80Mb35GFYwWtHXIF4M5pS-QZBHYTONk77u4QPJJg-byXZnmHA1W4oHi2tW2SJSzVoFmUnVnHXoSV682FGqQ4Rcx-f53Azo6ZCu-I5MQ2cU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=rrisaKTk2NDKxUIeamDQZhFNBJHpAdfKi01XO1842XmewdmuxAhsmqMcnzk6PJlDNBh0nwJ-iM-SJ6oXvsfBiwmNqOldEsh9vxh0Kbtq5Y0uBLjQ6wBw5iE7cQ_FU0VToeK7uwMyd1kzjbC-ULoZt3x_m142fr1sTZcrvQREPMxAOWn5E0QCEplW5qTaF08ww6I5jsCfX5FHnjHBhl4WrXzVW-l04Hs2360Vxf01Dk80Mb35GFYwWtHXIF4M5pS-QZBHYTONk77u4QPJJg-byXZnmHA1W4oHi2tW2SJSzVoFmUnVnHXoSV682FGqQ4Rcx-f53Azo6ZCu-I5MQ2cU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=IiSkqiOQgUA0JvarnWKSuL7iWgxKXLVTNFlG0l1yl00R3JGGXZi7OWD7HVzW94yN4awsuhHRZnn0HPQxwzXeFbazoSfBNB3L5ojNSR_Q72I4cLi51r6LyNWBKXKRH97Z1cDkKbx1KLRu0f65-jsSuFG80fs3AyQertMrbAtF7e2SzazpSmUsN8yk_TE3iCUtsckzPoi74FJADAGdPKTid0o2ghf_X5FWfAnfFJHBWUF1G3CjuPlapKIbM4Q4ot5an88Q7ewYdZf7wwu3hyV63Ar0jqh5YBdCxoophchYqhfGSWzNEfynU4avpynXlxQ32llUkO_-0myvYaJCsDcTTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=IiSkqiOQgUA0JvarnWKSuL7iWgxKXLVTNFlG0l1yl00R3JGGXZi7OWD7HVzW94yN4awsuhHRZnn0HPQxwzXeFbazoSfBNB3L5ojNSR_Q72I4cLi51r6LyNWBKXKRH97Z1cDkKbx1KLRu0f65-jsSuFG80fs3AyQertMrbAtF7e2SzazpSmUsN8yk_TE3iCUtsckzPoi74FJADAGdPKTid0o2ghf_X5FWfAnfFJHBWUF1G3CjuPlapKIbM4Q4ot5an88Q7ewYdZf7wwu3hyV63Ar0jqh5YBdCxoophchYqhfGSWzNEfynU4avpynXlxQ32llUkO_-0myvYaJCsDcTTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=UV0TnEDO4W-FMLO-oiLGcAetroF0d5pRWFryoggNAzIuK_e8OLLiN9dW3Lx-K6jikyiZjI3DO7ZR06eYdIFjdkrE6G-yeEnXNS4hBUl2YZNObTOf3Go9KhXvtw24VReXmBO1cYljDCVYCkbvRKbM_ely2WNUjk4gmYBbpx8fam2o_B2UkO-3-sEEGLgokbtq5jxNT0PsPF1Jfb8UxXrdMzB_j-D08ZixpapCURT-FpleZbITlaJP87melAsCFhtap80lBEyM-Rv8FXFHen5x6LAmzNeCthq4syUIW4WOR8gztKhEVLoFNkgoniMY0KDkfI52bO1lCTdvlDOIqwtQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=UV0TnEDO4W-FMLO-oiLGcAetroF0d5pRWFryoggNAzIuK_e8OLLiN9dW3Lx-K6jikyiZjI3DO7ZR06eYdIFjdkrE6G-yeEnXNS4hBUl2YZNObTOf3Go9KhXvtw24VReXmBO1cYljDCVYCkbvRKbM_ely2WNUjk4gmYBbpx8fam2o_B2UkO-3-sEEGLgokbtq5jxNT0PsPF1Jfb8UxXrdMzB_j-D08ZixpapCURT-FpleZbITlaJP87melAsCFhtap80lBEyM-Rv8FXFHen5x6LAmzNeCthq4syUIW4WOR8gztKhEVLoFNkgoniMY0KDkfI52bO1lCTdvlDOIqwtQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=f22JUw4uP34zt0FXY6Zep9lAy-fVB2pVHKHH--P8jKO3oVw0ue2VcjzoZ9zXilbQmUu2FjEPT7fbZ6M8g7c7MSRGnFBa6D1aa8FsR9gzhKXYfVZ5_8Z1NT-NOK4XOfwWJ2BANa7hmDK5tMztHEKJdSXD_ZA2Oj_Itcv_pVbpeZm3ZMXY_pm-8mlwkk-ZuQTBL8fAYH0xM2dtN9D7EAiLWPj9pHaJuBRA3NV3FBhi96aaB8iMqthANk5Bgf1USa-kMXZPZgZiM7RabqK4w-WsEJqi84n4plZ0ZdeCiUZPJ-rwAiAGONZZas38mSbVUXiocQ-uTUwxclcywW8AVgRh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=f22JUw4uP34zt0FXY6Zep9lAy-fVB2pVHKHH--P8jKO3oVw0ue2VcjzoZ9zXilbQmUu2FjEPT7fbZ6M8g7c7MSRGnFBa6D1aa8FsR9gzhKXYfVZ5_8Z1NT-NOK4XOfwWJ2BANa7hmDK5tMztHEKJdSXD_ZA2Oj_Itcv_pVbpeZm3ZMXY_pm-8mlwkk-ZuQTBL8fAYH0xM2dtN9D7EAiLWPj9pHaJuBRA3NV3FBhi96aaB8iMqthANk5Bgf1USa-kMXZPZgZiM7RabqK4w-WsEJqi84n4plZ0ZdeCiUZPJ-rwAiAGONZZas38mSbVUXiocQ-uTUwxclcywW8AVgRh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-taLyKPEQ8j0qGxlwYAzMSx5oPbdHLjTR53Yy2uos00SYJEG-0Cek6F5UPC8JwyWew8ml4OSZw_Xo-mlj1A8YQXI_dX7_8dqw9jMAYdrIivoM-_vvKbVvwiezxnL8jWNsXvYrEkOn2-xxvdDtOwjhLimQC6lbVJV9OTrzaFRve_EWMgWGo6mETahTQh-042XVrKfodz9rRTSZKRr1WjtOx4gPa-AVu8sx0G9yoIMNq4tvGcwsk7VUx5lpbLRItUHzm0P-VYd5gn2r2jGnQ2cmUxAVV_7KVrYfgdln_jCV8csuBYn8U5341QcCi_w8PLTwjl9-80wjQ-W8tKe6MFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_mtyOh0k-31ldDcpRLDIE-9bLX-JUnAA59ncO-EcPBNW5mei35BzxYYqh9xal0nBFJ4hAQT59nCUWYAzxSH-BG4ymNWrsJLLZ70R9MNVv6Vk9t5G_ddRjWOAonLkJ8npoZ4_nvZ7akQOuij_8KLJ_jX_jdU26HRNSW9bpCeDd5HDTDVlVW05A6pI7xDfw8lYWwDYpL8f3e_1hQ3i-o4n90u7-I4fUYOtYDNg2G9h7SjHmA-g_y0VBwZBtTtHfA01p7XF3_9rphQl7Mrh3YKrpKFADgWslyvbO1nHvPA1sDrlYMIds26FdGNwUyLhQUApeYWGsmEH72j-NqiF-sO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdv04PC3GjONLIlY5lAw5AwjUhGJkvYam-DBVA-CCCDBc0rxjRKRk3WClJRiKqeIBTmupxw9gzZNTLxwJdkui2CHs3vwrTA1Y1elN7XVQQPZb3_rLRNAO944nf5vaBs6HF4DWvdYOeernh8ly1_HpYKprMn9Nt-x9AKwKw1w4Fkdy-KrAhGnmtrTJI158UYcpJpRmOxJHgZ8y8doAx7WinaG6Sj0JUB6QDyb7FsrnC7BWkeNjMHXpN9THRKe9BYu4AVYKEsmdTZh4HjuaVdENjU5NI7MiVJSdw4bhdSbFUKCxmLslgEuufrUib32Zjwk7yCourKcn_mtZoztvyFJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
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
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Q45txNhNjUpJQfWRk_Lf7rDCGSbuFEs4yzwPyTv1NaMYJF0eaGp07ROgwsXJyTeACML1glPWNS0h05gS0_K7HJYy6IplElDPeXOdReDpTueswN2Hy11ogdfjLXg4nTdMd2jtH-Ag085U67xYdATLZOZeAbplKtoW8KTH8fxaRuUF5-7yOM4wHZIt_QriZRmJ0xF4skoAi2LjlI2WTnjQX7Gs46LE-QH13EW7FmkT0kHgQW-hpDUlXNl6zlO7RndJ7byjGVr0FkPrpaxkI3sxaHyDfr8KvdmxH3nnJKglx2trjP7QQJWWdOGxLjFRkOPHT330KVSwFM0gxjqFuh_rSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=Q45txNhNjUpJQfWRk_Lf7rDCGSbuFEs4yzwPyTv1NaMYJF0eaGp07ROgwsXJyTeACML1glPWNS0h05gS0_K7HJYy6IplElDPeXOdReDpTueswN2Hy11ogdfjLXg4nTdMd2jtH-Ag085U67xYdATLZOZeAbplKtoW8KTH8fxaRuUF5-7yOM4wHZIt_QriZRmJ0xF4skoAi2LjlI2WTnjQX7Gs46LE-QH13EW7FmkT0kHgQW-hpDUlXNl6zlO7RndJ7byjGVr0FkPrpaxkI3sxaHyDfr8KvdmxH3nnJKglx2trjP7QQJWWdOGxLjFRkOPHT330KVSwFM0gxjqFuh_rSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=B9STpXMiBiAfdUQLQTDKrcqETECbJP95DfEuqWbCxyXofxh3GUH826dPWY3LqL5PKdhxCCGN59J06HNHdzs8CGYgbZWOI6GbKo0LK8l8v7i1Qjvd-gCk4Pce2o1yBWuBWMMaTEAeYQp3KNX3sFkfOJpIhBv2ICGoiGQjUlmyWsvGM7ozSw7_zCvlCY55TGZI6dcpwbsoSPfAPTiEuJv049tG-F_X1j__oAbcevXsZ__XKju6jT-zfL5ltJyB4xTStUbK9c_8CBgVT9FLnsKwk9qZwKiz6QAQR4GIC6kaWZqcirWRb1Bwn-svLV0GGcvjSZbiWYQ_dVtPY3yE7i-CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-54oIM0O1JD95oMp5j7mCWpE408D8uKJsUSNedg6AlyrXosxZgxBaEpQNGHqUPs1qWBE7Fvya36HhaByMujCLkXy5Dc8PrNTTsOwGOYlk1VOGAG_DylSxyaVoVQCjWkS0YtOx-4l6cRPvY8zxZD4hsQouRiumHiv39LEape_S-2ybN7qcviYa_KyR1tL9eo78fgiS1_3L4VMMiGr43v7K0ZstRYYjRZvRUXxAtwgGza00nH5fMoonQYkfSaZ3nidi2n6UyzLuxX7YFLNU6DrpVuxhA_a9lWIH1p403DgsiZXQ73TotUZTaX-10fn-SWPg9sXDiUEqZYnk3MdFUaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=tEzDA6gN319mnRU7VNdr2nmyEO0jnZtxFtz2KjousjQHCME4zFpa-aEkHnewsmYHDW3s3bGySSbLfC2_Um48oSiUAFWF4X2h7VwzfTPCDaZKufHRHTeMsxDCpobV9w7cfEQA9oH_qzkn1zuREG1tcnmQpFJgWiGN401QhpHT6jBvH5wuD40_rBLYNwEjG9sZ3JRbe-pgPEf-XpQfzWoajQmyeG3Qvw1yYzQZV0frmOvmou8Wp9YRU6wss3Ea1dn0DDH-iaiyrRHd-fxhRbgQSEVb8IjqXWTZET1RrIbLnBDYd2sP-fBW0x19bcK3NTWnvMhMIfsyQYLthe0use8KKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=tEzDA6gN319mnRU7VNdr2nmyEO0jnZtxFtz2KjousjQHCME4zFpa-aEkHnewsmYHDW3s3bGySSbLfC2_Um48oSiUAFWF4X2h7VwzfTPCDaZKufHRHTeMsxDCpobV9w7cfEQA9oH_qzkn1zuREG1tcnmQpFJgWiGN401QhpHT6jBvH5wuD40_rBLYNwEjG9sZ3JRbe-pgPEf-XpQfzWoajQmyeG3Qvw1yYzQZV0frmOvmou8Wp9YRU6wss3Ea1dn0DDH-iaiyrRHd-fxhRbgQSEVb8IjqXWTZET1RrIbLnBDYd2sP-fBW0x19bcK3NTWnvMhMIfsyQYLthe0use8KKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZZRIK2LImwhBSem-f4uMAjgLj_QmSSIHFP6fVD1DagqjOhSa2PGF40NxU0iwSwdqdfHl3eC7Gck5fT5rx_uQHGo6n_llD55ZY4449Wd-1oAkQXpxzRx4_q93cg3_yKB-jwy6juM9kZ12qEvwDMFJxc70e2LT02pXJWdLF1dSbNFrvjXVNMVOg_OOKlqy1f9rln3IpsMs0dI490kOIPOMIqxaJskBCjnCYQHzaD8tJS1ESjCi2tf73CJRYCIf8arP78PfpGe5P21-qjE5uBq0aCkCigpPicEZ4DV025aKdu4zabd2NX7eOZKNrgcClvENk8ytOX84GrbQtKMMnzEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMktRqPwBpu8I1GbCl3CjDBwWXcMOwtEMzOCuyh3frvLpNruC9rsakxvfGbrrMDMOjlwmAllqKYLW4oFWvtjleWzgK48njxiNFhPWNIMhkkE3ZCQBQyXZhDDApkbKAIxSh3YgtjUNCDFb049MGXy-NvPnwkWBKIfom9HNXQfHwVQ0QkA84unlEyd13cVxU2Zd07DdgkNdQnEhm5CqzfYLC4ciXsj_TFqp8ivH77S03XmfWU9xs19FzjW_JrQ7Dd9Vod6ZepyChnGBJOI9FSZVZiEfWn-EM0s2XgPESzhMvNdFxWNTi7WpIg-YCrNni4cBJIuB1QsXn6-SZ15fqMxEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ScAiv5ncTQL2lQ8G2_qVG8U2R1CilBfOJNN-HVkUG7FOBEcEFnkeLMOur5Sh8bqGY1BRFCk3JeWB6O5I0tfqTv1E-XXYsyKsQ5BafbtAOLCVXreeoiSohIA3b6PdV8Jc8dzE0hvK_jOqzYPgomfn6E9o6nT-DS7wBUaMzRYo0nyOgERqlHoCk2yMQ3ziBF7TZW7cV3JYIxAEwuhLYgGcxpL_gupWlevV75ENbWxsTNqJyw_DzjA3exb-Xt4-vMC58iOpewi3CY0D0R5A21fmhFVj2-W4IgN0PNqXbSUKBqOxCL4Ll89MEzowkde_QYK2S9PQTThqDmx1xSlwXf1Rzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ous6UCwOKIjOdpeOwxTjyCOu0225twd7__qv513yhXFxMAuIvfA86IyHvsLQOvJIUrhEqP2WeAddsDZXcQt6FPf--IRkrx6VmbPejVh9iJR-ku6J4ksLSAbaIBbv-eO0ayJoaOQg6QFfuRxXqZ8K-nHJpvE2pkDWtTOjP9w3VPEORwAEbZMQbawogo_9hO7kwDzTCLG49_Wr9J4Mv4MAbcvSBZm5p34-2_wpKnAO5DkCnMrok-uUKMKIcb2SJ5AZbowZ8to5ZxU8cir8MgoQ2wA3QnkkaITsse_v9KxAvhyrtX_JrV0RgllUKqlkhS_ACPsv0XANbii9PWH7wzKyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AnfhueMmvAYy45fb7r6g3nZLHRlrYjPoCRKbClpfEvassIxKQl6pYWGphYJ8lMximlNLlhBQtpq-XzHjOIIawUs8qgIA7RdhW8EDd0oCgkQjcNy35o0Qbcae-dzpc2qs9GUJ4khSgQKom2cx-uzRIltgZh6REOLA73ZaDkzZql5oFPPvhAT3sOU7UCra_l_NIOFKJt1thPWE_WqBZRYMJwgYhejSYQZ9L8RoF6FgHoCZ8Y5WfSBFhXQdAoiElOmh5X1kerxSiX_nO3hWEdeuUfenmSA4djeqtUQRRbGvwHqimwIeYkHGxobeEu6XBdnrBgVgbkOL2cJZmSIAQe2JbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUkRCbK0Qx5SIo9mBBBJIb3uHmk7T9U0mBevyjMqmqdeAUEOWoaz3xAF0dmcqHyIBFxTOrkTS1_d5XiwtQWhZyqhLJg2a72inMlU6h3gm0hpBGXMeI5LShifSKAFrekmy-6dMK-KocAiXOE39wFzlotNGgrhj6fWTArTlBCXLgUWvI_bvI-ueU4t3USE-XumHQt1-AvKuc0Yr6lzgDLrX-B778QcVliWOm644sAsWivK41a5ZpG_vZ2_1pRHgMmHK4VrI8MmBop7FVHyyR9jMiL8FEIG_F9xHtrl3ybH7Vc-ogold53KMShtRhRJZSsbXcGljjDalldNnHNBtIpHhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=icamR1n6A_GMZOjFrPFgzbCpdhQ9ziQ2Zpp-H9ypzEHr0d0sn4TZZJTrSfXd7AWlsDI3xP0oq2leOg4m_AsP18D1eGQH5Wa_K1KWJzFW57ox6NMhRAmnv6006KuJ-KxKpFI-gkrYbFhAFEkzRQ_egWmSAiFnOfU73YbmOouv8_3tHXQxA3183l8qWA32ChMj7YVqv2GzfnZbNZMRozwcEUT8g48q_1mG7B8txCq1TTG-BK2ce4sBKMqvYfJxHSzFdri124d8R6BRnaf16w1qY6wmJLfuRCvgrWitCcZFImeyuhER7SLdtaET3zvslvJXZ6RZNVXbzbO1rjKC3amJ6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=icamR1n6A_GMZOjFrPFgzbCpdhQ9ziQ2Zpp-H9ypzEHr0d0sn4TZZJTrSfXd7AWlsDI3xP0oq2leOg4m_AsP18D1eGQH5Wa_K1KWJzFW57ox6NMhRAmnv6006KuJ-KxKpFI-gkrYbFhAFEkzRQ_egWmSAiFnOfU73YbmOouv8_3tHXQxA3183l8qWA32ChMj7YVqv2GzfnZbNZMRozwcEUT8g48q_1mG7B8txCq1TTG-BK2ce4sBKMqvYfJxHSzFdri124d8R6BRnaf16w1qY6wmJLfuRCvgrWitCcZFImeyuhER7SLdtaET3zvslvJXZ6RZNVXbzbO1rjKC3amJ6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=IrRt_En4vA4qGsaJEx-twgFYBhocBHKkfTDooMcZrMcTObz3ysXtUwxePofiE94ykDeJ_QGbo_8SKUiXLkaIAJNKd9RmyL5lY14Mioxkoqvj9xQDlwbpr9Ez8GAlMSIeRy249M6KnR781wsStzJvVnzRLf5YOUG-Lu5aU-X_1tRn6PNMZTT2GDv3ypNg4OjFBOSlB5Q7wIo0B3MdPhJ2GYdmR_O24hSpRMZM9zRZ_qGbKkY7Izvtf2-alGFTx2LCYdV96U4qeFt5LoR6cdDY5oZtYAQajnL-iTFP2Zfv6D_dnRqP5qA5zEjkbzD1tZ_5zTt4NuyCmrin9k7gGdaTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=IrRt_En4vA4qGsaJEx-twgFYBhocBHKkfTDooMcZrMcTObz3ysXtUwxePofiE94ykDeJ_QGbo_8SKUiXLkaIAJNKd9RmyL5lY14Mioxkoqvj9xQDlwbpr9Ez8GAlMSIeRy249M6KnR781wsStzJvVnzRLf5YOUG-Lu5aU-X_1tRn6PNMZTT2GDv3ypNg4OjFBOSlB5Q7wIo0B3MdPhJ2GYdmR_O24hSpRMZM9zRZ_qGbKkY7Izvtf2-alGFTx2LCYdV96U4qeFt5LoR6cdDY5oZtYAQajnL-iTFP2Zfv6D_dnRqP5qA5zEjkbzD1tZ_5zTt4NuyCmrin9k7gGdaTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy_WHKZoUcbawJAJc20MS-RGCm8jcs0LChfZBHiGis6eUXKXTb7bXgi6oGskQ9LpTrUtqKaXRUw-0MMmcoKcqXmpZ4W5XUgpapVkUKERjN1GbR_VMcETF3sgGRS-opTQ9-WgtKLcaxjDLoxNX-c5ES-bugIDDbmpuRe7-d54vjJhg8wcZXaVg5YiUPAVuzzPXXcY47FHH0areumHTKAb61mGYgggf-e9oQEnhlqxKxmSmDrBu5R0g_x7HIqzbwnXlC5QTJ78MCqEmUDgz6czdayWN_XkBMn8x5O4mYLQiVUp1K6Lw8xkUef6djjOcuWpLAp9oaDs1BFssfu0sALHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7PgVNswqTD7mlDW5khQtTPeKH2xY4M1Ll6xHr82ubhMnkZb9IJfD-x6fWmkcMZS9doFxqieR90X56mbR5KcNSuaUmxLIFzZbj_q0XrR58vxXNkmlNJ_CsyKZBSbsf58mxqUZktZ6HcFtFUIo0MwqTAwE5Oz4ne67xB7sE03GkIpjf0J8OLfTgCJDwzX-pqmv2yXYtWWiHU6FO6hqeEhnkyexEuX5SdVnieTqojrXwSg-gfsmH5S5C3At64BWCMe_sNg0ImJX5SKe-3rjUDxHC6ofvMLEPZSrBMmoxYne9iZOYM5bn4n2zecNLZqlTYaL2y4noKqqEjW5YqK6h3SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu7dZ4MaFHzifAKnfmWhTjKMgDWlncoLJ7pPhFnC5Pau9T25vqOmmzf6RERUm0ts0OBQoXq-e8gKOvgQTNndyL7F7he73il-pJK10FYx3u7yL3N1nQC1a2k1NX8HN9kZVrZeI4aVnftAbsW6QzvvxrMjJQhi5oB-JmdipuPN4TjvHfGrn1CQzWzoycmum-UT5VqDaPd8-gFCzC8yglZ3z4UWSA52ipKAA3ALaXQyk2ktPuaQSd6MKJbDjFBXlvxObXGYs_OZbALxQ0igm5_uFa8FCs-ENfhuDSZD8pVTfzp4pVgfcjWKVDkjrHvxGI2mELJMeiRN__g0sDpEm-m0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeEHR9qzZJrzppRwKM4aqkC0k3_C2v6uw9Q-egnWVSTOhDDoeR3qhXTBnjGWXEasfrTyxgVNZvy5cIbt3iWa7-bykqf3WYVDhfffSoGXgpa-yfmYkew8ojwRcOvvnL2czzl_kvZGuQHlSakKddN-V4wiGVUwPfaev32zkYTHpZM87bhagk3qt2BzenP8xYaP-zS1bKI9TpV4wczXvGRi-9ltYeXUhjEZoMRfdnBk08dBN9rUo-LO-CjyB2WFh0o7dA1GTqPd6HhFS_CeDreS7SsEijExqe-Xl1dHgDKSiBgfY_Z_0Gl6bwqTgmxpLG4sJRA_KXbj4XIaaVCWyM0y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw1FK1qalSOBUOA6pkQJKTCvac4tN67zCcmkG-Koi7MyM4S6mCdWu2yu6dk0TjDpqCIedk1l6h9rAlB7pFEMKzYfC1TZRIGyQOhVJgQbcd-Lrwram9Fs_N_RC389lAjWXTD5frXI2mlM--2YkVwxYExa3DhfqzzHSNtUoyDmB0YvYdwa9cTtZKiiOVAjBVUkFM7PTYUd06Q71j_2E_Xr3lrEs5Bw0fv1hAvHdQSPupyC9DQO9P_WRf66Tq-NjPXrVTKgopozBb7s2RVRYSGsP1n6HC3NMr8G-pcu72iXTEIuh5vL0hCmj_peTYFji0SfPOrtVymEwLRatZbSFIN3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnoZ7seP71U-eQIwXsQI2wSJ_a88-Q7Go6EOMYOfz-uRaevkA55qT6y3tkZuWWdW1PxERi0PRMypFM_1TO-tEP4akTiR8XY3nK3xODNmFVJ7OIpwA_V72ybL7vAHSfMHAcQgON3fwXGVoR-eG7rXd0ncfi5xTJ5eavQooYrQz5zRiDVu0ngIAvx9WgTT3-saZKd_g5wkw1r0utOG4SdpkQdBU2lp-3MHLmKRiwZk3bojde5CTlm3NImoV8QOmLvH46So2lSA1pLfU2ej3hLSKmBN2Yf9s61iaeyaD096bM1QRv4zE-6Oqj_dAsIp3F5NxVExVHyBAOsIsqNxdYaR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=NG2GvlzhGHTv-w9xarGLRhB5mAChr2S1MaiQL_Y0tsX9lv8gJVb83nL3axGNxcaXFZ189S4zJJnjfkQ-rnlQv4ZHz6EatKJU5opqO6ELkTMTnwYqZ6McauxnH5zefaz30T-X0J4lUCwMVFFEhA_5xKQVdzY-pkLtaVEJ_kv81YhWD2YEmIkZGrN0_-6ejuHi1YKtokDWLV5CSwppAAIolFwVjs9AYfru-4_agKqEimlK-kSBt9zaPX55i_jKcT3Wvc7AIKOkpOe3z3D6DWTvBbccVvO0xnm2JAVGltFD4yaJzbcQbWmEedWi_UhSU6NgMu5ucfjpRcQYsrsN1-uqmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=NG2GvlzhGHTv-w9xarGLRhB5mAChr2S1MaiQL_Y0tsX9lv8gJVb83nL3axGNxcaXFZ189S4zJJnjfkQ-rnlQv4ZHz6EatKJU5opqO6ELkTMTnwYqZ6McauxnH5zefaz30T-X0J4lUCwMVFFEhA_5xKQVdzY-pkLtaVEJ_kv81YhWD2YEmIkZGrN0_-6ejuHi1YKtokDWLV5CSwppAAIolFwVjs9AYfru-4_agKqEimlK-kSBt9zaPX55i_jKcT3Wvc7AIKOkpOe3z3D6DWTvBbccVvO0xnm2JAVGltFD4yaJzbcQbWmEedWi_UhSU6NgMu5ucfjpRcQYsrsN1-uqmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AdfFvRje-IGjykvjkzJ-2NpagqVTFSdB1D-l6FPIKM0hem_QYncrd_3qP0AEAXEK06NlJqA66cqBjK_fRKBhgG3gQ65QG6FKBlSZ1aeg9ccDaFHM3bOl121wr6MpqL8fdmR4RioqIrAJD7msn60X-t-ljHndm3sLuKqH4VNb5YDk3OWL7cZwLFDVCjYh_-JPETqF3gJbXgtofqPxCotexkF8UzOH4i1P5OqQR-JUOJSDy3y9urjwpTO6xyb9AxHa-FOYec27XSQIz4iqAyVO2gr4XsXifP43WZuI6SzBYFmRaSMP6fodjTsneSVIYQ0BHhHFZejBJ5sXTROaegGEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AdfFvRje-IGjykvjkzJ-2NpagqVTFSdB1D-l6FPIKM0hem_QYncrd_3qP0AEAXEK06NlJqA66cqBjK_fRKBhgG3gQ65QG6FKBlSZ1aeg9ccDaFHM3bOl121wr6MpqL8fdmR4RioqIrAJD7msn60X-t-ljHndm3sLuKqH4VNb5YDk3OWL7cZwLFDVCjYh_-JPETqF3gJbXgtofqPxCotexkF8UzOH4i1P5OqQR-JUOJSDy3y9urjwpTO6xyb9AxHa-FOYec27XSQIz4iqAyVO2gr4XsXifP43WZuI6SzBYFmRaSMP6fodjTsneSVIYQ0BHhHFZejBJ5sXTROaegGEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=fvmVjm62gStXmwCRm-mR-NThhcCvmdRBDoa3RrbieZpH8DYENk7iDkBdW-nFGM86hPiN0TOdk04zlKf-FnpE1uaDd6D8u9pwhceqh43VYj42IIBl9Q2bPHLAc2tQYIJMHPmbD7SHbbvPGSQ8db_Frq3ftACp8Ip9D3IREBd4SA572eADm4egctphPTrapIflmgJguEhw3lGnp_UOGE1_AigkjtmOOdqOjk7rjHPbiXY_w1CBXlegwCx9A0pM7o4Zp8vAb9Pb1Ab_zgR6oDedbJtB7lmjAU37SzRzUeeZvKqqc-1VDUEIWnkepqcVgdd1vWWIk9WTiq-8EGzBL0zjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=fvmVjm62gStXmwCRm-mR-NThhcCvmdRBDoa3RrbieZpH8DYENk7iDkBdW-nFGM86hPiN0TOdk04zlKf-FnpE1uaDd6D8u9pwhceqh43VYj42IIBl9Q2bPHLAc2tQYIJMHPmbD7SHbbvPGSQ8db_Frq3ftACp8Ip9D3IREBd4SA572eADm4egctphPTrapIflmgJguEhw3lGnp_UOGE1_AigkjtmOOdqOjk7rjHPbiXY_w1CBXlegwCx9A0pM7o4Zp8vAb9Pb1Ab_zgR6oDedbJtB7lmjAU37SzRzUeeZvKqqc-1VDUEIWnkepqcVgdd1vWWIk9WTiq-8EGzBL0zjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_myzak1SBPDpwyTqRJK2PX1N2oVdLOVAZo2XZc4L7A_GZgCMqUZV3sj0U1wRllCZZQGRmIcvkgmmlBcckwryTh9MSaYM6YZcjGcw2crOjBjd9qT89kdxYvfBjHSNodd5zJKEuD_P8dLEojYSRoWgFVxmKAKESvbaVaeLdWz_alpJM-AMugf5_PLHOG-XrEorxqM1GX08mrOMIj_TCj-MFtG9bOybmdMSYlF6azZMq7d2EPLeGa9mgDkjwQH2SpOAEm8agdeoqoNxkfFh-wOuePrhDe4Qd7b1Dvp9NxfYBGbwbjts73QgyRF4sGUSYKmYiqU1riP_g8V3OLDGnS22M4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_myzak1SBPDpwyTqRJK2PX1N2oVdLOVAZo2XZc4L7A_GZgCMqUZV3sj0U1wRllCZZQGRmIcvkgmmlBcckwryTh9MSaYM6YZcjGcw2crOjBjd9qT89kdxYvfBjHSNodd5zJKEuD_P8dLEojYSRoWgFVxmKAKESvbaVaeLdWz_alpJM-AMugf5_PLHOG-XrEorxqM1GX08mrOMIj_TCj-MFtG9bOybmdMSYlF6azZMq7d2EPLeGa9mgDkjwQH2SpOAEm8agdeoqoNxkfFh-wOuePrhDe4Qd7b1Dvp9NxfYBGbwbjts73QgyRF4sGUSYKmYiqU1riP_g8V3OLDGnS22M4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=XKcTuAjdWHK7Gni3hFdEdr3fbsPdyg66MBNHn1I02_vp_amBsDc1y7EseLQDNkASmxxATKz-Twmh_qOZGcLjaRJZ2p24MGTN3jnqQG7rPaaYkk-lpxa50o55R--WtChNGYWDi98eQQ5xXNyAFiwMMtfMgbn_xgiNRA8Eyc-3RvotKTIIFy6ud07878MHNqWjR_d-_n9tWh0LyCJwSdj0lZwrYhGGl8-i5KkMChkiVaY2y_JcJuznYGcG-GoGldTaW37-GfpVBMsuClsobs4Rlw7JKdPKjcHkfJzKXcKCluH2TknxC9LkNLdgL5cKo-DAIVFI0v88qJjnwWlf0jrMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=XKcTuAjdWHK7Gni3hFdEdr3fbsPdyg66MBNHn1I02_vp_amBsDc1y7EseLQDNkASmxxATKz-Twmh_qOZGcLjaRJZ2p24MGTN3jnqQG7rPaaYkk-lpxa50o55R--WtChNGYWDi98eQQ5xXNyAFiwMMtfMgbn_xgiNRA8Eyc-3RvotKTIIFy6ud07878MHNqWjR_d-_n9tWh0LyCJwSdj0lZwrYhGGl8-i5KkMChkiVaY2y_JcJuznYGcG-GoGldTaW37-GfpVBMsuClsobs4Rlw7JKdPKjcHkfJzKXcKCluH2TknxC9LkNLdgL5cKo-DAIVFI0v88qJjnwWlf0jrMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAZDMuR6W7UuIxUBkHsdpMSp73o9X46QQsCQsOI4SxnIsntKjv4e6khFxlnxCgV7TbGiTb_PvetodGLJfyXRPrpNC5bZiL0t8HzGBl_-7r-rQHC9rnnn1u_-Nrvkge0MBfPrsflbkLmhVOUoZNzfCSAGQvLTacAboF4jC2Duo6dcBUEc4SpthPMiJjgfooCWGbqusF47KNuVmdT4u57G2tl63BPBTV4ySV1Wh4MUPM3BxIcOmJvP3qouvHyv8qCJXubWHEL3O5HtxSLH4DbdFOGPYi4ENhtrembZEjUDwQXV-rpQK4LgWDKrxi0GBzy_NRBZ4SZL-9GZXu_ZuQPQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSwmSkD2fOraJf4FfSNa0vwiKeX4sbbqZtboLcOiHfHQjA4-s1qlRb_oHfBU9vOPlcEJf9wVgyt0S2Pproh5LuY70ANZQbQ-ayZgeh6zsiMK6y_kPe3XGXUY6HkULAXeAj8Avd1g0mNfSTqg-08KR0xE1s5Uribwb2qAS3-dfQ2kh7Q2MOqn9FpgUikUP1D7J96_lfl4jXVGgbuaFy0yjYhCsT6C_mfnCy1ZJOUVPWu28jkJelGS1ZVMwzrnB4IJBggIxpNZhREVZ0B0qhpc4gZFeAW2HLxReKB8mm09V1_ZuH9F8IG3-Qx-33SFu6JAJBJbeVxkecbXyg2Cnt3NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HfpNLqEHwCglal_bo-dHo45sbOTjWawdRd9BzEjqxK1KtmY05nkQeialosoptF_nuvc3Hjtb0wS2sMbgIoF2w2Y-KuVNKZUyXx9CIJ3uBuLoqka5fhw8VWTQJvBAyZBZ61iyZab5MDbVHqZVEjkydh7VvyNZ_Co4IE_D9T6q4oh3SPEYA0OikBSvel-0dtm-kSOzw4jsYcYvEjwFzv6e6JmbqppWVQWwOkzXfAOf-rLuHBjtRR6VYv860VmEzPRbrDp5NsgkFuuL-gftWn1px5vFQJtfabE4ju2mwJn9kSjsQP493MQqD9GY0ScGgT5ALgCIoVTtBcuokLY-6xXKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HfpNLqEHwCglal_bo-dHo45sbOTjWawdRd9BzEjqxK1KtmY05nkQeialosoptF_nuvc3Hjtb0wS2sMbgIoF2w2Y-KuVNKZUyXx9CIJ3uBuLoqka5fhw8VWTQJvBAyZBZ61iyZab5MDbVHqZVEjkydh7VvyNZ_Co4IE_D9T6q4oh3SPEYA0OikBSvel-0dtm-kSOzw4jsYcYvEjwFzv6e6JmbqppWVQWwOkzXfAOf-rLuHBjtRR6VYv860VmEzPRbrDp5NsgkFuuL-gftWn1px5vFQJtfabE4ju2mwJn9kSjsQP493MQqD9GY0ScGgT5ALgCIoVTtBcuokLY-6xXKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IspNS1fLRUPYVdSYWhXZRN7mHoYThERzvda_WLUPT6oYYXjpeEDgohR34OfxRySq0fv3LAUZMbU80HQrGpC4S8uw_lsUBtFgXwbcpiZiHH70_GZdp0leKKFxx8TJyl1TVkR3SvO8QuFLYUETgi2xOXr6xllZlbycSTufS4wLco0V9WGG9kxXI9UVXgqR1C8j-DN1npxvtNFbJBvkFwouNaiagKJMkKFTzYxbWsNAwW2fagueYsVeHtZVRcSXagcaHSRY2lW9b6s9dLX-Uyk0ylbXTRVy_2vwTCDPo6_zBUMbeeiFDx6jFnvmSk3ZPeSfNurykdsI1SRC2iMNOhw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=NOdGvtCXpY2RCW0KYSO1_cJSK4VIlNUu4eH4-YA0iWjbleVZkyX4dzf-EPO1z0vlxSUOPXg-oGwT-5LUYgh1cO-ETKjZ_0on5DeWszdmS6yKcNSdcH4bth0MCNvtYhp_DCbBOOE8T1m3zgIVjuAJ45Zf07s_KoIPPJxvBFB3w4GxPtQANDg5CoPgvZSrziDgjG3buGEiQrJsWHe74liFXGOkTGvavSO3rpjBync3kqMkQcPf03l56ws8QWHzn-4jnJnpl7eB46TUHs9z46-JBJnmvITqrXkdo4ixAIVXJM5eA8fx17V01zNJggPycRo9jmrwlfjVDqbSUu8LJPvr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=NOdGvtCXpY2RCW0KYSO1_cJSK4VIlNUu4eH4-YA0iWjbleVZkyX4dzf-EPO1z0vlxSUOPXg-oGwT-5LUYgh1cO-ETKjZ_0on5DeWszdmS6yKcNSdcH4bth0MCNvtYhp_DCbBOOE8T1m3zgIVjuAJ45Zf07s_KoIPPJxvBFB3w4GxPtQANDg5CoPgvZSrziDgjG3buGEiQrJsWHe74liFXGOkTGvavSO3rpjBync3kqMkQcPf03l56ws8QWHzn-4jnJnpl7eB46TUHs9z46-JBJnmvITqrXkdo4ixAIVXJM5eA8fx17V01zNJggPycRo9jmrwlfjVDqbSUu8LJPvr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=rggpR0hAL1D8RD13F57Kwu9ptCBgbqFgwpKYEKL2luFLToZi43CDD8UUmSMTp5b1RKBw8tuEhhWqUlBNpe4-E0W-VY5daSLrABhyNxftw77LU_wW-zp8yXp0JKNR0E-uXjG3ppfy9moX_n0EhxZErHAuGE2B7zw4BIJF-VsXv5OY6kwB4RIcADne0NfcFMVjw7Nl6RrXCJH2pIryFQTRwjW1C_6sqw4oWCC2u3MvVWvxYy9SZM4nQrCuDpeU6KzWp7H04Dd8IP59gnRUPlkMfG62FWEJQGqkkU2N2ubmlOODNb7bhyCTH3FHp0kvyYdfO7Z2p0SOkzRdqZezi9V_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=rggpR0hAL1D8RD13F57Kwu9ptCBgbqFgwpKYEKL2luFLToZi43CDD8UUmSMTp5b1RKBw8tuEhhWqUlBNpe4-E0W-VY5daSLrABhyNxftw77LU_wW-zp8yXp0JKNR0E-uXjG3ppfy9moX_n0EhxZErHAuGE2B7zw4BIJF-VsXv5OY6kwB4RIcADne0NfcFMVjw7Nl6RrXCJH2pIryFQTRwjW1C_6sqw4oWCC2u3MvVWvxYy9SZM4nQrCuDpeU6KzWp7H04Dd8IP59gnRUPlkMfG62FWEJQGqkkU2N2ubmlOODNb7bhyCTH3FHp0kvyYdfO7Z2p0SOkzRdqZezi9V_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkZfaB8Tk95IYjKmaAKj6GiOsc2-MWTZzAcvg2xkqeupwsl9BELBssvH_4DDncEGD3dQM-3wv7plWsJtakxS5O2aofXr9NGqFdLduoAvqchKEJRwTJYQYvSvckCsg4bG6d4uQiipwy2aQLniB2ck_bE1zV8XwZyiPdoI89G2_nNgO9i8lDjnKOPXVqOfo2p-2FmkSNeelzHknYRDMjgy40wZxcAMBUws2LCdeNqi0xs6spyl8OmQZiFQ3ifLnpHutRnQQkjARFRUepTpMlIPtt_hZpVhhmDvOVhauGDHxoBhzxwkVKWAsVALRK0DPVxLF6e6XdTXZppz-a2PqOTBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=i4QICn2vQlVhIWtziw5_HbctT6ixiIRX1yXwcst1i_Wm3Tp4k02_JsXpWSFLGxsN-tyT9A7XX9kzyTvduO1Y6NhsW8ozV7-0d7DyQeYsRHno0G03QndJ8OP4dO55tEJEDT5XjopXQzr-vpRbIzqllTyqq17gG3NKm6q3iu-9B9UH_J2dLSyzdym_-OLwHB7CL9fh7rjWHXs-ZI2laKTzSEm09d8go1evpKsxUV4lDED0QOOdBSnDf63YNJdcagr32zild6IQEyp-jy-X54lah0hoPqzZ-2sayWzVjiTx_QHiPM9pEK6iH1RfMPbfrmcI865uXy3OVA5OnpLfcTLi8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=i4QICn2vQlVhIWtziw5_HbctT6ixiIRX1yXwcst1i_Wm3Tp4k02_JsXpWSFLGxsN-tyT9A7XX9kzyTvduO1Y6NhsW8ozV7-0d7DyQeYsRHno0G03QndJ8OP4dO55tEJEDT5XjopXQzr-vpRbIzqllTyqq17gG3NKm6q3iu-9B9UH_J2dLSyzdym_-OLwHB7CL9fh7rjWHXs-ZI2laKTzSEm09d8go1evpKsxUV4lDED0QOOdBSnDf63YNJdcagr32zild6IQEyp-jy-X54lah0hoPqzZ-2sayWzVjiTx_QHiPM9pEK6iH1RfMPbfrmcI865uXy3OVA5OnpLfcTLi8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=Yu-vCoOhzRjP4qatODSgdDlKCm0iVb6LJ34YrpSmbFt1dc6KMM2LM2450pf3B_LSU2bcROKC4V9t60lz9lFll6D2sm8ggRJ2q7GqITfWYgIq17PoRVutJSaikY0jgZJ3f8mXTJI-gv9_eI5v5HU2IUyPruun9jDwL4UZxuhjz6gbgRdxsDRUtvCeGGMjv2pu2DV8nG-Vvk9LI-2yT2ZLY1lR-Inqk4hfsQv9Eepw0LBEjNMi2r4x4UKUblQ9JmDX4hNYqMgGkrY-xZT53QlTp-kGfOA56krWqKEr4PJFzfIpik1NhV0nd-b8-MCMOXHKndRrbuJVLXeyZD_g-Rl68g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=Yu-vCoOhzRjP4qatODSgdDlKCm0iVb6LJ34YrpSmbFt1dc6KMM2LM2450pf3B_LSU2bcROKC4V9t60lz9lFll6D2sm8ggRJ2q7GqITfWYgIq17PoRVutJSaikY0jgZJ3f8mXTJI-gv9_eI5v5HU2IUyPruun9jDwL4UZxuhjz6gbgRdxsDRUtvCeGGMjv2pu2DV8nG-Vvk9LI-2yT2ZLY1lR-Inqk4hfsQv9Eepw0LBEjNMi2r4x4UKUblQ9JmDX4hNYqMgGkrY-xZT53QlTp-kGfOA56krWqKEr4PJFzfIpik1NhV0nd-b8-MCMOXHKndRrbuJVLXeyZD_g-Rl68g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9GnG32fb61g5_fqdGh8aGIFV1jGdlvnbQqCDWv821Tqn8VQfQnJHom3i_jRqa-HDpnkxk_eI_jM9l3RFLvv2l--IpbzAF5YvYF3oypwuk7fPU27HQ0wpHKLuUG9LIzaoYlu_xbOBl6lXHCbpExgwapWzVkASz4F62bhGfoDGNSo_wCyneF-NaHEXjt6T8TcXSlmQy8YicaLLwnE_NUQuLz07ArTIJTpNV16eCAfF2eIcBcZiUjas_SLYXJi0SrBZBRTz5LZ2MG8PPMOKwK1SzQxq-JJkf1uubZkvejlb1dh_fKFVuR94WFuZIPxbynQzjmkAHWeSNZ_0RMI3bTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=naKPQOlfl5vCa43iUj4mMIh9vnwo__2smmwuhvsdPcwnbyLuHC6uOnoV2qtWTtyPgXI2BA5VpcC0MTKmRS5-fjQOLQd80lH5uDRHyuFUR3n8HAuDtXAdrHQEL0v3iGIhQG-cumGNVlLZodqUuG_A7HvS91eGhnQIO9rK9_KiWS2rVbc-m1JIrZGxIOaWcxQP1STcd1qrUFBaho7axgPE1upyzRDcL5WptZ-bL42fOOamKMjSbYBO15N2T3JBgENyi2cbp1U_O4nvwKKlQhF770yrR1rx0M9doEJ4S9tFIFvWUOd7vZWvRGKvmAsF9ctFooMD2r2JWQrbiSrPdZbTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=naKPQOlfl5vCa43iUj4mMIh9vnwo__2smmwuhvsdPcwnbyLuHC6uOnoV2qtWTtyPgXI2BA5VpcC0MTKmRS5-fjQOLQd80lH5uDRHyuFUR3n8HAuDtXAdrHQEL0v3iGIhQG-cumGNVlLZodqUuG_A7HvS91eGhnQIO9rK9_KiWS2rVbc-m1JIrZGxIOaWcxQP1STcd1qrUFBaho7axgPE1upyzRDcL5WptZ-bL42fOOamKMjSbYBO15N2T3JBgENyi2cbp1U_O4nvwKKlQhF770yrR1rx0M9doEJ4S9tFIFvWUOd7vZWvRGKvmAsF9ctFooMD2r2JWQrbiSrPdZbTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=FnhfmfMKerptCN9TczG0bCGZGUaIW4c2L9EFj2UyQSuuuWYmWQ-Agi6xQbkfjdKagLDhEKu1RXs6xqlaex9lmwZwYfKi6LNW0ED6NmuLd7luL3AmjxQSPCUISiHo7i4c8QycnSutyyz406lzFJpnIIOx8wbBOlI9BA3_4D6GO-m8zVLErQ9RTF-IrJ8K2I5elLgP2c9VuFopYjzHD2_5IbQHbxD3TftIWs7DvAQls_sq7b_JQBMk7V9JwD1jh4xq2J8Js_Ctmi5srdZVASD71LZVpSBfGzFZF0sbu3YSIfCA2lUf2O4ScGkeFxmPC8X0meBm1UFDKwArgHRibrnv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=FnhfmfMKerptCN9TczG0bCGZGUaIW4c2L9EFj2UyQSuuuWYmWQ-Agi6xQbkfjdKagLDhEKu1RXs6xqlaex9lmwZwYfKi6LNW0ED6NmuLd7luL3AmjxQSPCUISiHo7i4c8QycnSutyyz406lzFJpnIIOx8wbBOlI9BA3_4D6GO-m8zVLErQ9RTF-IrJ8K2I5elLgP2c9VuFopYjzHD2_5IbQHbxD3TftIWs7DvAQls_sq7b_JQBMk7V9JwD1jh4xq2J8Js_Ctmi5srdZVASD71LZVpSBfGzFZF0sbu3YSIfCA2lUf2O4ScGkeFxmPC8X0meBm1UFDKwArgHRibrnv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr5h3Dq-X3C5OS6vfDWwdFRdRu3bREsrj8nxrkakNtkWPJ-bUUtZ8kuMwKXug8paRxGXqrfjqJjEGXfZHEXsr9A8I00FdBNl-LJt4dlcuEaBxNvRlxBdSX5zMI-fB-GZ3AxfTSZ6tWB57_L09LqwyDpBwmyx4dSxBXMlv29JKnA_xtu8AFUNjW4_Ew0mTr8DdFQfcQ3OXf0WB5D8vL8RbBqW7urtt-HxCq5kiCuVJ2YKIOLuzkj7By20W9H9wF9vPonaP1pnYeaeY353mMHYZeyT3Ymp91jgreq4Bxfp6_0fcPY6L8l6MF9nq9_wumxnZycfeuaJt2g1eC8NILqwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=lN4YFwc0y0WoRWQzxrQ4tG9tay1HJLugKRrQuKtMtMpkpiimo5YI2YQsD4CcwNAB3ahkoWTV4TZduB5MumxFsh9Rt-oqE7bQ3TJfr7Fj-IcDZIQNG1w8CFtg-VIc1zYPlfyzbi21B4NyXtVrA2TNDFEeK65oQsU8PJRZAKeRFJSj5eXMj932M0THL5MyTyQsTKL-31zWAHUpKkl2cIguPa4mXfb6fhtGa1lIm7BcJfutqTYO5BzsqnCKDSPcnhZ32aA26MFV7tLKkXi3w63LZkEFK0RhCUEtNWgO4j1cxAQzdk2ODdhby49zkEvF7e07jO4thrFy-XRL74sTGHu1DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=lN4YFwc0y0WoRWQzxrQ4tG9tay1HJLugKRrQuKtMtMpkpiimo5YI2YQsD4CcwNAB3ahkoWTV4TZduB5MumxFsh9Rt-oqE7bQ3TJfr7Fj-IcDZIQNG1w8CFtg-VIc1zYPlfyzbi21B4NyXtVrA2TNDFEeK65oQsU8PJRZAKeRFJSj5eXMj932M0THL5MyTyQsTKL-31zWAHUpKkl2cIguPa4mXfb6fhtGa1lIm7BcJfutqTYO5BzsqnCKDSPcnhZ32aA26MFV7tLKkXi3w63LZkEFK0RhCUEtNWgO4j1cxAQzdk2ODdhby49zkEvF7e07jO4thrFy-XRL74sTGHu1DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=JomOjQbD_Ca7-4PkiKDHphA8XjzzEupKQ159V2So-fITo7gRGZkZbeoOS-x5zWiM6cQGAeYSJUu5kNCKeyOkSostrMI0IkVQPfiH0W1LmV0KJ_SLmkBcor8q5ywFq6N85PqY4lKjRiUn_RxDkNX87cAnWXQ6TdBmudGSlo3GfZxXC3IpsOdERNcG_BNmGQo4S3CtVXY6-c7g0PgKZpdwcOrBujPfR5hD_6JMKPp22LhDy1B32xccr84oixsNNqyY0SAGvvMoH4wFb8ffBUAsXXjKAHDMauj7iYYqfKeeq8UuHuB4WUnfTyKix2LyFfsXmk-6j5UuaZ6yA5ImSk3Vjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=JomOjQbD_Ca7-4PkiKDHphA8XjzzEupKQ159V2So-fITo7gRGZkZbeoOS-x5zWiM6cQGAeYSJUu5kNCKeyOkSostrMI0IkVQPfiH0W1LmV0KJ_SLmkBcor8q5ywFq6N85PqY4lKjRiUn_RxDkNX87cAnWXQ6TdBmudGSlo3GfZxXC3IpsOdERNcG_BNmGQo4S3CtVXY6-c7g0PgKZpdwcOrBujPfR5hD_6JMKPp22LhDy1B32xccr84oixsNNqyY0SAGvvMoH4wFb8ffBUAsXXjKAHDMauj7iYYqfKeeq8UuHuB4WUnfTyKix2LyFfsXmk-6j5UuaZ6yA5ImSk3Vjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

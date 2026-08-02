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
<img src="https://cdn4.telesco.pe/file/o4bLWi1ynTFG6MP485nQhDfl6LyZBkKmNVQg24VmVRPLvzpmcy1VELVVw3fq1-B03ywU8Y8gllbWetlUlAWgTNGyZAQzzxJE9YoKDtzYEdMCUUBKssz1z0DZTTafEdA4ZdUxz_G1msnl8vr3q3H3dOvRZMqPZnrqjLdzrjAr9DB3r3sDrUcx1-cxp3ZQ-HnCMVXeN4Aqn97geqv2tLVgCWagXeLJw4w67mVd0M9n3uqtG3whyXGeHsyhPYF_JwSvcO4RPwnyqSgkCw3TW_vqCn-6okjheCFwLc6-dTDLQP5St4p56I9bqSKHs5J5tcKGcfeI3bqQwu_uKMD6HgwGwg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 137K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 16:02:47</div>
<hr>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=fga37cRtC424zZVaZ9hH84zVQbCV1zd27FlGH492C8FUKryC3tIhkZBWyWRKLi70_9HEsm8NDVHw2W3mvmHwKkS_nJ1WdZpSP-R5HidHCZlclrn5BLfjFwxiSG2XrBqmYxENACbB-Nr2fxY9w8cHP8aznug-54HzlLy-RXE2LQ1M0sGeUqSGp5UN_jBlMXRhl3uQdQTI1MRXAOVXvQbjBOyYSYKcQrrF_vfJ2ixxzfMUwQhHIJmMNK0tYavdV5rjvT3s-gAXtoWf99FIP9m2J3tgkI1T41dTbiGlAQT3eO2bvXOqat-uKMc6PEurKJgNyjTR6tYumzmWLyaXtYR3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=fga37cRtC424zZVaZ9hH84zVQbCV1zd27FlGH492C8FUKryC3tIhkZBWyWRKLi70_9HEsm8NDVHw2W3mvmHwKkS_nJ1WdZpSP-R5HidHCZlclrn5BLfjFwxiSG2XrBqmYxENACbB-Nr2fxY9w8cHP8aznug-54HzlLy-RXE2LQ1M0sGeUqSGp5UN_jBlMXRhl3uQdQTI1MRXAOVXvQbjBOyYSYKcQrrF_vfJ2ixxzfMUwQhHIJmMNK0tYavdV5rjvT3s-gAXtoWf99FIP9m2J3tgkI1T41dTbiGlAQT3eO2bvXOqat-uKMc6PEurKJgNyjTR6tYumzmWLyaXtYR3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=toi1jcQXLmx3JRwX5YuN_9G76RGLBeSWQvu_SNwQbRveYgV9ubc7k8Gk61vs5QMdYec1OseZH4iZ-IAfkEmraasAn4x6XN53Df9TcYC1at6I2avZTIsMeCM0yMidJu0vXgTLXy994gpUdMr3FdwXZOwQY_FPWwx9_trvkWpSF_UXSNh--n1EcN16drQMbronvJo155jWkiC-M-HyjaB2NxxxBN1P3tpIj1L63TqpQiNMqMeZHCkVQdwicv_J0SCAK5BNKywIpHk-h9WI7KtFxa68plEWCIC2ST7IqRxbErlKE8pWqnLw92642a5003-9UcCezCHFfTZGep0NyNTJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=IeXBzw4sas3cbIize4-ZW8Xn4tK-hqkN2GCm9DvnCRtbClJhqtNiQg4kkCEjONamEvc8K4_vmyk5y4NeuK3s1wgiBuiiU83rCrhqQsp43k7MpvSFMovFEHvgFOcz8-3h5TGFQaP7FGMukrFS7-WI1KGWmx9Va0gO9C1OIVHbeH2IVtwyF9CvwUcMaa5t6_tQIi5pK2Sf_DzuuMlfEcv2s_QM4AxoS-3qep_zqfq1Oj5tYxRN5EJxPLVirfvE2j0CsYNHu51hzL1DXwmg1L1aE9hRD6OB1ExrdUOdqMk2-c-BhpQ8hK83dYGhDMi9We5OPeSZENGaMMOjSlr5Sgew6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=VAMxtv8wEYXvcy9oJ_tnDY658fkRF15sLqv8uL4FYDaZOg2ekAjm6EnT7CAWMfSMI8ylOX24WJAFJtEh_pSH4bfkOe-0QNpE79UMglO2PBvlE4ANawjRe7QmV7N94S_KxA3BrV1VJYNSbJ_Kj0ftMdmp4CVLC67gM06_2shS4e5u-h18Zgmxx7XpUkPmQ1G0YAquam5CHuTz0nCo4QCwZme-TCiftpyOnLkQyIXl0DiipicLqef3nRh2sghi51lKqW2kOzRLXZ7CyBgeKrXDlE22X9anxQLXQR9RdM_Y0Y1i3_PUpiJdIOqPb_nh9lnFGGa0ZkSv88-iIOyA5sLgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=JrjWFGmaqmlf3NvbAAomY6_zK46m4TklNO5hWZAsAJIGBAcWR65JAAVDi-xaHRfMPYcFusXtqDGM9hpzxAIFVMBhHwlh7RiQfYu-z6DF-MySPPSue1p9WauzseQ7ixHyilg-EKIZXk_zLoBvTyXEsavvFjJGSvU--d9eHrNlGYWmlJIRdKSU8kfN9bB_SV9LRszH_Y45UOjoCP2qAACaGgxbokQnGH28q6OsHQO819kTE2YjFbEKyYILUGPAho5Cq1mu1AuxsCLijbK2oUI7Wv_07p2XzGKVejOx-4upeBiPD0J6r9eW0284Z4Nn6U__pfOUF5gwfdeGbkXymJwEBUXWFcQMmojfKfzQ3c2jdG_kk2Nd5SMrAfTbtJdxAFSUvCz_2F1wbTnItZOx8hUIiMjbJNgoRh3sJxeo215TiWyVOWIruDtCZVEdZ8JMyOAsQNdZ0kfBjuIDSt3MDPtefMI1mpLNeYcEpVbeUx8QhcIHTGQJi8IH0c_5nbMZacMFxmc1yfbi7m8VeU_T0VTKdxEPJcKMQ4bdwjNJvkbKN6kdvGqScCjQbXnbZTC42LsnQux3MojsLBhQYhW6dqr3ANuiJwCYTk78I6Z_wM4VN0hoborH3MI_GQZ6WouF1h8SIcOb4hMsOr4Z32e992O_VH3H8-KCApl5ZPbCSHnDWR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=K6J4WrxtLQp4c78asx7FP3XeoRzyz6xdejcuYb6a_5dxc2j-uUY1D-95JXYrXvAgtwuy39R1c54pUm63uU1-b0vAhGgqSSABC5uSnTFOmvdcQaieeCuM0QLOVYYYCJZuGzVqzSNAlNldYXnVx2eHPy3V4uF49e7V8koNaIcgi3f_UNYahOfPH3oh6xyMMNysbxC8E46mxh0yUC5SoMTMVFgJ0VxauwUw8vFBxu3WwwxBmGPBeWghgPXYHq-D1E3qC64tAhTSDUFI3w2xuvivJGSwRRKwSr8kbOnXgnA0wbybmM46JndCCLGK6K4wS2cPph2c4uvUaiOBA9-BTJ94eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=K6J4WrxtLQp4c78asx7FP3XeoRzyz6xdejcuYb6a_5dxc2j-uUY1D-95JXYrXvAgtwuy39R1c54pUm63uU1-b0vAhGgqSSABC5uSnTFOmvdcQaieeCuM0QLOVYYYCJZuGzVqzSNAlNldYXnVx2eHPy3V4uF49e7V8koNaIcgi3f_UNYahOfPH3oh6xyMMNysbxC8E46mxh0yUC5SoMTMVFgJ0VxauwUw8vFBxu3WwwxBmGPBeWghgPXYHq-D1E3qC64tAhTSDUFI3w2xuvivJGSwRRKwSr8kbOnXgnA0wbybmM46JndCCLGK6K4wS2cPph2c4uvUaiOBA9-BTJ94eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=VUTrkY8AmNJGwhc6c5fR8NmPkpyt9-ZI9UE_PIfgXfsGysCvttqJ8CCI_7P1pidwKd3twXXQwGo0JBN4MV3mW3wTI2cAMtJcXJrHlPHdBML1SP1849MjN7NY77-1iLjyr0A5Sy2mD4FnIaX5pwpeD4toM5K6uHS7mLXrk04ToSKjBiunFusO8oNBVfycJOMg2wguggCaETD1ohF9MQH0g5SscHXVBgJImOyzwBqwjdmbxYpNdG4WQJCsplcyxomK3o646-YMAj1eZBjn1JZTjI6qjSP1Le6Im6YrLjbFbi4up1f7Q3mI2laOM1GP78N6x7ml4I3pD-dJChlvA8Wq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=qBFQkw1xFqxFuw8olggR7EtfA3suK6JCuQWbrVKYh7f6CesvV8B7UG1zUWumK3qtw7ONQ05-PALBEWglg7xVE748K6osMCcKOlup0YG8aLqjB_FNK2pDcVdOZyk8KVHLNJ7E8RnVpzPd1QtQ0l2NC-yhxd6rRg1oNov1E5oDeQE6D4pvE8dF_PSUnHW5hdLZpM71W-xdqdfmn97fpnXsSySvmvT_DfPO40NKIV8IhkPQNk0gl6r_1dnGd_wWn3pJ_hsv4JsPjg1axJTM86cfFYmEvlQLVkUHMsdcsUBxOOJ4jvncK2CpATJ4yDL5JI2kzU2QOl1EiOEsanB4aBFABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=t7Xx-rFRC9O22-7XGm7zb6x2kn7r24I8YL_6I87Ii30o6qdJnRspxYIhP61TzdBZKiyPM_AY9lgy2a429w7jtp7lbjqcGqoHCDVPMf5ZIUr81-PqvTNYFAb8Sl3Tm3SELN8WKNRHNucaFdgBH3nNUe4kNrxM-q9xSyCxG3PPEpDvnpORcjrTQd4fpIOq6PajaLKBymYl9TbBy56Fzbi-ES709SWkKv7GMRlVA276Po_ztF_hjyGfYyd9_rY8NEqs19rPnXX5n6eGuOOj8XGuHi5eGOQc4CTwELt9AhyGrW4VPTIBD-GShV-H221X-RXXqajHL1D6PIGHBqkUq9T_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s09093O-_hNw6MiFoJRxHd5y2dh10ROsfoQKvhAlfeJoVx1lr-hjVTGDiAt7beVCHE3l1dDW1RJKW5tqc3djfma_qoD-ExHHwc6a4H80Hrq1FFfyPOzUM3RN-tFnGsUu_PGXpXqY9ZgacHwjuvLGLMT_-dFqxoZ78JRjBWResRBcSp4lQBWcYA6y2_LHW_TgeSZqNQHbw3qh4GHc_6QU2xJj4UTgyA6-CcpbxYpGOU3O0hSnEGL8li8zydLmc9viZ0QipO44N0fHtsXHMO_BDbUleUDSXkhXg9q_W5TDVsraPf1rkJxvmcLDJ7QNaVNdTirc4GIZIDt-W8u3M2QI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTbWcFqK-wmHBdHOLMQ9B2GqQyRSlPacvcSruz2BUlnwKCqTxddm3s22crvxW9bxiuc_187DWnfFLjEqsMpomKx_F0fI_3ai0SSlnWODZMrjhv3Xf0hi-ToPbyk2Ld9R3UoIJflB19raPq696XBKAR1S6zr5uMLbhool2cPSYSssazbEE5uKhxRAjrOX7i4fCfbocnB1dhTBkAVRW6SDLbaAze0_MLtTRej-_t43zQ-Bw8dOCF_x1Z32Xq-5GyGs4aHzdI11Xm6QwA-kr56EVARlGBcFqzXu0RrTL76OzNWglejlc5CDRa2aX2KftGRkaINyioolzYI9zfIVbjZSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=DwFe2LHFEqJsgnLtepq1V2nYsD8chLLnyTkHVmPhn0hzvA54TBP2unxcAP9-qaR5w-X8OX6CM6I3e2Y4K652cOZI_R9X9OWQKRGpSLftGSxJctTkmsnPSCszYWtOTqc_-uHirS94RwMSB_bWJzns1Ls8cTvonxgAQFHL0SGWEZR1aF1hEH0iurHx7nTzIBVaWsEyPTcKL4qEC7XSBo3SrJuZCUjwrG5MlxW2N54XkdQ3V-iW2M2Se-fcwED3ujIzmNGadb5l23xArRXhW81ygf9lc9Yhe5buwO7C3TSrOZOEtwmH9VwfEEsn06z6mfnRkqVRHBTo8xo5tTFlhAPiIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=kCvLolWW8UTbQ9Ll5gAaPbP-Y_okmGfprtQPPy3UN4UW3ZKEVh_ZY3mr6gGqdLAcP6lZAqg55GBrXRCfMC5-TFhSfWlsowT1MG1ybPsELfZOp9bbBKA3lkF0Ay5CiP_LCBkk1o2TXa6y5NbYRHv_ht4DJGDRtZxQaqqTgFr3q7TL7lkkT7y0SjxiiIVz09enD6T0kPMRY0Gqy1bwG1mx6j9IZDg4QmiyIuYgNTtootdt9TWe4sd2VL_kPdQMK7h6AfGtAP30jv6ZTC1eUdWn2iQBZgewAqrvEOT3eMwSR0VGvkW7vGTI76ztIOPqkIrt63lhbi07-C92zO_6bz_3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZZpaHFq1WJf3wUvz9j_SqxjYNBdtXjSbSGpJjhDlg-ZcUR2uPVLP9Tg30gCSz-SZ8FkIgqMa0-o8t55Sd04MG0eirUmtVppTocc0IrgnpqXHjIZN6D3sT_VIk9Ao_fy1K_5azdHNWHrGkPGM75wePaIEuwZQQVQc9rfcnln35o4_hyrWz8ViJ3AKENtOe-5uGd00m8-gyfh4YYXpC7rRlZ_0TqA9ZqWII_RX2OPYKzf1of1qZfw69vm_ektA85Gx-w8leL6zGEFCcbRFMcj4uxtIP1OrzwMF2iQfgZi8d6b6HwBtV9EAyYmtl6gRbcqrjXDTuDGISKYhccp3PGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tME_uG6_SgkzPmhJACwXCgGWGKH6eM7mAaoPWJCmjGCTQPJOHy9yDoxO0v3JNF4YQlk2iBaq1upfQJ7AySp4xr9YUTzYyGMwMttXaW76LQDrdRk6I0ei6lZfE3ebfFoHAnnFGHBj8WFnnDwPb62ntQxprb0nCqwITyUo3zC8eTBAfLnNoIwaU5ANPkSfaNC2RYJ8uwI9aeHAHro2bzz4GUoxV2qeB0p-dJRkrXM33qP2tvBh_SfzEouYUHM_opup8RcpQ7Ek6bQUYIibNpBbdnzNnyqNdTmhntVNxOCmcKP_oot9abD3cL0_KGi1cn2x6RdIsWkiosrAwkGpGEtyXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=ouZuCmTRrUngWDR4lZKnD6RGL61I9h3M3VHOmGVHhM1bdYwyvUsG8o0RJ-dGCnyWTtNTW-gR6Ex9VMo6s7J8EKgUb0QL8c8CNQ7iAy5VC-7PFOE4C49ZGjz-FquM1xP3_48QDT5Ikp1orvtHVXzucEsC3b-4Si8Lqx5V3ZCat80Oo-hKfwfZjtLD0-kTDRnuUNkAH6HpowNLoiwUy3rKbO0YPEtc7S5lfYJ47culORXYKmQIv_96sqzqgK1YTfD6R06RGGhRDvyfw0gcUVMFQR-M94nDWaUP-8sBSQMUZGp4MCuuqtH9p-zyvECglMmaVk5owNCLWSO7rEz7duNErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=tDjZBT02CoFLAhF9VLv24OJ6BxrLEZgfW6lFLfh6dAe9xFAJ-kwQxCJYw2bu69nvvDvNUxo7_GOhMRMW2FDZho4YbCSUTNmHw9qOJUDqRUJGKvwgBbCS1qIAOfPxBK1uypkvpQz9FlOUV_BJm0TVBxo7uGTH98T-r-Wqv4cKqRFD_eYC-AMETpUVyuk9FpMWE8p7VbLWFx7ucXPR3ve-7Ts02BxHi4hPr_Uw7ljhGpMC8KJ75ZvF9r7ENLJaEMDZHSVdRMxMZ6F4H7pVVbLWm9szzfumBoJXk84zPHGuSuHYYI_VDLzmbeJXPLDTGtIOhxRvje7unc2pm6NrtpXtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpU4zbHkL_KOZyxBivseaTpudCIOaEC9vxPKiYp2T9_FRnpqIc0_5ynwkBFiH5-mf9XRR8lwZFroTVG_13l1whbMzcciScLCAvc5PUENHP60wo5fOu5gff73egpOHvRSe3nXKpKlvo_bwjFsGNSWsVP6aSWOpM9HvbVHQCMtdwQVolZ3QIdkx2ufxl9xpju33IypIjAwp8wehdXlS1dtzfgfja_c7l0pEIDnwkAe6JE_83zSWuv2yenzOTKf-dU3KfLcZFRkjGU1dMjLaw3Gru2Hrh9v81-SLKVe45EsiqMoh38-qb-PpgcAYmRuTLzGpL7bKqk_h4MQfx4r8TUG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=d7S_j5aJpuMzOkBK77wggHBTaYBhj8501FdO2z5Q7PfgftwrG0RDLcsXno74noJMdiHG-3gMtkNVQg_q6sRVwuvGWFo-A_LJQVxO1Bq27d50wa-pmaMXAnBCv65coey2B-KD8QWh0MBnJcJk6IqwIt33O6SvfH_CZo46S2oHnnA-vfMOsKDEKBWd7azCX1BsZ27Zz0JE1GL1cV7RHEZFu1Gph_MvRlOvroNcO4ItgCaMyfGf88l7SbDsHrxTwcoEOjXk3_OqVGwN7n0YJKQCoE-UfSgVw4_nyrCGcNGqW21SnAX4O1kniFpihYIa6vtbsLRYkn9wSjINURjg7BM2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=d7S_j5aJpuMzOkBK77wggHBTaYBhj8501FdO2z5Q7PfgftwrG0RDLcsXno74noJMdiHG-3gMtkNVQg_q6sRVwuvGWFo-A_LJQVxO1Bq27d50wa-pmaMXAnBCv65coey2B-KD8QWh0MBnJcJk6IqwIt33O6SvfH_CZo46S2oHnnA-vfMOsKDEKBWd7azCX1BsZ27Zz0JE1GL1cV7RHEZFu1Gph_MvRlOvroNcO4ItgCaMyfGf88l7SbDsHrxTwcoEOjXk3_OqVGwN7n0YJKQCoE-UfSgVw4_nyrCGcNGqW21SnAX4O1kniFpihYIa6vtbsLRYkn9wSjINURjg7BM2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JvmPjfQB6pA-28p5r6h4IW2jo10V9nYqJMhcsZXtGAxG6gH4wIdiFbduGoBssoLmz6o_vXddtxQVc4SYtF3resuFqx6UdHtrFmYqD5sMpEZCEetFX80PxqkS2lyN0BbwwbkSgQMmXEaiUC1t0VmLQi5Qcm6roeEt7QcSQ1uBHqk-hv0fwYGMEEZXjC8tnZlMk87rXZCaO_ZL7PIwgdySDvwGG-c11s5KZvb4btufaJvay4jvtMP_0HX_4d9E_VhLfvTblaQpKph99qQUaAjHnDQGbpR0pGa2UYGiKCEMJn7qvuB5KcNK8IVUc31RHzII7LPlIc4DNRqfMmZ6yPqQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=X_kPMcTXjrdhbQKrSUJrqk7svNzRm8cZHNJwkeUg7-Nk2OfHG43oAkYBDxhMswI4woTZ7NJKBP_IyqWLdOnfVPQCSTbHl8Ya36yUg6bkXbhT1rcM1Ec_DjD1zD7ceSkPQCjJcBYJdC2Pw7CFlQAstxVrUcoZaucdFggLqUbPs35ZsJFi86l9OqOvvKihEZS9C1yqwtru1No_boGtKpAWOh0agbsHvnrHzNbJ8BUR5pQ3dFB4c6z9VWipQXvAkoU0lmyBUfGu9SmrWiYAga7SG02Xs1RWrSpVyNijxf_CZyl8FWJBQjxMRyomYASly0mvQzSZCT3KI5SxlUF3D7HKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=X_kPMcTXjrdhbQKrSUJrqk7svNzRm8cZHNJwkeUg7-Nk2OfHG43oAkYBDxhMswI4woTZ7NJKBP_IyqWLdOnfVPQCSTbHl8Ya36yUg6bkXbhT1rcM1Ec_DjD1zD7ceSkPQCjJcBYJdC2Pw7CFlQAstxVrUcoZaucdFggLqUbPs35ZsJFi86l9OqOvvKihEZS9C1yqwtru1No_boGtKpAWOh0agbsHvnrHzNbJ8BUR5pQ3dFB4c6z9VWipQXvAkoU0lmyBUfGu9SmrWiYAga7SG02Xs1RWrSpVyNijxf_CZyl8FWJBQjxMRyomYASly0mvQzSZCT3KI5SxlUF3D7HKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=I8vSk4_U_kB8scl22EXCYXagXNGdMrhoJsj39ae71eX2OCApAfOEWyIPOc-Y1uW_9UAMh5IoIlxLApizSWfjmNCCjoPClA5bUikmg8dQT1XTL-35NJry-gFmjxpfwqUDWNSWv9O4AeFaQjzWKWHvOwKaYeEJG00CY1oAoYZI84nyIvtH8gBty3IFMlMXzDskQpVvV51R1EukgSHG5Wl7RlgRzQPnXNEb0wgQ3Dq_hReKVZmT4gvkUcCyfPqMsT7dNXZaYBRmPdQK5JQC8Un1N-c_7szQdkSxPCZrfHYVivZarovXwAqPLih90WR00_6xzyrcOq5kbbOMfFLHSuhvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=I8vSk4_U_kB8scl22EXCYXagXNGdMrhoJsj39ae71eX2OCApAfOEWyIPOc-Y1uW_9UAMh5IoIlxLApizSWfjmNCCjoPClA5bUikmg8dQT1XTL-35NJry-gFmjxpfwqUDWNSWv9O4AeFaQjzWKWHvOwKaYeEJG00CY1oAoYZI84nyIvtH8gBty3IFMlMXzDskQpVvV51R1EukgSHG5Wl7RlgRzQPnXNEb0wgQ3Dq_hReKVZmT4gvkUcCyfPqMsT7dNXZaYBRmPdQK5JQC8Un1N-c_7szQdkSxPCZrfHYVivZarovXwAqPLih90WR00_6xzyrcOq5kbbOMfFLHSuhvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL1s92kvkA5Ptg-lylyZx5__Mo7O17Irqtw4F6yl3sYC4-4itjPzYzkzm_f9qgtD8vphPSL1qjbwVRw2w78h1gU9kQeJPnh55m_-cqjzrNJs4FWuVZJouhR0XsBRlJLk9TCVoAHyzcjZPpG-kAwlWSse21szA5h5cFOuNj8E4pknqDTbBrV3eJp03RsJnbVEe7uEyCDnmM6Dve4QIlDkNfObLStiF3FrtAMbhDUv6GTT9f1eixWnPtwQ0tBH5Cp5E1t2K9aALWOt4aWE0q9ddIWqF5K_c_AwoVsvueuqKS3X17hfma2O9vlSbQEhEl8y8KhBij02v7jh-YJyEdm1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBBG_1qdu4hhrIBRNVCQnJTRjZEjl8F5O5p6_XQrCz1KHkgPCORrFPRlogjcgNG26571ZISY1G-Z4Uzxnhp-tmqHL9lqat4tH23g3-D1gfI_hp6U74IGthxTYDMFBNgB1kbwSFbs4u037gjYAav3ymLUa1TXQc7Kvl0rWFmt5VslC2_PBCxCxlxoBsIBeS1nlP4Ii0EbvR8IPj6yT7pFFqcXtg1mFBKqQ67QcUzOyNSZIaS5C7cYuXL0pCDNFeK7-OiT18pyidzY_9KIw1iXGnWJJdOtL4JfDGIUS_YQufrtxO_glvzd0Fyyvg-kinUjBdk1n82v3CIa1ihA_fDFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iP0Aa7lfHfh0mFUo_MGLEjZ6T4hzHIksQTI-g_XVrB-V4mmKZYHO5K6UyBjovAt7zkvVLPgs2y4QApzfRaf30jY3usRIc6gbSccWs6Pxtl_MfPJw4PTD9TjAhjP9FvHk7RrRNBensqGYaqgcoP3T2CNB0QWBnyUtM_CNiLiqduG_CCHIAis-DDUvtJnvyt9QwismU2u42z9w_BPnBXTw9QfgUgHRVi0RIQZwaPqZFPSzS2BVKHi-UMV3UdbJmMnqhmwKLt4pjo7ek_r6N1UhcgOozDHbaENP9OzxzvnwBwgwYcSZClRvgJfOWVG_GFkQxFh27VulQljkLUiH6YFdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQcLTr4IY-wbLnRXz2_hrXQNgXq2n3BHrOCHgaj3eVVBcr9v-TLvnjj1pvgMQWyfpq-7LZ3lM5kJXrfYcYfzkE0RfAR3pVONgyUKMMZN8cVXMPqfHJ-qvLsgw3l0BhS9M_QPqIN4c3-0GMXNqlk9oi2jpkRIOzOIVkwbWpDYCbCrX5sJTF-PhtLejDQkmvi6wOQMTFW_dwdDHETz_-OIxoIvQgXJIP3zqTvFovngyfg0YQdnHBMVewyHDaTaBwUylr9hvev7STj0gMb18Ir5u4A_CZ8elSFAvFwHbgaXm8EmOGhnn9FoJsXIjZX4eGjtlVsglt62RFkP1J1GUzWu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR_aTOIOg2pBNpZ94ARLKL-5qCGW4iYBU8Hflza1sp4UO8gYk1cSSEbIUDRpFRmK_pfGiyvOxB3BQ4jdMBbcZK_f4MvlNrVqAF6xcftwzfZn7XDputhXCdsNkK1UBDdILNctsBlTAmQwRP2Qbu_wBJkWbIwrZqI1vqcxmWA6eSw_24VYSJYX0kf5B5Ct4KtgYwnjMvoWHCyyewqMBtmc-amWMyDN8qotExyRGbrLKKnxo2oohC-XY0AQoIDXSiU6ZIZSDTzTJvnPbqutECE4iPTyHX-8Umo9I7yopTM08xzr4fUkoOcRu8n6vnCQqFbQr0pyXMdpNUTaRyi_BoKv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7otGrCrbcsOxhQXEY-yoWBHhVl-Oo5pjxzGYP0aCvsMsXigRo_3Uba4gh29ohBIX30hxIzHM74q5CmBB5Yhc9XXKql1TX1NCbvyQRwKybxxZ-_GaSFlSG2lE1fnboGCc5-zwNBOSH_QnJK6T6zeFDquPsWSy0KTOi7k4TwApiEU8WxM8fqt8Ut02U_jARXsOKfiQi_59QRJTJlfKrer4Hfl8RUuPbwQNm8aclg5x6hVxyK7xYJfoaz6RZRmeKYR0d3ZAm-VG4LGxrpxktMdoH-JPUzrwTHFk701SLL0duRG3VKnNefWYzqOImiEMkihsyDYtMCgYMnXlvAi7If2Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJM17yeNfuzPfEYWxUDhjbIE8J7UYie4CvB7XX4lSQEd07TOz0apHJtAq0JexZWe7wPrCulq5V4TTutSe60zyz4Ia6OzgZfCcrofAZHH4jCiZCtee40LMKAc_vIvZxq-T27iPLYREG98B_aKOvY_H9BL-p2_4gRYd-ImWk8oz9-H8G1W7WXkizXfQEwIhmlCjmDwgvMnuc-SGalEdujEjEptu6HJ4VkJb8LhZMZVkTYmBQQx3YVwcPWzBhQTlLfi2Ce-ClxLZYLoPsIZ03A3sDjx0KPKARJ_xzgm7nWATiEk8fKrdHUdGYbZ8-uHQVPC61wMmN2aOqACyz99QE5JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRrOuXpU1bwhvctyNWSCxmbU4h1rVkuw1j6Zwm4PvD9LuvtbUBvSX5Z4hRxhwvpjJMoczksfuKNIVcwrz5imunB3T4OExdUCh2ZdOVOXEaOk9YmmoUPA8Y21xpuLegX_F_4RnjDF1BUU03cljF7Gs4V9rVJcJ7fETteTBNSWD_f1rvA8hG7TsjLBEXI8ym6hPK48f-7PYPLIPYDFqEp-tkN6QtJOHhq1DQs0X7PyfME1z6CTaBSUCsZ3zijkOyCegdbPvXzsqymH9afE5gijAfdkDZ5xCAskfmZz-HYBnLezBUCJQmPet51enicbpsr7cYCeAW5_4TUuqtrAzVgzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBE7x-E8DOI01PaWj2auSkzbPjVjLnn0gn7gcX1Ko694_JLHtrXn3DmjnVWtkwhDzacUXvGKCNITHXB84-Fk-sbCxvZkBE8MKYmI8cHuU1CqsPNXTLHHwSQW5JM6B1kx_iw5gHzZuY_NSi91V2NY6vu-fuseGqOwTPHgE6Cyvb5_pmlI3W8M5quN_tdCs0yPV6vu4AG4O7hGSNf2j7Eo0L0IwVJrP6lC1bKsNp1ejBtCdKfgjYVcE4fWw3vgdYdeGElkw9uYeEfMuejtby0pGjmwdVeGILyn0Xfr5txcZRUXJc1svRrMIPsm_ovtHFPKDvCcQMR862I7_P-C-jLoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=Zyoa9hxNrjUe8ItAajFf707Z52KxKmKgFSJ7ZbC4ouyowVlD6kPmzgA5RksMZwhsxYSXoX8tToWpC5uYNerWk0Py0MMuhOS141x7De-FLFfHRdr6j4Z4YV5GoHpOGLqp0EDGn1-7Q5O3k7i8FQbfGUuokkHsGMX3exdeFlP5w1qzRqPeA4pJZYb6lnNiQhyTyeyn-3CJMpcVbE3I-1L9ypSZeG0CVR_OX5DTCMe0D4tFlWvYbwYUnhzZvjuCGI-QBr2Ic2NogO2i_kVdbz8Sm7-gVmEwzra6qwzuppA1mC0CZBDrcZTM3cEyLYYpB3GWQbWb9E-WmJOhC_YB2wse3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=h3cq_bW5ELD_Nir-HbidtTgOcH0wksDygUS9wXTrHb4B_GT5hKOmYV7GwYiTjhqA0EmAoaKzEZebkSxslmH1D4f5JixT2rdOCAdHEC4lhcZNDoOcYbRmY-BYwtMFOaUU_pJZQIHL0IaKqQp2vC4ogyNII_B-h2mCZTHRrDVubANRVSIzziy8Z45IaMAXkzyOM0gxl2gxyYAqFtsqlsl3lm5Jn8mA-hTKKbGFLV-zaFgbqeVf1JH898TsJUBxz8MwjVe4XctKOenEDW6H5jvDJXHvtDyiKIzLhHlf3gu9gvrQEe3m05jPYvlqYJu4ZKT8aYf4K26zeWbgRyFVnduFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=h3cq_bW5ELD_Nir-HbidtTgOcH0wksDygUS9wXTrHb4B_GT5hKOmYV7GwYiTjhqA0EmAoaKzEZebkSxslmH1D4f5JixT2rdOCAdHEC4lhcZNDoOcYbRmY-BYwtMFOaUU_pJZQIHL0IaKqQp2vC4ogyNII_B-h2mCZTHRrDVubANRVSIzziy8Z45IaMAXkzyOM0gxl2gxyYAqFtsqlsl3lm5Jn8mA-hTKKbGFLV-zaFgbqeVf1JH898TsJUBxz8MwjVe4XctKOenEDW6H5jvDJXHvtDyiKIzLhHlf3gu9gvrQEe3m05jPYvlqYJu4ZKT8aYf4K26zeWbgRyFVnduFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=EJJ3irpqKNN9suJEXvX9peQEkWX-39ZXLlzQo6oxG4C9ru2IdT0HThEJBuFhMP8r7rAdfRX4s3k9KVkUsDquh5G40lozPcKDMAeveLpk9FKnnGPBcD7wIpH42LZf1e8bB4ElBKKrHsXvtd_waoNVO3lRWmEeiwqS_cKYk8qaXjKLvp5BOdHSpPyMJyE41x3eHQGMYv6KKuE7al7Fr8ZdjvH9U4KkRiq8vKucWRx68njGedi1PVpqocxBCSj0PuTWyY1zJ4elbR1WWF4nxuVeny2MGnneOP8kWT-8Pq_r48uwii68USMgjmt4jPr8mel2Oc4PfjXegPiZp2-NAE1iugNbXwuboGWtcujUCSr3vdyv1fJa0-wPWDBnWDzL7-MMaKHCM2Yf8lN7bqWWlFhGlMChVSp-SMdTVqrr1CYnHp4YM1r05pBeuYHh_z1j6BzWau-7-LkqO1rWEMJgjwIsrOkBzWgb-AvzeXJmrjjokHCHgcnRbyUrSilhX5OQocv3eSmHHQB_HSkpk1dd9UtSRXkfCc5HI2toCXk5IxFopwu960eYPIJ9VUzk5ksSdaG6TMyRXHkjIGIk1CE-zrhGcEWxzLXDR_2AI3i0QUvVRk_8qivBU0MC0G2eDgkywKXDPuMnoFg0LCJ_xEMXYeJxGsOqkIoDhuKuBLKTTjhRh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=EJJ3irpqKNN9suJEXvX9peQEkWX-39ZXLlzQo6oxG4C9ru2IdT0HThEJBuFhMP8r7rAdfRX4s3k9KVkUsDquh5G40lozPcKDMAeveLpk9FKnnGPBcD7wIpH42LZf1e8bB4ElBKKrHsXvtd_waoNVO3lRWmEeiwqS_cKYk8qaXjKLvp5BOdHSpPyMJyE41x3eHQGMYv6KKuE7al7Fr8ZdjvH9U4KkRiq8vKucWRx68njGedi1PVpqocxBCSj0PuTWyY1zJ4elbR1WWF4nxuVeny2MGnneOP8kWT-8Pq_r48uwii68USMgjmt4jPr8mel2Oc4PfjXegPiZp2-NAE1iugNbXwuboGWtcujUCSr3vdyv1fJa0-wPWDBnWDzL7-MMaKHCM2Yf8lN7bqWWlFhGlMChVSp-SMdTVqrr1CYnHp4YM1r05pBeuYHh_z1j6BzWau-7-LkqO1rWEMJgjwIsrOkBzWgb-AvzeXJmrjjokHCHgcnRbyUrSilhX5OQocv3eSmHHQB_HSkpk1dd9UtSRXkfCc5HI2toCXk5IxFopwu960eYPIJ9VUzk5ksSdaG6TMyRXHkjIGIk1CE-zrhGcEWxzLXDR_2AI3i0QUvVRk_8qivBU0MC0G2eDgkywKXDPuMnoFg0LCJ_xEMXYeJxGsOqkIoDhuKuBLKTTjhRh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=R_YOXNtR5wfhaNV86wfRkXXxhRXQ6QTM17KIGc2OPCJ92b1UTjjvIio5xTNtgps3EV_qGBa4avDap5v6fqtYXhOARvoDJcyFKC-dQk4jl1EkmdMuWTk6rIQHSfJ6Ed3Au2PPvLbKGAJ_WXPKuLc2-88xYrNvfZDbHLRUTuSrPOg0vu2D-wq1uewmQTHROaINrATOS0-Nu3iiemtYlcBD3c0TT7r8XjHBQfJksBmnpF3xLBoTlGW7bT8V717LbneMNgEKtDx48k9WfTombTpTOiNtrxGj_W8KPzYwA-dVtH6yIj8LvTSQxrgYBuCyjxBlD1kZLH0HL_ugrbWl0BsAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=jvb62d92n19WymbjbpUVKsjzcHovzkxvcfLCtmAFkfNeNXuY5S6qfR8wgo83kT03I_-qix35nV-VWPEarG2WjLxP5TmDNdMk4SD62LXsSJUU-rs23f2-CqSr8DVp3Usi0rmtvvisHJ_zkGW1FMRed0Slg2Gw4GHfuureJoymcSl1A4XYNMAVIr_0xI3KhbTggQBKOj8zMsHl3bzmGlvhj0sD86xsxKOt0wGX0dmvEg4OwbJR5xHna-MlZjfZNlweEO8qS7JQN68fKamzg_YYIAO5rVR-Wo7KDYCZbI2y4hSn7olrlR05BM7EBdw7Zr-H2mIMJXyW_0NdJx3O0MCdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=jvb62d92n19WymbjbpUVKsjzcHovzkxvcfLCtmAFkfNeNXuY5S6qfR8wgo83kT03I_-qix35nV-VWPEarG2WjLxP5TmDNdMk4SD62LXsSJUU-rs23f2-CqSr8DVp3Usi0rmtvvisHJ_zkGW1FMRed0Slg2Gw4GHfuureJoymcSl1A4XYNMAVIr_0xI3KhbTggQBKOj8zMsHl3bzmGlvhj0sD86xsxKOt0wGX0dmvEg4OwbJR5xHna-MlZjfZNlweEO8qS7JQN68fKamzg_YYIAO5rVR-Wo7KDYCZbI2y4hSn7olrlR05BM7EBdw7Zr-H2mIMJXyW_0NdJx3O0MCdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=E3shZT7DbaFLwPNLKceNjN-JrPxkDJJb185Sr3KeF4JQlaclWsjjzffWnae0wV6dmqKQ88jQmcLXad3eEjk7CGg-lvZoNxJj2zS_4gLZaf84ARqXhT6yqUiQCDWtg_hlso_ouWYXLn-59hcuazPfiU2brqGZcLb_GWrk0nYYC7WZ8c3FmeuH5KauIrdeW07QvRKqDPc0xYgw43wwGAVR2Xk4wXiR5OPVgp7rYP_oIZxa2OQRdVULbmqruSxJuSQ5JIJeigEa3gNvxUlKi9abqIAC_ipwVnomLwOpGPOZ6Ve2kRMoWdtQW8sy5sI77eV3HQzzqsm-08mHBPhsmZe0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=E3shZT7DbaFLwPNLKceNjN-JrPxkDJJb185Sr3KeF4JQlaclWsjjzffWnae0wV6dmqKQ88jQmcLXad3eEjk7CGg-lvZoNxJj2zS_4gLZaf84ARqXhT6yqUiQCDWtg_hlso_ouWYXLn-59hcuazPfiU2brqGZcLb_GWrk0nYYC7WZ8c3FmeuH5KauIrdeW07QvRKqDPc0xYgw43wwGAVR2Xk4wXiR5OPVgp7rYP_oIZxa2OQRdVULbmqruSxJuSQ5JIJeigEa3gNvxUlKi9abqIAC_ipwVnomLwOpGPOZ6Ve2kRMoWdtQW8sy5sI77eV3HQzzqsm-08mHBPhsmZe0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=kKmZFH5TGdwLyhJQIhsl1-7inUNm7RsuCpmDRTg8-loFpvN3Th63uj9ABtWmS-Qh6BTBAc5tVHCoJHp3GqkSxpPEVmi3TAbL3DgEDZp_eX0Om_Ny1cgNNOiXqBHdchKmfj7YOMgPWA1LdrhcEiDzmmS4f99qAtxN8kxEC0bPFIfOdw5bqsM2cX7eUtJ44g2J7Tc2qzaVlOiug6PbF6_VGAULtTrjxVgEID4-GowuxCS8MAzcdbz-B2EY91qY-iZqgmEOR6ZsuO7k-3mDmmN_2r3ipTKxpgGGOFzfbsTMNW3YM9sxtizsYnkD2URTJspyFSSbbcciIf-UjzYjsLSH-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=kKmZFH5TGdwLyhJQIhsl1-7inUNm7RsuCpmDRTg8-loFpvN3Th63uj9ABtWmS-Qh6BTBAc5tVHCoJHp3GqkSxpPEVmi3TAbL3DgEDZp_eX0Om_Ny1cgNNOiXqBHdchKmfj7YOMgPWA1LdrhcEiDzmmS4f99qAtxN8kxEC0bPFIfOdw5bqsM2cX7eUtJ44g2J7Tc2qzaVlOiug6PbF6_VGAULtTrjxVgEID4-GowuxCS8MAzcdbz-B2EY91qY-iZqgmEOR6ZsuO7k-3mDmmN_2r3ipTKxpgGGOFzfbsTMNW3YM9sxtizsYnkD2URTJspyFSSbbcciIf-UjzYjsLSH-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9fLWH6pOFQDtAWaRrlGBSZHeflZZk9HVBfdCAbeoMNCA_hEe_mdk8qPJHRWjAbTJ8vpNSxDKD47MPHHSYvBxB_rm6kSaZ4nWGlLy35_g8U1kXkBurxq5yNDCHl87VZ-00lA7WBgyffGYYb2xmopWLPcqNE_11r3kjdTJLqRn5TSbQZowJKf5R5uf3beCl7xbXEAPBgDnnGlW9qyJYgR2pSjP1-cOlm57o2S36hgeJwdip_DO_HV-hU8dNnZ3Yng5NL3AWtKAZ8YjYtqm-S8DK_oPghQRoh5oeEgQqWmrKiTai7jBEprtKH2vOzigB0SyGluDkVNMhrovR8fi1UpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=q_pcbxSIHFcH1ZBuM0xGNQ-CCfbKB8GxzxlKQEBcxx8KBt-65sXHi5dhKqGRexIz8D8Tj-aEWnN5rMz8q8UuFls94y_i4Lk9TjyL-oa-KZVqQ0sTciLyoOPQccDG5NrfEO2ADHlx4o7qz49pyH_tyc8_JYxTgHk93jkypeYf_YnOnjKg0xGkYHJwMLjWUHrNwqv8KWumBd6LPgN_OVqfYo6dGwX7hDU4Hr5xndut4KxNhiMWKzkIrPqd35esDJ_HPUrAhNmK7LjVvyo-f7h5x2wv1pxcopTvCOf6TI4IhY_FDo0G7yeNUA106zxlMu5MHg3BsR7PAKkLFW2ro00-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=q_pcbxSIHFcH1ZBuM0xGNQ-CCfbKB8GxzxlKQEBcxx8KBt-65sXHi5dhKqGRexIz8D8Tj-aEWnN5rMz8q8UuFls94y_i4Lk9TjyL-oa-KZVqQ0sTciLyoOPQccDG5NrfEO2ADHlx4o7qz49pyH_tyc8_JYxTgHk93jkypeYf_YnOnjKg0xGkYHJwMLjWUHrNwqv8KWumBd6LPgN_OVqfYo6dGwX7hDU4Hr5xndut4KxNhiMWKzkIrPqd35esDJ_HPUrAhNmK7LjVvyo-f7h5x2wv1pxcopTvCOf6TI4IhY_FDo0G7yeNUA106zxlMu5MHg3BsR7PAKkLFW2ro00-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkKGAVXRQjaZUcE7_6wbe66DsAiKuc2OgTDE4Wkdh-iDPbS0mY1g5R944TbhAQuV_gT1UZOz0_mN0jSbVUDJfp-_5z_U7FqXK40QEuJ_aroi-4Bk0iR5XAKWRFfmthm0hnDEtaTCgFmp1OOyj9Lf6D2hBQ_QSf343HfKn5mi1wi6E4eeqcY_Dw_R0hp_c8imQ6h8ohddPb2qrPOBVzGIocxupQc9PN2u1EnD43xV0Sm4pd79fBMFSLIA9k3xDpIv6LXNiNRHlrA0MMGbb1ByNCpfPy5EpdP0XYI9eBsKVztFFGVRZg3MzgjXcWvOTFj7YK2RpXAtNndn-5MqsFbB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auwfhAR7cNQO3GYXqStQTizk98e9vDWndRnOhdRnBZVXjvErYQvSBCynoWb8ATxOCT9A7_liU859VRMJQjJ-ws2kyjdycIST49L3ifhcCBdzbydEXhe-nV2po5EypHl1RtgP3WH_wxqme_5A9B4sjdio3w96JHVa5G4iKxPlbvyuBnEnrLLHU8HVYjwPqUlLKTOJwN6BqOkYuXmQ_faq_Wi8bgYvJNKOkoeu7zfKfnT2cXuEj5C-O43KBhjRH_xERnXvxJa7JHpcU133wq9fgxpHGzoXEm_7hXRdHbtkMWwt2d0l6u34Phpr2qIUE1Cq3ymdTAbm8eEB1Z-wNBR2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXsznxWvBiWtPbvA9vfryK4Rc6hd0ZlnPUP8VtuBSOJCM5UGFg-_IAuuZLpi-NKcMrVPzcqyiJUc1wqnfuh74FLrld3lg15_Uh4pbK54qT8KkcjVi3ixOE3rdXmYMbvIttbKnskUPUtLVK1Hg0bQhs47RHQ-enCBwv9dnPe-AyP4nyjWnJrd_H9T38hDTcCHaRypttxbyMZ9OmZLh8l4duDM0NIvsJNXmKrYwrViVE2sZ0_w0VGjhwUojpWNPS5htq2vCCWV9zrMpLxF0NgaAyfvzjnBcgUff0JKZJPIuuQn4-O4EUHHxrdsOdBwLX0pqMxgAGXzMpK9T03ARfhfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPYIXAc3vKcyDUhGPWOfs-M8eNjoAkeCO49CaIc6LDi7AZ24BYlGLq6w3RiKDywgfW5E20hWA60gS2BPvkpW0hvtMop2YHNF_QNmWJBP1RTORRpMGLgPlktW56zxR0v705TNAoSH-StSf74wRYJiGQjcM8-OEpxeIcYeiWrEWS71ChXhpsIsdTeH5w9FVKT6DU5ntojNPUws9fnLAekZZftm7VEvaf_V-W8AIAMuTORBz_N5NPaoTCUl3LM8KSCMSodHRe5Fj130zag6osuMMF9mI02bfA3WNjkyeE6kZADajcQVN3Zm-kCQ1t7AXb6LuSiKL-TjRrVqos3StvdR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNbAwTTZNO6VIa42h6glmRbRqmZKSEtad9Y-8bgOk_7OThp219QwLbGdL4qgEcWPfIfHtiEwn6f_Ie8BXhsbtOoRzi8fohp8oi6xqG5wPX_7CGUFnZwbsPTkEKclYuRThARSZHHdSm6KrXxNkF-ksZ1mSllBADFP0-53KwdcSILsG7YpuWahA0Ve3wwtwJKouG-got2KawAnOtMrsGcS4m46wS0sXSRyuwVlbLjCUBPEhW6nry6z7kuxHqMp2ibr10NTc0mujVWFnu_RsA5hY1SrlxtgcF0Kh6anf5fthr9NGLXaku7yZHMCXG2or6eSVeSNaSJ9jXzhnpaSVYzwWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=VYf1FHdhFZvC9drcJ3I4FwEPCWYb74g6guZ2mg0EdHlWHXwn84c5vxZMiQgNSk78K3fgc78EF1sRmASU3i3dJ7MCWvvPz6sdrk0A_TWMKHpFf422v3U4sRcpXCY27ugQJCyupPe6-OyugYpwwBXq8xUOiynCpUqY5Cl9ppYVZDvDjHcadYHaM7c_tZ5w71Jj-7UD89F4R7m87i9rjNWc6KTbKYl2JxCYZFn2JFIZbCNwvYcdVr0cxELRTUVgkCvJUkCu5GHAZcFipII1IDJfjbnpxhuDsawPN5JGZ4knJ11S4mEhjebFS7z5mWw1tsvoeNrDjykdHuSrSoUmJ8pIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=VYf1FHdhFZvC9drcJ3I4FwEPCWYb74g6guZ2mg0EdHlWHXwn84c5vxZMiQgNSk78K3fgc78EF1sRmASU3i3dJ7MCWvvPz6sdrk0A_TWMKHpFf422v3U4sRcpXCY27ugQJCyupPe6-OyugYpwwBXq8xUOiynCpUqY5Cl9ppYVZDvDjHcadYHaM7c_tZ5w71Jj-7UD89F4R7m87i9rjNWc6KTbKYl2JxCYZFn2JFIZbCNwvYcdVr0cxELRTUVgkCvJUkCu5GHAZcFipII1IDJfjbnpxhuDsawPN5JGZ4knJ11S4mEhjebFS7z5mWw1tsvoeNrDjykdHuSrSoUmJ8pIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh9AVp3M8JNjqKZHDqJXvjmT88wYQDKbZ4Og9ejqK-wOPjSYMnkrtv5qZWicvKwn4h36y0EWp1SY79je0WkufOIDlt7L6tYRrAIwT3KYrjON2VLvs60K7Xbw6vGhsVVKE2LcQTuvztCGAyPWvkwuLQPAadkfuJm3d3YQTvDu1oE-OGZDCk4LM1YarbyncrHmd-cj57kEJkxBMDcYexunyBaG-p7_2MzIwimzreeG7exXFtTRM_lW7kUPlm_3zcPPMuuTYYFxICvNw_uQbwGxO79veqidz1gsfbTcrGdVDe3OnnICLBATrcvs_cUZU0r7bVvn6Bvvnt8YZc-GlsFHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTdpSEOzOJZ20yKnGmWJT89kLpJWm09qy-KSsNWm8IY0DsIxeOert81POblpDjsbxPW1v_puzlIeptVheBbqOIFEk0h4SMtAZMhANYzWKKS3wXeV1ac9opAiXyiKLVrHW77W6d7ellHj-U_3o2E8Q2bfmOBIxyAu7Pbdik1_CGKvJtmTY3cUHhIU16qPB7WBPYCt83PvMchA_ZLhrpUolZqLf3baK_b_BYV7cjbk7pv-zlHcsX3N1PSkOuYvQiqry_xDqKty-KQ4URYmZd6nhL7-A7sBCc7MUMz3SSUFdLjrZr39NNPtNue3erTnBtCeEDsPTKfw05Wc7xzmkrnqbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLi53MH7DjPqMP0ZK26f71l4giA0CBtn42EOeA9xUesDcICFs7CnXVvYiQDnLSQ9c8wkZb5lans3d0SjImJGGGyNtERm_UYCNJU0rRNIl8RVJ6QTGFMgtcAe1TXRnBB21rFvrgZaXpXs9z7Z12wPhxqDAimdj5Q_5wn9FMs26AhlNtH2cAAZhzYj6kmh0BGctZ0OIw2Q0OJiIYvWbRg_FCxsc5ksjc2Z2oSBBGM-dU4sRWCQj4mt4A6fpaM39sZgfWlpkGgyHfd4UgnwD4BgJdceO8JtXQjxlMGCvUZflqlnwgrw6SclfAXzwj6UmjsZhmG7h9T4CnUDp713QixQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=mWPS9C-m9XrLTtiufpKSNW4oDU1jgEzdzxhovn27WKMFI8h3UAvq8MssyBs9Iv9pTVtbzYT1z9fklK7EygPWOfTnOezpdCuv0ywwiS91PFCAFgmt__LE2a60W5UJSdP1tcGTkajmDxv4G8bo_6tqot7dWbB89eFcH0O8-YI5E2P-4dLxTHmFseRIH06MY7wWtrMZvFz5CQQLG3Jb9xPTGcLglNcRNHx3ZolE5Hwiy9AgH56Cbgwmspd-0utCy2vlenb7ruEo0I4fttemlIWs75cn-BKV6Yf9WBBYhHRPsbjGFQZhPNsZjKH73GWW0gBSJWg8rzBrG01HV2hFahe--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=mWPS9C-m9XrLTtiufpKSNW4oDU1jgEzdzxhovn27WKMFI8h3UAvq8MssyBs9Iv9pTVtbzYT1z9fklK7EygPWOfTnOezpdCuv0ywwiS91PFCAFgmt__LE2a60W5UJSdP1tcGTkajmDxv4G8bo_6tqot7dWbB89eFcH0O8-YI5E2P-4dLxTHmFseRIH06MY7wWtrMZvFz5CQQLG3Jb9xPTGcLglNcRNHx3ZolE5Hwiy9AgH56Cbgwmspd-0utCy2vlenb7ruEo0I4fttemlIWs75cn-BKV6Yf9WBBYhHRPsbjGFQZhPNsZjKH73GWW0gBSJWg8rzBrG01HV2hFahe--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=TQJjd4lMZOdwzb3DRnxL_rNHeeP_R5abbQVw5RxEdmhj1VeCTaIMKKigXK1EIIzwQ6-2-RViYHqZNPKuo7gvjHWEg8FP8yf7ch6p_LNjSHsBztjJIQoGPogvX1mCPJHFiXCItSDNZNXDEIFCqgZFnWrChlkELf0WdQF6XucfwIg2am_dn1TfVqzOoC912qlDXkgRaQO2cy3RevhhOOK8HUdFgG6a4IJGt7UozGpALEwQSRo34TBFUzDStAs3dGiydbRoR4NS0x29JdG8H8Th6Sy-4QpS_UuRuvQwvvsMrvFrDxiHWQynf954l4Qs8EfgxbW2RVp3CRou4-ZG61fEMIinS2yRbIASBLuJwNXWPGL0y40ADhMelKDninIg6nI-8SyaACfeXXlUIikdEKBtU6kZ-VJyelrix5f7Tsc6YvDnFORvA2aX3RbBjOUU0oYeMCoIepI-RWCc4o4nbrPEUv6Vi3Z9JPt_XR0-QjALDZZZ-6CR1p3mabaJXeMFcChUiQAtS3w5FPGpD-GSU5rQrBacJHIk2VD2JZjQ24InOYmghm69PD-hN9_uih-wq9M8yfDtsgAGTfcox2ZolpAUdMjnWgq5ibwauLMMq8OftlkYhEmjYzmrwCJW0b4tfGD108qcwHZ6z1XZsc4LZnSiL7IJfhyYCFGKCaHqMhhe71I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=TQJjd4lMZOdwzb3DRnxL_rNHeeP_R5abbQVw5RxEdmhj1VeCTaIMKKigXK1EIIzwQ6-2-RViYHqZNPKuo7gvjHWEg8FP8yf7ch6p_LNjSHsBztjJIQoGPogvX1mCPJHFiXCItSDNZNXDEIFCqgZFnWrChlkELf0WdQF6XucfwIg2am_dn1TfVqzOoC912qlDXkgRaQO2cy3RevhhOOK8HUdFgG6a4IJGt7UozGpALEwQSRo34TBFUzDStAs3dGiydbRoR4NS0x29JdG8H8Th6Sy-4QpS_UuRuvQwvvsMrvFrDxiHWQynf954l4Qs8EfgxbW2RVp3CRou4-ZG61fEMIinS2yRbIASBLuJwNXWPGL0y40ADhMelKDninIg6nI-8SyaACfeXXlUIikdEKBtU6kZ-VJyelrix5f7Tsc6YvDnFORvA2aX3RbBjOUU0oYeMCoIepI-RWCc4o4nbrPEUv6Vi3Z9JPt_XR0-QjALDZZZ-6CR1p3mabaJXeMFcChUiQAtS3w5FPGpD-GSU5rQrBacJHIk2VD2JZjQ24InOYmghm69PD-hN9_uih-wq9M8yfDtsgAGTfcox2ZolpAUdMjnWgq5ibwauLMMq8OftlkYhEmjYzmrwCJW0b4tfGD108qcwHZ6z1XZsc4LZnSiL7IJfhyYCFGKCaHqMhhe71I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=qVxiYiUKXOW7JBTLgXDCJc4ro-SOzInf6WBYB9NniLNwGnQTCap9vY4vbfN-HdARPYCH1kZBJVVJMIuPhrsAj8rr-CMyeTvFyxBiLyzuJ0cAmSpmDN178629TRlmhia9DPyxjYQu-wss2VIKaM4kLSDTIMGwLSYCePWA3L8inJldTA0rVZwRziP_ghJbNgng-RppDf_UhK2ZZvgYoZFGXZiNZfSV3jr1o_NLIpCUVEVSkV4S8gwIyimPUU30kKI0Glu052v-3TaMB_InVO2KheQD_jTWBkToYAVb5SPkSGIevhkOV_dE5i1uRXiRFyLaym-bvd5GMzCrNZDXMfz86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=qVxiYiUKXOW7JBTLgXDCJc4ro-SOzInf6WBYB9NniLNwGnQTCap9vY4vbfN-HdARPYCH1kZBJVVJMIuPhrsAj8rr-CMyeTvFyxBiLyzuJ0cAmSpmDN178629TRlmhia9DPyxjYQu-wss2VIKaM4kLSDTIMGwLSYCePWA3L8inJldTA0rVZwRziP_ghJbNgng-RppDf_UhK2ZZvgYoZFGXZiNZfSV3jr1o_NLIpCUVEVSkV4S8gwIyimPUU30kKI0Glu052v-3TaMB_InVO2KheQD_jTWBkToYAVb5SPkSGIevhkOV_dE5i1uRXiRFyLaym-bvd5GMzCrNZDXMfz86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=Tgc_TTDZufMcyfkOi4-zjv_a6x07zS-jsedkBvKci4PhogyCUhrIKzSPBs58kXtDTF3sit5gnf6CwmboR8IdsYlatUAiCV3-X0YYlv0zlR-stFR8H8DthlUCf683PmVcLATMJmBydqTkeUxYoLcmv4-VXrhMabglBBHfjoZNq79VZPLxeNsXrDYTNhyAeHrUrl3HPevRL521AuHcyrQ2PrtBgXfrUbyODacqPTyGOYgolXnkbDyJLcAFrBp8X37UHSFStqgUQQ6dOaDxsL2arQYpvLAcNBDJ23OWkiDDIslMETDjklV73R_ji7VQkoyCfHylh4jS8t1dP_z8sXlEug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=Tgc_TTDZufMcyfkOi4-zjv_a6x07zS-jsedkBvKci4PhogyCUhrIKzSPBs58kXtDTF3sit5gnf6CwmboR8IdsYlatUAiCV3-X0YYlv0zlR-stFR8H8DthlUCf683PmVcLATMJmBydqTkeUxYoLcmv4-VXrhMabglBBHfjoZNq79VZPLxeNsXrDYTNhyAeHrUrl3HPevRL521AuHcyrQ2PrtBgXfrUbyODacqPTyGOYgolXnkbDyJLcAFrBp8X37UHSFStqgUQQ6dOaDxsL2arQYpvLAcNBDJ23OWkiDDIslMETDjklV73R_ji7VQkoyCfHylh4jS8t1dP_z8sXlEug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=nu8cIUQ5X0jAPQiFk4S5QrZ5cZanpaZRJABL4YnoloeAIpI_wV776iCHaTJhzporQvfKtfFaSwIAAZGo8r6jCEjKP92UBdhVIhwxSgL7a6ttQPe4NJR5RFTx2eCSxXBT6CEIn7UfxI8O7kyVqBtT4o6t8QnnrH1xiseC-fVxYYoRqbgrKO0y-AZl8Jd_OlqpRmuf2eWdBu7F3Ztki0jRrDP8Z9KQLS2oheNJs11qs-93OptVLaf8bq7ax1u3OGY1NZyuJ1rw-7XfNsZPemu3BA-SM2IDe9OB73yoK4ZD8nFwNzL55P3x9AUQ9MpxifKAbvP6vab9EaOY9zTwT6_b-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=nu8cIUQ5X0jAPQiFk4S5QrZ5cZanpaZRJABL4YnoloeAIpI_wV776iCHaTJhzporQvfKtfFaSwIAAZGo8r6jCEjKP92UBdhVIhwxSgL7a6ttQPe4NJR5RFTx2eCSxXBT6CEIn7UfxI8O7kyVqBtT4o6t8QnnrH1xiseC-fVxYYoRqbgrKO0y-AZl8Jd_OlqpRmuf2eWdBu7F3Ztki0jRrDP8Z9KQLS2oheNJs11qs-93OptVLaf8bq7ax1u3OGY1NZyuJ1rw-7XfNsZPemu3BA-SM2IDe9OB73yoK4ZD8nFwNzL55P3x9AUQ9MpxifKAbvP6vab9EaOY9zTwT6_b-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=Ki1aqJBUYsSH_4PwQD9lYZUtykP_5y7107QnC0_SeYs5QO1n0N4-eHE-mUrbH24qUm45O7S1vtr-CmosZB99VGA78N5TQFKYABoUeKzo5X1Bh1ACdELst5Bb7Sz1QCWU3ncCQT90BtxtOC9LrWU1XSd9oSdkJS_VWcmc85N1ijrIhEzL2NKQ2ac87DtZXBZhOXaKDhlCKtxmrxT7Lf3kHMOnrd73nbChK4RsL9Kw53S1O3ztwcU6kjAm4CHECyAxGM266w7CZWc1n7LTvkywwWqLbbEeIONx3ECLiSe25wy8CaB5hjTQUeWsjZWbzqaXFfAF66hYPVHd_G3QvwEyNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=Ki1aqJBUYsSH_4PwQD9lYZUtykP_5y7107QnC0_SeYs5QO1n0N4-eHE-mUrbH24qUm45O7S1vtr-CmosZB99VGA78N5TQFKYABoUeKzo5X1Bh1ACdELst5Bb7Sz1QCWU3ncCQT90BtxtOC9LrWU1XSd9oSdkJS_VWcmc85N1ijrIhEzL2NKQ2ac87DtZXBZhOXaKDhlCKtxmrxT7Lf3kHMOnrd73nbChK4RsL9Kw53S1O3ztwcU6kjAm4CHECyAxGM266w7CZWc1n7LTvkywwWqLbbEeIONx3ECLiSe25wy8CaB5hjTQUeWsjZWbzqaXFfAF66hYPVHd_G3QvwEyNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=aN9xOkkZRLSBK9BdQ-ihpBAt7Y77iko_e286aBGcEcdd7oVc8BtuW2g4kZ0RPdUd4mAOLGGqI5IXuNUlhm5z897ZK9wzN8kfL_VBLddKKSFBUdwnnQQZH2TALIGnUK9n80mJze8RXfkn1LkvYdh6Aq-xXE09V0NsfI2SoXzH35CcyDq6E2AKjxT7LQbvwq_-X5dkDkpEtW5_OV8HRuKS83vOC1sl0YPH2NLKhXKqF4yoAM4l0rSl0pfo9stJqK1Gnyxuep0AgA5oAwoG9wWogTU7JXoUAzLAwqqRKtMs3qA8zLImuOX6avjk5vPEKLj3NuSA4rQ91VJt1oIKtIQk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=aN9xOkkZRLSBK9BdQ-ihpBAt7Y77iko_e286aBGcEcdd7oVc8BtuW2g4kZ0RPdUd4mAOLGGqI5IXuNUlhm5z897ZK9wzN8kfL_VBLddKKSFBUdwnnQQZH2TALIGnUK9n80mJze8RXfkn1LkvYdh6Aq-xXE09V0NsfI2SoXzH35CcyDq6E2AKjxT7LQbvwq_-X5dkDkpEtW5_OV8HRuKS83vOC1sl0YPH2NLKhXKqF4yoAM4l0rSl0pfo9stJqK1Gnyxuep0AgA5oAwoG9wWogTU7JXoUAzLAwqqRKtMs3qA8zLImuOX6avjk5vPEKLj3NuSA4rQ91VJt1oIKtIQk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruV1XNtft5MxRVys6gWCf-_-mDJYagp3XCRk-qCyl8IwUGa1rLdSCVWY1zUTxuC8zrnL_77kk1OJDCZa0k_Kl20cAYDsPDOGHfvEH34Jr4weQUSbp651L_P9vPct3IEJQsclDeoIvGDJE4FwNwJA9P7PT3cR-TuUsn7w6_4fFrtVCXsrB8ywJTA-MiawdYa7sGFQtzWVDNb45nmSdyvfe06Xw02fvnT3Lktrq4FohXLLKo83wfagiuwOqBIcXzqwNoM-VJgCr11DICmJmfdtMBMttxhApVwcEEFgjWu9T_IswMIgs9H1xyWEt-hl9YezJHUfgfAn6nstJzDYMFIbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=SLqWe_3d4P_ACNbC1qt7fAd4gjFXNfF1W682FQ1glK5ugZK8hWq1YdTUxIbyuc3TxUKYSUr07_JnN7-rvsjnTJgkcQSKEH3kgHDEkg4VpC7q-8nIByV70Yyfaq3DlwmmXCd6Up1Wl-Dy-vDNlhq7-LmuJnC6_SSWOq3o-ZWjaVKncW1I2BYp6zm9QHBKFTu0x127J-LV1AEX1bvTF-jYN5VF2VMrpK5hd7knnGA6IT_PXvXaeokEkEg1vBiAGDVNTix6CGrH-bUL_-ZUlgKWm9Sa9BRmvwwSs7IpkkSVqtE5Qy25HM6jHxd9R5lJZXL3WO7NSRe8B5ninirWCEtRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=SLqWe_3d4P_ACNbC1qt7fAd4gjFXNfF1W682FQ1glK5ugZK8hWq1YdTUxIbyuc3TxUKYSUr07_JnN7-rvsjnTJgkcQSKEH3kgHDEkg4VpC7q-8nIByV70Yyfaq3DlwmmXCd6Up1Wl-Dy-vDNlhq7-LmuJnC6_SSWOq3o-ZWjaVKncW1I2BYp6zm9QHBKFTu0x127J-LV1AEX1bvTF-jYN5VF2VMrpK5hd7knnGA6IT_PXvXaeokEkEg1vBiAGDVNTix6CGrH-bUL_-ZUlgKWm9Sa9BRmvwwSs7IpkkSVqtE5Qy25HM6jHxd9R5lJZXL3WO7NSRe8B5ninirWCEtRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=Z8P0oVdsaaIj1zAeOQsN6BfHPxAi0d9EfrMqeNAljjVNuk-GxV_R1VUFAL8wo2Xdn6gkdokZ658sFZBO9We1Dv9sbW4olapuyI0mCEOoiZ9S4F7dMW8qUa4qpaffxTgsXWJ8MGuKtpivD14lmSpYIBVdOGjM3j_Q1CMLhRLBEM3QKvgXu3hVxZTMxg7Z3Uuhax_QJZaIC4SBGK9fl6PPHezs2UYRT1ZLqr9mIYPB-Nc7QpCO22G5mxLgLUzfOo45tdCoeM6tQ0Av3AalGJTzTADkr5FsRr1VwUuoIwjajDA1yaVSr-bYGpseFBe7h-kpkXwI-gWjcTWK06PMmF40YYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=Z8P0oVdsaaIj1zAeOQsN6BfHPxAi0d9EfrMqeNAljjVNuk-GxV_R1VUFAL8wo2Xdn6gkdokZ658sFZBO9We1Dv9sbW4olapuyI0mCEOoiZ9S4F7dMW8qUa4qpaffxTgsXWJ8MGuKtpivD14lmSpYIBVdOGjM3j_Q1CMLhRLBEM3QKvgXu3hVxZTMxg7Z3Uuhax_QJZaIC4SBGK9fl6PPHezs2UYRT1ZLqr9mIYPB-Nc7QpCO22G5mxLgLUzfOo45tdCoeM6tQ0Av3AalGJTzTADkr5FsRr1VwUuoIwjajDA1yaVSr-bYGpseFBe7h-kpkXwI-gWjcTWK06PMmF40YYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=I0Kz41Gf-o7uXwOtGCmE41Kr03CBn18_2L8DeaC75lMU4Yw-6Sd9ZuylYdXUXOep0lx-5_9Da7jMIatLpFwhgK4GrlTrxdv-Y19sA7ma-a4mpNLNSrMYdErguuxFEENiDaf2zvIC305Wz5gXBMhM-WBBmObO8ixfMenzwn1tcbOrclNYIqJw8RtDmf-iZCG7yWQv8bQKuNmI5MjdmnWQoWY9vW1k7EEA-tiqKwllZ4xcRPdPRHXPfIivw9tVtxAsXn-sAE2Ps_X5Uz4jcoe9QAjbaPLn8ShKfF1VzIoX2C0M0mRSjCmm7Qs-EB4pFXwC1VYCs-JbO6GWa3wTDyX-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=I0Kz41Gf-o7uXwOtGCmE41Kr03CBn18_2L8DeaC75lMU4Yw-6Sd9ZuylYdXUXOep0lx-5_9Da7jMIatLpFwhgK4GrlTrxdv-Y19sA7ma-a4mpNLNSrMYdErguuxFEENiDaf2zvIC305Wz5gXBMhM-WBBmObO8ixfMenzwn1tcbOrclNYIqJw8RtDmf-iZCG7yWQv8bQKuNmI5MjdmnWQoWY9vW1k7EEA-tiqKwllZ4xcRPdPRHXPfIivw9tVtxAsXn-sAE2Ps_X5Uz4jcoe9QAjbaPLn8ShKfF1VzIoX2C0M0mRSjCmm7Qs-EB4pFXwC1VYCs-JbO6GWa3wTDyX-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=nS3305c7DF8URJb12KWBszxKii67t-tJSgUTjRH2sn0NXffiflgQNopj_bCPY7S2uE9sb7CN91Rzsg8ORehW_qV16fcy5UpI_77se6WXiMndU1Zx0_7l-Fv8vsoaNqo2kG_1hezIet4h3gMaCFmC2R-fT8wqPuPtZDE_52Ug78odKWO8bym8eaUc5Q_vJT6OrKRSbaSEAv6m5LSfq2pk48d4Q_qzLlUmqBaLeDTODd90DzKIgtd3dU1aB8lAVpg9ewvx0XP9DFOZSzopujiSZBqstk3nZL7EBZWNNFAXPR8bOXJq2CRsg47YOAFz3OHn56g_ZSeGmtcCEOiH4vVB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=nS3305c7DF8URJb12KWBszxKii67t-tJSgUTjRH2sn0NXffiflgQNopj_bCPY7S2uE9sb7CN91Rzsg8ORehW_qV16fcy5UpI_77se6WXiMndU1Zx0_7l-Fv8vsoaNqo2kG_1hezIet4h3gMaCFmC2R-fT8wqPuPtZDE_52Ug78odKWO8bym8eaUc5Q_vJT6OrKRSbaSEAv6m5LSfq2pk48d4Q_qzLlUmqBaLeDTODd90DzKIgtd3dU1aB8lAVpg9ewvx0XP9DFOZSzopujiSZBqstk3nZL7EBZWNNFAXPR8bOXJq2CRsg47YOAFz3OHn56g_ZSeGmtcCEOiH4vVB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIK7i4CjCmZ6hPMrVcRKLEYhz-gs-F5IQhOoduOHd9KeyeM-1oWuHHNqKcdHltCsMAU7n6XwrDPRYO2nanVq4BM1COQdo31xlV7cPOjhlr_RZh_xVXWAucoYXyqcMY-7jhVw10WaK1pS5CPYTdzUN5H-0R37qZIZlWB4DQK8Rl7F4bDmuEJ3vVtXzcFs6_8f076dgU7jyppLmboBZlUlKOwJx8p9SrVgOBhB29rWuTEGt6SLClm6CfE8Pc8nOyfX9072WZP2CVO4O4nca1v5l59UY5Dc49p0owhAqsBBJcmBZL20WKnvErWiH-eU1qwlAXsHaX5Cy6m4ZX-due6-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D77rLyqeV5YzeK2QW20X1SgDAyMMZ74zxgPbpTLrgsFr_qdwqqUuSB7OEB6R2KB7Tovr7jGe3pzuHZpOCVM3IqQC6takBJ9JbT78ryKZJyKuXGuHfrxXq91Qxrn3ZTHEwx6pVoNLvagNt0DeYTzTtHHFw_P-GAvsPqlGjL7FkH_TmD_E4KkKI6MYdcbHS_jJ_qrsEiAVGDgt0wK9In3YdP-dUVLHtwfkofAXOi6Mw6eqJDVoGVeNoOS2JD05nY2UfhuNJqePgmlo7SH_vDOn2GeG8LXrsWJRXC3FDQfRoWdK4-Kuf-zhUR5PQewFcae-Hv8v2fG_wwOjeZ33UqW4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlo7FPmypTxUHrBPUbADd9p7xS6F6nJbhePGRmMuZDjK9ktniLvm3sB7SJra6bs2b8VbGalGtd9uRUnH_XpkLjcNVN3fP58j34QJbJm94UjJ7IttN9vwjWz4kZ2Dt3j2xeFgjl1Gk53d14iFVfQPeUnLM_kahATE303L6h-no-IROth1SOJKAGS4xtHuwcUJTdvt1Y2eiOuCiiE2fJVV1TwmHR9Ms7ZRth7VWtqD_hWDHeDP42s0MFqlRj_tOexK2Ri1TWnPdqOLaAhsG6EBD8ONaueZw3Evl6rBD4acBS2AHyIY2R10bl10Gb40j8nNNzHgU5oK7yyefFuzgTjwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=oy_yaktAHIE2v7kKZkkhOWpFDC2OiSj7ys6PfiAp73fLl0zmXgNMyxHUU8sz1y6T2WsrpcQZKldT2V7Ll8o7qGwCbX9twX_sugoIG9-IDe3869Y0wxkohw8cMAeAbbMcBPFqVl7YxFLTYZLI-OqfhAZgTzWq_p_7mPLeQTQnO_mR7QVYDQJXhn_RUfIkyTqggdy2V6ayhNsTJ0a6t8kzWwCrwBPUxvHJzkG1MIMqxMaB8OvNVRioy-q62-uEfZ2vrxjbYRgRsRd9DduQ9PZQQ0aieGE_Uw4VdpPP5BWBHM7q_f6Vn4_k-91xJF2QdT5YkdmulEdREXuf-NsWZsMhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irqtuR4v2RYtwFJxtvJ9E3lEMB8Rg-y8H1RVtsqwpEYgvC6_icghDdeaRs5yBU_h93BoIDIlrcI9AtSmY_riRL4HgodvAucGSXdjyTlPFeRam5TY_I1DFVk77cdKK-nhXwbjgmclP8NisFFq3jiwDyaS0siBnEVXoR90jS-l8Rcdubz-5feyiPcu84feQjskvMVVyLGaZjU1zms4CT-qnIzdrCVZS0U6M0t9LS4z668R63XT40TYu61fUp0UPyKKcGqPK67ejeqg2NN_Vz1l0rEmvgTC6XCZE6H-EZAEYhAxF88zmKqs2XpfadhdNIkAKCfZmk7Jy0CmLSd9_kYASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=XGWaT-yNynmwEt7UVHima_V4m48qqg1xCTxi2a8GzFAW7x1PDkQ7IbBja0lrkqQO7VDycWaG11uCgBzTZdvP22plFhKFSTx8haPriXDffzn-iemiI5bo2bd4oWYGFYgSbefW5k7rmIX0BiCUxtHv5HBC7oryT-eW-dSqjqtgdIQqJAmYxg95HXfH-ctKBQcGi6paA-orhRAIxx7ghbEqK5plg8mXvU1OQYsMY649PA1AJOLo_DE3AlONFj2DCUWPppBXj8_GvkHQYgDPVAsdMK2n9oOWJuqmkBNadSohveYL22BCvt97hq2qEhKkJeT3L3IWYC2TVNrIkkEyIL_thyeBJm20oTy4nM7zX35xiCb0H78hx7pjVGE_fzgUWZfUEsLiAaB4UexQHd47w7qyrCm2E3An754FHlkljplnnh6KteyackH6XB2e_unoX5Hx934Sj8iMAW-f-MEf3D3vzI9dnPcEQVgAGv41Z5FkFzkeuJ8dieSr4TIie6dTUbHqsRLhUd0t7SXa0x78xYnmdCUKfFc6ntHJX6jIoQpo43wdSlSDYfOJmJ35Df_rg3RgF3C-f45ZFlbBBkS1WJtycAG2LF2WQmDe5hQcc6pCRtju4vvEm08iTcJaCtiPQdYLoXZdy2FYBqXrXhl60DeWV1p7RQMV3ne2Smmz1g-rM0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=XGWaT-yNynmwEt7UVHima_V4m48qqg1xCTxi2a8GzFAW7x1PDkQ7IbBja0lrkqQO7VDycWaG11uCgBzTZdvP22plFhKFSTx8haPriXDffzn-iemiI5bo2bd4oWYGFYgSbefW5k7rmIX0BiCUxtHv5HBC7oryT-eW-dSqjqtgdIQqJAmYxg95HXfH-ctKBQcGi6paA-orhRAIxx7ghbEqK5plg8mXvU1OQYsMY649PA1AJOLo_DE3AlONFj2DCUWPppBXj8_GvkHQYgDPVAsdMK2n9oOWJuqmkBNadSohveYL22BCvt97hq2qEhKkJeT3L3IWYC2TVNrIkkEyIL_thyeBJm20oTy4nM7zX35xiCb0H78hx7pjVGE_fzgUWZfUEsLiAaB4UexQHd47w7qyrCm2E3An754FHlkljplnnh6KteyackH6XB2e_unoX5Hx934Sj8iMAW-f-MEf3D3vzI9dnPcEQVgAGv41Z5FkFzkeuJ8dieSr4TIie6dTUbHqsRLhUd0t7SXa0x78xYnmdCUKfFc6ntHJX6jIoQpo43wdSlSDYfOJmJ35Df_rg3RgF3C-f45ZFlbBBkS1WJtycAG2LF2WQmDe5hQcc6pCRtju4vvEm08iTcJaCtiPQdYLoXZdy2FYBqXrXhl60DeWV1p7RQMV3ne2Smmz1g-rM0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=TSLxQwgkaFYXG0RkRsyA8CYIE0674KYkzc7skHa64D9vndYx7rK_1YK6ZnhKsrCqudCHAcpKDcbQVAr2YAiS4O--k8OzTS9ahTZDQC3en4mt_I5ywRvF8EpEGfr0VRfJ2EyPwGHcij3FYjhKG9opRQ88kTndCdJgaSDXeyvY0sYPwz4eVrD42bauTzCsJb70RuLwCYaSfLLJcwqi8N9ubs6qteHlR9nRi737gCeT6w6L9LrxPHxSNt0fTu6j2NOxrc2a8_oaEYL4tq6kLmbet1mjy8RFiPqaxUKFaLUipLvEOm2VLhQr0MxjHnpx2h1Xz4pD3UHxQ5ZGmcKppOfTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=TSLxQwgkaFYXG0RkRsyA8CYIE0674KYkzc7skHa64D9vndYx7rK_1YK6ZnhKsrCqudCHAcpKDcbQVAr2YAiS4O--k8OzTS9ahTZDQC3en4mt_I5ywRvF8EpEGfr0VRfJ2EyPwGHcij3FYjhKG9opRQ88kTndCdJgaSDXeyvY0sYPwz4eVrD42bauTzCsJb70RuLwCYaSfLLJcwqi8N9ubs6qteHlR9nRi737gCeT6w6L9LrxPHxSNt0fTu6j2NOxrc2a8_oaEYL4tq6kLmbet1mjy8RFiPqaxUKFaLUipLvEOm2VLhQr0MxjHnpx2h1Xz4pD3UHxQ5ZGmcKppOfTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=V5xUaGuglRR8hLcEN8UpseaGEk59tVhjgVAZhy47Z1knApOhIq5dus_rSs3U4I0PoR1xAti8XVY_G0y57ScOmhHFspGfEpt0P47_W8MoJQH-EqsT3bxOfF-umuxrCAMUZ4FzDJ_CcpFwsigrW26xo8NUTwbDBTqK0y0HWktSB0KdZq2QCqpzxEagJiN3XXYprUo8h6mVVPbK3LVoby1_nqEQOZNK3lB5vuKfASFFO7v9k95BR9XACWBvzlAqhxJmPw4TmenF5gmSheCc_B2JVURkEEy7t0Cvy1LjHA6exD0HBVu8TtXoLz17EaZJlo2o47HONuUMK77kx7KN9Rz0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YobqDl3wKZ85Yt5v2DndDjK0gIJPf6KobH2EPx0FTNMbdKlnUEUWxaLjwVKjh3m7AUG6tIRvERm-6C_z5C5qFU42jUgNubAyDbjRxX8LThZYUB6IuSJ6BqtAksrg7FLgqBQIviEacadEGyT3N1i1Vi195Bckp0qLOUz-o4oeasOpBlpn1RoVa2Ujc4wY9EErU90zsQPDvEHK3zI6a_hBUAySOoQAdiONu49hYlXDdsFnRVWEB_qZVj3VPys3dkWk53m7m6KqMCXRkN5ZNXXR8KcKBt9tiRxzbw_Wyc0pA7X8JGm-clXANskU-VJyGRZ-7Qll0whWdt73tFNPTYx7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=h90afPXSU7KFhIvUuVYVT8e_w_5RtrgkABEW8BkyXoMb5hOG3G9v-4-6gO7FhbPklGWVHmOFheaezu1roYR9PBXu9aPXcx36oGuXHkpobLwuX7vlzbiW7u7AiH2sBBz4JDXfmRh7UBUr_ekwTp4tJyETopGb0P1XzlPNxcpOe7b4bqOGd3JQaNg2Fi3Cl7gR937yz8KNrjt_c43a6cBfHaqZtwE6O42b46F7XGvJFfBvpt220Dg-rDwrz-HAX4Ca6GKyGi9NwRbk0deXZ2D_jLxQtxOtLEMKhRjU5vU7aHLa9TTXUCc15125s1PsYqDbX_TyhHKL3DOPxLPr_MTqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=P9pj9qaZ1KFojvfkZNF8vs8Lx0oMqxfjClbKTHoSFahpst6gnn1wNBoOG6wdUCyvYoU7hJcX6RbBZkgti3L5NfWBulWJ5M_l1Lop6IoHgL0kRs6_OAuklYL5_5vnjRgGx1hMAjuSNCUjOi89ejxTXAoQw4SAQYhxeHE1CPkGo7_AGJ0DDLPJ6R6YqD6Hd-ohTt7wLt3ubfy95LT_0tqFGmSGUgDYsyRjWDnnsfGEwQTjFMdk6PNORNd6q9fcFW4RCkyRhW8IEr10_qm9NdyQIDA2MaZ-voyyTAQPErDmV3Ah4EAkYj3HOf7iIXxlfWToXNiEGfLwUcqYgtcXmtCIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=P9pj9qaZ1KFojvfkZNF8vs8Lx0oMqxfjClbKTHoSFahpst6gnn1wNBoOG6wdUCyvYoU7hJcX6RbBZkgti3L5NfWBulWJ5M_l1Lop6IoHgL0kRs6_OAuklYL5_5vnjRgGx1hMAjuSNCUjOi89ejxTXAoQw4SAQYhxeHE1CPkGo7_AGJ0DDLPJ6R6YqD6Hd-ohTt7wLt3ubfy95LT_0tqFGmSGUgDYsyRjWDnnsfGEwQTjFMdk6PNORNd6q9fcFW4RCkyRhW8IEr10_qm9NdyQIDA2MaZ-voyyTAQPErDmV3Ah4EAkYj3HOf7iIXxlfWToXNiEGfLwUcqYgtcXmtCIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKSTYOqlh7bFHT0vlNb0xxOt0WN0-hOeI23pHQYRW4M3BlUCE_HnLGP-ZchPtYwQOxhN4sfEbIBun0QID51gOTyVlvBZ74G8W31wOyzhQtF2aUIDvvXC6wYpRmJW8IVbl2axcAo-gpu4So10ALFN5BdYfsCEOu9h2VWaWMdclaX6puwp3RSOLx_jFc8MEoP8pPhBOWbwaTfKBbTFni4VEbl8SJmKubSbXtSDmNaa5ggSBI7lH1ERlYYWcrjnIabTb_J2cyw6QEtEL9ibVVN5WBykxzHXsHPzyqGL5_zHUvm3bWCgjSHgLYlLhC5jBltBXDCUISo8C5iLcFKb76mP9KgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=QhsIkaw4HyeuCKuvEUv9prGvdiWoCrw9uCQkgyKO5of_XSop24VJ8FC2Vnz4Omq9qgvRV16Kt3-gIw6GkuOzOA9xVO2eNwkYO6D65niBxCEVg95gTbwq1nadkdPBlZxiv3Mfc6aseGacdy2Gijy6yHv31iWMe2_z6RsUFAXqSSweQkgK9g4SQmwsvQPeSfkOMCZnVHtYTqy5-rMgIWuYPAtdIgeIFeGl2MM0iHSBOoaiWmjDEYTy2ZW9lLY2K92DjN8Y2nW-1lRV33FVoM3Alqn9lLVCTuQojPMp9y5EgYdGD06qOf9dF9gVYdKNtTlwmdQ_5ILC76ztNBAPUOSkoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=QhsIkaw4HyeuCKuvEUv9prGvdiWoCrw9uCQkgyKO5of_XSop24VJ8FC2Vnz4Omq9qgvRV16Kt3-gIw6GkuOzOA9xVO2eNwkYO6D65niBxCEVg95gTbwq1nadkdPBlZxiv3Mfc6aseGacdy2Gijy6yHv31iWMe2_z6RsUFAXqSSweQkgK9g4SQmwsvQPeSfkOMCZnVHtYTqy5-rMgIWuYPAtdIgeIFeGl2MM0iHSBOoaiWmjDEYTy2ZW9lLY2K92DjN8Y2nW-1lRV33FVoM3Alqn9lLVCTuQojPMp9y5EgYdGD06qOf9dF9gVYdKNtTlwmdQ_5ILC76ztNBAPUOSkoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=NwqlUeTsfJJU4VVz6qgAfU6NAKot4x9Iu3bZz0khuiokUX-6IJh5Z06yKTvKvF71PuyriF5qS3Sd4V22QrEY0HCEyOy83rv5jH5EbtiwqcJnbP0LO3YWSfeji3ugA2jVs8gCvFAAdapSR80cetBShNHk-mhmzw8kYjX4857VxVR6CWLpGPUxs3EiC5IRSpHRXcVadGRM98bkNkYULA1MJbQpCfecPQVbeXWt5OSLnMwNDk2LQYNXsk-GbR8dWXDbs_bYv05WOKdLfWXvFRPG_n6FbdlShlCo-SH8BRf6lzbjJWLY6eaM1m3v5AK5QfebNU5ywA7hkd20PPJ4_e7rSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=NwqlUeTsfJJU4VVz6qgAfU6NAKot4x9Iu3bZz0khuiokUX-6IJh5Z06yKTvKvF71PuyriF5qS3Sd4V22QrEY0HCEyOy83rv5jH5EbtiwqcJnbP0LO3YWSfeji3ugA2jVs8gCvFAAdapSR80cetBShNHk-mhmzw8kYjX4857VxVR6CWLpGPUxs3EiC5IRSpHRXcVadGRM98bkNkYULA1MJbQpCfecPQVbeXWt5OSLnMwNDk2LQYNXsk-GbR8dWXDbs_bYv05WOKdLfWXvFRPG_n6FbdlShlCo-SH8BRf6lzbjJWLY6eaM1m3v5AK5QfebNU5ywA7hkd20PPJ4_e7rSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=NW8WqqNvlQ-xjsMmlWajrnUzg0VnCnXgQQP3Sm5EHCRi6uXNR07EzJWitUm9SrzBKguZy_irkk2pa7038_Z4bDg5Bj3Nx3-JkncGhLQzgvGirzpq8LwcycFAfa5kqtkVkBwOhIGx3AbyAo5LWzUsyDO-0BiLfEm27HLBn7ehlsw4t1zcatpUOo0taU80QO5BTqvDXg4qjOa6JquKUj7B8k65bt94zmnj6Rxa7xuSWcmeqIh2073GXMs6LNw9R-sw5cFlErzAFtpeTF_rIwNVUVltxsMC75A2VTyCKbWpBcAnicrVBUSSAtnUll66lhlaO5P5c1ZdV1CNyANp4gE-jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=GCEaCrwaPLaiAOZ49zUl7G_gFtWSvsdJe3PrMbFokvh3b7H_Lzv7ZgMVTMV4iNN8J7wsAOhxRz1jzTfUC7F4Hzjh_YrhTzFyuVM5ckpwvK9sHnKVUAw4dBJAk7uP0j4Lre8aoAdl9YVsgd4zYdFSXN294zj6yBPYzRAngs4U1PrxWSv3ALgTTdT1vAqS7xWM0jNWs0sXYCppYXfmTwGDjjBFVUApoBdXQ96irHZo1KmYUfzOj_pQTALelINpJOWj4w16Sod9GDaLN4Gmc6CO7uwf77uOfAr2ifkbOPsOVwvO6oU9ZCxyJs2rd8pV4RYCq2FQ5TrmXFP6dEE86vVJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=GCEaCrwaPLaiAOZ49zUl7G_gFtWSvsdJe3PrMbFokvh3b7H_Lzv7ZgMVTMV4iNN8J7wsAOhxRz1jzTfUC7F4Hzjh_YrhTzFyuVM5ckpwvK9sHnKVUAw4dBJAk7uP0j4Lre8aoAdl9YVsgd4zYdFSXN294zj6yBPYzRAngs4U1PrxWSv3ALgTTdT1vAqS7xWM0jNWs0sXYCppYXfmTwGDjjBFVUApoBdXQ96irHZo1KmYUfzOj_pQTALelINpJOWj4w16Sod9GDaLN4Gmc6CO7uwf77uOfAr2ifkbOPsOVwvO6oU9ZCxyJs2rd8pV4RYCq2FQ5TrmXFP6dEE86vVJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=Za93wskXjKYwrgzKzfYjvwRGKJMd1P7fzptbJnMboT0nsj1m2TIftJLCGYIW3BosxhHmLn3Sc-BN9yVO2CwL-NV64AZX9KLVG8ZtF1ps3MkZ1RFTcv2kq3nj6ci5yBkqzziijwb0CGXLMoClRNAj7SaCjrX8saq9Ohc5zq7PzAo-RqLGWPQCgHVeBxKpd1u7vcrvKnSH62QY1-fugjkXxOVH6BvWFaCyxd3S3jVZ-wHvrltblEEszYbKqVmrO2HmpqYpx-XrQpDtJbmDFKjfdyKhlvHZGW7RrntlEVb3cqWOdCA8-e9kPiv663YGl8hUen7xQfiZYfCBmCZGqxhoGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=Za93wskXjKYwrgzKzfYjvwRGKJMd1P7fzptbJnMboT0nsj1m2TIftJLCGYIW3BosxhHmLn3Sc-BN9yVO2CwL-NV64AZX9KLVG8ZtF1ps3MkZ1RFTcv2kq3nj6ci5yBkqzziijwb0CGXLMoClRNAj7SaCjrX8saq9Ohc5zq7PzAo-RqLGWPQCgHVeBxKpd1u7vcrvKnSH62QY1-fugjkXxOVH6BvWFaCyxd3S3jVZ-wHvrltblEEszYbKqVmrO2HmpqYpx-XrQpDtJbmDFKjfdyKhlvHZGW7RrntlEVb3cqWOdCA8-e9kPiv663YGl8hUen7xQfiZYfCBmCZGqxhoGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=pE3VS25cQeFVeI-wa5Sr_ABLQPH_orq-yGZT5vzb--cT_tjqxmkloV58ZmBh87cxGdlPTbYZlZ-3ShbOXuKmD5W6KIaFGYTtf6YMG8EdqQ8Xf2t4IHIH0CXwoU_4jwVj-mnvGsizJQf9ncn_4OraBFeok1jDF3SjKdcpHvgp1WtSwolUpxHor0eFwET8Kf5cEhk_AUFPEKbZer9WV8eX36Td2Qs6EDt71SIDR4IpyT-h5zlscdpejMGvgqElTXe9lEDJYJQvwhKVyrocJ3KI1w1og3pNNw87Go4rYt2JkYxny-b7ycmi6cg3IzhwGy4Mut6nOSY109xUFgw-cHfneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=pE3VS25cQeFVeI-wa5Sr_ABLQPH_orq-yGZT5vzb--cT_tjqxmkloV58ZmBh87cxGdlPTbYZlZ-3ShbOXuKmD5W6KIaFGYTtf6YMG8EdqQ8Xf2t4IHIH0CXwoU_4jwVj-mnvGsizJQf9ncn_4OraBFeok1jDF3SjKdcpHvgp1WtSwolUpxHor0eFwET8Kf5cEhk_AUFPEKbZer9WV8eX36Td2Qs6EDt71SIDR4IpyT-h5zlscdpejMGvgqElTXe9lEDJYJQvwhKVyrocJ3KI1w1og3pNNw87Go4rYt2JkYxny-b7ycmi6cg3IzhwGy4Mut6nOSY109xUFgw-cHfneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=D81FxDxZbfuM5EsqI025EKiDbPKdwK-2voWhyjcIS2En3V8ZRMJptoU9P1qQtnAV8FLPgCvnJkbZa-eImp_jSdHsEPZ_7iByBKVI1ulwMqqMYwroBsgBnS0Y6RL16_hzzQcfx-d4d9dsnQ55rhe5Dnv_tFXU5ZGfRYepn8UMuusa3W6JfMmTNgVtNkbJ6caiISxtGOZ1njQEepy1aWFWUgTKM_5lb2LTzHm2Yh_jm9RlJlgxw64_15GJJ0JfOmXEIrqKOL0jDW3AHfSioqpb_KuGi9smaSkhqKYYBlVGW_n6CVxESlFVjuSyGxHscKhvPbMaD0s1S9PG4I9zjGGHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=D81FxDxZbfuM5EsqI025EKiDbPKdwK-2voWhyjcIS2En3V8ZRMJptoU9P1qQtnAV8FLPgCvnJkbZa-eImp_jSdHsEPZ_7iByBKVI1ulwMqqMYwroBsgBnS0Y6RL16_hzzQcfx-d4d9dsnQ55rhe5Dnv_tFXU5ZGfRYepn8UMuusa3W6JfMmTNgVtNkbJ6caiISxtGOZ1njQEepy1aWFWUgTKM_5lb2LTzHm2Yh_jm9RlJlgxw64_15GJJ0JfOmXEIrqKOL0jDW3AHfSioqpb_KuGi9smaSkhqKYYBlVGW_n6CVxESlFVjuSyGxHscKhvPbMaD0s1S9PG4I9zjGGHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=md_Jc6WNX7NnH6dhfGfL9CfrbkkfN0cbqHKeBLGpUYHziY9tRFkkifNdLo50AeeK0cDjgyswVNR_zd8mGQZwFA3HfcwjVDwtsmYHAYjVpj9qEMIr_jJt42sqiA364uwusNxNkNYg5uNCZam-4gCBi8olnJwub8SY8igdHrpHXXZNUxoqiJOjA2pugrYix90GrXV3xfBi-7izRTYGUgPyKWQrKEGAa_WeP_YZAu02po6IWgqHLmDtAud_KKVB8cqqEbrBswA40kL4ej6-ZC2p4IHcSwLL0pQoXg-xrOijR56Hawdbjcmm4ge_H9qgbrnIsQoQjpaZOfF687xWqOWwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXWmr1KhbO6sex9JB0kBOmLRYHpuonMfpbTEr6uZnXK2pe8O9pjXLgj2Qhg5Jem18uQ9Jyplc7LASvOpRUGAyOjNjA6a7RlOjx1ISV5i0hFAABP-jsdnVGwumy0KUCgRvYtB60lzQnbr050DQtSTt5Ne9boX_RO5YVYIKxsCGbU98vk60xoxQx17h0Fp6V1Qlr8179Ux77FWrHv5AsX-2iZkUza4mxCwkzDBqnnILALcYGWTW8fOwtUwGTvmiQdgNk6Abm0cIeSemlp35l4fbDzxyKCoNaoOuRlNnGCFj1tNcFcutMwlsevPE_q4A8btWf1e43zo_bOpjXBwhvkfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=njlvUd4vBOR1a8jIQiFuWUVb307rvCCY83AKFXk_AxULOpq4z2PhBRLLlQGWrD00-GH7VdViVjMTHVE07Xd6ygFMlteTWwJMGMP2iLanmDfPB--yEVttyBk35TgF7oqltj756EGbZe39gA6KzM6LDjj9_kaEktZKw0KOUOSqAj7TjLh02EtAyQKEKlpmjxf5dlizLRbHlUKEl-_8steEzpkBmsct7M6wJJsn1ulmlTM7bcvXHs8mMDppO6g6ASLOAaac9lNIkefl9PP47wMyATOZ7U1MhrtmkH4G2WVmgQwgxMvkAuob4RhJaqMV81_t1DypPL-hbmWXBe9L-tdN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=njlvUd4vBOR1a8jIQiFuWUVb307rvCCY83AKFXk_AxULOpq4z2PhBRLLlQGWrD00-GH7VdViVjMTHVE07Xd6ygFMlteTWwJMGMP2iLanmDfPB--yEVttyBk35TgF7oqltj756EGbZe39gA6KzM6LDjj9_kaEktZKw0KOUOSqAj7TjLh02EtAyQKEKlpmjxf5dlizLRbHlUKEl-_8steEzpkBmsct7M6wJJsn1ulmlTM7bcvXHs8mMDppO6g6ASLOAaac9lNIkefl9PP47wMyATOZ7U1MhrtmkH4G2WVmgQwgxMvkAuob4RhJaqMV81_t1DypPL-hbmWXBe9L-tdN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqGj5Oyb_ldZhOLwLNWEb4Fyuo_yP8d0DfJaHD4NtsJEgEXzcYnMHxlSIZW9Zm4oWjg3v-NwKCthgUO5kc9_uyWW_P81BDXS__TDJSgeVwS8wlM_DuDcA5DOiRuSHI85pfYM2izi6iJKTJaLCwsTY2b0qIJn_9UrDvxWpts_8rqJycv8sbGK3nvEJiT2HyamorkdR8Gtwp2mNJuhGH5e_Q__ZhOOB4x8rALZL18kHNpkDeMq4-oG2s7tDYU1811Crli20RwisQWqJT69enB8Bu95Z9qgCrChyzWwc3Zr7TOKlKrAt6kpCiiVqhnFlSupds2KPhDeyFSLu9jjAOQSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=tB4HTnTL_wrHNmJFi5mtJqELxJudONZmyiNhFY_AV226xuwAzHsT_UwwiksVA0iSpsRJ7ahRAu6kWdTdt0-TAMWEtMtdfxTFVDPiBYfUEhohS6S4p5ojYRZLUekwOysjn8Jt16VUGW0GYt4gK8dxQh-eNqq5RyQ6HU2iuyyBx4RDDwvEtfR_zixDOBLFQpOaQQOqUrBPiIvFuPaaS_TXM_6QoLa5bJPaP0uKyPNsQw5CHQpV3c-i6S6q_1QUBoIl9pYlCAvca5UzKkl9bRSEbaewQGVSDI17STvCStzRuSDlkjGtqmIM3SnsAEtD1hROFRv5zO3j1XlmGPuEhQvg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=tB4HTnTL_wrHNmJFi5mtJqELxJudONZmyiNhFY_AV226xuwAzHsT_UwwiksVA0iSpsRJ7ahRAu6kWdTdt0-TAMWEtMtdfxTFVDPiBYfUEhohS6S4p5ojYRZLUekwOysjn8Jt16VUGW0GYt4gK8dxQh-eNqq5RyQ6HU2iuyyBx4RDDwvEtfR_zixDOBLFQpOaQQOqUrBPiIvFuPaaS_TXM_6QoLa5bJPaP0uKyPNsQw5CHQpV3c-i6S6q_1QUBoIl9pYlCAvca5UzKkl9bRSEbaewQGVSDI17STvCStzRuSDlkjGtqmIM3SnsAEtD1hROFRv5zO3j1XlmGPuEhQvg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=oxVNYD0b6X00UBsUayhVKJSSrDG8dJJEth2LVMSlf4wIVUBNqJ6l_lAXiutUZZdc-iFdC4h_JBtirQYTDUSJQ4gcBBHzvh2H36kz1CI2UGU1GMdlEoEgFPJPil4uv76lbqndnSXh2OeF_wC9ELPJS-fFceiOyGk_wVITpAeJLATORjz89efBXWl5eOn_JF7iA5XWXfP0_XXtgaTe3x4D4z3zKlmxB0NAs4cLHUIepn7h0H2LMP-7lfna6Wr8w6lj88Y0JeaeIUWozWh88Oh3hUhU1S_r0ddluVt3NxA9M5bVtfN9iMxiy40ueJH8jmbVVKiitIzHhjebIeBQbOdpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfU8z8ZZ--XTpo-fX0qRmU-4ZXVNGC5jBadIAWvu6UU7RL1fb8TeKvSyhrSHGBIGyi7kGPCY1IkbtIKo1NTmbN70eJooPOr0alkBvwkX1jvVDP7xBPbwiDT6-UEgfnqnvV0pNbaJ8upaM4Dmh9oIYvQLX-ipeiMYLoikBPvLjDqfc3PirF-nc2l12QHXSB6k5P06dxBAt4Hx2RM8J8iujg97CotRNpL2bU27fiZiVY9l9W0z71tT01t3w6mJGkAOevsTeQ1RjYbV0aKpmb8Fddoz0VPNxnrHUrNlx9T7Z2zGuM5KvyLgmSk8JdFZp2B5y7Qz1ikA3FYcSEOOKbQaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEMUrc3l5_aOuLcUFEANXx_oJUf4lJItws852npDjO1TegLGcxD3aUr_m6_pqqAL5bu2Zv6i9__zPWecKkzZW3xSxfBSkKdua-T09HdYx3g4WaSSnqrDD1-jrn9JoGm4yohjeya1olTe85ShfjOUPKtVVHbiMuVdZCxXFIbc3itgPd906nioLPfRFurk8VteCbuicdARBkm3Fk_E2_UqVGC83OfGh3wqCaoF8JmogWo8QNnvoAJO2JwG0oqZHsjjrEIqUlxEE_T7ycGnrg3AjbcG-gpOODjedyA6QivKpKGEXykAzONazXlIRz0bavHY6Jl2jxP2R-qpwLSicrZhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vti9XZLtpl2Z3lAOTIyVjTYIbKwwtGwfQbHQHjA0SfS_I1dBLaZjRBG2SdGPwiYmJtRLfrIv9HZwl8dT_qZxeCsWtCxv8dsPJQKydE6_t5uL5PDG6F0I7dc4iYL_Ukj9JhX7t6xhVXeeAjKEtb7JGnOGRkSXKTgAODpfNnxzNK7SH35r5uWci3kR6QBl8WSoTNYZ3iLy92rF87a1-2G9Wx1rkL-tb5DVCgywSbBO2dXrP_J_zxQir2QaqTYdBHpCRY4GkFr2vTOmGc5PI0rfOJj4hILDxr196qXUBATaM_SUCkXyaMjLbDYQmGyhd082w6hYbK2iVjr3vJ7k4Pn3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

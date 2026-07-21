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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 156K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=cCNhD1LpKg76DHq8lhAhImy1Fj5daSeRNrd3udsLqBx8zE56k999YCGdVPRIjgLWkhfdYzNz00ErYO-7l9h1Bo5Qt40B3moEpzEMjLTwW2aTdv_p-lR0zO42UORkTRLBeAzbezTaGhZ7m_MqaR3_RT2oPeIwLi8BvP9Dhll8CSrDXsjWRtR1gusK_IiWlKZ54GOXQmLiAw62V7TpT53lGez9D3UjkBJYciHVhQVdOOtFqH08qozo3vCpmroNmt0vAdtXOi1Els7a5NKnMX8iEqpM6rD8l5ObMIBYqgzrNWXB6h_TZgvJ-osDeEd_u6ukh18iTGattYx0i8Z1W_IIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=cCNhD1LpKg76DHq8lhAhImy1Fj5daSeRNrd3udsLqBx8zE56k999YCGdVPRIjgLWkhfdYzNz00ErYO-7l9h1Bo5Qt40B3moEpzEMjLTwW2aTdv_p-lR0zO42UORkTRLBeAzbezTaGhZ7m_MqaR3_RT2oPeIwLi8BvP9Dhll8CSrDXsjWRtR1gusK_IiWlKZ54GOXQmLiAw62V7TpT53lGez9D3UjkBJYciHVhQVdOOtFqH08qozo3vCpmroNmt0vAdtXOi1Els7a5NKnMX8iEqpM6rD8l5ObMIBYqgzrNWXB6h_TZgvJ-osDeEd_u6ukh18iTGattYx0i8Z1W_IIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=dWak3anlvwtulfuhyIYqjzwmyzkHnjZMsywcYRLa8V9WJpLW1wClxtyOV6x76cs9nqvQxntY8Mtz6vilJk7YvggQRxjVQYUB1NClFNvu5hmD1nXREho5wpOlYJ0blc57ez0GIFUxHWEqF9eyzbkNP80fF7SSq1siu-C_JpIQaLReC3kJzcudhwOdDTGc8CwUxSxdZa7SZkgkSRpwt5n08q9FP26VRFwinx2WPncx1Wm02ZgRbRk4PokOHAK7aZbq50x-pOqZVwU-uB0FuQ32GUqmPPxm39xAv5xtvs2HcvsfVz7ukGwQgcbnGvjPJ76tlQ-sDWApUVxoHYCPRDFFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=dWak3anlvwtulfuhyIYqjzwmyzkHnjZMsywcYRLa8V9WJpLW1wClxtyOV6x76cs9nqvQxntY8Mtz6vilJk7YvggQRxjVQYUB1NClFNvu5hmD1nXREho5wpOlYJ0blc57ez0GIFUxHWEqF9eyzbkNP80fF7SSq1siu-C_JpIQaLReC3kJzcudhwOdDTGc8CwUxSxdZa7SZkgkSRpwt5n08q9FP26VRFwinx2WPncx1Wm02ZgRbRk4PokOHAK7aZbq50x-pOqZVwU-uB0FuQ32GUqmPPxm39xAv5xtvs2HcvsfVz7ukGwQgcbnGvjPJ76tlQ-sDWApUVxoHYCPRDFFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-KuXPZluBTFKxYJQZr_XyPa5t_zVRpaNKUvYjVPHsdaUs4dibDIZxNyHiPdkDt8-fFQDEkZWiylzLu7UpGriW86wfa9V4KHO_xExXAhgG1I5vqYwLJmQ3ooNiLP4SSQyzOFbv9K6XOlhwz-tRBugKwA2moyho1GpEKUU-Ruy63j-guNMtzZbpgPinjUjQ6k9qbW1AiTLOwN3g3h7kKO9AXkl8HhcPJlZL7N3F4ruK39f6VdVT2kjga1WDgp9Ofp4xUsT3hybMFtoINHXyKNQUqKRFTLepa6EC-1gESxXP-QOc2lAgUNN_bGzfNGWSFPnU1urJlqbSSarOhQSrltVIu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-KuXPZluBTFKxYJQZr_XyPa5t_zVRpaNKUvYjVPHsdaUs4dibDIZxNyHiPdkDt8-fFQDEkZWiylzLu7UpGriW86wfa9V4KHO_xExXAhgG1I5vqYwLJmQ3ooNiLP4SSQyzOFbv9K6XOlhwz-tRBugKwA2moyho1GpEKUU-Ruy63j-guNMtzZbpgPinjUjQ6k9qbW1AiTLOwN3g3h7kKO9AXkl8HhcPJlZL7N3F4ruK39f6VdVT2kjga1WDgp9Ofp4xUsT3hybMFtoINHXyKNQUqKRFTLepa6EC-1gESxXP-QOc2lAgUNN_bGzfNGWSFPnU1urJlqbSSarOhQSrltVIu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=nrbm8W9IOtB56hVaQGSaUAHFqec8ciBigNdbv_p5WN7hVbijoRJOkxsppv1zHIQnw-xv7HgYQdgodNIeZW-K2_1XhQkYC265wAAAUBY2m1CGBkXPGLru_P1wwD4YDw2y-oNaUtviocVpmtwe_EdDM6_u8B3pEHqaqQqOjrOWOkPjuSkGznJKVOAyffe_aY-6p3QQHEIwmKEqyVBHYapXQmiu0WUSk6SIhj12q3CGTs9FpchvGI0LwXRiuV7HCjbmvAz-slJtKL06fhGqKUou08bDMlDuMI0jDErADmax4u7NJISmtE1Lyj02I9xdPuhv7LIYY7_YkynqWfywE0Yt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=nrbm8W9IOtB56hVaQGSaUAHFqec8ciBigNdbv_p5WN7hVbijoRJOkxsppv1zHIQnw-xv7HgYQdgodNIeZW-K2_1XhQkYC265wAAAUBY2m1CGBkXPGLru_P1wwD4YDw2y-oNaUtviocVpmtwe_EdDM6_u8B3pEHqaqQqOjrOWOkPjuSkGznJKVOAyffe_aY-6p3QQHEIwmKEqyVBHYapXQmiu0WUSk6SIhj12q3CGTs9FpchvGI0LwXRiuV7HCjbmvAz-slJtKL06fhGqKUou08bDMlDuMI0jDErADmax4u7NJISmtE1Lyj02I9xdPuhv7LIYY7_YkynqWfywE0Yt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=hreO0ZkEBSsJAiAByssxAXVj6nZzpkFxrcFMLIV_gSZemdAAdAISD_M3M3mxLupIr7Xb3NvtGkmZcJ6I8wf8dElm-PT9GMoowOM0RFNx0O4RqRpR9mgjb5R9xJQtRV6vgYKOFHSXI0EzCpYsnTH0iMMJ-CoFo6CmBIiTZTRhMxCiDgxM04glvshz60f4yd-6BfPLqfMKY_c_kHl_X1gBquu0ewXigVndWrsude2oKVNe9bWP4yYBk97qpqHh4VpaYCCQF8OGlWgjj3iIQc4qNfZDI1zJ6-u8bBH2MaPxANUXMWanKiH7PuU7QwZN1bl5vmYcayN9tfab0h6vOWTq-rOrK_Wn5YGDdU_1s958_TS6qGadr-HasRzNSgtzibcWSSjal6zEpMzkvNK905CJln3RBurffDmbvLHFlaFt42cHQYpdhtiojmpbkyB668lNHCYa-Jrjbr62wGpqsUMikovIOiB80kXE6XAirkNvJ-V0_NFkxvYmRKwmX5r_tIsQ1g23jEzNpSOFYxxW1yM2aaVXVCnEh8YzyeCXOkXaStxQatx-KKjvhbMEKcN50ZFvfDZE0aY2NJSoxpSACdqEVL7Exd79zd7ikB2IUb54JGVYs1cR1ouGejrBCRFW0LZQJU_b5i5Rq129S_W_YrBq0c-5QB7heIf-NiGpT7zpCzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=hreO0ZkEBSsJAiAByssxAXVj6nZzpkFxrcFMLIV_gSZemdAAdAISD_M3M3mxLupIr7Xb3NvtGkmZcJ6I8wf8dElm-PT9GMoowOM0RFNx0O4RqRpR9mgjb5R9xJQtRV6vgYKOFHSXI0EzCpYsnTH0iMMJ-CoFo6CmBIiTZTRhMxCiDgxM04glvshz60f4yd-6BfPLqfMKY_c_kHl_X1gBquu0ewXigVndWrsude2oKVNe9bWP4yYBk97qpqHh4VpaYCCQF8OGlWgjj3iIQc4qNfZDI1zJ6-u8bBH2MaPxANUXMWanKiH7PuU7QwZN1bl5vmYcayN9tfab0h6vOWTq-rOrK_Wn5YGDdU_1s958_TS6qGadr-HasRzNSgtzibcWSSjal6zEpMzkvNK905CJln3RBurffDmbvLHFlaFt42cHQYpdhtiojmpbkyB668lNHCYa-Jrjbr62wGpqsUMikovIOiB80kXE6XAirkNvJ-V0_NFkxvYmRKwmX5r_tIsQ1g23jEzNpSOFYxxW1yM2aaVXVCnEh8YzyeCXOkXaStxQatx-KKjvhbMEKcN50ZFvfDZE0aY2NJSoxpSACdqEVL7Exd79zd7ikB2IUb54JGVYs1cR1ouGejrBCRFW0LZQJU_b5i5Rq129S_W_YrBq0c-5QB7heIf-NiGpT7zpCzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Z65lrQSDwLEtLGA9JQ7Kuoraql0ih1mBnTsfoeysPS4Gy_M9CNBJuAwxFKsCzy7bAVOQLlmNv5-ykcDumYQFVELhPJhQ6uMJlpN3bTxjJYz2a-RoNjsUBmrMHTah2PHxmSa2E_n2xDIDr_Msnn22CdCgDco9mgmUoDmlNwcKp2mXjpjlzQjhf4bkbzF_jfiWLIvhn5BHGZGrRceKa-k6Osvq8vA2CmG07vniAVVrsUJZjxUS2pccDZ5Egp0aeh2qfN13DS1GHd-BaLukYuOtpF7NhZAi43wxhIcQxdRNmbFb_ch5bM_wLRlLt-B82BkRgMnYv5KDeiwrKSwmJUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYnNGZSy6NM0kxP6OWe_MWD1etk49zmBwZ9kqXY7RN0PfmtUZtz7VSgQhLqYMhxcVXa6l9WOiWqVBmLAbXAfzscTF7PC-aYo-jBTdIbI6rkII5S2Gl3n00fYNNBUH1x9EWbLKyigTfn4cTeJ_ylhDZEgtl6HMXRkJN5lXDt2aJbBFXJzRIIzVjO4vLBNiGjn_KqM48QkNVMWpKImTv4oNk4JwFqmxJ1vMOwTq4XOiVDe1hN4DCaLReP11T72-02Up22b13F1Lzjy2G5z_B2K9x-Ucb1WkRc7lxXNV0qJLWCLvkq8Qn2nJmwkBg224nh9Karjwnd2WANgGojAn0WEI34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYnNGZSy6NM0kxP6OWe_MWD1etk49zmBwZ9kqXY7RN0PfmtUZtz7VSgQhLqYMhxcVXa6l9WOiWqVBmLAbXAfzscTF7PC-aYo-jBTdIbI6rkII5S2Gl3n00fYNNBUH1x9EWbLKyigTfn4cTeJ_ylhDZEgtl6HMXRkJN5lXDt2aJbBFXJzRIIzVjO4vLBNiGjn_KqM48QkNVMWpKImTv4oNk4JwFqmxJ1vMOwTq4XOiVDe1hN4DCaLReP11T72-02Up22b13F1Lzjy2G5z_B2K9x-Ucb1WkRc7lxXNV0qJLWCLvkq8Qn2nJmwkBg224nh9Karjwnd2WANgGojAn0WEI34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-1Yp4S9Ue66-D7Ym2yCu2WPztDJS2Ixh2o0yNABCJCMuilRg7rVER7U9iD0EmVNL6y04Aw3_6NVpWDRFkru83L_xcx8PRf7P-AjUtGIV3ba8-sSCYFFdjDjpELSe5DsR7XCHdYTYUDtpwBAKhic0PD__n9nacdQEKWEOkarlE8im7jZpVfjtU7CJikj238E0Fb596MXQ54PvCE6mFXkiREpY12Pt0d3DEsoyd2SoTsW68U4kaebbul7VJ2Fx8D052prYSdSLGzaVoKHYQ3_hw8NJpwPNoMmgee59I5tuas3WUihUhP-ghh0vWEStBsnIrf6hYMyL08TmCEI_kERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/OEIPAJc9r5PWJSde1W_eGMIA6L8irXsSXx467Hz9SSkGTCO5am6C-ToJaY1CMpyNTiws06JiiL6BPfeF2qOvTHGEpa72JDQ9bmTm5noYrBRCeP989DxPKKV0pJJcgYCnoTPMeyozSXWh8ck80N-1qM_KfG-yH64uYTbJi_Cz5otoWs5ZZxfIyTQbv9DYFJZwupjmzai5A6u6nfrzmlbNh34lyyug23Dd_QDluwVMAJFYl0cR5v6PucxT3ExLzQGhz4e66Bj5OjxsH6vscNR4BfV8aQp4HZHFwQd47K-0o_A-gdX21uZbxHSjd3cyBaOZjTxGbATQd4UbrLOsuecSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/jfeTqOL7tAK2hY5uFrElhvjFORhEo7pnkds9i6Xfi88cQ-k4uUCUTCtQA6D4uj-dYTAfDoELvXE1j1uoPS756pFgXZtXR30lAoSBe6ctNkKtT6dMKy0V7WAtFExgJ2Bi6ES4g4PRLI-7Hd1JATwuDpaXiSAf4O3anoTU6vsJb2-qg9S-o6DkQ2SDfoJRwgLEUjyCSn_URgA9QdIxwTrHuwd4n7Jj3mNtanM7aOMhBI9xznCed6xJ5SIeDAZrVgnP20mW-inPRnNuO8OsxCrL87kB8VAAVNOJq32nTJMYk7qZ6nXJII19uOGfU6fHNM6GuCRrPHCWIsl-OCLxv5HspQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=VirdSLGrHqOg4tNx5x358pMupAHpsTYxa31PELuR15Hy5tT89fHXMrdOQGy_5GoxbjWWtT2-lQzvk3hzQinAZX-6cK3MSHQvJ_f9aZT9345ZgFx-DC9PbFo8x9TiY8Uk6eEks_ihWAGmJH7tMslXsama4TZsuOuzmumx_fDrkUPz736ypZk4UVXLd-GMcJxM1lfdI4fErJRTIvt7clubLqgq7hxTvUoIlfoO5V8cwWRMSkz3Gc06W17wkJ-MNOK7tidruuT9xSxyQS6JFZ3yd_q_74NSmqwf5c4PSwRKJG4rjZvHHhBnSEni6xLw9Y4HbGlJ6QtrQC0qJ00uiy3nPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l43FwaK9il68Ce9HkJAbVy8vE_x-Iw917uamSbHRjXz89GyLoFTJrwn8-QXBaskw9M8aYzc9Ydo6JKVrTVAWH9jywvsc1Kljb1CwMF5hdCw1h4pSPICo8cI8HvuaOeOHlf1eaqIz6hzLtMoW8w4d6JDPO1wSOB21DB99hwEflZweoveDDoMqwXAPjPx0tyxZ-jC-CI3uTYsJGV0V3VKzbPZ-483RU4MfeFB4_00qFsZofFrf_r9cM_qW2v0luzm4u1lHATpYQc7asIui4tk5_RhlDijWqZwtWjKqMzc3lLCH30KcL5jR5MpKcBV3fu-2x_YpbnzSmLI-BREj7IfY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=PqFhcWd4M1XLzFSmj0nhytnaj9tPDaR3J-T00pNPqpnj-cIJ5iUM_1gdjjYY43iqyyy3cDf0kk4V8poQ3q1jx9_23dNWbZT4Kd90xa0raKhEug0lmEPktzejtCs7Wr0H2E5Flb6Jio9Ac8oKkKyukm_C_fp6dCdy-iHupVNuTvPi0LhxeTnXypBTRiOwv_ZQkkoYrgrX5auhxcBWccKeIulWT6sQowBAeFlc8CNLi76lYj-7CkA3vLY-wI3yncyyylJF-V2HUB5MaIVPBopsBTG9fId22N5CiQPJ1Eif9UbbDa-KSExpmdJ38FvyI2LMLb2_-u990ljavvnd1WePkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pScCYD3_0dU19LtQFKnaskGR9rpnr93Q2389UQkSfxJ71wSgnBNGlZfHQBA1XCO9v0D6YzWcGFBccfQhf4nR9hmKnDDgrLZqzdzHMXmiwoz4i2zO6VH8g99bme16oimDy_LwBvUyNddNlfOuqU06J-FlEU60rqg98OfT1fH3ScFQN2TR2QbcLC8K300aATtBoYGAxU3blieXUp1W37qQ-6wRjQjiJA2VvPMTErCRbK93Rc1liNmz-bn3tlo1008yA6P0EmBmhEOP_KaqLdETKS9Wf90np9kK0OGHFIk05P20Xa8pTv-JHHzA-aTcOqzgWEVnDMTgNZIjreQQ8D4tEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHL300cIlVUaYCdNQVCb9e9LYYEABLRiXnnNjMqPfb6E6PTxZQnv3nIce7xKuRZJbKWXOAsMxkJk5OLEBD4btDsSRDBQMnJa_GmlGoy_Y6OFgMD7C89YwM_SAl5NYlAAfbAqfgBvOA5jzZvqPnX8lw1WbdLcNSIH2B8bLRrQpB1ir8oktP38Fghsjlpciga9-LN6NvaN4w0RQcbTGcnfj3N6weUbwq03Wv9ZL0LIZoweJiP2Kie9EJlaiE8vG2qfsnyxYw9Q1C8eg1JGNphDxSs8spqj9kO0dq9mztLdqCpEeWDvKL5oa8TS8yMgSTML7ETjAJ3fPe768K2sBbHHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7KFb5QCEDRQVWyFlyIgcOEGePjpKJ6dZwnFmpdG_ncMoFujLKKxSiAgU7cbrUPuzsq5xhtRSTovDkrDHOJrJRp40_1nBYtOOtiHxQjrf2gYKpLuv7DUK1Duef8vIEh3TISpPnKeeu_yXSqGbgz1MrLtL5m_ADV1GD9KlUOUU07sfeWa14XXziHCEJB8O-oE8qFtwuXxudfUMkRDj_RuX1qIMAiImNaJfppJPSJHwBZb1gZyNO28WdBJ4zAu8g-MhAkMPGoApdZYZpws_qLBXzEk5oQkVBnyFo-5h51xivCi3-X0Ot6SVQJbVDUD5uDWnLaa-Ez4Z2bFUJcfzjwoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_63Sll41xy9ZJsfZZ_lkUBQbIii0I7PkiPMMzIcPE4tnONGLkAw0XAOtven772Yp7jPDX6w8ghHzOJC6Oy3V2LgyQPOrlE7rSU36Zz4Rgv1ra5sdc_6N0jDROEFR75nv7gsBdrfrpdE9o-tv8Vjo-isP9m0kGjPG80lT2aTOr1nleVYM77glPJTn-D2F2ByLBFm8UQcNxg8h6KuHA0oUO7nyIC9TdiSHQeVoixgXqjXITXQeqRDoglzyo3qT9JgNcfU9vcA9Rzx4DLF0miTKu_tZpS30OHYR_Py_3wme30ejorbnKOfKn95n6gaBlbSEPMxE1GERVdHeb3BdF9w8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYsjs4dZOeyCoZgSi4dx2WM88Ikr7zLw9dmvsFxf0ixksppXaW19fzZM_TQiJH8tROWUbzvTqneu8ynHpb4yEhnZMUkdvyYz9pgrQXgNZ9cKvOzwqTn-M3Az5rcaN_-KUmHxbbkIXWtgkFVZWHFZrlbmjXonne85Eic9vOv9TmeiKtebr4g5qxGcDrZpcP8OCPZGFswf6RJmffmAzUbDLgWzsBxxnMjPebpu9yLShfgrvYFr4CYSgvp1Cdzs_05lCUU6TM27R8IxLYLbaGXn85IDGD37wjZQ_Ua1Oyomx6UeHGlimO66I29DXvnsWUy-GXxMddXtgTmAnaC6q9vNWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6PD3-as8ywkMOEzELZf30vgirQK4BUlhj3evbNYzhwKrNtTAj3O3hm0xdW3032843Z5SbOgtu81i_tKBiLvEA7xXWCV9CRgQEeUKv-3D6bZLUxqsXhZVFRyN0nb6SD1XfZkj5cUoVOz3bR1Zt1OJSnO9QPGcTOgKcHyu8jk67cu4Yo5GZETDE90qG7zXNVNUpsGdhdaAwF39QmAj75YrT3tiBAPF2wwbF9mOpRD5EIrXVBEJ0PJDonYr1P3wdzD9lDdc6LehCfW-xIlkm0pm4Hghmgk_YLtVM6b2kFSdqpLz_odWdw9QxiV4EcZ9w_0GuymHG6i9DiU9mVmtRbSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=XAcQJvaXCK-OOpDKqHWMzynLfQaBy4hFxJUtDHo42nxCT6Ovdqstwo238GZHKD05Ikr_clWCWhVjQiW7Ei52eUHYR6RfZIvTebODvS13iPJlrBKWvFkk88y1eMX5OBHdd5TDvePh7UkLzDkY5T8Q7gq7TuTTCNxFtdA_uGF6Yl6jLQ5qyIj7xb0O12hlAfo4SURYbHuKSZ4y1rQY8BWN8vhbFORngFdktvsDxUAzXi4jVK5Mu3GkMgBjUsGM82McRZfrZ_xHbc09EWuitOi-OTU_9zOpKPCZf1-c2CjvPu8KiXGK7yn4F57ob_4DoRm98vCffWgE7Oy-LklQzX0SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=XAcQJvaXCK-OOpDKqHWMzynLfQaBy4hFxJUtDHo42nxCT6Ovdqstwo238GZHKD05Ikr_clWCWhVjQiW7Ei52eUHYR6RfZIvTebODvS13iPJlrBKWvFkk88y1eMX5OBHdd5TDvePh7UkLzDkY5T8Q7gq7TuTTCNxFtdA_uGF6Yl6jLQ5qyIj7xb0O12hlAfo4SURYbHuKSZ4y1rQY8BWN8vhbFORngFdktvsDxUAzXi4jVK5Mu3GkMgBjUsGM82McRZfrZ_xHbc09EWuitOi-OTU_9zOpKPCZf1-c2CjvPu8KiXGK7yn4F57ob_4DoRm98vCffWgE7Oy-LklQzX0SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=lRjaKW61DFN8aJ4cDIUyRfmxcIJW_8et5nvraoeofLsjbgEY2GNan6aNqlCP8XInAA2x3TpPFHVITOVtoqBEDGRuRXEikrbm3LJf7eTWHNHRutIOjWliy3QV2jUg0LVv6RjqZSFMXk2RY4zlvc4ln-hiUZuFnTSk2O_D0j_H_8OgbM1Z_KzC12VmZKOFiG1_Ix5ubyzn-uiseVeksSMHqkIoqtLKhuw8VbND85Mj7qYvTlRkRTcvEYkOiiHjU5LylfKZ6Da2UsHLxBwV9mmC3QQGDSsIdg7xZ85OvB6npGRqZZr1sUCqeUxh4Rh4dVCB_67YLBS6nl8aQ0a2N4O2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=lRjaKW61DFN8aJ4cDIUyRfmxcIJW_8et5nvraoeofLsjbgEY2GNan6aNqlCP8XInAA2x3TpPFHVITOVtoqBEDGRuRXEikrbm3LJf7eTWHNHRutIOjWliy3QV2jUg0LVv6RjqZSFMXk2RY4zlvc4ln-hiUZuFnTSk2O_D0j_H_8OgbM1Z_KzC12VmZKOFiG1_Ix5ubyzn-uiseVeksSMHqkIoqtLKhuw8VbND85Mj7qYvTlRkRTcvEYkOiiHjU5LylfKZ6Da2UsHLxBwV9mmC3QQGDSsIdg7xZ85OvB6npGRqZZr1sUCqeUxh4Rh4dVCB_67YLBS6nl8aQ0a2N4O2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=TdxsNiRE8hZnKtxkjgsjCavyDFBBPN5ZDGtYsP6w3apMcsgyWXXtvk_i6m416uYWlEULMaFwpGZrgpsV_AiO_N0PFe_hKN3IJK-Gd8oiuj6d33rgfQpyzRng5NWEhWZF5DQk6B5Mgzh0Ccfo6qgzwR2kn6cNoEYXEXDDqAmG01r0NhdFpUABhF3Rr-vEwetZNxqmuyxEFWgevn97iZ6lqfi3fG1VMoB77aJ87C1wIatmc0aiuXI9Qk_AKmujrjlG-wp8vvPDids3dJX_qAjVlH0hpCJ5_Ycs9h-CDHERaR95TqGLJo10pp_kJ41g27PgYF7Wj0QpVXPsGCorltFPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=TdxsNiRE8hZnKtxkjgsjCavyDFBBPN5ZDGtYsP6w3apMcsgyWXXtvk_i6m416uYWlEULMaFwpGZrgpsV_AiO_N0PFe_hKN3IJK-Gd8oiuj6d33rgfQpyzRng5NWEhWZF5DQk6B5Mgzh0Ccfo6qgzwR2kn6cNoEYXEXDDqAmG01r0NhdFpUABhF3Rr-vEwetZNxqmuyxEFWgevn97iZ6lqfi3fG1VMoB77aJ87C1wIatmc0aiuXI9Qk_AKmujrjlG-wp8vvPDids3dJX_qAjVlH0hpCJ5_Ycs9h-CDHERaR95TqGLJo10pp_kJ41g27PgYF7Wj0QpVXPsGCorltFPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpjZx2lNtvdjGVrIo9LwoSGms_V7-MiuN57yWaAgOHTYDniD8BSHK11HHz6nNv8Haibxezfqa6gpb2xAFYrPLwM8sdxdyy5Y7VZ91MKS-M-kxpMbpv2xCiZy4LzN_r_XdRn-jD-s_xo1dvRkkLkBlqdrmj3HmT6p2GRoy3MG5cxgmlvqq5PHmv-QkmQto3Zv4x2WimNf9pP_a2IOI6BJqsw-h8doKZDeig3Fmz-9RKN7c2yADXfNfMQkG3NDmPa70TcwSb8kMmbBw-Ch5IZMUKK_KFUcRcPzeUN1gCuT2lsJYKSzu3IjN3tbOtFTvdpFGlJ2dahJ4LzYa7dBieuUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZJ_gHBGAtM2GRVdlxPehcP6kH_HquLC00vslxQ1LRkLNLdA2zGZW8oaT2wIZnSKmRP4pBlkZxPgnEdlkpoqj4K-Nf4e9HwCsjVjycREpYfX46Zs5zZ7sr5Zgkuw8joc_s81mdAbfGjiqnU3Mfy7_TDlGEp_o7B55fSn4Sn-TsKfMuZAHDjQVJWdTnnhkTWaPqdBoZQm45QxGl-oPS8OXQ9WCJTQMOrPmgi5UY5rZ9DL_ujXjV4xtHQwdvevkTl0G0muvEpHRGNDZKYVqVJQb8drolPTGj5G7qzofoWAzeJ-qZZPw0jhKJqWcHRuhew_gEvW08m8pm4BktDSTA7dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzCgJcHR98zrhWFppoECc54jrMe7QyDxKCZ75N5HGuDZy6Wlqcuzbic2X2IB-3SK7fZux9jimbXRvZSVOC8TnRzRptdSe83effP171ISJogDdQ65JdfkxHh77L13G8O6_k2ExuqBgAYpol1B2OeaSg8Fm-0QAUr-mKB60hLpZzcMyTdrl_TWMWTIfrgsKmwHjke7PUdG3FB7Vt7L-ayT0-ILpMeVXZkHqRboBsrLdibU8zJjrthTvchKfmdQooraTlq4P-FK-pGDZg7DllQTs9O_N_MxiGutRRYjj0B0QQTYUWRfb7ClYrsKB6fwWhkcHtEfO0y7B9dfyeiZrOuplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqbyC8xaqHJz2jgX6fZXnh4O-OTVxQunh-PQFc0fzeedqhlHccUoPCaCW5iusuA9-DZgXMbcyBgXbgAv2_GQ-dAXSeevJYliiuXO1VZa3u5OX4xBf840G0yMpvTZDx5yKfbH7JBvR9yJW3MqpZODsjEZzYOpNVr7S_i8WqHQAZzQD4mOjU9f1kJTTaCKhSX7FwTdyXOYK90-ywxb68OrFdcy8UE0ZiuMDgRkXwt67oKOdb0VsNj2AszTfWCgmneNDcb_vt8yLTh1GV8ddEXYOLOHVKbZ--OeFSMpGvFZcncuv9l_2UTg50yK4rDoJNVpnmWrFNSfgRgfC-P1NkczQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORxwusqCJPNlfCk-vQ5ImrKXLD6t3tNldqXWeUnApLIhl6CXXqIF3420TJaQdH7tB54UBvlnrd2CGE5N1WYL_g8rt1EDdRPV1mWdkEK50AH8NCx5AevARB5Eu69yvEsvCUI3YljbVfZdg_TTnO26GtZp7xBchUefRV2qIhph62F0yxeeJ2oxL4jqmHPJxryboL1AQRfJv2FlK2JQA91qjj05EZqtMyagpE9S3PUqvTvBiM07CIFPcQL1uv1pxIvmHDomMgxIsnaDgB8JetkMc7BMzTsvkc03KNbVPnxivH2yWa1hoU8DdzoxGsf-AsNPEoIl63GmxBFDYCnBkgj5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PWD34dJGGfZwyJwlN1LTMpbgisgUZ3WRdkmA-sB3nRmWNMzyxRLXNusAytkecHeDdQO9ivZ0W2txFxQxwRLwKvffHrbuB-w-clxoP5sf6YHUBhf_zJoa7Z-AJY_CixlZddT5S2FuKwjo5Zx4foUyfioVq_NlSBuaCudoU6F-4UciPkqM1xmAjgy4nHkUNMzWbCLYlgwvyjnDQvnak-h0am5KUAxFPy9fCMfGf5X_NeMOKk_aPipYysJQJpQGIyhsQ28K636VI0bqvAhkMTNaJ_A8m3y8JFfCqMzJFoInzXPkU0XdkCkhi97uBAwWF7DlQ4u_hjLcMxcLx--isGI1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bvciZfZln8gJE0m5Y_eodYsgjeEU7d1yCcytDVbpSfVhWLE26gTqgUXeUxUdhJeC9Wj1y50tgI7278VS-H1Srk4zYX5SPZWHcog5F1n5E2F4yqFABxUq9m-ahdf_-z-f90t5kwt2pchpLMCGGhmbfJ7_uAGALi056ef2eLTVLs48x8Yn6HeaSzeRm9sOj-40tjAEpul0Xqu1jh5Rr5Ktz92dsvrK3O0F3DDlZm7g8LV3a1jFjf0dCM0QPVnzU3AkCKF-g3bhtxVq3aAQ0zZdHHGMPT93kBNYDL_0PKrNHTvGBErXnnrian9TUTCYG3NqE0ZzGTZ_vc-6Lm0hnmxsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juNDBaxb5jFu3c3bdmSM3QkKjSab1FBqVz3HL4feKGtCWfJq0jLbVN3ceiFZB4SLo4OieZ2eHtwctwPBCA51Ali4z7IK6mw_hHHAsh-EnBpnAZEowmmutrxL_NxzborDhOY0qtAILBdafOc6IUmAtIBIXwijN2npHet_Por1QCYGPcIw9Z7mK5I-4WVpRqWyaEs403wS2dTnyA-cEhfcVQNBJKotALY1BiHOLUqK-AQl55bI1CmLyMchfpmsbpyYBfUO-uHXiPPlA-IlcxzBz4BTbnfzAT-PDX1rOWAwOD-R1oU-xWeegXTsSjxvK_1MgP3XhFo3JHUr_FGGqBhgBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=vas-Su5Ry_Ye6GvPpWSlJEkRunltPItAp5UA-i_6SQKZjERE8xsFU-izW0MsAy1vGO2uA7SE0Rw_VoKy2bTVosXcLwKUz0Wk65F4X1zJ5W3AwCOhePQ2jyLfl2rj4Kd9JT-HYIOcz42C69T8U8OlouEo7fkXsmQo9f2aNkHYc89Mr_UuAb97vhyQU1O2N7Ek_RZGzIwlxKsbHkOn2DVn7yTA5esqHc7Px1h7P_5begGxRsa9EhXulA4H8n_70L5ZgLII9LK32ytk6socF6sumSPYld0zAA6o6MzG9oVafLJVa70dgmoMnJvTStkvWOhZEyF6COAh-6XUECq4c-DL0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=vas-Su5Ry_Ye6GvPpWSlJEkRunltPItAp5UA-i_6SQKZjERE8xsFU-izW0MsAy1vGO2uA7SE0Rw_VoKy2bTVosXcLwKUz0Wk65F4X1zJ5W3AwCOhePQ2jyLfl2rj4Kd9JT-HYIOcz42C69T8U8OlouEo7fkXsmQo9f2aNkHYc89Mr_UuAb97vhyQU1O2N7Ek_RZGzIwlxKsbHkOn2DVn7yTA5esqHc7Px1h7P_5begGxRsa9EhXulA4H8n_70L5ZgLII9LK32ytk6socF6sumSPYld0zAA6o6MzG9oVafLJVa70dgmoMnJvTStkvWOhZEyF6COAh-6XUECq4c-DL0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbhEaWmZW-ofzYz5KaKj-NrdGoxpIhnh2HMo0FD-iFDFnsCuW5KO0zOhuwNEcMX4PH-sXPfbQj02hbzfOBUU19GSlFWDTjNpVQLwFqf7b4I7HdKHmdpfN7Arbf5mAo22At5_lhTun7y-TIT2X2u5A8TOVbmXshBdlzDLC7G3cfv7o7C_zZVtPyemDR9t7kGtmq8EfnUcVUMvYqFiof-vVg39LLj5vR-yDqaWih_aBFzrlMNYMIcLT13vJXWbVKtNs5tZZAXgWI7wnE5JzzcnxsyJUeWtQuRcydMzh3rsSEzGR-iVjyjzxEuteUkqH1MLA0OOq5X6Leqldgf_cRPCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=k6DHEylG2vzO8-7pSby_DmAn6VQKjR71xU-FWPmxUHwE75L_3S9TLQ5njK3TCPIFNqxhTUzBmcajhMqfx91lvKAf5sZkYaF7KZn20BObyo7ucFzAao-eq6VowYMEuPPVr4-_tWMbSge9PrWNp-Ra4qgHTBbySXUZ6rTGNosM_Gbd65Uufv8AFFH6kYjdlxL59Nvb1DzCMK7jQXa_T2mBRT6zlbDEzpSdqC2q1NMH891S5l8MnErBbikD_UWHDDtBvgIaOrL8vsW-C_b-Dnj8A3DOUHrWwCJYSqwXqcRjMTuUJT00yWT-mNKUNcqBSqBL8n4c9Vsn5GgTwmTreBHGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=k6DHEylG2vzO8-7pSby_DmAn6VQKjR71xU-FWPmxUHwE75L_3S9TLQ5njK3TCPIFNqxhTUzBmcajhMqfx91lvKAf5sZkYaF7KZn20BObyo7ucFzAao-eq6VowYMEuPPVr4-_tWMbSge9PrWNp-Ra4qgHTBbySXUZ6rTGNosM_Gbd65Uufv8AFFH6kYjdlxL59Nvb1DzCMK7jQXa_T2mBRT6zlbDEzpSdqC2q1NMH891S5l8MnErBbikD_UWHDDtBvgIaOrL8vsW-C_b-Dnj8A3DOUHrWwCJYSqwXqcRjMTuUJT00yWT-mNKUNcqBSqBL8n4c9Vsn5GgTwmTreBHGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=rbVLuOcOQnynUoViy_XlO8CAunqbNRon7cRaVCKW4QGdY6-QbqEsrbXcI06gHwwI1w6P2Vvfq4o7oeI95xKRCicgmD0JjAQVLiJYLrvSrAXlhB0wky2-YD3Rwi_EQj9O-DcbDp1F4X9D55V4sJsr8axixI4SA7yU59i-92BIHn9_50HyEX8fYqxUUOCMPjthmvpswU7LvsYd8HZfwMGY3XJjzjeXnjpbCd9Fx_SrdMy_xH_oNd2uiB2UPiXb0Q5X54_K347wQQ0FGu5XeSu_np1pkg_M4_ePoLS-84W19YibnxW-foBrwQ6HFT_motsqnCP6NoPirxxPmzOeD7agfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=rbVLuOcOQnynUoViy_XlO8CAunqbNRon7cRaVCKW4QGdY6-QbqEsrbXcI06gHwwI1w6P2Vvfq4o7oeI95xKRCicgmD0JjAQVLiJYLrvSrAXlhB0wky2-YD3Rwi_EQj9O-DcbDp1F4X9D55V4sJsr8axixI4SA7yU59i-92BIHn9_50HyEX8fYqxUUOCMPjthmvpswU7LvsYd8HZfwMGY3XJjzjeXnjpbCd9Fx_SrdMy_xH_oNd2uiB2UPiXb0Q5X54_K347wQQ0FGu5XeSu_np1pkg_M4_ePoLS-84W19YibnxW-foBrwQ6HFT_motsqnCP6NoPirxxPmzOeD7agfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlbYnyHt3CTpgRTJvJ06c_MEIyJpNi5VMtzh64_BE5rVqEwnZz6dhEE14dCNMiPAbWv0ZRTV_w14pwFDrOTOrkVtmJFyW2Hcnmpi8aGKOYFURtvv0Tq6_PVUcGf6Xa-LzesUEJqUBRrRaozkGj115PZtY17JorBlpIgdY5ak91bGKxJ_qitotJaN5AkNEc9QOq-cTi1-as3g184z4WhWmWrkzP4UgsQ6Y8I2ouSLhqAdnXNEva2aZE2amZwUTMM97CybWGDt9eLFdeGJgxd6RGGeZbbflX91AOy3o-mbrmed923b0yhunLNomi3bqZ_c4_GZdDUSAXwArxmTcTjjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e80MKZKeHCORRbBTXi4y1N73dBCdYmNx9TUlCPK0i7f98slBj0Nh90Nf7kTWO_5flesd8jpAPNRxNg2zQpPvCdCW9KuI3WcVL2S3JxskSHa973P9gD0Kyz8a8bzk6WkUMxMKq_U6Ji8M85AeZmpHlvxTJlq27fplRpiqAnhrmnTmGz4ndj22faNwDn8a8QGzd2eYIlzeZFXHy1qvrsDFQo67HWA3Hnhp9DU96X-yrj6kcOS4PQ6ZVKDUUipZYvbh60BfQm4zlRchYHipzp0pzBi4hDL2ZK-7PhF8Ng007c6z1TllM5IwFRKaB6k4lxnk6RfFpdN9co8LkFzO_RqzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdBS1kD3MVYbJ8sUIGVq2vs7ZxImy6d-Ggi-iYzvIbAEXMKQt00MA-LJCNjSEs8sn7nkcZe-Vgh0q2Juo6lAzaLKb50_JPvopjesio0nhVIgbPpZDRIJpe9HkzyuibVtsTs4377uUshapyGNlm_JlVYqDiH8Ds8KemmnhsUCGCzm58h_Gyey5cmhpTOzzs_Buoh7jhcdSY5JyBd-r_nP-bD4_8Ab3rGhcCVmWtODN0rw3ur2Lw9zBFlgCR2vopBOm2kUJtx4txFm6yOYjxleqIMjvYYTSXsTAJz3lktaxQg8T29R-91-6Eb9uuuFOfT1oszNRU1mvn99Kk0dBvGf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=PpKlhTcMx3HHzZo21VOHS4DIMlRZVPWc9cLrC7nss1jR9t798MGIfrOFrv4T_ckXCdCTzdKwqbsVLWMgpDrc3S4aAY98fNbMvQxKKx3a9SBe5CSwhizVPnJgBovo0wzYXp_EWN2Ozsk0gklnBKsVDDmYIgORvnjPDWbbO6WSdtj2dg99X5_Tz1Jexn2njIiVWadVQ2ys9Xjln4JK4dtO-W1Y5Gmy_uxpMDd5NUPpRjWHWSyfywdC18nvhYZITHsLjGcnEbtVFzOZqqj7DstZuwEb5WvkFkIzywKjmOgesH2QW_SBkmXP0v-n6WYDkVAwnzOyuUjS_fWWT5IX6IFdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=PpKlhTcMx3HHzZo21VOHS4DIMlRZVPWc9cLrC7nss1jR9t798MGIfrOFrv4T_ckXCdCTzdKwqbsVLWMgpDrc3S4aAY98fNbMvQxKKx3a9SBe5CSwhizVPnJgBovo0wzYXp_EWN2Ozsk0gklnBKsVDDmYIgORvnjPDWbbO6WSdtj2dg99X5_Tz1Jexn2njIiVWadVQ2ys9Xjln4JK4dtO-W1Y5Gmy_uxpMDd5NUPpRjWHWSyfywdC18nvhYZITHsLjGcnEbtVFzOZqqj7DstZuwEb5WvkFkIzywKjmOgesH2QW_SBkmXP0v-n6WYDkVAwnzOyuUjS_fWWT5IX6IFdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeOLk4h7z1dudYB3MhZlkenZEwVPqH1I1aJBO5E4iK8zyPm_Y__clpZkyncpVRW_-s9SXDVaIEuOFsyTraqX9b6nYSxaax3gudsmy9lkQUcZPA5ncxwi8lYHrftHUhEQqDYkNBBPeW490gckIaWELvktav_NDOR9GIfjOH8mSiq5Ywnv8SHgLSZPgYuDRyA4ZzGXdjKH0afRepbTDUrDzJ4PbVOQ1XPXfMzUoO86cJAA2oLxCuIi-umD4yy2bsA75ULYX6KsdFxZrG2o1wlWyBb4tGoj2hflrg1IV59p_srWqlQ2Wp3Qcnpt9hFkavGc65lYOxbYsZ40k1ZjdxLUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=rCT28asWR5Ef2N16QJnO8GRbUFEE4NOZKkdDUtwY_yXFW-x-VlP0i-xsYYhip3TboXzBkyD0g7WDPsHNegc_VigDB_ZhZb152Gs-XEa0ZFvYtony9plKJHAMXYq2XpsaYuXgjKZ30LrPxxLgqW20J366lQNq4QqMmFZZzZYQFvfOY2Ih-zGZm93T07oLaoMp6kgfdc0v1zUwOaeVsBzffKt_8Byz0EuM7OhoDSmC30ZdSlI_UusTE6PzMbYzZ87LOs8dd6e2s-gfJqGeAjsHKGYwGN0qQvDeq7JVKoH_wtKhWzB8wuzUuH3IP-m0gX4Pd2Q6vq1ZmOkdV40NSBQgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=rCT28asWR5Ef2N16QJnO8GRbUFEE4NOZKkdDUtwY_yXFW-x-VlP0i-xsYYhip3TboXzBkyD0g7WDPsHNegc_VigDB_ZhZb152Gs-XEa0ZFvYtony9plKJHAMXYq2XpsaYuXgjKZ30LrPxxLgqW20J366lQNq4QqMmFZZzZYQFvfOY2Ih-zGZm93T07oLaoMp6kgfdc0v1zUwOaeVsBzffKt_8Byz0EuM7OhoDSmC30ZdSlI_UusTE6PzMbYzZ87LOs8dd6e2s-gfJqGeAjsHKGYwGN0qQvDeq7JVKoH_wtKhWzB8wuzUuH3IP-m0gX4Pd2Q6vq1ZmOkdV40NSBQgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfmTLauXfLXb87VjWY4vhRF7GuTELRdDjOfVt7QQHYsOtAwRRTi_bk6AChQ2inRmnSvF2aJ4DQVkQIA_u2sMScwd1BYLVfkDAWdkE0lhPf_ndx2OQXvKZjuCgPXcAIXkgaM2U4PsEV62XSRgJhDvBZJKh4R2Rkxhfic2iiCAA3udvl-MLz6soW2OtoKmpV1o54MCsFcOBVV0HQ2XlIW4ZW_rDwIS-T_NBY5QiVkuRMY9szG0-91YEMPOBTkAvmxIGuv1DIT10p9dpJlLz_jyDL3_tG7X9X8OfheAwYmbUrzESo9vLLoimijfnNhOeMlbCO04DHxAWkon_v3aEPu0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdmZjo6HgDJLacyS-2oZnyTmkMQRbByp3mJSofm7tmP88Ix4eP_eXj5vjeplcaCPhUnk3B3X6zo7NSWlZFTg2WphUlWii1T0uoSCDJj59uHtoF-wztm0Y8AadZs4GF-PJ2bD5t234LpT40DbcL5dXh7UPydQwglj5zZn-xIwPj22G1ZPlXfqVZJrxwIQJN209TOyVxqPUErM2YMghFqOZ_qHoAAHM2nkz3P_db6M1LL43wHhT2cVjDgtvBF6duPTVjtfOmxdm-QCHqH6w4aTCGDSvzJ4p9v0QXVPtmLcwcQbIAIMMgAx0rpTNlMT1SkYCbNECBbd3vyV8oJPL_huuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1-cr7P8dKS7Kv24UiRm0OEX_iDtImIyenB0Im_r6e6iou5XaXeFAlVSKGdTjr26tctrkwGqhpyYUJDN0ynVSYq4bjlLokkRiaRk_CTCzhcEIF9y_NbfwdlGntMCjjTDY_iTn00QGGWEuQL-Odv9BRHsbcIDcJrfZ5hOpDKxXQwUTTaaOTKy7RJj_m55CM7zLI1KU05ktZIvnnAq02wTdtHAeweOxm0h-5pIqc28D2IEsPTtxA2DTeYUhVB7jLRLtK1jWWFp75XORI0SW6y2ErnFWQRmKhFxCnAKXzmO7Kdv67KGlOmzm1bP1mKYr-lxdxMPvUtE5Vu11DifyOAyag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJzJMeyz_v_79JvIrfWIZwc5VCi49K_omRA5PMRIXRIwYi0a1ujt47FjTb23hGSsKx0b3ui9EpW78t7faHGUbRIgUjSuP__muBQbHeKROsv45w1XymTvLkNHs8xL7SRizC7iH7D1aP9vBt3OZ-vkPytZuDtGFe7U7f8PvF_7M3egnoUBwVJ6TAxuJlP2TcJ0X4TjEM1foQdQODdeXbBwAGt2QNVgz98JURZ7QkT_RmTr2jzR7G9mVcZLqCeTUmAtdUMuTxUGeiL4Bwl8OjQEhpzzJijxgm6c6fGoRDFTQhMNnvVLxyLCn33pcslDVQCWNBbZib1JG1YpdiLTUBx7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3myURtOukuJ1J4-ft8Bvf1gej926JCX04BYa8jCZdDo8ZwfENhwETEOsBfRYWg2PyKROM5gT09wM0uqQPCC25SNWsk1xNpK24Z-HtI7WL4pOkryjrw8sCvVNDb_dqUrI73Fk433wNkvga3NDsPRY63IWlnnSJzxjXYj3gOEYj7u2Pk8ICulHnTgVfhajxb5ZQ3WJm0rtusTqO_8YVAb64K6bW7tTPbQUs1RS__AgYRfVYlsfuLQ2NajpIMZoax8x-WwXo9Luh5hRpfo2i2BNgKKkBfTjOW2PvkblEB8AKNK1ijn3bi8mekto5NURH4L26yAE4JkkDTnn1JRw-ymBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj0PBdl0QX8vuRaRsLS9j40oP0HyoAH2aeUpwhv2oQnHS9mamsK_Cd6AN5EPZ-loQ1KeApYNFeicZqULXZoWokEtF_vQ3Kj2YU9xwqbxefYoeJC1FMfzTDSzCOOn8tl1JaHDSHjTfY94ItcpihpFTMAz8GjPrpZbGGq97viAz7iLod9tJY0j0kBZ79NfvCseuhYXvNFVCb3xzKHaMN0eOJs0ydhFZIQddKJu0T4R8JulY4qOktQOlEKXouKXQS7I48ScdMrGCtYn9ypRM6Wk1M_-J9nOn7FGT8QXCDJHHK5H5EdAUu1EXEw50aYSb3lXHVXwTVn-4wc5vP82rvFL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW_QE5NOYr3FByIULtqqJYvcA9m9ZgOwDwqvAWVvnwMzMb5cxSdDhEAY22HcBe_Is7u6upXRCj-7v6lXZNecWMIqTgqeu6PgSqJNyifDvJkr9W33ycQ3iijv8q-1JDfDJVY_kRAvk5A1h5k5lY-P2xZ-9N3SGYKUBx4oKjUwovipjwFr7hoopEOUY4gUEWgtYNXvlVlZUhYaZ2HMq6RxblWpKLGrkVpNjatvMEhq_NBIQ7d3o7DIdx3SjCiFPwmm7Z25m6FZUjVzOnVdKv25gpx41dQnupSYakRWvfKOf14NzchyPWXVxGMPCZXXrHDCp_OHH-dy8m1xSjPZlxVoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=O1CIAGBFWFhbZueRHUsFgyAUmSXkvJF1E9GXwjq9U8tI89YwJPs9ncVj-KH4-7Cxv4nDvole0OE_u2h-DtIHLtm6ODhzHqs0S-M-GWYl4OJDpxtngpf5UUBkONBiHj0Ing1Uoevrno3g_bnqBDzSvhvC1oBN4GnbHOYa0VugTHe2ApK8u8M5Qcs-HdgZFpeZC2WAczVQn8xnW1wW1wQDH1Y6wNIcCBIeJa0QhhqAHvLrCMywq-B1Mk4nNKBfcqqSNAnJL6xMEk_5rFB0gNGcR2h8PLgMUXGJf85T7X7b6eRkDPOoHn16SCLVidio5YansuvtrBdi_maxSazCDiMK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=O1CIAGBFWFhbZueRHUsFgyAUmSXkvJF1E9GXwjq9U8tI89YwJPs9ncVj-KH4-7Cxv4nDvole0OE_u2h-DtIHLtm6ODhzHqs0S-M-GWYl4OJDpxtngpf5UUBkONBiHj0Ing1Uoevrno3g_bnqBDzSvhvC1oBN4GnbHOYa0VugTHe2ApK8u8M5Qcs-HdgZFpeZC2WAczVQn8xnW1wW1wQDH1Y6wNIcCBIeJa0QhhqAHvLrCMywq-B1Mk4nNKBfcqqSNAnJL6xMEk_5rFB0gNGcR2h8PLgMUXGJf85T7X7b6eRkDPOoHn16SCLVidio5YansuvtrBdi_maxSazCDiMK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhjdrmzIA2Atc-IsFOI8Req1qpbw47arorhaqrHRm5q7W0pBCgyq1tJoK7Qj4seazeJMETIndKGFrRIDazObJ2fmQzRpWU_yvt2fyIaW8uAbx6SN8p3_0zjvxryH0CfFnLDfdkDpcN_1MlABPJGAfObaUC_VxWLZ03_yGiPymPLU3sMgTauDislC6BAezDNqRqlnJB6Q3uX86pMQ5RptxKBGrwcrUKnkG9lAWy_HWRXpRLPStsy5gxcpDcsy3yZOGAT56uQTqiDAFQIywx4cNyPy8qtApJ0fjz_-nJ3vhDlIVgBDpMIp9SvdlbXO3LULs6ewSQ8uYwnjvLcFlu2BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=qyxXo-DboU1hCXkYGyjMMM69_2hd6NSfVJp80A_7Hziyu-9rqNcg7ZOZA3f7wyQnUZdWCDhTsu7XnPeeDJsUN2MEiVqZgLT71UtogVRMl5KUpltx0HjirxwmNt_2xvCVVxhwA6W5HporVvYpU5T2feORJSNhajK-bhFKYuLBZQyxKrzpSBW16s23Fj0sI3uxPgCkvS3-qtVcK6o13KgNHKx9riYede3BqNytGSircdYCfVz-zF1sRRE0CnYUATSyV_8inWzGZGZ9JTeVdb478HSI_rf1k23yJMuf3mGsu7qkUbMB5Lm4YUU14AEvPqYcANr14uDrsngwVZcmO1xGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=qyxXo-DboU1hCXkYGyjMMM69_2hd6NSfVJp80A_7Hziyu-9rqNcg7ZOZA3f7wyQnUZdWCDhTsu7XnPeeDJsUN2MEiVqZgLT71UtogVRMl5KUpltx0HjirxwmNt_2xvCVVxhwA6W5HporVvYpU5T2feORJSNhajK-bhFKYuLBZQyxKrzpSBW16s23Fj0sI3uxPgCkvS3-qtVcK6o13KgNHKx9riYede3BqNytGSircdYCfVz-zF1sRRE0CnYUATSyV_8inWzGZGZ9JTeVdb478HSI_rf1k23yJMuf3mGsu7qkUbMB5Lm4YUU14AEvPqYcANr14uDrsngwVZcmO1xGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Um0__AmTqVShE9cYbgCb06mEMGvLxJnONVBnm4PpTXhWrUqlPn8yzltxRiVrLA2amD80g0zk9-qJhxwv50_0ckyR34EWTZ0jahS8nfbo_rWYCYnA8XqtJc2ptuXzI2WQx1i_MPtv3md-IOeVgmVKIXQD2CAHZADWEWh3D-QKFVKnYfr28jh6-s6ic_AWAgXZsgbcPaltmsUvcxI5p2q-p5RztBcXLUL2ZoMJnSdNwG9jVljLLSWMlTFrJiyejz1gPKa-kD7byxrMj5rV2cU4h7a7mZaNyQ2vgOtC8LHd9EMSQWnRpFHBmBaT1_ZklAUFCtr1jECSY2j7rVuDqEQfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qufXM2HmzQeJ2LVIf9znn7Uask2T3iYesZ1_4scWdle-zFFuzxjhog_B7jnAVHiYEHNc8S2HabDno4P-yhgcNjFAkXNjzgCjNkY8lAS4OA3mnpab0LVVC43skN40UclHApXoRssVenI17LA5z6kTNK6NBKk1bhR4iX2ou-ElWdbo390JTId42XEhvE3hVeBDM9spKh8snbKAayGspCxMnCROBIGxHbCJYd8WhhNTKQ7XifeguMhlPOw-3VYQXkWGMuoIrfluMbe4K1XDe2uPIuHtKgG6Jfkv5zvT9578e4Hhmbzfz4PRa0T5sQ5OYvIl2owic6PPghZlCQNnKYrJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFIx8ueu2kvWUJvNEPGpvVehWQVL2GOtcFzBQMDlCjsBZiv6JRR13h5vurpWZNWQVKpE35uGdKdFEpfe4_eRjHcBSmuDUn2W0qNmSOXOIBWDrg0uEIuQT8tabPZGyyw4cqpaBxud4ASgdAM0ubCk_DV_yHYLmWS4QIgbOwDKuIfTMMnhHABDqmHMj49hl_Za03D2fHKnSqvBTJ5R6czY3AuSaPVjhoyWc368dl8F1Wc4O9NS_yFBjFg4zANBHwlcZdkIAVXxmVzGlqe6PLu7X-T7SmRt4S4nQYd5Ty7udlGA8xZFPTlRW-M5svWt4IlUsCR9RSjte9QVvkz6636u_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTm-DvQTI7dLSdZw6asUehyH6cx28afRTNlQj13WfQg6dMtuEOaCBab4jP_QFS-lXvNX83w5xJG6kxCqQKcrQLFNga_d4PrsEssjhxdb0bb8vOWZSivQAYfQsFUcZVvTT4iLz49x8XumDStX7rP8VRU3NSOC-lvp1Z7kKNLaNvVuRUhpihyUnhlLxzLcZAqqDp2VLPkVt4udTW5fFePzZbnzaD88m9OjDErbiW6zFdw6aCCdordgDrAbftBvSi_-DUhQEVMzTdpXEgJDqFioo_JKLR3Bb162AotZ5joAxioJJbRHppeHz5QPCo-osZLK4wFEaDg-h0Oet8k6O4UY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=SgkCqVnZ-WlptWRGYaw0JxcJE4LUukpRoV64zUysRfGstEzfRXiVwfyFZfm5GM4ACsOl23G6X1u62cWDwJMNmWKZO8AIWjm0j9pUagA7M8Yx5FYWz7ImDVYpKN2ZZGNRT93XSgViKYPPt2zWiM4PEjIpMxL4DkkHhnHCjE_ffCBEabLP5F-gBmG57Qj8ecOFjjnnijCoKm43Fuqtqh33D6Q5gxs-JOeLAe6KdH0maxsY9Ay9L5lSzpDQBdfQfWCY28xxg83sVOSLFLpnfMDG_6a5HACFGkBQGP1uXMu4DTJnkYiY8XdMJRzxOn9QD4XBnGHeN5ij7KvjoZd78Wu4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=SgkCqVnZ-WlptWRGYaw0JxcJE4LUukpRoV64zUysRfGstEzfRXiVwfyFZfm5GM4ACsOl23G6X1u62cWDwJMNmWKZO8AIWjm0j9pUagA7M8Yx5FYWz7ImDVYpKN2ZZGNRT93XSgViKYPPt2zWiM4PEjIpMxL4DkkHhnHCjE_ffCBEabLP5F-gBmG57Qj8ecOFjjnnijCoKm43Fuqtqh33D6Q5gxs-JOeLAe6KdH0maxsY9Ay9L5lSzpDQBdfQfWCY28xxg83sVOSLFLpnfMDG_6a5HACFGkBQGP1uXMu4DTJnkYiY8XdMJRzxOn9QD4XBnGHeN5ij7KvjoZd78Wu4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHILomu5itMq9lyBgfwSJzwzHgtgPHH-dr4p-ZR-Gf15-FYbjICEBe_iGytgzMlE6KES1FMKGMbe6hCVZViCHPcigj_lVinkM5pj1nGbFQYZQQ8mWrYiejFsze3dvp1sAgssnfJQeTPWLcq8K91sG46WiuAjsM2Xt24JYrpRw4Ku8ED1WrtT4HAt5zAAMzDs2vS_zI_J-1PyO87U4Q2KF9050cyGugWywS2ZT4VxgGponFjQ1H9QZ_8KzpAwAI3op1HlC6eqZcHc_RoTeUsB0YXqscFNeYZXwg6yH4_N2BRR_KntBIXzV_sWW8RXF0ili0PSMB2ESgDhaFvFT0UWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5C7feqAObhcgv-sRdEMV8fTxI3gm0EKBIHFDHeNoTenxOddBwKSUdi_l_ENT59EVIbdGCeOMN-UXUgjTptFGEUizJhbaJ8yYcb9Vqm3Qtn_TO4q5yIAOC3MOh7oNg90jgEShp8TOqnHxQlS1fMn_FeRfS2YZIYSACo1uTJ3iEzkr0rNpgpWFYJMcxZ-U5TOr_e_ya-n5BtD3eAIyLYBsM9FQ8x-8qR6VMnozdWytknpdvsEsUKZN2y4icxIyzQmZSh_WUfzWW0dc_Us2wtrgV4kT1XW8SlZPd8wuhjOARiCEJlMO81a-f446J5jywvtNFA3hIDtQpxBXg4BTttsBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJombqAw42IdjXIkrjhqPyJ-bn7WDoN9AEyMgFMm28qBtSR28y9SO2raYo154CKBUezjlNUBcZsZT6PUEYzA9vQkO3-Pdj3l7J25LijVAj_GHDMOVOFQigsu3zvEpx6TmpbkM06tDBhP0DEg-wuBwKaPyn1z4pwCNrkKM_N8PLeh8fmJxYvMnxOdCGGml7tQNoRRp2wcxseHnkiA4vxN7qo6aglI1uInTbVkUrzyHVrDk1HDxbyseYrvbBdneq4eaj0WeBo9UAR0c4o8sanwnCUtSVePNsSyX2ITzk2RJZC3WlsKrebnNOfMAjiRxJ_oNi6G7CyR2Q7WiT3_iiw_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk53MyIp1iuhj6adqE-hxBPDqJuzRLjmUSGogOhV_hGvrKlRfVvR93vnc9FvytBYIj-lOEVPJ3ae0KzCUTxGggWgKC6zbaH1MdW6eu1JZFBhMEojIp69-HTswOp8iYY6-ZQWaL1WanwIR8PvXLVMVDtbJNkpu2j7qRDqAlq8afhFaqWs7opDEACt_JJaD_iZxRpKRLVqlh_A4YG7xJ2yKMQAMkO_Y0hn3GtpuWnkqqBVQJvAOSe7Mf6WMgWF0mPwWz0HTdaj8E8X1rPgyXXYiHTlGuOWI-eq9Z9orToC5pBuRL06mp22--swffRTneiodq_IgTqZF7DIi_kWUl0YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf3w67PPREqsX7CNwIx1GQA-RpTT7vx_y30e7EVgbY4BcSfg2VaA5flOMWwrMpKRNQCgzdSWSx1dEG_hd0jxTaZJHl3Fxlg4mw4VRwqf19BzCoAKLHTjn1wFu3GYsUsvLF9WANQyr_L_TlN6ZwzClmbLJJnkSX0LnEgDokuVJnz5Fs7mwZ0RCMEQGBXSyxXxlwHp3sucs54iXXKBkRrhqLlYGivA4q_cDA-VfFWVXKC121juXLRQTJeC5cSLCrulu7tkdArfa-21h3vWU7OLTtJ24J4ou0aYWuDVe0trf8ZZ2G_1yds0cryGmxfbQ0-TyJVYY1sCCOtPKO1y4RpHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=pTL81diTGmx97HcFQVkeqkdnFBz9OLmWE80KIF02VjVYoBPYPsPC0vzftxsM7e3e0E_2fJZf8tpaw4Rng7_JPPQJ9YpAn22rTHXAyZOSQlE6RMcrJCQEesfyhk0Zu4ApGlrc6Wyk4POC1Jz_QlWzA27ddlzvzWHvs7vcWUHUHfzCqPBU0PkoxiBXvJh8JRnBIZB5wbELgIupLGZ_sNF5k4gJarqjFhmrNwbe-r8GM3GBoSD4AHjuZWKkZ1sNywhFBMGL37ub4ZABhXLI_Ov6OhsXA-LOFtblhOjDt3zLTYX-OuSmnqvBltYDlqnuV03529_CwWq9f-JYznOEYNpE54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=pTL81diTGmx97HcFQVkeqkdnFBz9OLmWE80KIF02VjVYoBPYPsPC0vzftxsM7e3e0E_2fJZf8tpaw4Rng7_JPPQJ9YpAn22rTHXAyZOSQlE6RMcrJCQEesfyhk0Zu4ApGlrc6Wyk4POC1Jz_QlWzA27ddlzvzWHvs7vcWUHUHfzCqPBU0PkoxiBXvJh8JRnBIZB5wbELgIupLGZ_sNF5k4gJarqjFhmrNwbe-r8GM3GBoSD4AHjuZWKkZ1sNywhFBMGL37ub4ZABhXLI_Ov6OhsXA-LOFtblhOjDt3zLTYX-OuSmnqvBltYDlqnuV03529_CwWq9f-JYznOEYNpE54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnV018cm1gF2FeifRZHUM-Q0oC1JSqPhHFbOTdagfC_tAu5A7Ia8nDL4CnPlpTmNPYMoxvpWMK9cCsoDAdHpVyNdE04_vY7MpjjKDX4V4hIqssbcKT3WknUZItaxCgR_lND9iIjxNBTJLPS9QIVRnU4Tl_Sj1F_-vo0mPvstrTGmaxOGALC7KAVQYsS71LkwTxejwNotlSMbr92bS4uYKMtCwrh0aeT8DL78capCrDIygzFGG5mBJKRQ_NPkLn6McnMcMBZClJEN-WtVoOgJMta7XMB4LA3v37m2npTFBm81gCPDpa2zBSUYrFfL7BN_8uBlG3BrN_QsJO76S9w58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdg--yVmN2CoByxG7HNksyfhfyjaiCveVgwIo72F2BNo2YGpeUpGMwyJ8hDKum2bF7vjcUEV5WrMxODqppvNSqdT8V1ftddi4HmvgNIy71syQOSiZOnPSG3z4H8lO0decMqwH8gU3DLepLqWn4qKmujD_lg6LpfNIjdkFzibKh_xazTU23trC-BRECDzqljl66Tx-A0TspUJunuWP0MduiWowvGxS-qaQb48OGCBNPa9otpwveUiq3ANRIo5Dn_getdyvebYvMTtThjNkTdftAnQJxG3cER6LgXUlX-KgAGZPkBKXGW6vMcXXXL7crXwrwv1vVc66tp61TWC02c0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=GTDiCNPFDZUuixsiXOd-aizqUSB_tKXgFnu-WmlSlT8R6o7PQNmlIs94q6lYyraUNybQ8vHKvT4JeM6NcM8Imtj5s-YF_MvcYrHD2vm_7zqWQi1Qq2IlFtnA20olpVVe2k4rwI1AxtqaXwNHMthJzWe-xAS9zM2DUJ4Pfagk0AnldfFO1i-gldCKplqgL-J4OJaBkVNMaXqHLvEn9sm13R-A-Kgz1-fmALcK0_0qC3byf4vGp8YhcyrPIuyOmQK0UoZcBL_OZSX4isCCnlwKe6m87Z4ks0MNZ2_lYUz5o2JSIcR_SVRqkJ5hwY9bICj8m3Cjqv1F2QEwa3KD9nwgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=GTDiCNPFDZUuixsiXOd-aizqUSB_tKXgFnu-WmlSlT8R6o7PQNmlIs94q6lYyraUNybQ8vHKvT4JeM6NcM8Imtj5s-YF_MvcYrHD2vm_7zqWQi1Qq2IlFtnA20olpVVe2k4rwI1AxtqaXwNHMthJzWe-xAS9zM2DUJ4Pfagk0AnldfFO1i-gldCKplqgL-J4OJaBkVNMaXqHLvEn9sm13R-A-Kgz1-fmALcK0_0qC3byf4vGp8YhcyrPIuyOmQK0UoZcBL_OZSX4isCCnlwKe6m87Z4ks0MNZ2_lYUz5o2JSIcR_SVRqkJ5hwY9bICj8m3Cjqv1F2QEwa3KD9nwgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=v6JZTwkLhFLVx0ge5dG_od-R2U-EjxS7bzSbuZWmqw2wf2nG_zpHw5XBgQXk2vQskC1luoz1EW_lbLnsoMsbp0Q5B_dhrwYVdiYQEPolnTAbwjg2bkmvvG99ev2ev62dUicKQdrqVYyQCDw1HTyGxalyXHTJLRJ-zP5vv0k4MSVy4khhYk_GLcsP1Ca4NuXlDLMpH-lHImPdO8vktbGmf66o92NMaRqakXqcx8b1gKbnNv2eC_ELNupW2tFa4dLW8KQUa5Aoz_bOHwxLUr0ykQe14xr2kcd6LFDhnh9POgmea-YZOurhJx4Gch9_nK_UoEZJXoM2VyODolu3wgbqgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=v6JZTwkLhFLVx0ge5dG_od-R2U-EjxS7bzSbuZWmqw2wf2nG_zpHw5XBgQXk2vQskC1luoz1EW_lbLnsoMsbp0Q5B_dhrwYVdiYQEPolnTAbwjg2bkmvvG99ev2ev62dUicKQdrqVYyQCDw1HTyGxalyXHTJLRJ-zP5vv0k4MSVy4khhYk_GLcsP1Ca4NuXlDLMpH-lHImPdO8vktbGmf66o92NMaRqakXqcx8b1gKbnNv2eC_ELNupW2tFa4dLW8KQUa5Aoz_bOHwxLUr0ykQe14xr2kcd6LFDhnh9POgmea-YZOurhJx4Gch9_nK_UoEZJXoM2VyODolu3wgbqgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=fPQXD3ZsFUE9vFpPpbyRqquMB6LQR8zQbZtkkGzWoATnevy-npXazqcVkBCDbILfS_T97Xw2w6XEbmM4I_3cGYnrunoDEDUb6_Wg4vq6GxPcIjM7NdAUFqub4tUUCJ-6o2G_aRVxejFmezVBriPh2EdeMqwZ7bmlMHbNchP1lqid18o_qk8lYblgodcMrW195vwm8Ny82P38rV_z23p6rm1-Wq14IqiNpkkveowHmXtwswvmnCCAilLT-CDTBMwLqYe_lc0fNqf_79UYTEJokyZHeuZTJBEZSHS0ajCO9BfwdFzWz38n4u1vSatlB04uD8Cf3AJzbKLAYbFLO6YPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=fPQXD3ZsFUE9vFpPpbyRqquMB6LQR8zQbZtkkGzWoATnevy-npXazqcVkBCDbILfS_T97Xw2w6XEbmM4I_3cGYnrunoDEDUb6_Wg4vq6GxPcIjM7NdAUFqub4tUUCJ-6o2G_aRVxejFmezVBriPh2EdeMqwZ7bmlMHbNchP1lqid18o_qk8lYblgodcMrW195vwm8Ny82P38rV_z23p6rm1-Wq14IqiNpkkveowHmXtwswvmnCCAilLT-CDTBMwLqYe_lc0fNqf_79UYTEJokyZHeuZTJBEZSHS0ajCO9BfwdFzWz38n4u1vSatlB04uD8Cf3AJzbKLAYbFLO6YPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2X_sFmnncuckdaOn6tO2jqibuSBms3VxdoGpwtGfATWQ7JQOBC-S2na5v0ZkKivfNMbP6xix-XQFqjbXFZcCccr2XDvelvHxNY0snZ-9hc1NkU_40ANYpmDp_Io8HVyoMRxsTo3UKTrJMjp4DwDPmibAD-tG2g-zR5NnjkTBurE_j5AXRLFtQiXv9PH5InWAbsjdaMa6GUZVu96hLlExznFzigEG3gQ4YAhbaB8v7WVou_2up9xzsswVmSMmHuAnz7pEjroTIwGF2kYuF2bwS5d0UQcImrsnGMrN9K-pZdBE62z-OrhBAhrg2Qwc_ZdFGTvAHqMTOUXqVh2bUEVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=abfoAnQQOt_6S8usUZ33TB69aYrce12E6iTxPKWKWzB2ImVb4DNxAiH7P97vzsK9bIoDl7SHvCa5ePR9PrNuQSIIJ19H9voV72cQBJagUSnL12iG5K16Z1jUWft_pKPvLSxP4SQeg78gLdZ_TUZ1juM_Nhe9rzTSYs8eyqmTsgjjujI5aLnSCHJrWJdgMabtGNtAmtSyQB4Btq96HkOTfq4e84wn5i2gxaAfudn3Y_8n-ZmNn-Xob1ua2FPuWPDAQSWhlprO5Mu0VucLMUEb1uKNPZww77FDPCd5o_AW18vq3YgdW43jkR1j26fAPHS_DU-UiirdfkvgTaxHM2w8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=abfoAnQQOt_6S8usUZ33TB69aYrce12E6iTxPKWKWzB2ImVb4DNxAiH7P97vzsK9bIoDl7SHvCa5ePR9PrNuQSIIJ19H9voV72cQBJagUSnL12iG5K16Z1jUWft_pKPvLSxP4SQeg78gLdZ_TUZ1juM_Nhe9rzTSYs8eyqmTsgjjujI5aLnSCHJrWJdgMabtGNtAmtSyQB4Btq96HkOTfq4e84wn5i2gxaAfudn3Y_8n-ZmNn-Xob1ua2FPuWPDAQSWhlprO5Mu0VucLMUEb1uKNPZww77FDPCd5o_AW18vq3YgdW43jkR1j26fAPHS_DU-UiirdfkvgTaxHM2w8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=SpcsToVU15Jr5yGQ0iTLs8b9lPvEqhiZBaEXPlZ3YpHIxBsgGi--fqXBGfBIhKQ_--FMV5X-WzGGAH-H8kGsQ6ZUugyDdab_IVi2TEWDV9tFYm-OWNc3Oo8eaHzf_I3TINxdG-x1Ag-b092X3w978tH6-Q8EMEdpaRbUr7l1bcbN9cFsMJwhWU3HIda5TWwXxj-otX7PpzBSonqVhA_N4zhXYsXN3h6Zrfo40betcDqDhpkpibXcRKqsslQ6rOR8t6Nn3MffU7443K5jmiy58cyn2CS2Bve1eWh_y_45syigY3sA-NdkKJ9irejq_juyCGrXYPEnjiErEvR4rKk5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=SpcsToVU15Jr5yGQ0iTLs8b9lPvEqhiZBaEXPlZ3YpHIxBsgGi--fqXBGfBIhKQ_--FMV5X-WzGGAH-H8kGsQ6ZUugyDdab_IVi2TEWDV9tFYm-OWNc3Oo8eaHzf_I3TINxdG-x1Ag-b092X3w978tH6-Q8EMEdpaRbUr7l1bcbN9cFsMJwhWU3HIda5TWwXxj-otX7PpzBSonqVhA_N4zhXYsXN3h6Zrfo40betcDqDhpkpibXcRKqsslQ6rOR8t6Nn3MffU7443K5jmiy58cyn2CS2Bve1eWh_y_45syigY3sA-NdkKJ9irejq_juyCGrXYPEnjiErEvR4rKk5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fETtdXnz8vl8ZozLgZOIpd2KUJ44v5KO41IXGVPbTO8G4EqbXprLxVnrelUxU1fGEwubS44uAnkCs3EVbyK4pfcNp1gjr1cxGWklGbKRTqpleF_Wpk_l7ZME4mEYuDnaV07epZBSYA6C8DAkQdEzxkkleQb0skaeIUEggXspFgn6cGU1BDF1k82HUBiwvGNLpLinKw4SobKnQSO9-poEcSW5ty1kHE8fwzwDBmmh_IJOqFO0DUQqcpeNoqQe0sSHjCJ05cCB7zIP2Gl9pDqryPg2piLBCaDPprhXakIgyhDQjkv6ZliXzwU4-srPV_48kg9HvH0uX9q9wcRUOFd_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=WlXvDIf2aFAlfhfJVIS7mtiFy2EE5nhIuXvcAqViYnb0cL4fFS1-RoDwl3bckoLo_8UP3IWxPZ3zwrwVFPMEr0W46ZOnezNxTkely46TDYSM0gCIXJXAq5-bWLVMi579xOtPKd6xGuRtX_Kx9Sru2xUEwRMx2zh4zi6u9S4T9NISlne-_evkRIWTgISI4Ka7WIsUjFYBhnPVxmxCDOAHHiq56nviCT1y53o4VtWCAgItSpZvoGU1rTt5EQOkk1oL5sxBvFvqvp2xHePltrWpLEAGQGKuhJSPfxtcitRjq0nulljCp70jUSH8EVfhv5iGyeaPFLPI7VefYdJwxvr5xRXid1fti8hTbIDpIGmppRt4vZxvMB8g0QpXRPW32Jg23XBXCEytHb3g5UVDUedr3lz6VeDBjBYjAn8s-AVeZIrOMvPbOVk4m9MXByvdBmUbvFa2FCDkeRcJ_4R0y5QEjVukytgGZZ7ax9kHtJBQgb8K-DMf4P5KtV8xEj8c5sxKratfNESHcE-39OcgNMRCmTjQXRs2qF1PFolWJ_6t04fo_7ni85jbxDvdY8xbB3oizv8pLkKyVxyZukkVOrm_UITTOsAZhu-ECGfP2wm34ExXQA8AWQBUbHRX68S3-lutn8Gjdx2-r80zH6XNoxbCkbxxCUcrgclt7xFP4qtBlKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=WlXvDIf2aFAlfhfJVIS7mtiFy2EE5nhIuXvcAqViYnb0cL4fFS1-RoDwl3bckoLo_8UP3IWxPZ3zwrwVFPMEr0W46ZOnezNxTkely46TDYSM0gCIXJXAq5-bWLVMi579xOtPKd6xGuRtX_Kx9Sru2xUEwRMx2zh4zi6u9S4T9NISlne-_evkRIWTgISI4Ka7WIsUjFYBhnPVxmxCDOAHHiq56nviCT1y53o4VtWCAgItSpZvoGU1rTt5EQOkk1oL5sxBvFvqvp2xHePltrWpLEAGQGKuhJSPfxtcitRjq0nulljCp70jUSH8EVfhv5iGyeaPFLPI7VefYdJwxvr5xRXid1fti8hTbIDpIGmppRt4vZxvMB8g0QpXRPW32Jg23XBXCEytHb3g5UVDUedr3lz6VeDBjBYjAn8s-AVeZIrOMvPbOVk4m9MXByvdBmUbvFa2FCDkeRcJ_4R0y5QEjVukytgGZZ7ax9kHtJBQgb8K-DMf4P5KtV8xEj8c5sxKratfNESHcE-39OcgNMRCmTjQXRs2qF1PFolWJ_6t04fo_7ni85jbxDvdY8xbB3oizv8pLkKyVxyZukkVOrm_UITTOsAZhu-ECGfP2wm34ExXQA8AWQBUbHRX68S3-lutn8Gjdx2-r80zH6XNoxbCkbxxCUcrgclt7xFP4qtBlKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkTDsVks0QUO4P0tuJi6qLlOIedDJaKUC_4GXTQu0kOarg3OtiY1xlrpwoRB6IpmIAHmJ1rbkXTJUSGPJ1wy1DO4CH1lEAz-aJnuyhEcND4zNafkp3821d_rwObFhtX9o6wowhRXVz8n16_XMjCJHsHeIbyueFz8J9UzQ69VkHJP0HlHD-h1owqyX8NfLLkgfqaWnKDgzcMCZeCY6JGESNLRfBrQef2q3QhoFqhyfyCHv30el_JPMvq3zuDEnRB7ZS89ADV6BnCuY_tm6JY9_9tVljTZuhUNe9dknP4o2cZH0FGFVuoNxL6SoyoI7Wql0niwKX98kuWGZqni9xnNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ047JJIpWUl-6cC35eSLmLl1kRzB2AUUjw4Mbv3tE5jjxpUuxQ0Wo6_DAMbKW3cJQsUVx030HmIExlYVqAoY0QDUVQxX7rum3H5wdqbjHTao9qthWUJlUROIvN9AW9tcub1k4k6V_dTreEtMpSSx1yKCZfOtxrd_ux-b621wZsT6MyqV8T3RsjHqRb4a721pbuKZbRqVYTtqgNGVqGggc_ZiMYEZAc6evJJJdpCbkFQ3zICUsp5NDoSE8u1f4HwQRGxiiwDyJL74EyrSjegYv6EMyr8eln10mC_94Rh_8wywP128MLGq53fmhbJzfAXQh0xK07H6RZUEHZp4xJ6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

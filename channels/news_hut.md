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
<img src="https://cdn4.telesco.pe/file/GqPjsC8fnTI1h9DSArFKyY88nYzUyyqvjWsQ9SxBq437Fzqp6aUmPkOzzCCvCjBeI9U-uXU46NGm5xnS74JDk9LkePyhw7gqtSqVaQUyilEEjGwGvnwlM76e6qplViV5nMBE-raX6lXOYOamZqtTgQbb90ofL95WAgHHk8SKvE0D-2VxYbHqWln6CXD-YFQl9kqn318MwjgNS-EqBsXp0PCivfHOEZF7Eay7rTI_77WzYe7_Z4r0oCop7Ewxw20CGSCH3GSUe0x4uXQts37EeIFxRWEc-HQcPgaK9I7K1hIcS5f_WczzseyajQklgbf5zvz1s9kjF3JwrlzTECDrXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcooEuKYzXSrS5sDVJzabcHgqG0EcdBMB-Y_JCg3C8Krzl4HvTlej8Ah9ieEJa-8oYkYj2cwe9VS_IaGO49-r-nz4K81ZWeyNxxzRsI4bGKZ2vSTdmKzKJHBv_FQzj7JjmEThHj4B8z18N_2fR6mQwUKRmorjZIEKs7qPAW9711LLLYqYM5jFfVHOMXzYF8_E0pUF0Evdl8OC9Xh0G2s4Fwpbkt0woRxE_PCNN1oVQ7atZbvwSzWrp8KfVTlqKPOP6VqiZ3gPU5vV7pzGSrFdp5cy2K8AE-xC1BWg6DObrlrBt5X9UtPF1vrGQyGAf_Mxw_U_ZPX4nrEufemfFlhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR3otybLs2aRRcLN4mW4OkqeTKkxlqjQIUkEX9Wppe6FrF1XrFFepfsgZ0p6YWjrHOC8MLaM3SStfuqvSoRPDgUjWPl5BBmtgZFvzREdI1oG2ouBPBme07EIvxJ5CZQfWPEt-EhN44sVZj4VW2F2AXV94glHalycAk0SUClFD25PNXRFUFgYDkpKqKPItnXNMwiUY2AP9_7Czr0AlxPrJpn_rM8LdRVZB-boivAty_yQ4ZAcrre6vSHfEQq6d7tL8oN0PfBc-TSF3U0e5PpQwSZp54FN6wlqRSgzNr-uT-sbqPms6EzoCRUG6Qp-H98VXbei18GrI1KiWfvlWaLrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu3hUBLJ7-enozJzDojnB_0_o7SdXlX_oD9SvTu5lOjXBsse-b9fJnH2EB0kj5QDuQ7V2jrw7K91GU1KCjfu5q7DHgffLbrMgcS3aHTDbqm9FZlIU6dt0sbtWip_0NYlTOsEjo2tsYd1Vw1sPQzZIhIQBrSM2Fem7E4E8TwAUTfNBw9wI5vMQzcdDSqKh91CCUWb25F2eUqxFdK588luEb96K1mSmVUI8NKNIVFCYd5MU4saGRrRpy4HSaIvt3u6xb5-GlMaYDtH5U81dDpDzDcChUxlD7fliBfpfAvZdlzD8IStE-tL-bokFfRnqkYaNKp4cbBnbOthvzN6mQqlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdEhpHlpzfRLUmIiiACtbk4VruEym-8yMhJUI3ws_KrtOOVah5v4yncrkoT24qXAJod9AQUAmz9oT6WdH9esAUF8j2JF50fuBunxsyanTppbajCWi131vuUkREO7GwwADzYU3gGFV2t7JI-IddVi4oaxIxTVAPk4kAxGOJuWYWnczK4_PX6its-vvHYrM8UZyMELaghydCLvkPrS3vL1Ypd9IQuWSws-EPykhhlpi2CxTyDpPmhOdR7OOoGgc8C-ydC-rc0ywcgaGxZbQIMApbxi9JfJS_B1gJhfgTaQW7F8rV6HIYkgabftrtYEAc3AcEUWbUWnkqA_LkXLEIin_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmKh7nnoiq_slPtrr3Fdqxci7VwlvKthqGrG1ZbdRd6qs6NtVUYN15HzKPOoKOKlvsDSxn142MSm85U1UNCGIoQhzmyF7VTVp6Dft_h21YiCRtUfTUuWLLt27yTK2tCFt6VwDcfXXV8gfu799HSFdOWE0xmqzuAB_Fy7SDXEkqN41qdy-7CpKeSaU6k8kXJN4tdKiYJeiz0unUk7SsfsjXQMqI6NagWjLXpxpRpTqd2RYyLA8h0jO7vqr72eurz6c8tuscLm72b4E917uWuIkSUNlBBg5t8PB8TWRlOMQifF4vGk87lq3ltsHq57-eanyEBotUxDn3ulgZtlnFwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1QuHE63OsTASea9aKnkJrAOr19Vdk-1EaIUgiF2znWyfGvLy_Jv5LRSfirXLejJqznD4kn7yEUeZ2evYDdfFVaabshRAaFLbyEfHSKJzkIxYCVKRuqPxSLX4gEdNdLVyZIMFUzvaXYN0YXRxTMoBhbikLIG_oFZ2-8ZTeb1tKwA98TauuW8rrzmvUVNPcX2JS9F4g1ZAJo-9R_aHeW1uD52WJ39aMmbwArLT9Fb9RErFtnRJ3zHgKHe6QHFp-Ku7BozMF63jhPdAIuSRfTz_jnTawqyGtCSGUgCMWfDarGVz8rz_MUrHirI2BbM2E1e_aGMThqF-tJorOuSWFdBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1q71CYhLnSDuybInhRzU9CHxv5rDxKGw4PYGH2mFPKHLV5wsQK4v4VNYgs16WLLncdYVmhkIrDIWPhverll-2TS401dKAZzPMG1JETWd9Cd_ERR2PElraqY_TM4cZNrH8u1zDwyC1hjQ-PRvpqLCYQnuZEHcqfbLS-V3paWA_V4LsOB-noLR47M0T0Scl2lL8pdw0wLl1kf8SnUMvzk5JQ9qB73fdxdEb3i8X_6T4KT0qMTLGJFTLIR5VNVZSXxC7pFn9tZcpvgndkxAUVW8fGN8aRAlnOX5FUZAg04nAfI0xtEjDsPXBth67rUnghaMly9rOTr6BpzXrEoiYv3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=L2B2szhTcCH1f4czLPQw1zZ3mz3PrQ1kDv2sFBz5ObqTl3O1PDBiHuWZorvs0BKshpwmyD9OHbd4AcL5IOEwD7JILPBQyoJxXm8zuKSeRM0Cr8Imyh7AZ954KS9igBMyRVc7zaE-tD5o06YJH3QxqGHqE5aRn0HzEKv4wbyOOBxnT93_a4hRgI_dpF0Wo1w7jEgI4-vkVRLXGx-r0dHLlLfEFGwZCX3fUOCQRke_juwInq7h7XrjXbOKuC8dAGTryhHSawPRGWkTX0P_mP_07m4D09pLl5QT0YaVhnGL11qe3XGhsUegRj73APKGvDnsxygHHlxildaoOaxp6Jelng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=L2B2szhTcCH1f4czLPQw1zZ3mz3PrQ1kDv2sFBz5ObqTl3O1PDBiHuWZorvs0BKshpwmyD9OHbd4AcL5IOEwD7JILPBQyoJxXm8zuKSeRM0Cr8Imyh7AZ954KS9igBMyRVc7zaE-tD5o06YJH3QxqGHqE5aRn0HzEKv4wbyOOBxnT93_a4hRgI_dpF0Wo1w7jEgI4-vkVRLXGx-r0dHLlLfEFGwZCX3fUOCQRke_juwInq7h7XrjXbOKuC8dAGTryhHSawPRGWkTX0P_mP_07m4D09pLl5QT0YaVhnGL11qe3XGhsUegRj73APKGvDnsxygHHlxildaoOaxp6Jelng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=IwN6Wlxw2Ax-lxcTEgYl-YZJPbfyU4p1LgTZTCozLnMv7NOIfC9amGHVJ31o5MR793fMkzJav3Wth7KwyFoKswQM7f1pvvpZGto7M6ClWJ9V-c0HByyzFI6xUroFyO1RgXmTqZFL3QERO2eT0z1ypRlfv-tHiSI4s32bMKDPi18wgEH47ekZUZQFew9xuxSTYUdSwbJdUiYXckP5MRD7HbbH0u3i68bSbAiCJBFtUmZCPLQwgqmZyb9PDrQcJwK2PgFeKtmD6Y73M_gglPCa9QSd1KxUhtnyKgaTjqexES4q0EVwGegW16V05zKd6TYeFkqi2dCmIJefu9zeZ0EgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=IwN6Wlxw2Ax-lxcTEgYl-YZJPbfyU4p1LgTZTCozLnMv7NOIfC9amGHVJ31o5MR793fMkzJav3Wth7KwyFoKswQM7f1pvvpZGto7M6ClWJ9V-c0HByyzFI6xUroFyO1RgXmTqZFL3QERO2eT0z1ypRlfv-tHiSI4s32bMKDPi18wgEH47ekZUZQFew9xuxSTYUdSwbJdUiYXckP5MRD7HbbH0u3i68bSbAiCJBFtUmZCPLQwgqmZyb9PDrQcJwK2PgFeKtmD6Y73M_gglPCa9QSd1KxUhtnyKgaTjqexES4q0EVwGegW16V05zKd6TYeFkqi2dCmIJefu9zeZ0EgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWXk1lib8oZ5Cz6EVtYeLkXT9wmKpgfFYEywgirpXr5LFd5XIOj_CHROQvIG65i15ahlyDSJysv0pVl2B9V2RnVpcBa97qf5XvSDk_VHp8HHGlco1K6KF7M-0wkMuJW9kO-3nq1Oq6qPOMtWW6jLEE-AXv7vAHHMYPVWVb9fBs0QjuxsRQjx2WtWalNpg0dBZz9E0SsoO-6NM-D3MBe5lwrudEqE-NXNrZ9WSsrgWMho71vI62ZNKRvhEggISI5oFLMRf5FOaJPghlGFQUkJSy1iGx6SYJeWZwHpR_VVplkq0ih-Jec3R3MTskur-8MiwNintv-IKCgdq3lzCq7aAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7Axdg5WXg_0t1tisDDyTbhLcxNmSQ_c5jsb6kmCvuOwYP2VdIhklOf2TtjXe_K8cwLO6i8k2Jt2XI9MxzIMfig7Lbe9aQks9OioccrAjQeqzS3bosLlkyTMeO4VB0r6p7C4feEP2jDJYl4Qm5o5TMGcOKi10EQREPFtYpDULq9-J_wih_f2OCcst8A9_JcNkzaWgrKcuT6s5r_uqYTmcK8uYz2PgUncfZJ7QDf3RHa7Jkm0nHdfFG9eEPV_WC15FYzbRhtcnYx-ggMxce07GqGibl12HPOczGjv2qpAhmlHypQ-1Jeby-_rjXZ6ZrFccJFNO_ARm88DwC5Nkxajxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCrg5M32y3c91-li-jdssAd12KAKcLfRUELIelk4cJozSQwaeoutRHRJ_Cm1I3I__ccu3NqiYrR4IfOK7QImao3yBXy6isgQ24PchuHnwOecwZ82W6j6NNbuirjLThajUsSoO7lrFuvq2ebn4SpRU83hFOJyavhERBZKV_9LtoXf7GLJOIo29Zikz22P5JXrjSmwPJxVkqYYz9XU4AtGRsz5nU0CrfW7Fq65wQrIJD7lHxFoLI8Bzk8S0swQJaJGHR9UnwkACj_WuVxPwXFJYJjUDnFyF3W-DTibqYmuUkqZMQSl9GzyO0LvnEgJG797usdfsKaG8SdMAW1OxXiA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=WnbQ6SFhmCf_fdh3LMinACJCE5qFrVID7dWlGfTok1sUI_zxeaD6mbrOm1yv8wmyW2SyO5xnlpe16u64XtE7xp2KyVpQ6hHEOyr4ycBqaNKIYWjrIhl8_bSAK6yPIo0q7ZjDiFoMqwzgrCeCBYr9YgIpJflAwT85-wD1FGkTvU7_aExK2FlRhF12Zyr9RsJFDic2GwyFepAYvCXiDjE1c6Hfb77iJj2wKyvuyBF5NWnhme81mpn0h9MhxMw6Ou5Ei10UkSnEDSjB9qAIutmNUWkQ0qvTv7XSNV7gu2yHh9uyNTmVAQ5E_NP3_kxjkBt1U-GFk_B8k4xNjIGrH2FoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=WnbQ6SFhmCf_fdh3LMinACJCE5qFrVID7dWlGfTok1sUI_zxeaD6mbrOm1yv8wmyW2SyO5xnlpe16u64XtE7xp2KyVpQ6hHEOyr4ycBqaNKIYWjrIhl8_bSAK6yPIo0q7ZjDiFoMqwzgrCeCBYr9YgIpJflAwT85-wD1FGkTvU7_aExK2FlRhF12Zyr9RsJFDic2GwyFepAYvCXiDjE1c6Hfb77iJj2wKyvuyBF5NWnhme81mpn0h9MhxMw6Ou5Ei10UkSnEDSjB9qAIutmNUWkQ0qvTv7XSNV7gu2yHh9uyNTmVAQ5E_NP3_kxjkBt1U-GFk_B8k4xNjIGrH2FoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPSmmcgo1SB4YCXZjWvsuG4XnmJo5AlFJVo_3leC_kLyOv5CQpfmztSq8kBy6zmAodxeITvxGTtsLlmzouwF2AYRgTKSA1A1x9Gi3dpPFoZaweAcTfoy__CqryWOB2FdGkwVGAeTIbG_WAKhyfCp959ZN74BRNiWb0pem35rlZnu0LJAYTd6ZqrDoljD9Ov_3QKC2DOPod3sfAExeYwzQCji6TjN6WISwmUB0Oxq4MT9tXhjrsJFGnpV16BrvOi2fnRhD0pFXZJzWY7De62t35r_HjBam2-uAcD3m_nmKehxnQ_9cA3N4TjuzQ7ChzyYYHQs8CXGMTmvBcb5WBRUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJcFaeVJGK4au7RzfPIOyTmyS9jNLNZfQeSxr4gcw-Rh5Ihu1tPWSQuUwUCMP74TZgbK9o0fXPHb7WFOopsBtpAPTwYE61jyfgwNQydCYqbUJpwa2J6xjPTz8Xf2xmvh83q_sVivBs-jLO9YN8PQE8u99-Ndm8a-G3vH7Jz65CNiiimwgH1vnTl_qurR4XCWZBALfOGwkS-uNDIvOM79fiGLm0alOZL8eECmBPMdx7DzA7MJpH5rgHfj6vqi7f2UeWzJHB8kj94zQucBPgMmUSJJKtAkHbUCkgz1XHHG3tyIikHR-DjxXn3UPLYdncaXdVGz61_Hpr_EVeOHVr6AEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=ed2s7MM_EE4J30tFsA495fMjl6wwSyT3YXrBIINXUjTgZGZgYrZruZKAPxoL6qhgOr4HNqdtamB9Q4Gx0TqAtOlgv4VR8i-4wQYuM9NTchl-7UKsVqYvD8QkfOuSkc1z1jU44j1Qlzo5qJdu0vcFyDf7YuEDLX-u42hj1NpibRTeWJsmqXDb2lHmJEejqTnTUmCFHW2k9e5YzHwvECY7Vyij-xhs_WjfdT8gmKpUf5TIZdo7oWc-G9fto3EOrJ5_36sedgDSelsEUWGpYCdw-Y-AT4wBfNFIhGpO3WDrBl63323uIB5Lyv2eFnUazeRv4KPLOMN-TuP7dSjBGAdQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=ed2s7MM_EE4J30tFsA495fMjl6wwSyT3YXrBIINXUjTgZGZgYrZruZKAPxoL6qhgOr4HNqdtamB9Q4Gx0TqAtOlgv4VR8i-4wQYuM9NTchl-7UKsVqYvD8QkfOuSkc1z1jU44j1Qlzo5qJdu0vcFyDf7YuEDLX-u42hj1NpibRTeWJsmqXDb2lHmJEejqTnTUmCFHW2k9e5YzHwvECY7Vyij-xhs_WjfdT8gmKpUf5TIZdo7oWc-G9fto3EOrJ5_36sedgDSelsEUWGpYCdw-Y-AT4wBfNFIhGpO3WDrBl63323uIB5Lyv2eFnUazeRv4KPLOMN-TuP7dSjBGAdQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=THQr_blam8-lgcnVPpc9pAl3Uo2qb4cRYHBq0mvqc9-7wVR3lfFgDz5l9Ph5zzocuDlhEEWUSFCXHK1trglt9T47fL9M7g21ssNf_9FJTnnTv4Q0sYNnOzS1S6T9-uGcgjmTpCdoUxYAb7an0EyskAvsEQf5P0m-q1-mH8Hr5Sls9KdoVLocQFHnahB4JMmWBNL1Tw07bcoJqDvPLsaOsFMg82TpFTdGM8yAVAHo2MLddyowpbgLatbZGStXDAF0Ch0gWE0qUBRAO9VpBuVoSWnTrbfxZ9s3I1YbuTKhnlis16Psqns2DSf0v0Ji52PMH-sSbT5PcEJmJQcspso5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=THQr_blam8-lgcnVPpc9pAl3Uo2qb4cRYHBq0mvqc9-7wVR3lfFgDz5l9Ph5zzocuDlhEEWUSFCXHK1trglt9T47fL9M7g21ssNf_9FJTnnTv4Q0sYNnOzS1S6T9-uGcgjmTpCdoUxYAb7an0EyskAvsEQf5P0m-q1-mH8Hr5Sls9KdoVLocQFHnahB4JMmWBNL1Tw07bcoJqDvPLsaOsFMg82TpFTdGM8yAVAHo2MLddyowpbgLatbZGStXDAF0Ch0gWE0qUBRAO9VpBuVoSWnTrbfxZ9s3I1YbuTKhnlis16Psqns2DSf0v0Ji52PMH-sSbT5PcEJmJQcspso5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=OXlRZzZTIpuUwP0IT7Tvi2IWxrujDcNUpqBi-e3x5Fd1lAwM0oceR95a5PUm8x6KztRn2J7-yo-7Cw8ts6Y7j1kbIUJbSu6ka-EkPF1rQecWLQrQ0O5lxycFnIfwABaAwhmPYTajneGEBNX6uCWZX-ujgoJ7UN-lac09QjKEWmKW--KcHeVJsBnMX8Hk06-1A-JUkNpMch5ggHK39oTipSWadp_VJxr1dwWhDE3WwqTcVBLPZ8ASNdLaqGeGs7zLhPYow1j8d-1jLYdYaAMuM9mlSAafyNL6u7E7HDMSRlEbkDhg8Ddq9ZS7CFFshbg2K0vHwibdK8MZBn6SUJW9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=OXlRZzZTIpuUwP0IT7Tvi2IWxrujDcNUpqBi-e3x5Fd1lAwM0oceR95a5PUm8x6KztRn2J7-yo-7Cw8ts6Y7j1kbIUJbSu6ka-EkPF1rQecWLQrQ0O5lxycFnIfwABaAwhmPYTajneGEBNX6uCWZX-ujgoJ7UN-lac09QjKEWmKW--KcHeVJsBnMX8Hk06-1A-JUkNpMch5ggHK39oTipSWadp_VJxr1dwWhDE3WwqTcVBLPZ8ASNdLaqGeGs7zLhPYow1j8d-1jLYdYaAMuM9mlSAafyNL6u7E7HDMSRlEbkDhg8Ddq9ZS7CFFshbg2K0vHwibdK8MZBn6SUJW9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=catJngza-ekBeOoeJJW9O4jJR7w_joMm1y9MJvnKoTImMIT4hM8Z_76GkhxvXDyu5yxuEfawaGLneoPCTJg-JmoVEnZOCVq6cH1yFiPa0_UCl_ZOMU9xIj4k0rSysL2ejgSPiTRGEkytM63qXn02DnPm5A4aSAlhk0R9f_35HXP0tQRhH86YS1x55fBLxxaVSy7MyrUfwlyOTVvzJjN_8IJ_mhEnYt4WQM9-74pUKDSNdUHT5mt4vn-UJJiqhrfuOzqZAeigtwpIJs6-TTZYsec7odjzqeYK5s2Br4ClWkeW6D_4msKte88T9WxOBAaNU_z0jGObKGLX5RfjkokQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=catJngza-ekBeOoeJJW9O4jJR7w_joMm1y9MJvnKoTImMIT4hM8Z_76GkhxvXDyu5yxuEfawaGLneoPCTJg-JmoVEnZOCVq6cH1yFiPa0_UCl_ZOMU9xIj4k0rSysL2ejgSPiTRGEkytM63qXn02DnPm5A4aSAlhk0R9f_35HXP0tQRhH86YS1x55fBLxxaVSy7MyrUfwlyOTVvzJjN_8IJ_mhEnYt4WQM9-74pUKDSNdUHT5mt4vn-UJJiqhrfuOzqZAeigtwpIJs6-TTZYsec7odjzqeYK5s2Br4ClWkeW6D_4msKte88T9WxOBAaNU_z0jGObKGLX5RfjkokQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK1_Y3aR0puhr8ztwo7eBzkXMkcmMHJifF5sCplZxZw2Ucnltu-0tz9R8lIHws_F9xVqjAPZX0X4o-1tLwAMnhvOJR2A9l1_AyogG3v7TbRiBj6XtYrycPgSMdtkabnG6_ig-aiWRZphaA4HaKpLwJJUcogbs1AjpzlEjwd5FCCNFKRyECqPm5wthnQB8C-t1UnEC-TPoTsrGiNcdspOYnGpznK3Nw95pRqroK7ujb4mceL90Fe1YXIWrW5k5eJG5L6UoUxwACRq4INE71oCxbkuKlk452eMoYt7ejz5KeRjQdkrxDcJ5CjwDhM-hMPbI2z6aPuul7mWy6sTxwcZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=qh2F0HEPGXe9fz85PsAqpEK8mUgcU54kVfKxHyohyXQqyfX3HcaGscJCfcGKThRBnVGpq6QkiGvsy4BITYT3KfQtMzoEA2kNiOq2_zA8ise3bZTL4NTf-iJ35idrltah_oRbQ68Yr15-iXuli-JiDKNTeDE73GLUWhjarhx_ciQkMDRG9O6_o6aVZiP7thdG2C_PDjcNDyA4gB9Yuc5wwSXoN1X0Cg_LjqvkIAILMO_tz391cpG5kZKnw3tUqNOx8-YfuLrBg6vLNrSLmFT60KZeXhTCYIUXc3k70A6-g1-FUJixh2cITjsfG84Tui5a8NW2TeNAeDxdMc2HnxkpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=qh2F0HEPGXe9fz85PsAqpEK8mUgcU54kVfKxHyohyXQqyfX3HcaGscJCfcGKThRBnVGpq6QkiGvsy4BITYT3KfQtMzoEA2kNiOq2_zA8ise3bZTL4NTf-iJ35idrltah_oRbQ68Yr15-iXuli-JiDKNTeDE73GLUWhjarhx_ciQkMDRG9O6_o6aVZiP7thdG2C_PDjcNDyA4gB9Yuc5wwSXoN1X0Cg_LjqvkIAILMO_tz391cpG5kZKnw3tUqNOx8-YfuLrBg6vLNrSLmFT60KZeXhTCYIUXc3k70A6-g1-FUJixh2cITjsfG84Tui5a8NW2TeNAeDxdMc2HnxkpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=gYU6ratPSTFQ8jNHEhKi1HMhIFu1o_-m4yaGaYlaAw1K61g6uzoF7g_9eUyhzHg3P8t1FkgteuzwY_2Bau_0QkTSE6rDAshJkmm4dkTI9pnm-alXzRW3V-W6ymX2XS-zhuicYBe2BRVJQKnstEVizpMRUCjksYwMFOAWc72qBEqw-wui0pa6UCKfxS7mFthixbVn05YtEie03d19lhdGUfYarBDlGcH_DQWqXS1SHbTUB3TIeESoljZCcj78NO2PqF12DJuBC9eKgMQWbxZPWnYnf4_-2NlMDp1IGoGsvsfZkLwOMh6byZhlWogp92d9Nxfo3covWON-IIKHFRjAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=gYU6ratPSTFQ8jNHEhKi1HMhIFu1o_-m4yaGaYlaAw1K61g6uzoF7g_9eUyhzHg3P8t1FkgteuzwY_2Bau_0QkTSE6rDAshJkmm4dkTI9pnm-alXzRW3V-W6ymX2XS-zhuicYBe2BRVJQKnstEVizpMRUCjksYwMFOAWc72qBEqw-wui0pa6UCKfxS7mFthixbVn05YtEie03d19lhdGUfYarBDlGcH_DQWqXS1SHbTUB3TIeESoljZCcj78NO2PqF12DJuBC9eKgMQWbxZPWnYnf4_-2NlMDp1IGoGsvsfZkLwOMh6byZhlWogp92d9Nxfo3covWON-IIKHFRjAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od49JDptxUl9NKaP_GHC-jwFfwaQyFdSvkVc2HFiiEljxnS54_y7mk10qUTLagKmIJ_OnikxZRwpsab1uIKg6gbI7MqPJ5DWYxjx6uwjRnBM4NiPRGUpWiIv37vv8oj9EAUozZtasGd-QytfsutklBV4uGHhTUQn0juDyV9TppO-jUeE63wT_98ryXw1hVCfd4hRvb2abhfoZVzKXQ4o9FvWow53i-VFXQkbBHvt778gNIvQk3ahDj8_Oi3JIdLI8eqTj2Gs_pF7bW9Jq0BYOcYE8c9cjhjDSr0ObH66z6sAdEBC85O2hp4sH_6C2JWhBkxOqwPw9UThkowwl6Vzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6JzBFYxvrNQNaY5OXjTg7iKK5Da2H_lT7lKxlbsahIWC8NYZe7zbbRNioKKwNS6pGG4s6RNq8NM0cfoOokP3zKu4qgpfM4eAvs2E3bDXAYJRgA4eIahJTf_37ANPrPtRFGoj9Ov9x1O_JoBF7L3DzOcAKjz1bxN49ZcyjrQ6FNj_IfPhKGvISzCBFnGRV7gpWhSzQ7DGqfFHo6rVcscOgdH9TiOCX5IGm4UFIlwQLd5vB0wpYZmcvfAdd7F-yEs8WIhNg22ytSWs1JavdM90wGk9CXb69Ne-5hHjB9LJqcHX73ludFGZIjvG_0_v6UdC0-lmvA_JVZqBkEjfHxNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JycZRmpVccKkNZ1s9rL7j9QRIpntky__GzaOodXSR7FZqBXFpwdFUh2MpQ9efdrZbf5RcfNuZN80iU0kwcPHSrsvORFViMSVtYZEvBIXoqNt3MPJMNi2TNepSaINJNQB22w5zI_XSHsrtT7K6tAb8J-OSqTOx-uSsTw9VWsAPQH4Z0ayONAX1yh8lKPcQqIhZ_tkzjoV85Nhy-7Uqz5aewxqRhotynR8O1rJu_PnrEYKmR_oD1kp6rVWQc_sTrr05iht0RO2lVOz7khC43IP5V4vGVSiP4qxvtEHQzHwxc-3dGRhv-UCom2s9U7H7HKPdOSQ4zyIvc0XJ_t1v5HaAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=hCCpLJq-STshK1PncJ41rOAt57Dz5qd1AFHTaIki0l93IlpDON2BD0xKOGK3JeQL-G0xtsdrQ_IJSWUURiuKRMmj6o9YSTIKuBy7ApkFAhzjXgq_ERudvJhRm1KZuHAosm8YLc3V4N-soI_g1wuFWtAScAQOg7N4TH5yaU73rldWpOwlHlHZoFZF0_loEpJWvVf9rUnREvszPxpng0QgKybONAEpfJMk61jpxT6-dK-oyDH1nbkHgDUc3Jn_wdvp0d7dCbPBREs6Gduk9TmQDpAdLIGP9GBgXOlXo6a83OFKBG2HgtAXwrRwBizGSYLUwvegRZOWa6ik188eJQZVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=hCCpLJq-STshK1PncJ41rOAt57Dz5qd1AFHTaIki0l93IlpDON2BD0xKOGK3JeQL-G0xtsdrQ_IJSWUURiuKRMmj6o9YSTIKuBy7ApkFAhzjXgq_ERudvJhRm1KZuHAosm8YLc3V4N-soI_g1wuFWtAScAQOg7N4TH5yaU73rldWpOwlHlHZoFZF0_loEpJWvVf9rUnREvszPxpng0QgKybONAEpfJMk61jpxT6-dK-oyDH1nbkHgDUc3Jn_wdvp0d7dCbPBREs6Gduk9TmQDpAdLIGP9GBgXOlXo6a83OFKBG2HgtAXwrRwBizGSYLUwvegRZOWa6ik188eJQZVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxuPZYyUolhnpaZVDhi2QDn5TM5RTN1Kloi7yP2Qhta5OTiZTj_P4QGpMKsF0S_PnQ48DLnJZSRBWPEVWtbfnHgP88yaqJ0uSKk_9pBs97CkGQW6-_Ubq1UqhK-BwBWgXHgz0RfIr1DKNDhEhCyXFwJjAxFIhCMP3KNMbjKYKeNr0MNv1hJ5-eak6imLAihANnJahnwRluLFhFCL5nHCPTyg0aXGr-3bMkNZ7Fz8Rg_rt7TYRNaKWaU0er6hpGgzdM4Ncw3IYTrHl3h0mF7l5KHbFzcZHfIPeByPYQZeIXCphYjrE5sOiaWUU4EVI2utNBq0YvrrL4dfk1GK9XrjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=rodYbaZOGDfVDcEQ0ykmQjjUzB5Uvj8u3m3Xt0UdsrqB83gIyHD1M2ldPrSznVNvsztseDbb7GMxKCDFE09WV8AfJPt6u2bJqMIOF0F_8KyxapP7VTiy2-dMaVUAoU6YHS-WWgHHB-m7dLe71KBrPuVzikAF8CH0bNiGlE0rwKkv3Xz9arHR9neBGL8EZXId4MgYKGxeTbRAgd2rCvfdal1EcGVA_VzPY-ZF-icbFH1I-9pAhOpANXJSnbmw-7Bg1MTMXjwOLniT1RZQEMG78Hr4oc7Tq8WeEeVY_FA5yyp6rlgRJTZTOWmXKs_TQwPBWnNaZLq3753zjgX0V3Wlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=rodYbaZOGDfVDcEQ0ykmQjjUzB5Uvj8u3m3Xt0UdsrqB83gIyHD1M2ldPrSznVNvsztseDbb7GMxKCDFE09WV8AfJPt6u2bJqMIOF0F_8KyxapP7VTiy2-dMaVUAoU6YHS-WWgHHB-m7dLe71KBrPuVzikAF8CH0bNiGlE0rwKkv3Xz9arHR9neBGL8EZXId4MgYKGxeTbRAgd2rCvfdal1EcGVA_VzPY-ZF-icbFH1I-9pAhOpANXJSnbmw-7Bg1MTMXjwOLniT1RZQEMG78Hr4oc7Tq8WeEeVY_FA5yyp6rlgRJTZTOWmXKs_TQwPBWnNaZLq3753zjgX0V3Wlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=cza0huOxEIHAzjZGDLmek72Gm11YL9JBoIp020bLYKfxX0H1ILC_iWo1DDL7Fd3YItIwfbRKwx8SnRPskHoF6jUeZFq9-7J6N3DKa6_WsP41FDlsTVyx2EY2QLu-cA8RcMb8PAVMaS8b0LIRNvHZK2uQZsLlq2PttsxV9za9lVFflIMkCbyPD2P-rnS_Y9-bnNYxqaFKBs92x280sQSKmRjjv2SDROc3iI4XIT3faYTLT4Hzxq-_tzynZsfi7JZrp5PinmlgXHDgoLo9Zn1gNoJMqyq7pswA061H2H8ckaYkpduYJMTw5z-SF-pad1Wf4KZETKqBInnS4WTAwKnFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=cza0huOxEIHAzjZGDLmek72Gm11YL9JBoIp020bLYKfxX0H1ILC_iWo1DDL7Fd3YItIwfbRKwx8SnRPskHoF6jUeZFq9-7J6N3DKa6_WsP41FDlsTVyx2EY2QLu-cA8RcMb8PAVMaS8b0LIRNvHZK2uQZsLlq2PttsxV9za9lVFflIMkCbyPD2P-rnS_Y9-bnNYxqaFKBs92x280sQSKmRjjv2SDROc3iI4XIT3faYTLT4Hzxq-_tzynZsfi7JZrp5PinmlgXHDgoLo9Zn1gNoJMqyq7pswA061H2H8ckaYkpduYJMTw5z-SF-pad1Wf4KZETKqBInnS4WTAwKnFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=kLCC0xv4quszdrV5yJeXU8I4n7_7DIVVk8N4PixoVrufu6YFB6IjgaRI48FQuz-qC4CXTRBOt8vU3RAL9tzCv9iVaS-gqBTcmREGIjsKPGIZekuriiGjXpjpDRFT8KKDQajt9E3J4ocLWe4vruOt0t7plIjyqwgiK2YlEElDfxzlE4Et7oAXh4XDCJM-ETUoFgkDkIgEzQN5jY3bag0Ox9OLFMiePJcAKDahPP3ndQebcQOgv1NlGG94tJOozETqiLK41AJQuQy42BHi9N4WPg-pjTdogl_3Pp7F7uXNvqK8sjggar6oqqIfCgqc1mzey28p4CDDbZl5Wg-mEuWEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=kLCC0xv4quszdrV5yJeXU8I4n7_7DIVVk8N4PixoVrufu6YFB6IjgaRI48FQuz-qC4CXTRBOt8vU3RAL9tzCv9iVaS-gqBTcmREGIjsKPGIZekuriiGjXpjpDRFT8KKDQajt9E3J4ocLWe4vruOt0t7plIjyqwgiK2YlEElDfxzlE4Et7oAXh4XDCJM-ETUoFgkDkIgEzQN5jY3bag0Ox9OLFMiePJcAKDahPP3ndQebcQOgv1NlGG94tJOozETqiLK41AJQuQy42BHi9N4WPg-pjTdogl_3Pp7F7uXNvqK8sjggar6oqqIfCgqc1mzey28p4CDDbZl5Wg-mEuWEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=pdf55slPhC0lCpyAASU3_2JGzEd21izhyv7W_EjH1BIEazpk4nV8Xr3Y6NL8IVkJVtvsPSCd_jk4Mb50LK_iEqYW0O60AWOATkHCyXtA5l6TtDEUtMalU39oESrsb57V0klWlDvtJyUfy1mPG2wJew4ZPVRbp7qfPiQ-f1t0XTVcAvzdXu6qY1DgvtFG_dSPuCPJ8d15W_Ip3C4YPZfoclRANmQAYeNI8NB-y7TyXaT_-e8E9QZl-vo179NBuVXOsS1OWcKFfTo9rmq8mNi0xzXnvvo8890hBAA0ayJa72IvK04jjJEjxg72MZzE5cUxK8t71wNXFP9HV4opoBAHqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=pdf55slPhC0lCpyAASU3_2JGzEd21izhyv7W_EjH1BIEazpk4nV8Xr3Y6NL8IVkJVtvsPSCd_jk4Mb50LK_iEqYW0O60AWOATkHCyXtA5l6TtDEUtMalU39oESrsb57V0klWlDvtJyUfy1mPG2wJew4ZPVRbp7qfPiQ-f1t0XTVcAvzdXu6qY1DgvtFG_dSPuCPJ8d15W_Ip3C4YPZfoclRANmQAYeNI8NB-y7TyXaT_-e8E9QZl-vo179NBuVXOsS1OWcKFfTo9rmq8mNi0xzXnvvo8890hBAA0ayJa72IvK04jjJEjxg72MZzE5cUxK8t71wNXFP9HV4opoBAHqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LulQgDLJzJYrlj9kCuNcrnMgEkUxCKQucSA8PgvVlqsFu2ap49ZhvPHhvjNDBDvHe7RBMYqFf8NPFaRMqsHScg2rRBNWPlSf1rtzgyQlgY3z0PLcrZzN1YZpT9Ovm9ybWfPq4TGdnWnYmoQh0lfja6faoPT3NK3f03u8AltC5OHknw1LhuUXleSJWAoLwtf8JzQLniyRQ1pjnDD2jqJfzt3GkaubP68qnNtaD_sl92uqML3Back3hyvFbWtbCT3MYnVSXzOLBquTwjQcJwUEurSiAIlQGseO7cZRnsRz_mOr__kWpRG6h18C3uZX7T011RvJ-_iL463y72o472L22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZJLfN7sIuWaVgahegnQp3HEzvLM0Bl09ae5FhoArWqRDDv5gzL21QEy_yx0LBpmw_tRek8nWzafPByVKCiL9mEPmoq_6Xr4ZBLMm33s3XSXO-FXm3prOhGq3pqjzlEGFYxYVOEoIFQ5O67NoJdiCi7uhO1SdMYnS7ofJt2Z_DN0tAfRMz3zdgCOtrvN7rAA6jAOuEtNckRE_GPuTsMSf_WA8fHY9ljMrrvXpfQlmC1Fj2YBtKnhVEcic6NH-fGEKqC7xpalgH6gmsHbypprabkviDZt_oSSbb23CklfrDwOW3x-WjnELBeWYxli_BE1ynfSWBf2o0RoDY7p4wI9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=nbBoJArQlND7pKL_b2tmeZkV3VtfVh8Lp-9qFyKC8AHoBLyt6BH0JVdHGj0cLUmc0majxUheomdsz9LQVdoJ2Qr1EFA5QLQ2ic0qmYGjF9ePzsq8RQb-0azG40vtXuKZRD52aNyeMgGWdx48rL5YThl9yo6FGOjT2DmCi7kW4VEYCjeGz_Hs8hpZdMb5WFpJLYRO8TqY7d9k8c58GQYxvufX3jx8l7tEOG7bZ35jpl-dR1uCopl4MnuZuog3n6RzZZoaYVPMZ5OnDnvucMMh4A07xxcIH7qzo51ljoMcbka1DgOCitg97r0FV5ZO-Ova88aHKmiqPBApBU20qnQWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=nbBoJArQlND7pKL_b2tmeZkV3VtfVh8Lp-9qFyKC8AHoBLyt6BH0JVdHGj0cLUmc0majxUheomdsz9LQVdoJ2Qr1EFA5QLQ2ic0qmYGjF9ePzsq8RQb-0azG40vtXuKZRD52aNyeMgGWdx48rL5YThl9yo6FGOjT2DmCi7kW4VEYCjeGz_Hs8hpZdMb5WFpJLYRO8TqY7d9k8c58GQYxvufX3jx8l7tEOG7bZ35jpl-dR1uCopl4MnuZuog3n6RzZZoaYVPMZ5OnDnvucMMh4A07xxcIH7qzo51ljoMcbka1DgOCitg97r0FV5ZO-Ova88aHKmiqPBApBU20qnQWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=JU1dc623oBr2SMBrru1nSCTMDZu-_jr63zrVNjNV1Ycwzy_DkUl_g_9vvOHS-EJv3yOjJjbOFgpkWO2Zm81nAehiuC0rQ0Ac6Ep-ItDPK9dQGgJCyHHrTXtHsf3XSWVa6X72KhD6flYTxUti--9j5THgVDWZoWO31X7rX4TR4sM-3d9FErfXQRFyaNjTuSRs1vYINIrzW-FsljAkg80J_VE1wtH3xKJe9FnrBp6Dblvbq8u8KL40PZXlFVobyajb1BXmpZ2tEgSWfWDhJBNlsolrMdAdSEFF80I9wIKOoD6O0ICF-i-GsgarEjpVxU_Uc7TrzrHppl2iaAfjv2Ifjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=JU1dc623oBr2SMBrru1nSCTMDZu-_jr63zrVNjNV1Ycwzy_DkUl_g_9vvOHS-EJv3yOjJjbOFgpkWO2Zm81nAehiuC0rQ0Ac6Ep-ItDPK9dQGgJCyHHrTXtHsf3XSWVa6X72KhD6flYTxUti--9j5THgVDWZoWO31X7rX4TR4sM-3d9FErfXQRFyaNjTuSRs1vYINIrzW-FsljAkg80J_VE1wtH3xKJe9FnrBp6Dblvbq8u8KL40PZXlFVobyajb1BXmpZ2tEgSWfWDhJBNlsolrMdAdSEFF80I9wIKOoD6O0ICF-i-GsgarEjpVxU_Uc7TrzrHppl2iaAfjv2Ifjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9zPk--hcVsK5JQ0Ci5xqBtpMfqFU5qBWhGT-yCpHaRtugJt7waUrsn_TDbZCDbbKFind3sA2K01G3JAoUbEry0Fj6C7FKP4SDoBDcpo4g42sSkNH8dSWpU7xurW4U1eiqo8uYG23R0Wk0A1HlraeKrsuS2__6mnRRePj3fHaTAWhbTQF5rOSO7QxmFDjoHblXYuY_ahqlHbDPE3xyBPaIQacPcgG4WHklM7u61cSLRHQM32smjm_ODvP3epXdrjf9inQmWKmW2fjiqdneYPxIDi_577PPGs53AvJ8DgNh0p76wTVQKdMHvrZTc4Fi4ZjAVp4RlkrF6Y_wRR2Sn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=EXdCNozkym8JF6lDpmARCvaI1bFf2LI0Z2XNk39vk2QJcxCZPZVbtHJ6wmjBhX5ZH39L4-nGXFhwqwMU-SpUzq8EMG_F-qbd3mlTUIMoeZQEVkeYZIm-ICqpUsWhL_sJxgssyJ_CF8n2bwWoA-EkHovuraWWejPMjle3TAwOAQEcZq-C7P9g08fbsOAIsSQ__dq6SESW9O8MuCCWm4NdSGwlNafP7vd3iB4MAALKz99ff1v_OSUvUmzEDFF4DdXDPj2rlGwrHuPr4te1UB3ewaKga185cRZAQmUZm0K6wP4ojS-DN60xA3lDo5AOl03cIaZlnqRZZv7SCQkTah33_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=EXdCNozkym8JF6lDpmARCvaI1bFf2LI0Z2XNk39vk2QJcxCZPZVbtHJ6wmjBhX5ZH39L4-nGXFhwqwMU-SpUzq8EMG_F-qbd3mlTUIMoeZQEVkeYZIm-ICqpUsWhL_sJxgssyJ_CF8n2bwWoA-EkHovuraWWejPMjle3TAwOAQEcZq-C7P9g08fbsOAIsSQ__dq6SESW9O8MuCCWm4NdSGwlNafP7vd3iB4MAALKz99ff1v_OSUvUmzEDFF4DdXDPj2rlGwrHuPr4te1UB3ewaKga185cRZAQmUZm0K6wP4ojS-DN60xA3lDo5AOl03cIaZlnqRZZv7SCQkTah33_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=kWeQq7E2RVWMckfNr_Dm6unYf8sQAe6uZhEm1uKAM4MADgHTd_dFx1pSHA7HppDDp48nO9wKaOUZrMqHCq94KhnC--XhCnX_gfjzJ64n_HNY8mW_RzV-6VhLF-MUk_aQItcPNUV0O_ONKFZQLXNBGWmY_hW8BRlvLQ8Y9NyjTeaMObcxsznXY6mgCyLCgMJmTZioVf7Epsgg59J63E0JSZY3PxYZjk0udLmJ8sG4Lb_Vzs8ZZp-UbW80OeKNa6FfsBRXPS59AJndfF_30fAD-4CKj_wTuZZjG-7IZRLB08eaka4jMfWoMZM2i0LGddZV2pUswZKZTR2Dsj2vfTrohw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=kWeQq7E2RVWMckfNr_Dm6unYf8sQAe6uZhEm1uKAM4MADgHTd_dFx1pSHA7HppDDp48nO9wKaOUZrMqHCq94KhnC--XhCnX_gfjzJ64n_HNY8mW_RzV-6VhLF-MUk_aQItcPNUV0O_ONKFZQLXNBGWmY_hW8BRlvLQ8Y9NyjTeaMObcxsznXY6mgCyLCgMJmTZioVf7Epsgg59J63E0JSZY3PxYZjk0udLmJ8sG4Lb_Vzs8ZZp-UbW80OeKNa6FfsBRXPS59AJndfF_30fAD-4CKj_wTuZZjG-7IZRLB08eaka4jMfWoMZM2i0LGddZV2pUswZKZTR2Dsj2vfTrohw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=eLmi7Wg4DRHJTsft4Okmmce_vAe2mlcdmUo5cvVn7NTUi4ekRbDTtcI9X5Xp-r7tNuMpY077TpT_X2L-eqjMxr8pMSnw3IspU_jtBiBETqTjBu_EEQQQxuPyfQhUxAD945QDavwo9WhZcLSxQTRu8Q2IISfQo3uO-dj4RRYad_AQw6IJEd8-iZAIicdj7aaNkFH5A329N2hjm_AU2MzHKfN7WCozusVIjBg7qISOc_SBKLtUVMsr3_2pV7MFrfVlmLSAmyfFshdQiRv_IKBVomD_4F3t-ohelv9HgdYYTo2rkLVcmqW1OgH0ugiJMY66iEABMcqtaQan3V1b_YDIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=eLmi7Wg4DRHJTsft4Okmmce_vAe2mlcdmUo5cvVn7NTUi4ekRbDTtcI9X5Xp-r7tNuMpY077TpT_X2L-eqjMxr8pMSnw3IspU_jtBiBETqTjBu_EEQQQxuPyfQhUxAD945QDavwo9WhZcLSxQTRu8Q2IISfQo3uO-dj4RRYad_AQw6IJEd8-iZAIicdj7aaNkFH5A329N2hjm_AU2MzHKfN7WCozusVIjBg7qISOc_SBKLtUVMsr3_2pV7MFrfVlmLSAmyfFshdQiRv_IKBVomD_4F3t-ohelv9HgdYYTo2rkLVcmqW1OgH0ugiJMY66iEABMcqtaQan3V1b_YDIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve2HSkjsWkdEHt2CyAlr_FAoKuA_cY_bTmS6bXmcGD1uYZpiJcBtGtCuu7iSRokxagWXu5wP3cIHt6OOc-BbcVBSTPBc6SJcDuxlrSssYUWwzWTB_ew920YPH2eL7rc0BN3DI1tAu9GagSpo-aKJ0avDEgDGY72ziLHZuzei-vsWPZgL8ISoZqUhKytWH609HYhrDEa56yN2cOR9hJOCgO98tIPZgMq8G_seHgnfLI397DoGdYrxi-ajXTx28jD7FyloGlCzClEyAl83hNk8l46zEKjni8Rw_6yWnOng9GHMOb5WUpza-sd2mOoubm-KKQNwaReVRACpokI7zUtdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErFYTk5hCBGHhFZmwxwM664xWZ0Pg4Z2od0V99k6ze9x476pidhGh1wcBiNhkWUEwcxe13RIcSuh8b9Lm932KJFavEHJCYhnKL9Jz9CTma1oUPlphoe9cY57gdyNPz6B5Il9_7-eckTTU-YPbqXPO2IiXDKvSV6Wkmybk_2vRov4a1EOO01pjxkQ97bFarSQDVs4AiZdxKta7vY5EsrJUGtxl7mngniYGi6SrZMVpU0-G3Mf9Q5Fi6jlQB68-Sq8QMv61WybsRZPRBX8tKZG1oDyYASi5NPaz5Bu8MqAVes-Qf8jigc_9GgrzcLNOHBaG5fzT-lBXhU3dwZ6NBHpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOTMn1pvvfNxvyXfi6W2P9zWrls0V5cxPWY0i2nMx3tkhbqjB2XoxGUze8dcPvik9WmV-dwT9RpEkGsDYJVtlxXAw1Wzy8n6H__2D1hsWaeqMs43lL9cUNpW3ZeIxmSALdYmdmI4xSChMlqaIHBrtAsHhvrbNJhx2_aMQK2ZBFNlbzUaSgD7MT5EmwseBxM_oU0eXLiYutZ5C7xp2H4YuNIoEPWBmSa8LNIr3I01j4xH8GwL8jIDZwz85QAJivPm-pDKCnmiwIGiF7G4vOGWhseUvdmL29FhSqJSJFJre1Ap9KcO5Tlu9ObRVxxo35FgJrF__W7ltuBc7o_4TfVMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTM2Odt5Vv17MEsN4b0MFyElzKlHKNVV1pEWpJY7hY9ecrxrzw7ENdtaCEy-yHBoP6W3zBDtBapRzZyPQSGNQFy1FI4l4RVFHOb2b73HynlkwvqRTb8qeuY-bABOYf1VB8_M4nKLOnxFiKcbow9T3zNuQBcAeKF7QNSsgaCjfYUAumSy_6iQO50o2DNJO3Ev8q7dZLmsXTTki3ytrorJEqrwGcDu2bzicza7IB0bDmpsG81ytSu_u22ZhVnz8Zo8J0WJL0bYlbEBUGkOk-k7P1L4IQxx7BnyKRYGJmscy47ka0Qofi8ZF-Nzj2TX4xMy6DBMLe-yeM0N64TypfNJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=Ue8If_CUbcHl9Et3L3zeJlreLba--wPW-70D4URlRWuISIzZBAoiP3rdJm_AbpfvrqfU6btwN34Qv2JlouczTSichMV1XZ7P_098A2--ICimrtDIpVQwrVD7yvsY-r37xyaXIBEj6PYrGCUPjGJOZ1709Eg6bNcT50vi_M6VHT-vOrRPerqeeASkA8M5IrXhR8pHk5o2_8mbjA9mu7SN7CObklTlRHLusAxxNJGCydpbqSUQ1ZGn0V-cobETkNW25C6adGWPcAK5EQiFnDtwRYjgm_jInABG488WGQSTwCbKpF9bkhzbblz8NcNR-yCgX2CtZjMIeWp-eFS9ycpuig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=Ue8If_CUbcHl9Et3L3zeJlreLba--wPW-70D4URlRWuISIzZBAoiP3rdJm_AbpfvrqfU6btwN34Qv2JlouczTSichMV1XZ7P_098A2--ICimrtDIpVQwrVD7yvsY-r37xyaXIBEj6PYrGCUPjGJOZ1709Eg6bNcT50vi_M6VHT-vOrRPerqeeASkA8M5IrXhR8pHk5o2_8mbjA9mu7SN7CObklTlRHLusAxxNJGCydpbqSUQ1ZGn0V-cobETkNW25C6adGWPcAK5EQiFnDtwRYjgm_jInABG488WGQSTwCbKpF9bkhzbblz8NcNR-yCgX2CtZjMIeWp-eFS9ycpuig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYjHk40xFMCd4UaIbriuTqP1UOJhbA3ooWMjFCPkZwTXwseRNW1m1yvCTVade6EyrL2G7ZehR6DZIyZpDFxUrZVniUqQAgjmTBCUZ-BgzPQz0E8ptZMGbZeULdHPZCSEVQSddTA4gStiGEI3-MYDgF0Q6abYMcLjgedzHqyOtvutgunM6dxUI4Ev1vmXtbbVodbzKISysQVm34YvO2XW38_HPR3AS2MymAuxEiPk85fPDqgmU1MB-kZe_laI4T8MRBJoafIBb9Vh9Td2n7f12IWLzOKqYH5dDYrEFWOWZKcpawhePHiUeHfPS3aFQjpmqoV6imZCe_FyCVCSI_fTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-Vl-p_HGkwuaJa3ebt5337IdL_BYCAGnheGlNxshy1cu6TOOsJ3YzNa5gMbgJGkJrpDSwZWncblBOflVegjIpA65nyyp92hW1vGS1QTxetmbByrh8knYn6lJF91bBq2qHc5vObh_kZ5BfoNr9HKh-6HBqL2xQnTXVRBkSlFfPvcJkB515c_fcr7bi3-7cxi1FiNHlseXjJvlfuhHyiGb3u6R9Q3BTa9-vQPlB9tK61FdwObpnzOSK82McyJ1G4fbc_oVfC5MuAh2awQF8wPLUwvuf59m393FcWEZnY1uGkuKFP4HqpI_KJslEMfl_aVURZ3j-O3JGLGi247xMXiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaiFXargWBnEbgJGaruwhCWBHv0no4DbF_iEiMtBi5mUNdtPEwUrTYM6hvgQkm0WjXWzhTOlPWjs_tsoDKYCyPZg8C0dH99abLs2-UZa1-O9NvqKeqHfH7_bKBPPv4IAk6y3TfM2L9YqDxd3Xkg8QmkUwQdXy4g1vbdaTCKghFUScxVJwIUElesQddTcp9AvHmH5lbCCFx_hm4bHbMvCn13m4XCx_e0w5gMpQt6wW-vqlwXX25wYH24TnyeJwwddZmaM9WgztLQR49CwJRK1Egybg48EWCduRymEdwJVqUrv9r5JvA5pqCG17_LJiUs5SBdiCNBlumucJKZD60hdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyLcl4YjEo1OgZCHsQIrwYfy14XeIy3N0NiU36Yjf1p-XhngNmMcjlx1SXP7IJH4C6XRA7YGksA1IquqOmCfRRq1a0_jyuIqwR5BSAhBypJ-9XSHlNCa1rqtVdpPqXY2YdUcwytWxm3dkFcGfCFenm8SdP0hxFeKkf7nuDyO3z1ThQlDShvFYMND7_VX1iQX-_rsYmPygS-SxA0NYvM1g7h-4WTA8-oD-1ab-VRPOnhH-jY8SBGsbxHuyKuJjIr9vYdDpcVYoTjNNJv8s0_C-Con4CswRkStSk_sykIfjiii6owuit35WvFzGL_qmwXcSOCBgn3mjvAk11UbWPFyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehUB50lEROazZYHxFGf1PbOnuYdu97PuE9t2u_6SRH3jIPthoEjnjfm-r4kI2hZX2iLMltPZraahaEsiaaLSAO2ILRj4G6a76R9biR6LgPbUy4GXpHjOL28fF5Aw5wtgJW_VqejGzNzp6QJsdGV20cCFeU1_pDk8toQ8Okdd5h-vnFmqSh6ezNrW3LMHybPisypf47Hr5WhXEjD0DMYAzo-b7Dfwl_qfWeXgHC9k5kKsZ6AcJsOGr2jH77c4smDeIk9PP34rM2fiQvQFHYlz7Ij68sv2n0u5Klu1cU1iHKe8yXHThCKOS1UF2OQVCjYL_DPyuiST5Rm9NQqvPfv7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=V2CJQl0He2QMKmbBHi_G_9Wb2mAAYWD-RqhUE9OoSy8vhBv62u3BF74QoYG5A4138830p9KCZ6WVedG8fXx6hoZm0gCzoyShoAyC8gbv-ITQ6rTpT52nndb-AdzLUKJ_QMxAdCTYHS8mF7aC1w5-MeSzK9bycGLbL2qJeWWw1dwZ5Y-_u6hqeMkJ9fJvOwp6qJ11hcbqIVIt-5dH5kOONH_qrhVEThfx-EsXceLoGZdlwESp6GZ3E2gD9JGVLfdsaqwUMPYl6NDZoZFwoxBeMKOSr17d3gvAGw6kvACUfaPcQyg3GiFGgbqHQwMdd1Zglzrer7JwBzRSfEV048SWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=V2CJQl0He2QMKmbBHi_G_9Wb2mAAYWD-RqhUE9OoSy8vhBv62u3BF74QoYG5A4138830p9KCZ6WVedG8fXx6hoZm0gCzoyShoAyC8gbv-ITQ6rTpT52nndb-AdzLUKJ_QMxAdCTYHS8mF7aC1w5-MeSzK9bycGLbL2qJeWWw1dwZ5Y-_u6hqeMkJ9fJvOwp6qJ11hcbqIVIt-5dH5kOONH_qrhVEThfx-EsXceLoGZdlwESp6GZ3E2gD9JGVLfdsaqwUMPYl6NDZoZFwoxBeMKOSr17d3gvAGw6kvACUfaPcQyg3GiFGgbqHQwMdd1Zglzrer7JwBzRSfEV048SWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=kt72Ct3kvW4AQswn-z9X3OVwETzgVHr0aifUiNSOEhhcURbb5XDBlx-aUZfa-h7P9pYN2leXdwBhw8FW6tZWLSocJsNa6JOUO_VyB9NH5JfRx6S3N31yU0l7Ujjyp6wCoFJA9gvoR4omUUt4sDyn0zLAhXfskMifFWjHHiAbvfaWtAMqgMP9k-jQjBlpnJ-pkiYvqFmRUDbEuxUkO_ix3pWElG_M2riTDPn_cxl-Q1X8HjcEl-EhiCk25ujRJSyMedFc_vmgHPbOigXLkUNJ182Bi9B-OHD-9RREgREI-NgWpzBUGlrxtYXcOwSXMPSpa_Uh6mOY85_j2dS0Sr1WMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=kt72Ct3kvW4AQswn-z9X3OVwETzgVHr0aifUiNSOEhhcURbb5XDBlx-aUZfa-h7P9pYN2leXdwBhw8FW6tZWLSocJsNa6JOUO_VyB9NH5JfRx6S3N31yU0l7Ujjyp6wCoFJA9gvoR4omUUt4sDyn0zLAhXfskMifFWjHHiAbvfaWtAMqgMP9k-jQjBlpnJ-pkiYvqFmRUDbEuxUkO_ix3pWElG_M2riTDPn_cxl-Q1X8HjcEl-EhiCk25ujRJSyMedFc_vmgHPbOigXLkUNJ182Bi9B-OHD-9RREgREI-NgWpzBUGlrxtYXcOwSXMPSpa_Uh6mOY85_j2dS0Sr1WMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=FTmbsCcRSXBe692J9HUjDhOPWEXgb4os5Xl9L4E5Q0F1p17VCronRVb3xMpwZb5nPRmW_Wq74A99GEzjJ-GFHTLyNkLkBIV1UaJH35_05ytHzbfOwcx1PANnvUSApset916CJCxt6NldgW5PONokdOt7JAVwfQ77XTm6x4Sv4t6_IvgQaC2-ein_HY_Ml7zYzHDa0UJBXZjm1xMU0yuY2MtqBWnrkU_LaNkDp1E-UHaSDpAuaLgFx_92hy_jQ2yrCpmxIGktVfsflbuIA6KNOOOGECnbZbqvRx-IimXX9qGgkOoYqMV1usaqEpz0UcvTQt81HHXqppZmOJywlDmBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=FTmbsCcRSXBe692J9HUjDhOPWEXgb4os5Xl9L4E5Q0F1p17VCronRVb3xMpwZb5nPRmW_Wq74A99GEzjJ-GFHTLyNkLkBIV1UaJH35_05ytHzbfOwcx1PANnvUSApset916CJCxt6NldgW5PONokdOt7JAVwfQ77XTm6x4Sv4t6_IvgQaC2-ein_HY_Ml7zYzHDa0UJBXZjm1xMU0yuY2MtqBWnrkU_LaNkDp1E-UHaSDpAuaLgFx_92hy_jQ2yrCpmxIGktVfsflbuIA6KNOOOGECnbZbqvRx-IimXX9qGgkOoYqMV1usaqEpz0UcvTQt81HHXqppZmOJywlDmBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=sTAj1lh43-uOok1TBK9XPrl--4UTdE0OmBk7BjdL3UGmIq9lXLSWzQm68ApvfCreqvVlwojRxH25mZi5f2KzGeQpErKH3cUYGK2S8SaZbShw98w3jjOmaxhTm3Wxek8-UaXm7Sh9VM-E7khoB0TWZmiyHxMZCq_ljGpSWenp3AE9vI3a2MoYGZE2TTpkny3Zat1rDoY7Bzz0K1jWJQnYPtVDGu6HETmtvqLtcfHykTnbKv8A5YQrsi_q7k3RBBb792vyrTtTy79JjX-GyZj2kJdr4XOhP1rY-jx4Kz12EiTKgMjtem8HksIj8vAf1oQbQCXWZuk5pe0UeObfxjSjRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=sTAj1lh43-uOok1TBK9XPrl--4UTdE0OmBk7BjdL3UGmIq9lXLSWzQm68ApvfCreqvVlwojRxH25mZi5f2KzGeQpErKH3cUYGK2S8SaZbShw98w3jjOmaxhTm3Wxek8-UaXm7Sh9VM-E7khoB0TWZmiyHxMZCq_ljGpSWenp3AE9vI3a2MoYGZE2TTpkny3Zat1rDoY7Bzz0K1jWJQnYPtVDGu6HETmtvqLtcfHykTnbKv8A5YQrsi_q7k3RBBb792vyrTtTy79JjX-GyZj2kJdr4XOhP1rY-jx4Kz12EiTKgMjtem8HksIj8vAf1oQbQCXWZuk5pe0UeObfxjSjRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=Efqv0tX5XULdyMafT6ChuJSd5hvlW0SeO_Hf5dDJvUd5Kuu0w2hbkkcQM42vYlWSCebwTnNycbvE_a-uc9GnU5Z5ET93bAy5TfgkUr3hE2oQdTnd8WFjI7QBsnUHiCN7XP1E3oBOhvsoSw3Ic2SaQqOAtNdjYGj9DnSUdEDN2ZlUwpGrzeTH24IfQjpwVha_dLADismibm6ThUII0CHuuc4WFifUSqT1d8Te7rhOBnPdUgvYha97tlUnsTae1uQMyFK3SzGaTNeK0JhisZ0gYmuRA11Z97DfOGkZMTvfOjafyHMnhIcQvvBUAwjxqRl-IGQIleQOFy6hZ3qYKGhPVT9zorupZg0z94OY3LcOxrEctP7tKiH1nq-FXkV-gapcCEK-q1wdMwBGGd-nmga396krCwM4rbuo5gVDDHucjky3w7XfnL4WmhAIkFNpEbCFtkAzd9lsVKZAHXB1i4LBmXW6XEqqvZTwPSJ1BJTmi4mI5usSZTVkym10K2zxty8ssyXEeLN8O2HBtlYsC52YubKvCg_DDwmmTeUL7TOL-lx9JE_HC0JfR2EyjkXot23o5Xp2aWQJf_Q8VQpt6kRJqTk6Zal6i26pIQJ6ToPeZweH1q7AKfGd3V9YwY5ileyeWVQez7UA0Fg4BzE2Lx5zKTf085d0L9pVLOYVEFgSjuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=Efqv0tX5XULdyMafT6ChuJSd5hvlW0SeO_Hf5dDJvUd5Kuu0w2hbkkcQM42vYlWSCebwTnNycbvE_a-uc9GnU5Z5ET93bAy5TfgkUr3hE2oQdTnd8WFjI7QBsnUHiCN7XP1E3oBOhvsoSw3Ic2SaQqOAtNdjYGj9DnSUdEDN2ZlUwpGrzeTH24IfQjpwVha_dLADismibm6ThUII0CHuuc4WFifUSqT1d8Te7rhOBnPdUgvYha97tlUnsTae1uQMyFK3SzGaTNeK0JhisZ0gYmuRA11Z97DfOGkZMTvfOjafyHMnhIcQvvBUAwjxqRl-IGQIleQOFy6hZ3qYKGhPVT9zorupZg0z94OY3LcOxrEctP7tKiH1nq-FXkV-gapcCEK-q1wdMwBGGd-nmga396krCwM4rbuo5gVDDHucjky3w7XfnL4WmhAIkFNpEbCFtkAzd9lsVKZAHXB1i4LBmXW6XEqqvZTwPSJ1BJTmi4mI5usSZTVkym10K2zxty8ssyXEeLN8O2HBtlYsC52YubKvCg_DDwmmTeUL7TOL-lx9JE_HC0JfR2EyjkXot23o5Xp2aWQJf_Q8VQpt6kRJqTk6Zal6i26pIQJ6ToPeZweH1q7AKfGd3V9YwY5ileyeWVQez7UA0Fg4BzE2Lx5zKTf085d0L9pVLOYVEFgSjuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=BYH190l-7EOmJuuZrmCnZwQPHH4KIyLdb3G1tj4Jm7VHnoTcSQe8WHtBcZTtulflNImA7My4QQaqkPD1LRpKoRu_4nWtD-SErI8KfBIH6ox6NcrJMeiogrdP1CB_-S1aJwgJ9h4-yHDvjENb-19cM0ykkYOMJElZB94O76F6ipKxdD1irgx0RvWd2GjsmUqGLQDFZathhquJne_EGmxS6tfguDUv1rQK1UN8h5AW7xtXDiypnm9tCZyNyFYsOVP4tGSH5WfGvTHQx6fCDuzcmyjSAUr0CSSn0375myLTWOu9so5bNa4u18Qe4Hltj32vO6zWS9n_oboYEZcHaxXRLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=BYH190l-7EOmJuuZrmCnZwQPHH4KIyLdb3G1tj4Jm7VHnoTcSQe8WHtBcZTtulflNImA7My4QQaqkPD1LRpKoRu_4nWtD-SErI8KfBIH6ox6NcrJMeiogrdP1CB_-S1aJwgJ9h4-yHDvjENb-19cM0ykkYOMJElZB94O76F6ipKxdD1irgx0RvWd2GjsmUqGLQDFZathhquJne_EGmxS6tfguDUv1rQK1UN8h5AW7xtXDiypnm9tCZyNyFYsOVP4tGSH5WfGvTHQx6fCDuzcmyjSAUr0CSSn0375myLTWOu9so5bNa4u18Qe4Hltj32vO6zWS9n_oboYEZcHaxXRLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM3N2re9N7G4xQ1ids-TwwG60Am17aFX7hr3LLixSA8w7NIS3OQJnlLFGiyQNcrlI961xpJgyaSshxWLby5-SKJQ4Bjp00tkzwi_rcNdtgeSvz8Ztt6Uhe74fdCzCeJIvoJOc-MONrNjKhr_EYgRHRdckgFuhCoy25bq90h6fLEKMVEjazSekg3V1F30Bk7InbyXE_vUts0saUzZzhp3cEjOwuJ3C8uzefjILFp67HfcNeOo2Zv3RVkYdvhmBkMJDhYSdaaEsbDfXEAW7fcHPfDNxgZT72KIkL1aDmDV6jreeeLf8FQvB2vCa0v1jAsc7eOnVY91reXPL2gE88dMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLoJy8Yl1kOvZ8FidhVXVdFXrecxTokrRTJ2xtgDRjMMS6qB11mjYTqc--x3RvK5U3jg8znKyqEn2yqDEhawlw9UjGJ0NO_HXhPhOt70dZUrRAIHEVvjObHCLlMTPz5HJ91BT9kgaVjjDuO8Lr-ecauKG7bDOhZXv3IesrerWYdd-kfNKZ0WpeUOO2PAO9-kmOH0UtklSHbLE6f78zLL7s6vHmGTcl29W1i5MG2wr6J0a24U-M4FV6hn3X9k2bdgB2_dw3-B7yjD1uFnd2fkMFdDJP2jSkFblCx2NUFAqE3sHon4m_iBzB5ZaH-2TfW8CHp_NX01569XS5rFQ5irEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6RAK3SockDu85Y_njHwjU-_HUr8QDW1V264GPCGkFkiiYvnJO1yNcWlubmAIMzP6vmh8AbYjlI_RGXGnnPI4Jfp9Ps7eOeI-5MDJMCLb6-0BdrBVjCf_iAz-_nod3SMhpXaP--CxwsjhZFd3BDc22uTxdDnufQQI1VlVMX9faidcN1Ad6zbUbLF_gIM9I4cN90B7Tx3K8p2-C-jmiCqSNvf_tJEpwTAm2HZrvMEJKWRjiZgQD2l-t_X6-3HeSFrxi2lrznlHKd7qSNArhtNgZB5rd7itCf1xRvP9Eeqt8FTDn2FvbykjwohoUMmpjFv5taO2NPswsH-kskP-BezcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MORqO9w3y6Sw-h0DaMyoZdErFsvRorl9NcVZeo10L4_SSrjxHw0lD0tZf1s07-Fb5QozNnSn9WbdgeqPoERKSPCRNQITkIassvwMKuzfiSYsKTaJ9hnhPhuSXdn48WgcgZ_CeVeSebQOyjSjLZCVap3gnir77Wy2zzrQMvbjoRQrGyFOCFs9Q_QCqkiB2KxvW4V-fkbzVD6arUBQDCYINkCryTexbNcwrripH1VGko-ZLCWYRiG_nX1-zKOuzYEyePsYH9qnj4aY9hPFYhtQRt8TFSpXa1MdQehvFQKeI8Y6It2DcS8f869CM74aQpZbOqIL9WFpA-oXZaJIcSjygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWY-uRriYmXMW8ZRN49JpaXsO_lEpnwA-rWFzsQYiCv7SAHaFpoccpU5krKw_VDN8h3snEAjyixvcK7hx4pGoID4JvLThMnNAI3wKb105KGHLajksxFYY7vqmuj0OR4fCbIIfSL_RlfzVRJc35qahn7q7n0NgNr5i2EPHNPz2J8uCgpLxlU1mPm1K5VztGsLjCwDYCjEVchuKYylB9wRbKFxB8aQFzqSVRfJMKaCkoM-UxsJEA3gVoklTw-frMf5MVmLetHQJGMk1oj8AxgKyU_Qq1M1liyhC4EUQRZn-CHv23F6KHCEN2z5cmCFjRJabXOI6cvHbYeKtliaU3ZCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=Vkg8PF6CNh0zewuQrHkaWfrVLVOkHBnhhRHCj61UAbsgxVjQrqaYMX4Yq08glg2CQB4b8gfAutR1J_AvEm3IbbGTl1f9AU7-Cn8AUzpcOe6Ih1t4qzj6Y4GS08AJ5gEWybQJrSZchfRVeCLsLvgYG07wHl6Awk7OAVgsToI_VPYB5N8DDb8ukpCRmOaOKW8wVzdEddPNyGPG4KnMR_zYQ_Be8AGa4_p2fshLljeUxKMiC7ryCA-uht02dPLEADhHKt6rQ28HZ1le8vGtv5jh7tfBc8e5RCtReA6UtfFLYkWcC8pJjEtgDogPZV3b55ra-yEzXtPbf2HJowtrroQlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=Vkg8PF6CNh0zewuQrHkaWfrVLVOkHBnhhRHCj61UAbsgxVjQrqaYMX4Yq08glg2CQB4b8gfAutR1J_AvEm3IbbGTl1f9AU7-Cn8AUzpcOe6Ih1t4qzj6Y4GS08AJ5gEWybQJrSZchfRVeCLsLvgYG07wHl6Awk7OAVgsToI_VPYB5N8DDb8ukpCRmOaOKW8wVzdEddPNyGPG4KnMR_zYQ_Be8AGa4_p2fshLljeUxKMiC7ryCA-uht02dPLEADhHKt6rQ28HZ1le8vGtv5jh7tfBc8e5RCtReA6UtfFLYkWcC8pJjEtgDogPZV3b55ra-yEzXtPbf2HJowtrroQlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=ag-z7TxkGwWGtBYfAveFYGKtbZBvykGG3luW7wf2t7Gp04L5pe1uFIcPYuVb0GAIh2xC5MlGHTks1bq-4sB5Elu99baoT_c3gVkO1q2v4BJiuqpZ7iriYC9-6ViSn-F18KYh2R6bIFI_zZkNnwTyETvssmuJ2o5BfGon28ANLXeEbwvnx5VcyKkYKWrlXQ7BvrIQevVAvRMHXvYu8cz2jn12aiqSONy7TJ9jUqTMwS1uG9iiMny9VODOvrDM7uRUd7JA_JHRoL4kkx1kAtVH2vt9AUYrg95nK4Lit-RjXkHLXQ6lzEqzrofYB16Z759pxGu7rNi-seesl8BzWdIWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=ag-z7TxkGwWGtBYfAveFYGKtbZBvykGG3luW7wf2t7Gp04L5pe1uFIcPYuVb0GAIh2xC5MlGHTks1bq-4sB5Elu99baoT_c3gVkO1q2v4BJiuqpZ7iriYC9-6ViSn-F18KYh2R6bIFI_zZkNnwTyETvssmuJ2o5BfGon28ANLXeEbwvnx5VcyKkYKWrlXQ7BvrIQevVAvRMHXvYu8cz2jn12aiqSONy7TJ9jUqTMwS1uG9iiMny9VODOvrDM7uRUd7JA_JHRoL4kkx1kAtVH2vt9AUYrg95nK4Lit-RjXkHLXQ6lzEqzrofYB16Z759pxGu7rNi-seesl8BzWdIWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=YaILadtWnf2m0LjvPIwsDnhfzRiGf2pqpigkLnD906tMc6hCF-bJ4y5UTJcvlcyiKRrVjtFued9V8V9dgynN2KN9Jg8DczfsFrcRb8cFWiG91JdQQgZq9mjZtz8lPgrE0U8GwCsRlPMJZW0foCnTz87hC4R05v8WG2EYpBNRq6ffII8zgvgSLLasp3r2ugNm5Py0zKNK2NMcugZ0S8t0BXliWD3H5N9aVRkxDsYcGMHsRt1sKFJcrsdxtGzz2SkEt5dSiKiH0qO-PXAtmFGnCoudMVOcnDBEQHL1a66aKPrSSz3zhONhwNM59CGIC0lBJbk08UtRZw6OfrUL1ISAtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=YaILadtWnf2m0LjvPIwsDnhfzRiGf2pqpigkLnD906tMc6hCF-bJ4y5UTJcvlcyiKRrVjtFued9V8V9dgynN2KN9Jg8DczfsFrcRb8cFWiG91JdQQgZq9mjZtz8lPgrE0U8GwCsRlPMJZW0foCnTz87hC4R05v8WG2EYpBNRq6ffII8zgvgSLLasp3r2ugNm5Py0zKNK2NMcugZ0S8t0BXliWD3H5N9aVRkxDsYcGMHsRt1sKFJcrsdxtGzz2SkEt5dSiKiH0qO-PXAtmFGnCoudMVOcnDBEQHL1a66aKPrSSz3zhONhwNM59CGIC0lBJbk08UtRZw6OfrUL1ISAtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqPno8XhgBT6H4Nn8qw3VvjUrMQumb-Nq9X7LYO3KcnBzQmjnba4FOrriP_-li3NFZ0Wt6QGxR2nhLQRMNTeIAUUHOL2B7ydFmwQidwEi3kzMb_Z_GsjEIkqtwWqLac_iz-7-TMUGtXqM3f-813aTL6QHxXuyi4NbUZ5Udki5voXDzXZ94GUlNBYdzfi9Fa2RjEr30gZ2l5uG3u_Y3eAZEXjdJJo-10zR5tmbfsIcC8LQmR-ydJd3kJnqY9H2Y7gNA6ZO11Rucl9o3hDmYGLOZ6LGb7qJo14_5NwKeR3ySRqyRht8i_My_ozOXwLuh71wEWJgeFJwJ7JQ7wMOZaakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

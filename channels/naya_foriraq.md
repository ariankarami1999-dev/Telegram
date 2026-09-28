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
<img src="https://cdn4.telesco.pe/file/K70ru_ZiJhNEu9qoK98qlMCbUXoUbQ6sQCKaeTvqPBgTtF-ApxI35utNWooegNCYyvJiLk8hNXPb4vLHFCM0B_GL4bIFZ76qlqQKkXgHFHIY_jYvxoNWejuc3JEbFESgDbKyC9aFsuJT1RlsccCGnrgNEaC460NTM9-J9HsPvKj_XIn7z4w7NS6kwXdSGgbw4Z5YP-mia58GTGVijRAZNp2FfHyXtAqmokOAgcmMy7L_JSLrEN-AEdxcSBp1Lz4ZoF0EgLhgy6W0_nLicjlQ9vMuudq8gHXDdGtbDG4RGR9YqXbpRHI312GyEV81xY9ib234qItpiIVsC9xm6ygCzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4a81a27b.mp4?token=bvSjtpvuKYCF3hKJjepmHnmG6_L_FBWetkP4_fhkzjmSMvQEwvGfRPAlLXZp_df0t-_eqOxKnHab3AvzeKYlduhQ2gmK6hm8x3KJzNoc9ZlUUr9G_eLSYEAMwmcwUpuOHnT4dOLlAY7vYXqsDfzCOZN2AWbt1QwyvzyR3W91mzwxYwO-eccn0ErAvzdq0sIQu8xZ9P19PTzMKjtKtc0TSn29VCqqiqwQjwm1qcfH_Bx6bLT3dQenZtyq3SN96DBWgoy7d7uUzaS23F4366VujxQH0RqSbHgRpvYCAzbV_SsGwKcht4wStwCmgLj4aai0fYSXVhMR7WDZ5hfXoHS-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4a81a27b.mp4?token=bvSjtpvuKYCF3hKJjepmHnmG6_L_FBWetkP4_fhkzjmSMvQEwvGfRPAlLXZp_df0t-_eqOxKnHab3AvzeKYlduhQ2gmK6hm8x3KJzNoc9ZlUUr9G_eLSYEAMwmcwUpuOHnT4dOLlAY7vYXqsDfzCOZN2AWbt1QwyvzyR3W91mzwxYwO-eccn0ErAvzdq0sIQu8xZ9P19PTzMKjtKtc0TSn29VCqqiqwQjwm1qcfH_Bx6bLT3dQenZtyq3SN96DBWgoy7d7uUzaS23F4366VujxQH0RqSbHgRpvYCAzbV_SsGwKcht4wStwCmgLj4aai0fYSXVhMR7WDZ5hfXoHS-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد دحر مرتزقة السعودية..
القوات المسلحة اليمنية تسيطر على جبل البازلة والاغابرة بمحافظة لحج.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/naya_foriraq/91830" target="_blank">📅 11:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
‏
خلية الإعلام الأمني:
تسلمنا المقر الرئيسي للقوات الأميركية في مطار بغداد.</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/naya_foriraq/91829" target="_blank">📅 11:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91828">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
وزير الأمن القومي الصهيوني إيتمار بن غفير يقتحم المسجد الأقصى.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/91828" target="_blank">📅 11:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91827">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa304d8f3.mp4?token=rLqbVK7M5jTS77ByTkcfyWY7DTWv7IzkZEXUqPU4yoYBUWqLYvS3THcAcq5R0rbkMCjHaP68Y_xlgZH7tZ7sqtusYjWlrW-IwE8mWcZJ44Ot1lRpDGX52rG-DeJ8tfuxOxe30FkmkzSE5TV6x-Vjm6bDzw2MJnMJrLeIEEXf4m5P6CO1XAOcifP18UuSfjW4gvJtzH2DUNzgop3tVSPxCAkQdElDSS72o9cj0FxS4cltbiIbleIoFXr-pMK8sBdUm5nvogVU9DZCnACZcn9ArSgwZdrKtSTYE3bHiEzBsIhY0-Lop8FWxffMefzN0WLtqiEJ_RcqlmaUEh8TumcRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa304d8f3.mp4?token=rLqbVK7M5jTS77ByTkcfyWY7DTWv7IzkZEXUqPU4yoYBUWqLYvS3THcAcq5R0rbkMCjHaP68Y_xlgZH7tZ7sqtusYjWlrW-IwE8mWcZJ44Ot1lRpDGX52rG-DeJ8tfuxOxe30FkmkzSE5TV6x-Vjm6bDzw2MJnMJrLeIEEXf4m5P6CO1XAOcifP18UuSfjW4gvJtzH2DUNzgop3tVSPxCAkQdElDSS72o9cj0FxS4cltbiIbleIoFXr-pMK8sBdUm5nvogVU9DZCnACZcn9ArSgwZdrKtSTYE3bHiEzBsIhY0-Lop8FWxffMefzN0WLtqiEJ_RcqlmaUEh8TumcRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇨🇳
🇮🇷
سفير الولايات المتحدة في الصين:
لقد أوضح الرئيس ترامب بشكل قاطع أن أي مساعدة تقدمها الصين لإيران - سواء كانت معلومات استخباراتية أو قطع غيار أو معدات عسكرية مباشرة - ستكون غير مقبولة على الإطلاق.</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/91827" target="_blank">📅 11:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/91826" target="_blank">📅 10:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmNII-fGJEfI8LeLaY0-qcC7sNC_4xAgd103QPG0dK0s3AcLYzjWx0X9ixIQGhrxKpmhy068NJeiyQRCJSBaHOEqhbIjTmGCwRtfSfKDOBpRyzdEG-NjJt2w9R4-LKGAPKbJz-fOxzJxmHX1zyFx31moGp_eBbAqaKHwgChP63P3z1GsvWDo3w6M5PHtLZQLuakTtoNcbeOmWn8noHA-8HxyUWkhnDxmxBxj0gLAbOeLndTBZG3_s8wrrEH8TlARfY8rcySIgHqOspXJZF3rxNKhHCsJWEQgqpDBfGriYwLiyAj9OpgN8vHdQT3fRfyzo6WTpZ7_UKiGVzFGeoQLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع لتلامس 108 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/91825" target="_blank">📅 09:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/91824" target="_blank">📅 09:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
إعلام العدو:
التقدير هو أن حماس لا تزال تمتلك 30 ألف مقاتل، بالإضافة إلى ذلك، تستمر في إنتاج الصواريخ وصيانة الأنفاق داخل قطاع غزة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91823" target="_blank">📅 08:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر
🇺🇸
اصابة اكثر من ثمانية جنود من المارينز في مضيق هرمز اثر تعرض سفينة لهم بصاروخ كروز بحري اطلق من قبل بحرية الحرس الثوري التي اعلن ترامب انها دمرت.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91822" target="_blank">📅 04:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91821">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏ترمب: تم تدمير السلاح النووي في إيران ولا يجب ان نقلق بشأنه بعد الآن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91821" target="_blank">📅 04:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91820">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سماع دوي انفجار مجهول في اربد شمال الاردن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91820" target="_blank">📅 04:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=PVTQN-eWUWOKBvV5Hfv4QqUQV4JEYQDGQ4eQH8W3e6ekwHih6xRNmziYTIxVtJw8J8b1itj3JYcF4zKsG0m3bON8L8P8HcYBSJw9QCn4F7F2k0Qf1gowNAzyt5O5nIGj6L5WQC82PDECJNJNKViM-qpLz87B23om_Hef2HBVgx9mWQ8SKHFkk-tudlmay0CAKWdysw9Dr8GaOL2qPQsc3ZqbGC0j7huGtTbNLw3AnTTZHA9v9nt4GD5SM2JgrR8cTvxhJsASawwfPF9mtSUAa22V929R5q2B2-_wKGrURf2l_hs4GMjaUORwNke9vqK5bVfjSqaQjCH0etvEWJ_ssA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=PVTQN-eWUWOKBvV5Hfv4QqUQV4JEYQDGQ4eQH8W3e6ekwHih6xRNmziYTIxVtJw8J8b1itj3JYcF4zKsG0m3bON8L8P8HcYBSJw9QCn4F7F2k0Qf1gowNAzyt5O5nIGj6L5WQC82PDECJNJNKViM-qpLz87B23om_Hef2HBVgx9mWQ8SKHFkk-tudlmay0CAKWdysw9Dr8GaOL2qPQsc3ZqbGC0j7huGtTbNLw3AnTTZHA9v9nt4GD5SM2JgrR8cTvxhJsASawwfPF9mtSUAa22V929R5q2B2-_wKGrURf2l_hs4GMjaUORwNke9vqK5bVfjSqaQjCH0etvEWJ_ssA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91819" target="_blank">📅 02:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91818">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886951be8e.mp4?token=jFa2W6KSjNYOTWK994u1GncsOdnfjlTlVsFbXzApbj_KIilbRTKaZwQ1RDbpsTVR7StCrK8VkPwwU4HHYT3bfmTnfsKd_QSPw3MdASqEy8gc31Qtv8bysYSSheXbeoxsFBlCRHk56MbYpELkwqtLfFvi0WutGCg8-yV9Qfyo424qdpGnCarIfAVdpSJhYoxawSERxm9P8ehRMLplQnt-mxx_LYDV8ivQFLvAFMcilhPxo0WAHXlEHO-ZlkH6gdiUJ1cGEEp-05KTihtAu7z-AKtWASrU9RDAzdjXbqjsnaGOfkpM08t12inLYWb5OCMYJYZ24byFt_zLzUSmRvSnSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886951be8e.mp4?token=jFa2W6KSjNYOTWK994u1GncsOdnfjlTlVsFbXzApbj_KIilbRTKaZwQ1RDbpsTVR7StCrK8VkPwwU4HHYT3bfmTnfsKd_QSPw3MdASqEy8gc31Qtv8bysYSSheXbeoxsFBlCRHk56MbYpELkwqtLfFvi0WutGCg8-yV9Qfyo424qdpGnCarIfAVdpSJhYoxawSERxm9P8ehRMLplQnt-mxx_LYDV8ivQFLvAFMcilhPxo0WAHXlEHO-ZlkH6gdiUJ1cGEEp-05KTihtAu7z-AKtWASrU9RDAzdjXbqjsnaGOfkpM08t12inLYWb5OCMYJYZ24byFt_zLzUSmRvSnSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات تتجه الى اهدافها لدك مقرات المعارضة المخربة في شمال العراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91818" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91817">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوي انفجار في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91817" target="_blank">📅 01:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91816">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd346d3b8.mp4?token=PmWlppmroNEP8SnorQmHtGbKSRk99aY3DN0CQY-A_xPgkGRRc0AeDew62kbfi1BHlsqBzNq3Bkj1TzKdmt0NMhRa3SnPYjlIA7Vm1su_iRnE7Cgp0P6rl9lq0dgxOoXQvhb5n3GMGZhkLTc9zCG0KdfOJBqNuP-LcRDMFQ1b26PtVqt87zkJKkxilUTP9Zyc22UkF1ZuSn0xKmXXycy2Ebz2KKTp9tbTepizLiyBocU4seshQi_-o56FH_S6djtOCG2j5tzPupbf3KKY2sqU2G7IWbjeBDxBONqEMNJ69939cZ7hzbXEqrY0kdeMtL615Ks3pcJ3flBlCVShsHYVnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd346d3b8.mp4?token=PmWlppmroNEP8SnorQmHtGbKSRk99aY3DN0CQY-A_xPgkGRRc0AeDew62kbfi1BHlsqBzNq3Bkj1TzKdmt0NMhRa3SnPYjlIA7Vm1su_iRnE7Cgp0P6rl9lq0dgxOoXQvhb5n3GMGZhkLTc9zCG0KdfOJBqNuP-LcRDMFQ1b26PtVqt87zkJKkxilUTP9Zyc22UkF1ZuSn0xKmXXycy2Ebz2KKTp9tbTepizLiyBocU4seshQi_-o56FH_S6djtOCG2j5tzPupbf3KKY2sqU2G7IWbjeBDxBONqEMNJ69939cZ7hzbXEqrY0kdeMtL615Ks3pcJ3flBlCVShsHYVnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصوات مسيرات  في سماء اربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91816" target="_blank">📅 01:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91815">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
زلزال قوي يضرب جمهورية الدومينكان .</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91815" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91814">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91814" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91813">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91813" target="_blank">📅 01:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91812">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91812" target="_blank">📅 01:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91811">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSGQOLFQI62VJFL_wYcj_7rfQZFmA_MDu6z5f-m0MXwZKA2r2YOe3Q8-OACdRgrJdQJadlwHkjnMDpVh1oRegHapFyPI4y-Y45G48kRjKpUkMLIAhA7bst8oRLYSzPJXGxLd4Kb7HtPjP2rUvm-qwZ6aNLI06paQnkjunHGwZ9us8oh8Sxq-f8WxYQUEcAPHepuPou_3azXrH_1LUP3aDNkWz3OQ-L373QcsXp8Wied03qYCZ_C3r9seGP-txZ2CeWw6WiLRZy0j-YSPq-XeD1ZFk9BsOMQrXh2MLkIoz7zn8AKAIHsoq3EyuWbVO0nAOfZpREN7GLlB7vzIFwTgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
This is the ugly world we live in a comprehensive crime, whose harm has affected children, women, and civilians, is being promoted and celebrated from the platform of the UN
May God have mercy on the late leader, Muammar Gaddafi, the martyr who tore up the United Nations Charter on television.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91811" target="_blank">📅 00:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوافل الاحتلال الاميركي تستمر في الانسحاب من محافظة اربيل الى خارج العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91810" target="_blank">📅 00:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91809" target="_blank">📅 23:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">كوريا الجنوبية:
وافقت كوريا الجنوبية على إبقاء عملية نقل أسرى الحرب الكوريين الشماليين سرية بسبب مخاوف أمنية ودبلوماسية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91808" target="_blank">📅 23:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91807" target="_blank">📅 23:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91806" target="_blank">📅 23:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91805" target="_blank">📅 23:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في محافظة دهوك شمالي العراق اصابة ١٥ شخص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91804" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91803" target="_blank">📅 22:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">إعلام بريطاني : الهجوم يقف خلفه عناصر من استخبارات الحرس الثوري الإيراني</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91802" target="_blank">📅 22:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
الخارجية العراقية:
القوات الأميركية أنهت انسحابها تماما من العراق، ويونيو المقبل سيكون موعدا نهائيا لإتمام عملية سحب سلاح الفصائل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91801" target="_blank">📅 21:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
مشاهد أرشيفية من سجون النظام البحريني للحظة إعلان استشهاد سماحة السيد حسن نصر الله وردود فعل الأسرى عقب سماع الخبر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91800" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مشاهد ارشيفية للشهيد الاقدس السيد حسن نصر الله والشهيد الجنرال قاسم سليماني.  الشهيد الحاج قاسم سليماني قائلا: سأضحي بحياتي من أجل شخصين؛ أولاً، القائد الأعلى للثورة، وثانياً، السيد حسن نصرالله.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91799" target="_blank">📅 21:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91798" target="_blank">📅 21:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
وزارة خارجية الاحتلال الإسرائيلي:
ستنتهي حصانة دبلوماسية المبعوثين الهولنديين في رام الله في غضون سبعة أيام.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91797" target="_blank">📅 21:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=fuiLyT9G6uDAcAz_lexcb9MCm5_rIWCzQ5rs6DTDzgHkdv_7FZW-RP2bhkab612K6hAbAo8QjPR0B5NSQjMrbWpmKi7pc7aMGWDY8np8WyxKQ53sxwmS7YHn1UMJ8txlJv7I2KO_isPEgySqcl381HKORkIvFIYc0Gt15fbONVqZfH5Xiws9PgFmZ-ZhHBRpIyxeih6LNOyOTzNRzkAVu9irLr4k8l134IuapYZ7enDOD0P-gvwmxbet7dtWoUoNvGHQeFY_Pn7EBf_hJddchJaKL9JymgrQs0bhfAQtERcpFufuiXxgopR6fEjxQL179kUDok-gNBnrGkhoFLqBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=fuiLyT9G6uDAcAz_lexcb9MCm5_rIWCzQ5rs6DTDzgHkdv_7FZW-RP2bhkab612K6hAbAo8QjPR0B5NSQjMrbWpmKi7pc7aMGWDY8np8WyxKQ53sxwmS7YHn1UMJ8txlJv7I2KO_isPEgySqcl381HKORkIvFIYc0Gt15fbONVqZfH5Xiws9PgFmZ-ZhHBRpIyxeih6LNOyOTzNRzkAVu9irLr4k8l134IuapYZ7enDOD0P-gvwmxbet7dtWoUoNvGHQeFY_Pn7EBf_hJddchJaKL9JymgrQs0bhfAQtERcpFufuiXxgopR6fEjxQL179kUDok-gNBnrGkhoFLqBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.  @Naya_Press</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91796" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
مشاهد حطام طائرة استطلاع مسلحة نوع "كاريال" تابعة للعدو السعودي أسقطتها الدفاعات الجوية في أجواء محافظة حجة - 27 سبتمبر 2026م
.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91795" target="_blank">📅 20:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب: الاعتقالات في المملكة المتحدة تمثل تطورًا إيجابيًا. المشتبه بهم كانوا تحت المراقبة لفترة طويلة، وقد تم القبض عليهم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91794" target="_blank">📅 20:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 26 غارة جوية من خلال طائرات "F15" أقلعت من قاعدة خميس مشيط واستهدفت محافظات تعز والجوف ومأرب وذمار وصعدة.
‏وخلفت عشرات الشهداء والجرحى من المدنيين
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1085 غارة جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91793" target="_blank">📅 20:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpWifn8q_inei4scOcRIPRbvNEdyPiU-5-PTbAOoQMGhI0M3CAqiLvIP9TtKrQo_gLyolzs_dRjGMtL1UhZKS02nbkh8y4sIANC2a2wbM2MqcEs-wbaQ0gcb68a1755FY0C3S05qdnvMh52j4LW0SwfR-cS6CxVrmUAl6Dya9XmSdIq48JL19j6uL4XcijEGtSV1TnBFEj6E9TYBs-TNMaf5-CmHaWb3s-qlMexdofadsx-EzyzZdwNmd85IobVdvCKBh68IuUXdRsh1NE388n0KncgFGFDpPnZxU36fOmoomG7pHr1Z2orDf2_ncutsCnKf1YmjIF7F2FLm0Cd3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مشاهد جديدة من الاشتباكات التي حصلت في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91792" target="_blank">📅 19:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=jIXs5uu6bjP_W4wRTabeGXlWLwWZxXhbHsyPIm18QK2_0vFqKHWPT04C5bKkSnDpQ5-GJoAAPRQfKBh10hc59GvH5V0w8fwpAIZctjNMWETHpFVVOUc_mvj_e3-HYXvOJfoCRaA7EkzMEzRmmo31_Q7RZUXBzs9phwCcoL9nJRyV2J14g5v-UqaxVdYi6biQT-olJuC6KR4GnpUwn6SoK05yHhWVxJnXOowdk5ZyoNfUqjqofClAIV6Rlm89MMHRy1lmVG-QtigXojvq0NqaVtr0eTk8PYqYFFNPmlWyP-FkeC9zScD1N0cxUb5cMT-YOwxkvQXmaFPMXl0muuzCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=jIXs5uu6bjP_W4wRTabeGXlWLwWZxXhbHsyPIm18QK2_0vFqKHWPT04C5bKkSnDpQ5-GJoAAPRQfKBh10hc59GvH5V0w8fwpAIZctjNMWETHpFVVOUc_mvj_e3-HYXvOJfoCRaA7EkzMEzRmmo31_Q7RZUXBzs9phwCcoL9nJRyV2J14g5v-UqaxVdYi6biQT-olJuC6KR4GnpUwn6SoK05yHhWVxJnXOowdk5ZyoNfUqjqofClAIV6Rlm89MMHRy1lmVG-QtigXojvq0NqaVtr0eTk8PYqYFFNPmlWyP-FkeC9zScD1N0cxUb5cMT-YOwxkvQXmaFPMXl0muuzCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91791" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=R8xlYyhnUdlv3ROSInoE4rh712UOd2-dhtJtnZYGVmkxRgtA2AgNv5y_eNLqWnMFixKqTnAqORMClmJUm_KXd-CBtK6sbu-iexbwpfeNxDaLMFqtiixqAQmcfIYQdrvLB9vt0bxoNvsyX8RkvX3lr_B3Esh6uq_pMxV9lAbSxWygDKexvE9rVzLUp2Q_6k0ee3VWHWHsyULdZhYSck8Y9UApGAF-WyiFi4QOFm8QI0zA8Ai6guO2LPuaUp0Yl828X-4ocIdChFTX2t9Srqgm9Eyxzt8KQgHgwaeWgnbNTiwMexSF6wLWk2KaJZ0AFGosEEiCaiUPE1veUMJ0gl7KiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=R8xlYyhnUdlv3ROSInoE4rh712UOd2-dhtJtnZYGVmkxRgtA2AgNv5y_eNLqWnMFixKqTnAqORMClmJUm_KXd-CBtK6sbu-iexbwpfeNxDaLMFqtiixqAQmcfIYQdrvLB9vt0bxoNvsyX8RkvX3lr_B3Esh6uq_pMxV9lAbSxWygDKexvE9rVzLUp2Q_6k0ee3VWHWHsyULdZhYSck8Y9UApGAF-WyiFi4QOFm8QI0zA8Ai6guO2LPuaUp0Yl828X-4ocIdChFTX2t9Srqgm9Eyxzt8KQgHgwaeWgnbNTiwMexSF6wLWk2KaJZ0AFGosEEiCaiUPE1veUMJ0gl7KiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثث عناصر داعش بعد اشتباكات الاخيرة التي دارت مع قواتنا الامنية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91790" target="_blank">📅 19:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7_mzG-LhW7K3ns9vjb5SlIkDRXz0ymdOXB7qr8A91i6rHujqNAJ2hAAtuH3fSwaNGUwShSC0baQS3Dx31OgnZs5R2Jb0ha1oPIiSKXNOud7lTXDML8B1dJAchwdAY980ZFMPMSZflxPtY-F21vxOewWVFgGfoXy8c7av_npJ96jeIfvSe5tMm1p1EBcUTXRlyf6mz8kuZLg4o3qSR_0C2YIypr82jZrl4CVAmROLi10VMDGss4YwELLHhfmsh2neSGq0Gm3S5OgNtziAGdSeGcY1zlb35Q-vKccyBMn4-RofoTHTB1gzAWlYEqJP6dc8D5FWPQMMKkitxzY5gwdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSoeVBF_tlEK5W9d-4tvPw13Q_ldOu6wQvQy29GojwCVi9wyLFYVzKllZLpdUFtVuNefOe9SqyOdYQgbGiHJ_wkW1IQOMYk6_pUipb1ljvYMnCCLY4PdZkx1OTipag2O-yMzFlR9ulldnJN4Cfl33AIdc_QKOszvjuSwGtqEcmQ1V6Qj04HMpmGBZfoWSrHEU4NNw9rrkDdV5Z0OX89vh3ocKqZ6Agp7LwOvgjWTTWxuqKhLQUImpVAR92UHa11bggHmG2Pcd1VRktUdbGSAD7CN4LA5pBNpiFJ8WVhICMGYWZKiGan8-lFBUoy_fVfZM_iwfqf6P2ABTjCfqwVT2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91788" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=rbzQ2peZO_r3lgYAIPvpTbSeh14xNwpo82IHUTAXQ4phhHb1zajXjKWPJRq-4G8pkJ7kja2OZvvk4e8nE-SquaGdHqDKzJOpNDj-56Nvn0lDTApNGX_E16f0XjHsn4SH1rxCpt9dO6EgppIFqPVpV6hTgAjnuwJ-PtHaids8MJve3zJQ2HFa_N3hobe9FgEVIM9rp1ogrl194ojbLGYTT8T-es-UJgFnwh0RT9S_MYbuP_h5xtsWgSxwAjSIs1ad6xHIF80Rc4Vjvr_BoBLnF5A4bJSXBRalTKRthy0pj5nP9Cw--GDkZslR8hmghX0ubMWUlkw8LPx6Pa8R8rzEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=rbzQ2peZO_r3lgYAIPvpTbSeh14xNwpo82IHUTAXQ4phhHb1zajXjKWPJRq-4G8pkJ7kja2OZvvk4e8nE-SquaGdHqDKzJOpNDj-56Nvn0lDTApNGX_E16f0XjHsn4SH1rxCpt9dO6EgppIFqPVpV6hTgAjnuwJ-PtHaids8MJve3zJQ2HFa_N3hobe9FgEVIM9rp1ogrl194ojbLGYTT8T-es-UJgFnwh0RT9S_MYbuP_h5xtsWgSxwAjSIs1ad6xHIF80Rc4Vjvr_BoBLnF5A4bJSXBRalTKRthy0pj5nP9Cw--GDkZslR8hmghX0ubMWUlkw8LPx6Pa8R8rzEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.
@Naya_Press</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91787" target="_blank">📅 19:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJABaBsML21pTZApH31QElZmjMsOBI45XIARJI6C-jCkbPknoM4PeoQ1zNQZQo7nvVCQgWWNMywLL6y1U1XGckPtUqvaG9gDVTuG1RKFT9cAWOboTpha4mYNBVFvlDdctmCVPoca-UJmDLvuwfBr0LN8o0hWEzzHdt4AEenaKEnII0B38-v2OCKxo9Rn_Krs3aVuLv095CpJP_kd8pb8bnRgDRviPBWZinOBI3a1eN_yMlnZhiRrklcDDi2bmU6FI1Uxld9q4aPDdFNieznMOnBAgusbgYDbxlRTDli7vxHfg3R1XGvzR2GkSnNujO3yIpGObUzczb1Zt8bLzaIXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91786" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91785" target="_blank">📅 19:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
الاعلام السعودي:
مباحثات وزير الخارجية العراقي في واشنطن ستبحث"استثناءات" بهبوط الطيران الإيراني في مطارات العراق. ‌</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91784" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95cba77d6e.mp4?token=qYym3R0cRsv8HBXghhS6nHHZVCnyZ9klt3lYQhhGoWg4StvequVVJ7CTklldfBggoiE6UVldp_IVb5RZR1_jkgEuPcK_771jKlCN5x3OEHQL49LyPbrZmfwNj5cxXV6MQuXT6Awty7srg5_d4XsTfPDf-LLk-vDyGoAg8wkWbQiXbzW5OWyAuQegUpTRqF6ySkJBNdiDZiFeUL4ojQ_U7POFG5uF9A6Iqcug8Q312NOI4JX8wraoOP3HJNUF0OnL_Lzq0AloHDeJBB0LJh3yvIXEHpoyX6P6kVn5JQD8XbTil55DgeyT5I_05LMibaIoedJTF_EbNUHmwuoxPhpKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95cba77d6e.mp4?token=qYym3R0cRsv8HBXghhS6nHHZVCnyZ9klt3lYQhhGoWg4StvequVVJ7CTklldfBggoiE6UVldp_IVb5RZR1_jkgEuPcK_771jKlCN5x3OEHQL49LyPbrZmfwNj5cxXV6MQuXT6Awty7srg5_d4XsTfPDf-LLk-vDyGoAg8wkWbQiXbzW5OWyAuQegUpTRqF6ySkJBNdiDZiFeUL4ojQ_U7POFG5uF9A6Iqcug8Q312NOI4JX8wraoOP3HJNUF0OnL_Lzq0AloHDeJBB0LJh3yvIXEHpoyX6P6kVn5JQD8XbTil55DgeyT5I_05LMibaIoedJTF_EbNUHmwuoxPhpKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91783" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ad809475.mp4?token=Idyc8a0lgc4igvNmOPsVSGC49JV7gx0Pwab1U5zXdxgBiDcIQ9LPxOYKK5OPNICBg9uW3LvldlmzWeV4dpwRBu3doCmj7PDWMjgpE-NBvSkngS0bzncxr1AEbG1UdVds6CXB1OowSvYsamiLlfpuVKRSF_BwBihzGjFcw3v9045qEET9_2IMG3qrcnnLcm35FoLAgqL9ROOmhPy1bStIv0G7O5OvRn4IY6Qw0LDvX5_K6-8N1epAptknxTZsmF97y-4--vm3q22wHhJlkEMKRrW4KaLny6Xh6f7ptaRaKG2_xeAAkG734EpOZxdHPFREyxddQSqJMTYMmgo_DEmv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ad809475.mp4?token=Idyc8a0lgc4igvNmOPsVSGC49JV7gx0Pwab1U5zXdxgBiDcIQ9LPxOYKK5OPNICBg9uW3LvldlmzWeV4dpwRBu3doCmj7PDWMjgpE-NBvSkngS0bzncxr1AEbG1UdVds6CXB1OowSvYsamiLlfpuVKRSF_BwBihzGjFcw3v9045qEET9_2IMG3qrcnnLcm35FoLAgqL9ROOmhPy1bStIv0G7O5OvRn4IY6Qw0LDvX5_K6-8N1epAptknxTZsmF97y-4--vm3q22wHhJlkEMKRrW4KaLny6Xh6f7ptaRaKG2_xeAAkG734EpOZxdHPFREyxddQSqJMTYMmgo_DEmv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91782" target="_blank">📅 18:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مشاهد من الاشتباكات في محافظة كركوك</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91781" target="_blank">📅 18:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترامب: أفكر في استئناف الضربات على إيران باستمرار، والاتفاق الذي طرحته إيران كان يمكن أن نوافق عليه قبل عام من الآن، أتوقع أن يجري المفاوضون الأمريكيون مزيداً من المحادثات مع إيران هذا الأسبوع.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91780" target="_blank">📅 18:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
ترامب:
أفكر في استئناف الضربات على إيران باستمرار، والاتفاق الذي طرحته إيران كان يمكن أن نوافق عليه قبل عام من الآن، أتوقع أن يجري المفاوضون الأمريكيون مزيداً من المحادثات مع إيران هذا الأسبوع.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91779" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b035464a0c.mp4?token=PXDIcMFovYU_4sfNmib0XM7m4EozXSwhHsQlmDWeHxuGK1k_FLUhDmLzCp-grXfZ_7qAZK3DDoDFPza4hc6IPc8FVgmftHl-pdDhglsRiBj_HqaQT3nPjCA7jMQ_SbC-uvQXuYw0eOO0UFphBQsfOn1A6DEvVEJGsXQnzSX0PI_KuYLcmt_MjUZjidsn8X4CMdaiDodAQd005CcFyvMUGCHNiPdovJg040daQwoAcdAwX2yolUov7Oz6L-eLxffKyMdIlm00y8D0kwILNAo1B8NRyhoAL4lAoPhrfsamCvUHzkjJ-x1ZVKMOLSPIJkqoIICXgm35c2B9NkRTS_7Bsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b035464a0c.mp4?token=PXDIcMFovYU_4sfNmib0XM7m4EozXSwhHsQlmDWeHxuGK1k_FLUhDmLzCp-grXfZ_7qAZK3DDoDFPza4hc6IPc8FVgmftHl-pdDhglsRiBj_HqaQT3nPjCA7jMQ_SbC-uvQXuYw0eOO0UFphBQsfOn1A6DEvVEJGsXQnzSX0PI_KuYLcmt_MjUZjidsn8X4CMdaiDodAQd005CcFyvMUGCHNiPdovJg040daQwoAcdAwX2yolUov7Oz6L-eLxffKyMdIlm00y8D0kwILNAo1B8NRyhoAL4lAoPhrfsamCvUHzkjJ-x1ZVKMOLSPIJkqoIICXgm35c2B9NkRTS_7Bsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اغلاق مداخل التون كوبري مع تواصل الاشتباكات بين القوات العراقية وعناصر داعش</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91778" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب: اشتباكات لابطال الجهاز مع فلول عصابات داعش الارهابي تسفر عن مقتل ارهابيين اثنين يرتدون الاحزمة الناسفة في كركوك - التون كوبري وسنوافيكم التفاصيل لاحقا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91777" target="_blank">📅 18:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الشرطة البريطانية حول حادثة قاعدة فيرفورد الجوية: تم القبض على 5 أشخاص بالقرب من القاعدة وتم إبلاغ 85 أسرة بالإخلاء.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91776" target="_blank">📅 18:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الشيخ نعيم قاسم: قررت شورى حزب الله تسمية كل المرحلة التي بدأت مع معركة أولي البأس الى اليوم مرحلة إنا على العهد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91775" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم للسيد نصر الله:  أنت المقاومة والمقاومة أنت وأصبحت رمزها لأحرار العالم. أنت القائد المقاوم الأممي تلهم الأحرار في العالم. غادرت بجسدك وبقيت تعاليمك وبقي النور للعطاء الذي يمدّنا بالعزيمة. لقد بنيت حزباً ومقاومة وحالة شعبية ثابتة وقوية وسنستمر…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91774" target="_blank">📅 17:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسرور البرزاني: يعدّ سحب القوات الأمريكية من العراق تكرارًا لخطأ باراك أوباما عام 2011، حين سحب جميع قواته تاركًا فراغًا أمنيًا في البلاد، ما أدى إلى ظهور الجماعات الإرهابية. إذا تدهور الوضع الأمني ​​بعد سحب القوات، فقد نطالب المجتمع الدولي بالعودة إلى المنطقة…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91773" target="_blank">📅 17:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اشتباكات عنيفة في محافظة كركوك</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91772" target="_blank">📅 17:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم للسيد نصر الله:
أنت المقاومة والمقاومة أنت وأصبحت رمزها لأحرار العالم. أنت القائد المقاوم الأممي تلهم الأحرار في العالم. غادرت بجسدك وبقيت تعاليمك وبقي النور للعطاء الذي يمدّنا بالعزيمة. لقد بنيت حزباً ومقاومة وحالة شعبية ثابتة وقوية وسنستمر على هذا النهج. حملت راية فلسطين وزرعتها في حياتنا وستبقى فلسطين هي البوصلة وتحرير أرضنا سيبقى أولوية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91771" target="_blank">📅 17:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf84221f5.mp4?token=YCJ9uip07Tlay5OXau2Bx4R-SHtU0zp7xFN1RveCuR-waWqd0guqfkiHFuFwp1XMhvpiKr5j0xXzD0GJiady0Bhd0Tzj7qOHWi_k3ZOjdklt46YD2xNJ1AK88eEM7tlIset8_1ZulQfpLs147Btfzez3wh076FUUUAN8TTLglHGD6Co9kHW98QB6RKVSFDkcY9k1HeofIbeu5nMnOQ3iY0hlqt34YLMCfnzGFNDSBuew-wTwo8607vmslXdsJDOATrh6kf3paH0nljCvMTjf3Sj5_6gxh9QyHPAS4oWupQYYTN7E3BwJTZ3T1bNxwasaaeaJEU-E2K9xXqvUxYjkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf84221f5.mp4?token=YCJ9uip07Tlay5OXau2Bx4R-SHtU0zp7xFN1RveCuR-waWqd0guqfkiHFuFwp1XMhvpiKr5j0xXzD0GJiady0Bhd0Tzj7qOHWi_k3ZOjdklt46YD2xNJ1AK88eEM7tlIset8_1ZulQfpLs147Btfzez3wh076FUUUAN8TTLglHGD6Co9kHW98QB6RKVSFDkcY9k1HeofIbeu5nMnOQ3iY0hlqt34YLMCfnzGFNDSBuew-wTwo8607vmslXdsJDOATrh6kf3paH0nljCvMTjf3Sj5_6gxh9QyHPAS4oWupQYYTN7E3BwJTZ3T1bNxwasaaeaJEU-E2K9xXqvUxYjkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات في محافظة كركوك شمالي العراق بين جهاز مكافحة الارهاب وجهات مجهولة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91770" target="_blank">📅 17:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2246b444.mp4?token=IWcKA2eZ7AtKIag1umQpU2ng0vWbUTKZSco-kb2BpCcFxMUkXJr3SOoBwpQvV6T2oOlpkneiyt6fTJ6wyqSwvqDkuout78OIViIIU5SaFwlbWZ_bLbbFVX0JFTwh2nRLdosPYPrYODpkQ3PI0tYzljk5RJHRa-0d_2JUK3KHbHmuczeDaWcrLWBeoftnqMTXP80A3dDXSQ5902RnSdWg-xkN6AOAbmxyh6D6nDEUj8t_vFN1mTIxtBzppHhdJQ4S0vQTPIgzsAZtXbQtnScSNuL13v6ZUET-pN4h9g4X1bAqVZHmW1OtjeIZf0BMgyEmz4_e-2cIS72R5JP6ltEreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2246b444.mp4?token=IWcKA2eZ7AtKIag1umQpU2ng0vWbUTKZSco-kb2BpCcFxMUkXJr3SOoBwpQvV6T2oOlpkneiyt6fTJ6wyqSwvqDkuout78OIViIIU5SaFwlbWZ_bLbbFVX0JFTwh2nRLdosPYPrYODpkQ3PI0tYzljk5RJHRa-0d_2JUK3KHbHmuczeDaWcrLWBeoftnqMTXP80A3dDXSQ5902RnSdWg-xkN6AOAbmxyh6D6nDEUj8t_vFN1mTIxtBzppHhdJQ4S0vQTPIgzsAZtXbQtnScSNuL13v6ZUET-pN4h9g4X1bAqVZHmW1OtjeIZf0BMgyEmz4_e-2cIS72R5JP6ltEreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات في محافظة كركوك شمالي العراق بين جهاز مكافحة الارهاب وجهات مجهولة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91769" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5tZXyTbApcvLi0X1Eva1r32Zbaeko-OgtELIl9nycLrXKuZI6OtN43B6TMGjoMrz2c6wKnBTm3BzGNlQP5fELfuBG-ZiYSVkw67ZYsvfoDcQI-uulUJXwyeBb1UTsaY3nKOb0SyY8SmdyMMTsSp8tC23XKV2ywLnSrl_tZOhHhZm3om7OgaXybpFa6AAejXZJNpECv8rymjfEnZ7dwpt3ACeB2ICyqPgyk6aSx8UO-hCCEybVi4BMdDBzuli94U-vRv0758BTOoZFlM4McwOlAS1zQ_l1SdB89NZnqIRZ9D1oy7NtFlwZcw-cD39daOvtnzOM8y9HAPRhJXqQB9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس المجلس التنفيذي لحركة النجباء يدعو أبناء الشعب العراقي للاعتصام أمام مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91768" target="_blank">📅 17:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
مسؤول عراقي:
- تعليق الرحلات الجوية مع إيران رهن بامتثال شركات الخدمة الأرضية لتعليمات الخزانة الأمريكية
- غياب الموقف الحكومي المعلن بشأن الرحلات الإيرانية يعود إلى حساسية الملف
- اعتذار الشركات عن تقديم الخدمات قبل الإقلاع وبعد الهبوط أدى إلى تعليق الرحلات الإيرانية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91767" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب:
أصبح النفط الآن أقل تكلفة مما كان عليه في عهد إدارة بايدن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91766" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
اليوم الأحد بتاريخ 27 سبتمبر 2026م وعند الساعة (11:00 صباحا) اتجه تشكيل حربي سعودي نوع "F15" من قاعدة خميس مشيط باتجاه محافظة تعز وشن غارتين على سوق تعز في مفرق ماوية عند الساعة (11:29صباحا) مرتكبا جريمة نكراء بحق المدنيين خلفت قرابة الــ50 ما بين شهيد وجريح كحصيلة أولية، ثم غادر أجواء تعز في تمام الساعة (11:37صباحا) متوجها إلى محافظة الجوف وشن أربع غارات على مديرية خب والشعب، ثم غادر محافظة الجوف عائدا إلى قاعدة خميس مشيط في السعودية عند الساعة (14:00).
إن هذه الدماء التي سُفكت ظلماً وعدواناً في سوق ماوية بمحافظة تعز ستكون عواقبها على المجرم السعودي وخيمة بإذن الله وقوته وما النصر إلا من عند الله.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91765" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91764" target="_blank">📅 16:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نظام الجولاني يطلق سراح (59) سائقاً عراقياً</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91763" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
إسقاط طائرة استطلاع مسلح نوع "كاريال" تابعة للعدو السعودي وذلك أثناء قيامها بأعمال عدائية في أجواء منطقة الطينة بمحافظة حجة، وتم إسقاطها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91762" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارة الدفاع الافغانية:
عشرات المسلحين عبروا خط ديورند يوم أمس في منطقة كامديش بدعم باكستاني لكن قواتنا أحبطت الهجوم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91760" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaRsMtbO-pz7DtQvASNUrHqbd72AhyFpA3d_9peDliy158W2zA4fOmXo_57W_xdtjarIyK1_ipyZBPmKEMqosSE96qCSY-tfr9fnx5njWVfQ0OqxD4A6NtHORCuhQNImCe4ecporU3Aev29n6ASeKYSe3jhWSi7qSmR3E81_GiCHrHki7M0YdBa2Yyro4tfj-nu9po4mn6Cy52UWZTChKMEayV61THQq31Xk03UY1sGY210v3z01-znFnSYihwebt_E27Fz7vKhNLH6lBQmUGDkCyy-nAIzJuFPd6rsOjnDFAp9A4SPDQkalt3BYj9V0UF26wkion4bQXuQ3YskGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
السعودية تقرر تعليق الدراسة الحضورية في الرياض وتحويلها الى دراسة عن بعد بسبب هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91759" target="_blank">📅 14:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91758" target="_blank">📅 14:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91757" target="_blank">📅 14:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مشاهد للغواصة الأمريكية التي استولت عليها القوات البحرية التابعة للحرس الثوري في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91756" target="_blank">📅 14:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
🇺🇸
الحرس الثوري يستولي على الغواصة الثانية التابعة للجيش الإرهابي الأمريكي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91755" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91754" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91753" target="_blank">📅 14:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4EeRuOE45dgiigV8V-We7eW2VUE-OW62CfX2hQjfM3LUdu145cEFqcFcrHXXbLcYSk59OHGwnMzeowt0f7kvpj17zefg7gB4CcfyjnfZlm4Mp2Wdxi8NqIIqC_zYpDMubDXUN5u85f3mabNsZ2XxcsWWppgWmk67vikHSamn7Fatsrd-9UALGmLqPeSTOSZR4MTKkwhsHpkyTKjUEMQR2nrdpNXukXaQ8VRjEo-Vtjk7hU8FfULJ_eGpZVgDAYo7VDD4gviSB_ggJNU5QNfr-VX5zOKjbZNwDbqP-kYqXmKPLa0zGrc0MShQgLL0vMVrUjTYj4ejoGNBsJEA56Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جماهير النجف الاشرف تدعو لوقفة احتجاجية عند باب دخول مطار النجف الاشرف الدولي يوم غد عند الساعة الخامسة عصرا لاستنكار قرار منع هبوط الطائرات الايرانية في العراق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91752" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
تبادلنا معلومات مع الجانب الالماني احبطت مخطط إرهابي في مدينة هامبورغ.
‏زودنا إسبانيا بأدلة أدت لتوقيف إرهابيين اثنين.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91751" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAveeC3icZ_SUj208TkiUd-N829rZprlbrwHMGo1sxu0tgbpwaxy8PLvU8xJiH0Jq4936AMJblJ0KndzTZ9Y-ivJi6I8TNng8oPY-qPdXZrn7lHd4e9n1mZ8vH_--pdbxGy-hkf1i5IQqlwfbbY8WZy8j4drW8Z84E2RQ1OCH63CTyQaHgj_PsRVKT7IgeDJCn6f8A5TEJwMsKCYfwsqOX-zBH5S1GyOMgt2z_pLbMsjygZr_s2MqeQHuj2HKr5n7Jr7YSHn2VVlBET33-IIY-SXWTJJEVR6GLX4w1AqMejxE8eTX8eQ2fdpaaK9F0KXPVt7lOR8lG3Fda8WLzSeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMlrH_N8w-_ZA1Gpn_poc-dwD_kShEFM7y9Lz8hAOjDOy74eio3j7qIL0xODi0MhIz6bBL8AyZzNUh3m-FXXGdSipW01ngzf3pixy3W-zTWDxm-Uu-XfaH0Gy8GP-5g2_5SM7v3USTVAkPv8cuknYrAUaqJqMlh7FleFCRK0Iu1CqmQM4ORcQy1U20yQmShL8gmuBKJiCK7qZZSNY3XRuqFZ-SKgqJAhQ7TARsDkGVgZkUkdiU3Ir8XQEAgCmZ2JLYT13k8Y-0a1EiWEan4ugtXEQvyfRTvX9hYK696lWg9VLYZ2wByjAkB7dPeXK3-sRoj-VoJcF2wdPUwb_CJbdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران الحربي السعودي شن عدة غارات على مناطق سكنية عقب إستهداف مواقع عسكرية تابعة لمرتزقته في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91749" target="_blank">📅 13:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من العدوان السعودي الغاشم  على مناطق سكنية ومحلات تجارية في محافظة تعز</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91748" target="_blank">📅 13:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
سلسلة غارات سعودية على مناطق سكنية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91747" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
رداً على إستهداف مرتزقتها.. الطيران السعودي يشن عدة غارات على مناطق سكنية ومحلات تجارية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91746" target="_blank">📅 13:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91745" target="_blank">📅 13:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91744" target="_blank">📅 12:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
وزارة الدفاع الأفغانية:
مقتل 28 مقاتلا بعد عبورهم من باكستان إلى شرق أفغانستان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91743" target="_blank">📅 12:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91742" target="_blank">📅 12:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91741" target="_blank">📅 11:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
قائد الجيش الإيراني:
الحرب لم تنتهِ؛ وعلى العدو المعتدي أن يستعد لتلقي ضربات قوية.
إذا كان هناك عدم أمن في المنطقة، فسيكون هذا عدم الأمان للجميع.
لقد رأيتم أن التعاون مع الولايات المتحدة لا يخلق الأمن. الأمن في المنطقة يكمن داخل المنطقة وبأيدي دول المنطقة.
لن يتحقق الأمن في المنطقة إلا بإزالة الولايات المتحدة والتخلص منها، وكذلك من إسرائيل، من المنطقة، وهذا الأمر ليس ببعيد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91740" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91739" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91738" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=V-9y2iVuOVhbh65rY49ouxu9UsEppdvPzZPGvdtkTxDekZjSvkS2dAtt6597m0fSWujTam1njXvPWU5EE3ClL1XttE99H_bZSds50dnb8EfiFLnFXmr4F-wdBT8BZFJjGuujHd78YpepnkcapscONf1SdLrVu5XsM9D7X3wEOXxmhCDcW_ydW7SIJbk0U3jCWk3yWiw-Tjz_82Q70uhiIMxH_2ZCqLkD24iq6IfOnNgBHyfv802wDHnp1q1LnDU9M5MTPed3Pa5b0p3CNAMjaRNL2dfOhnT0ylGjqRI2waaK1M85-o8PESleatx-4Zsg8ldoAN7QPJtHfaD6R6g6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=V-9y2iVuOVhbh65rY49ouxu9UsEppdvPzZPGvdtkTxDekZjSvkS2dAtt6597m0fSWujTam1njXvPWU5EE3ClL1XttE99H_bZSds50dnb8EfiFLnFXmr4F-wdBT8BZFJjGuujHd78YpepnkcapscONf1SdLrVu5XsM9D7X3wEOXxmhCDcW_ydW7SIJbk0U3jCWk3yWiw-Tjz_82Q70uhiIMxH_2ZCqLkD24iq6IfOnNgBHyfv802wDHnp1q1LnDU9M5MTPed3Pa5b0p3CNAMjaRNL2dfOhnT0ylGjqRI2waaK1M85-o8PESleatx-4Zsg8ldoAN7QPJtHfaD6R6g6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
على الرغم من الحصار الجوي الظالم..
رحلات الإقلاع من مطار الإمام الخميني بالعاصمة الإيرانية طهران تتم وفقًا للجدول الزمني المحدد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91737" target="_blank">📅 11:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
الشرطة البريطانية:
حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.
اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.
إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91736" target="_blank">📅 11:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي في هذه الأثناء يتسبب بإنفجارات عنيفة وسط العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91735" target="_blank">📅 10:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي يزعم:
إطلاق مسيرة انتحارية من قبل حزب الله نحو قواتنا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91734" target="_blank">📅 09:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني:
يجب على إسرائيل الذهاب إلى الحرب في الضفة الغربية كما فعلنا في غزة.
يجب ضم جنوب لبنان والأراضي التي يسيطر عليها الجيش الإسرائيلي في غزة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91733" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=TcNvgqShsnefM2NKRwRQJzaA01bfd5AyNjZNTVN0aAkoYhe00nmT6CyfMuERVK6egegXxxUyq5qkOrNYpPaBLyoY5F5nWBHPf6LempCDIz9wXv2NS-1N0X5mhYksSk-9R7eAgPpV8TUDJPOBZ01IVWo5jHAm1hjCCxULWvH_1jvqX53xRVcDFjWLATJzDTbm07yTTCSGIDnMlXPbgujjmGZMpLagrIIz94_n_WygG_z_Bb-uP0h2LAOd2_od81iFz2Z56QNOOJoCifK536fExX8jTol0ZTlbHCK_1FdxUIZhDN2iICDzDWyCsA0lwvaOiIPUB9rbDQ5rs-yGf3Y6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=TcNvgqShsnefM2NKRwRQJzaA01bfd5AyNjZNTVN0aAkoYhe00nmT6CyfMuERVK6egegXxxUyq5qkOrNYpPaBLyoY5F5nWBHPf6LempCDIz9wXv2NS-1N0X5mhYksSk-9R7eAgPpV8TUDJPOBZ01IVWo5jHAm1hjCCxULWvH_1jvqX53xRVcDFjWLATJzDTbm07yTTCSGIDnMlXPbgujjmGZMpLagrIIz94_n_WygG_z_Bb-uP0h2LAOd2_od81iFz2Z56QNOOJoCifK536fExX8jTol0ZTlbHCK_1FdxUIZhDN2iICDzDWyCsA0lwvaOiIPUB9rbDQ5rs-yGf3Y6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اللاعب زيدان اقبال: الكويتيين يطلقون تعليقات عنصرية، أنا أفوز، إذا أحتفل. هذا شيء طبيعي. لا أعرف لماذا يأخذون الأمر بحساسية بالتأكيد سأحتفل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/91732" target="_blank">📅 04:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91731" target="_blank">📅 03:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ccsw7wTW3Z_xqv_G9yKUdtE0vbhpFD8QtW43OTpA89AwCuv7OD-5aiO_a9cv9svy5g6a-H5WmnrlxrIx3K9k-D6NDIhlzbmQG-PEq7mDrVc0djzAyTuahqejjkm5YaQnGgCMTO7KSGpzoli-Nd0ArtZ7s2yjjhced4i7CQDWEhuV4Qc8gXVuECFYApip-rq6_B5D_iP-Mm3mtAbmhucj6v0CTAKBXEY3Jx8aS-rQXQSw59BcPUIOIjugRo-Fi_BTYwP4PlSrpCtxusUO5UWtDgDv6xw2OEFlpz83-q9t5r5At3WK79gWZ3y_gtj054-F-br-NLZUR8I3StZv7F5fRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91730" target="_blank">📅 02:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=YBxqgoQIO5ineuwYUThFs5SGmyeEkTs1fxjTqUbyGBQyluEdDnA6nxHRfb3Mpb0ASIpIH0lPtSNPq6Ml2RqmQ8SW_5Sd-mgJVa9mqJ2KSMLVuwmTc3FR1A8zSaf26o0VMOBNdF59PxZfj6nWqrF_cJV7NciAF9qp3jC6YNFaCkYdmBzD-TG9175CAv3m5FULNyiAt15wc228BBzBTUzmh3Z_rKv-UCw4oAkOPkqzc2MVuqCtF08v0NUQ4PRbfWvitXd6RwhOgkailInaQfZETjFEKJLTlyVUTmzG5LkIwrSphHPUP7rR-B4N31qlGizEddvOEmYPBdtWEaHxHn5rGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=YBxqgoQIO5ineuwYUThFs5SGmyeEkTs1fxjTqUbyGBQyluEdDnA6nxHRfb3Mpb0ASIpIH0lPtSNPq6Ml2RqmQ8SW_5Sd-mgJVa9mqJ2KSMLVuwmTc3FR1A8zSaf26o0VMOBNdF59PxZfj6nWqrF_cJV7NciAF9qp3jC6YNFaCkYdmBzD-TG9175CAv3m5FULNyiAt15wc228BBzBTUzmh3Z_rKv-UCw4oAkOPkqzc2MVuqCtF08v0NUQ4PRbfWvitXd6RwhOgkailInaQfZETjFEKJLTlyVUTmzG5LkIwrSphHPUP7rR-B4N31qlGizEddvOEmYPBdtWEaHxHn5rGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫡
هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ
@Naya_Press</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91729" target="_blank">📅 02:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/91728" target="_blank">📅 01:37 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

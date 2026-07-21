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
<p>@news_hut • 👥 155K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 21:20:10</div>
<hr>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_OqoopYPj8H8xYW6nqRttfG73Wr2W7oM758EkYYu_fFDhSdg3WoVtbX3JZdeyZMZZJY2jpojCroNY_QJzGiX7aFIoPhWEBEIAWvr0GAAja_sxIwIaHnNC75W30nDZY2M8_mWLrXXU5-x34XaD_mlnp9-Im8iOCrAJKotgyGrihgLkmnUTFeO_AUo0_L08Vq2vQXOJKlLD0bKdIj7Ii7-oNu2qXBMQBTOPeiDZfAsiPO-5jZbLMXxi8dt7MLNGZnoTxlHwgc2u1v7OPcqe2UGB6-DPLEdDskWJjZnegB2NytdVYxGvCKScRiK6KHAEzK6mEYCVr2hSmsMa3qfLaoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AD9yVaPI6UnIBgEgc1CH4WTut6R9vJdMCs-HCFhlr26b9oNATC4acEdLsNKNbfd4tiyjLOAOOy1s6XGQa0cv5Pl_BSvDuCYGflZm2vu8PNMTMoxOZMAOPL9U1kFnXKnposf3dh_hGtNYX-Tr3xw02ENjzgqyM5jLxypPwaKzjoZOKe-cCFv1DD9TljWemOlQUfyLYz4v6XtN2nW8kIQ8gDO9ey69I0OZ4QocMIqua6-P-ehLvNa2OZkDLdBEcaV2wOYlq8T1t8DnjIQUDk3Ae-LmPSDUGMMKfoqMI_JKN2nS1698Da4UhC1L4ZMw56zaaJqVFPjSZoTLzy6Cr9-dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-1Yp4S9Ue66-D7Ym2yCu2WPztDJS2Ixh2o0yNABCJCMuilRg7rVER7U9iD0EmVNL6y04Aw3_6NVpWDRFkru83L_xcx8PRf7P-AjUtGIV3ba8-sSCYFFdjDjpELSe5DsR7XCHdYTYUDtpwBAKhic0PD__n9nacdQEKWEOkarlE8im7jZpVfjtU7CJikj238E0Fb596MXQ54PvCE6mFXkiREpY12Pt0d3DEsoyd2SoTsW68U4kaebbul7VJ2Fx8D052prYSdSLGzaVoKHYQ3_hw8NJpwPNoMmgee59I5tuas3WUihUhP-ghh0vWEStBsnIrf6hYMyL08TmCEI_kERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l43FwaK9il68Ce9HkJAbVy8vE_x-Iw917uamSbHRjXz89GyLoFTJrwn8-QXBaskw9M8aYzc9Ydo6JKVrTVAWH9jywvsc1Kljb1CwMF5hdCw1h4pSPICo8cI8HvuaOeOHlf1eaqIz6hzLtMoW8w4d6JDPO1wSOB21DB99hwEflZweoveDDoMqwXAPjPx0tyxZ-jC-CI3uTYsJGV0V3VKzbPZ-483RU4MfeFB4_00qFsZofFrf_r9cM_qW2v0luzm4u1lHATpYQc7asIui4tk5_RhlDijWqZwtWjKqMzc3lLCH30KcL5jR5MpKcBV3fu-2x_YpbnzSmLI-BREj7IfY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHL300cIlVUaYCdNQVCb9e9LYYEABLRiXnnNjMqPfb6E6PTxZQnv3nIce7xKuRZJbKWXOAsMxkJk5OLEBD4btDsSRDBQMnJa_GmlGoy_Y6OFgMD7C89YwM_SAl5NYlAAfbAqfgBvOA5jzZvqPnX8lw1WbdLcNSIH2B8bLRrQpB1ir8oktP38Fghsjlpciga9-LN6NvaN4w0RQcbTGcnfj3N6weUbwq03Wv9ZL0LIZoweJiP2Kie9EJlaiE8vG2qfsnyxYw9Q1C8eg1JGNphDxSs8spqj9kO0dq9mztLdqCpEeWDvKL5oa8TS8yMgSTML7ETjAJ3fPe768K2sBbHHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMiydK4ANPGpw0Kf6FGyrtF0UYIqqknDFJkqlFPQJrERMkk-leuez9PxYBW4vAxVb8Nqxno4-jSoN917RvbReiHynIKvDuMSN7taulFpFlRb15K_jw0-qhshB1Tcbw3Uv0zfBcAIPE4EkX4R8xQcYIPJgfGo39I1P6WyVLvcHRU13olUiq_gHfwVw-TrROTPUrmesjRA4hKfsxhawmQqzgZZLttDohNyCI5trYU0H7cERebxebSpyyFZj81bQJYTMmviHoikTs1shHDe2ipl4OKk7nskv2djmBpZ3D42TZ6WBAeKTg2sqXS36Ki29agDS-w05RoH5to44D8rzExvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=Ys6tp-vkx6CsgyGTk7YbIDTk2EyKIR3nI-JXyJzKPTrtSu4gQDggJGwqBXFhGEzV3lOid6WxclTrD6kn9SB56jmXNpx1ultu4TOfjk0NnzKVAEMi2h-vLqUPNq7DKZM9FIQwYBa9dXv8EvMXOZ2ZufPt7JUoi7QpxRaeTtER1Hy01nI5P7wupYn1wVgLpE2lkkzj8RNTLk8WATRq0oThgKhDVcSXRKPnxSW4gjDweDCd5m4AoosfnaJz9VmFl2aJeHgPWCPYYQhd10Lk9bH1fE5J5HzqRuPn-5LMtSKm_bi1a-CzxX5hwc-FtAbe86a3ikwQaJBVmNoqUh8NURyUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=Ys6tp-vkx6CsgyGTk7YbIDTk2EyKIR3nI-JXyJzKPTrtSu4gQDggJGwqBXFhGEzV3lOid6WxclTrD6kn9SB56jmXNpx1ultu4TOfjk0NnzKVAEMi2h-vLqUPNq7DKZM9FIQwYBa9dXv8EvMXOZ2ZufPt7JUoi7QpxRaeTtER1Hy01nI5P7wupYn1wVgLpE2lkkzj8RNTLk8WATRq0oThgKhDVcSXRKPnxSW4gjDweDCd5m4AoosfnaJz9VmFl2aJeHgPWCPYYQhd10Lk9bH1fE5J5HzqRuPn-5LMtSKm_bi1a-CzxX5hwc-FtAbe86a3ikwQaJBVmNoqUh8NURyUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI4THY7zX1FQ2hC8X2wtA6a5KMda-Y4SjSne-U4moNSOC0D0TnCKvncIaEli5VMt7Wz0NCg34dacHP3ldZaDqI191CIoCj-q9D7UVAhyW2hjv1I2Ux2b1uwiAyW79FsexrEbr9k9A9HKMA7lyAcA8lc40fblWC0Ez3QiMubthTG_bHMA8muSg1CAaEMjdnbDfreEYToOfw5YpR9tzHskIPuSYCJ2Cm1eCiojg0-4lb3eRC7tsNty3VQcwuFloBi6ZcNjaw7Io3zR9WA03AXC24eSoGTktzUuTbWOYEB5T8NUlUzKDoUpHk-2-7ZJsreLAxPj6cFCD0vP0Kh63AmLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_Sru8OnES2mmXYYRR8t4Q1nsJAqRExvLM6JWhAo5BgSLgt6K4Pt0FjEU3S0MizCYUSU8o4qebsAwhD6WJNxJluZrysi4-6PPQFUNnwjYYxqHg-A_cO56kEcAdzJXGAHTGRsmSx4IdtaMm7cA4awvXrInQEsJi5qfDC_F5K_ktRjta_l1jjG9FEw0kfFOP9QRTGyiX87Zyb7se7S3TLMPWq-qsak1Xn81xvNhQN0UH0TUjZiEPlhFQxllEvIYnU9J3V70jZ7OKjbhYNjHL-Lb5deUajG1fmgbxcXw2CFSzpszres7n-PyPioNUv1bYE4zoL8PZhu5nGOxgM0SQj2fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvIcKFXRFfU7HsjkyK03zA8DJaIaYe-o_Ay-WoRrvswV1hhTvpu9yYpExz6oVHeIiyHYlWliC17OC2QIAOYkHfrrDUSweG8XLXt4rMiADkyfC5NqDj6_Rds41khXimqzFuwxB_vhcjB6_G6Ppq9Gl-G5xt_JyzGbqCGStlPBKpLa3pX8dZoN1vscGYK2mMFJRk8YpU7J8cC8lTtGskhkuWfzbva5GFOGNvGoZvUzogWPKhoqRvMGWsQ4nyoAJd62JtgjUcoDS-DCtd_F_CLvbe1U-1Gno5TizByn_9AHasVR2_keQzW1CAbbuFe3bkbHgqZe48ks0juqnSGCvzNtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=q2vBoJasry54QNluIUf-kcmxhOK-sQvKw_126yzDGiw41LDjMMUhUBXAuyc7ThEsDEVTwN74Gn7ViSXss1RrLHAB7iQ1b2QIvlq1G6ReCopc1QJhJOqA5MHIOyM4qmuX-u85dwsIdunwK4n6jkZtFd7cfTVg68TedG4xQFpAcE1W8oTXF8x4gcR6GOo3Y2H26Bbp_R-vRT2fads3aZ_35zmD90RZvC7AZNfnosmFIYwgaICv8_GiLZ-Czpu6YhjVzcrDiDx1Z-2sxJd7QnZER54aoQHFOHD74Qoms2C-v2LYfBlfsnu91zZ7o47IB1V6FtiSv4_wTigizzp3saepRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=q2vBoJasry54QNluIUf-kcmxhOK-sQvKw_126yzDGiw41LDjMMUhUBXAuyc7ThEsDEVTwN74Gn7ViSXss1RrLHAB7iQ1b2QIvlq1G6ReCopc1QJhJOqA5MHIOyM4qmuX-u85dwsIdunwK4n6jkZtFd7cfTVg68TedG4xQFpAcE1W8oTXF8x4gcR6GOo3Y2H26Bbp_R-vRT2fads3aZ_35zmD90RZvC7AZNfnosmFIYwgaICv8_GiLZ-Czpu6YhjVzcrDiDx1Z-2sxJd7QnZER54aoQHFOHD74Qoms2C-v2LYfBlfsnu91zZ7o47IB1V6FtiSv4_wTigizzp3saepRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=P9zR-lz1hH7dtoglGmfgCqEhE40wVhpE9zFe9c-d8Ku8KEvPFBPlQMjJI9_PyTw1wWO-lH0XAIHlLEN_qnS9Rz-nc-6TSjT8kMmRoInyvwgnl0fczMxGB_VeS9wO6JY9ECqlX_hnAPR7agGVm8cAq05Amdxn87Xh0vnMWekbWkjCaAtJK7C7OnnBWsSidXCzLN-1hwvSabbHeayF90N57VFLSFC_bhkLNyNzXkCPEVte3t7L_PxVIVS2nl3_cdXuV_1BtYrHNGI8cnUM-bvpBXma4mNhFuPWH6E_B7DrcKzPiSclfY3RslN2mFyc_DN9LCoGwHQBJ62U9xSqqicKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=P9zR-lz1hH7dtoglGmfgCqEhE40wVhpE9zFe9c-d8Ku8KEvPFBPlQMjJI9_PyTw1wWO-lH0XAIHlLEN_qnS9Rz-nc-6TSjT8kMmRoInyvwgnl0fczMxGB_VeS9wO6JY9ECqlX_hnAPR7agGVm8cAq05Amdxn87Xh0vnMWekbWkjCaAtJK7C7OnnBWsSidXCzLN-1hwvSabbHeayF90N57VFLSFC_bhkLNyNzXkCPEVte3t7L_PxVIVS2nl3_cdXuV_1BtYrHNGI8cnUM-bvpBXma4mNhFuPWH6E_B7DrcKzPiSclfY3RslN2mFyc_DN9LCoGwHQBJ62U9xSqqicKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ex6GrcPzxUgdJ1xj9ERTLdUUFHhD01L48C8VCxrAe33e1V6R7VGFjqRimxyuGSph41Atu4Xp_JJimFdJHff6F7uVCuIabjjaVbY4ZxBpfLbCrlDi938i2Ca-vBs7mDAol5kLHGZsoF9qvyQlQXhoZwSGhnrKUUYQQOD25qndfj5j2elYfpi4kfVBwMScfBbuCUEoOQXkAPjyEDnZEynvlkEmar651nZe-GQWDqe8X1fewNElC2WF8EYXuTxc5NkFNGUjoFYHiSWPe0hFGKCFD9KJCAtgP4HuGMUWIa_bk3XNZ0c7Foj5YVe86MbkbRXT45czVv__NIh1oyyT0rs15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=ex6GrcPzxUgdJ1xj9ERTLdUUFHhD01L48C8VCxrAe33e1V6R7VGFjqRimxyuGSph41Atu4Xp_JJimFdJHff6F7uVCuIabjjaVbY4ZxBpfLbCrlDi938i2Ca-vBs7mDAol5kLHGZsoF9qvyQlQXhoZwSGhnrKUUYQQOD25qndfj5j2elYfpi4kfVBwMScfBbuCUEoOQXkAPjyEDnZEynvlkEmar651nZe-GQWDqe8X1fewNElC2WF8EYXuTxc5NkFNGUjoFYHiSWPe0hFGKCFD9KJCAtgP4HuGMUWIa_bk3XNZ0c7Foj5YVe86MbkbRXT45czVv__NIh1oyyT0rs15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2sa3Oyr6pE37AHaPI_b0JVuDsNBPhJgA5UtZCharYS90x8ZDVzpNs5tDRa-VyAOTN7_v9WD27hfPDhVjKJhQAi9HwPJMAGAkWZlEv8xwhVFeNQyCwCF4KqZu7gIjBqYRj-5IMj_acwKKUFVq-dcgdGMtW2S9ImZSUiVVt0oqc0q96yLVaNglqF4mBWY2uNjNyIo8FZKEFPs2Xkp82_0Fq6lIqi5wlrf9GhIe_KiLmiD7kpCHcyxQcTBexwnkdt3YnIqFKlZwwmA8nwqAKRku8N4q-FGdT0iIggdFVS_KVouMGxI4xlE2iNP7G5P6fX_AnuBq-vNa0IDiHiNUdpD-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYSr9IL_wR7WVqQsRiJqnBvWpZM0d8-n7Oz6HSur1iyrfzwdqYXehNJ_IO9Qzlmzl-FySsBPABOwp0eiQ2qCh7WAA60HU47zqKbfBTtHHS9gvkwF70CV9lyiq9Z8QrDu64lKpEgq_2C5gGidkm9qcYCiJVDhKWC8RQvEHszE_YJYRlxhOhhen0GHw5jiMz3Fv_S5BZAp6Tc9MfN6loWnZEDCwJmqnOIT8NguJ2fYa9JLeCx_-dofIXztB2ixbz16675WDxr8t09eaEzqF28P-gKCrM17wYdG4CCFEv_FF-3CMAAW8ges2Na6W9vVoIKYxjyFUzv_LmWtWex8UT5QkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0QG6ksuSOAsYoBgDaZubqgNJEFj9BrQR9nyzphRJv4skSc1X7iSiCclp1HBNBkCV9TtHAWu_FSjjEZ22YcExmOdMSVQVacxX2OviDEDJhFTdYPTjxNf0CTFWjWyAfDvqAAplANSzPndX87o8cPPThU17jbpHg1ESsSG4eKZ0Z4Gd8OVL93034Xz1__O-R8eWpb4EkeQ40QcQxCCgiTxMId7edGY9hOP_yNIXge-K-FHZWm0UFEkhF8Pbt5Mns-r9kPWrcU6tXZuVhppUdBDkMMmyjDtN6rqP2icGFjQe7hzHl7jPBei9N2vl0WIxjgZ0IXlUcF1uBZ1kjkGhhTamA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8i9oIunnSbap7rsNYW-bs9XOGHcZww1u7TjF0yNP--j_TIz5TEJlOmyalR9KO3DJKBfsp4NO-ES36cYdhrvd1y2qMe9BzfX0ZR9UQmQOHL2SjA9BEV8_09GgCtqdO-DChIJY3s7oC82Owl2Zbyq0yDPfm4j7VqFw7lWG9tpfT0-jRx4xRO5Rd70UHcMA4Vsh5cyzSyLGwIGZGLn_Fg3ewKVxzIEividnttit-cDxBFOuSOnxJrCaiJunsxIb2q2YuZSMoAQAVSIMvu5TGV5X5ksmDWMQ2ZZNZR9jbU43L-V-UpGjGN80QSRWxApgKK-zwjs_sSPaR9ULOuzkv9_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S1e0-5MWZItydZrcpSjhm3E7HiZ8vy0ewUDS1Z272tkGwTlr7tUuDXKqvEcwbeyF8JhmOPWibOmzZU8o01y4znNPIRulhcVWRPVlR3mTJ78gW5LvfjRgVxxzzEu5PWcVvtVonTc54MiqXeARcG2ElB-th-BeFrdyd7to9X_YuYnsvIjy3chliI_zl01CitIJlVY42nXm0dIE4IsMD9RZL6w1Dkm3Tp5SRIOn2GnnFkbSAxXQYqB2GKkZpfg1SpAOa5l_rchpHKOlOPhzd5psjTAkjqCLaH7Z5WCAXHLWl7f7y00RYqgnQ_c0QHRQ-DEAf-EE62x_qr_M3hVQeRjN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aZBwuN8zH59H7csDNBde709-jrlbVfT-lu7j0-xHxRv3_0bV2NImQc8aveoV4xEgZEBObjuqF5WArHkpPozvyfWFJ99biOIyxum1Qe1VnfaRJY3E2EON1sXSokemoHEBuLNelvMfN1nqCnqR3-ki1ujKvYXRCkBJ_FTMOn9FbAHJ5FDu_vmFaof2rEi3POT-Jw9-8URXPpPm5FG72lBgDBadGpFPcFCZhUlTuY5Tj6mIqA5raUW4JSzznBQGH9ieNYUxa9WvGctvUZBf4NOGKEzbrgYXJZcCLmyeYxnKeTHl7ucM8q932cnJoOelDSsYGr6d3diJPJz-EgtTrsjuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aIiav_cUkmsS3AMc1weJg_yBPE62fkOLcBQuKldjMQ8c7f2Qw7JjAeZDlUtdVWdWo_NukiESc3xSx7QpgwRRktcljbZ7KT5Y_rYDCof45Ul-BeQ-QBS0_etHIhTAYZaauGraIsHwU_lVipUJkG4fOSC38Q9jQfkvZQjruHNAPIpQ_igQSrWxJOIXrPqE1BIzNSWWyckNNuLhMaoETRPreZc3OG2E-QzHEGzQcqFR3svgVEfSVCHRixf2fA6Pi_sqHpTQWA6Xv6E4Ag6AZqJFAAdub7z5kpHUceEDKDVxBy3MMMb2-ArEBXwUXLP4DgtCM8pe8YZvCXFiN69kROlrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juNDBaxb5jFu3c3bdmSM3QkKjSab1FBqVz3HL4feKGtCWfJq0jLbVN3ceiFZB4SLo4OieZ2eHtwctwPBCA51Ali4z7IK6mw_hHHAsh-EnBpnAZEowmmutrxL_NxzborDhOY0qtAILBdafOc6IUmAtIBIXwijN2npHet_Por1QCYGPcIw9Z7mK5I-4WVpRqWyaEs403wS2dTnyA-cEhfcVQNBJKotALY1BiHOLUqK-AQl55bI1CmLyMchfpmsbpyYBfUO-uHXiPPlA-IlcxzBz4BTbnfzAT-PDX1rOWAwOD-R1oU-xWeegXTsSjxvK_1MgP3XhFo3JHUr_FGGqBhgBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=WOZldq13b-6Kmr7Sm4D7C7awrMy20CN8fMA0Ci6HBfu-xR7WgNogotrt2nYm3a-wum8J2ib_oWz02u5gY3Czt7QLHn_XsjSsXl4ixh3dkSuWOB2SGAx02aPGqR7t_O-eZ2IXqNr2mqQStyaxG0RPXEGZayhYm0eFENQWlKGIx-QCb8dJAkiRHarRQo7Jt81WLVoy5drMreaGdCjyybpCmh6ht7bnijquXCpa8N7UBGgxD2T2y4aEtBa1yW-gVxYp13dpEpLBYHpG9CdWcL53Mpi34cBWgS8W7Jg3NtOWPOy1QfuSpkpsclQpNmfn5NWmbAPNZ2VnMulmbMpz373qVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=WOZldq13b-6Kmr7Sm4D7C7awrMy20CN8fMA0Ci6HBfu-xR7WgNogotrt2nYm3a-wum8J2ib_oWz02u5gY3Czt7QLHn_XsjSsXl4ixh3dkSuWOB2SGAx02aPGqR7t_O-eZ2IXqNr2mqQStyaxG0RPXEGZayhYm0eFENQWlKGIx-QCb8dJAkiRHarRQo7Jt81WLVoy5drMreaGdCjyybpCmh6ht7bnijquXCpa8N7UBGgxD2T2y4aEtBa1yW-gVxYp13dpEpLBYHpG9CdWcL53Mpi34cBWgS8W7Jg3NtOWPOy1QfuSpkpsclQpNmfn5NWmbAPNZ2VnMulmbMpz373qVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9qPeVYJ24GLS7hUZ3OaZzQdVD1oL68ME0IKOFimgCfkxsZZhFitJpYxWg0d4naLc4bm9Bq_w9xAF6uEU-rkHXpn-DEeETILuWJo2e1qoco0R78L389i5mzyOCDfssYY0fych6uusXuSxLBVJjlFvlJYzkhrR6GcHw7T0grfWhCl7-75RfXrJxmz2bk69YaOXn-SQEgZTzeJLX6AHy77Xn_KKmDdcbCS_yIwRdgc-S0mpZQW76zni9Jd8G0osgZXQSV57BolUtj6B3i-GUX9k32eZIwMlQIVP42g6UGveLo7JN_ECzaWoY9iUOvWJ18YOkL4eCOL7H55PIngFDtaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=pdR7TVOJ9eHecrK36Yd1uBr0YVqLCIWr1ycqaBIm1Rem37wg6O5f4pp5HH163AyuXKglOJKQw5CuV2igVOuWvIUCyeUfPs9C_jlF56W2vcOTdx1AVzYc6vVRLtgHaNnd_bxivfvgY5XIug0YCYCvQg3LUoDTxlVzD4opfaXBYQZ04QBsdYWGGGKDwc_hsfGSPhMqjVSx4a43e-DPXs6nLac1L8v6uveSW1Vw9_b-lVf-nTQ_tvJ-u2ZMfUu1_yIRgG8_eVq4gM1EWb00ZKyMDaEveYMG4WwF_ciAtukmdOPxCuz85f0G7fhwc8GYbOMkwvWoc3Wjd_HTwLRm0fGAcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=pdR7TVOJ9eHecrK36Yd1uBr0YVqLCIWr1ycqaBIm1Rem37wg6O5f4pp5HH163AyuXKglOJKQw5CuV2igVOuWvIUCyeUfPs9C_jlF56W2vcOTdx1AVzYc6vVRLtgHaNnd_bxivfvgY5XIug0YCYCvQg3LUoDTxlVzD4opfaXBYQZ04QBsdYWGGGKDwc_hsfGSPhMqjVSx4a43e-DPXs6nLac1L8v6uveSW1Vw9_b-lVf-nTQ_tvJ-u2ZMfUu1_yIRgG8_eVq4gM1EWb00ZKyMDaEveYMG4WwF_ciAtukmdOPxCuz85f0G7fhwc8GYbOMkwvWoc3Wjd_HTwLRm0fGAcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=S-bsK_zZZzIVs_5iqCWRpZQDoqYmS-1nxROUagRAQNI4qwwhabXesQqGC_9p5vI-JAM0AkF-G5tSNJu8pdYyTvlZ6y_oOaxtLkahW0E8zQ90Q3I1tm1Mr9T5oqbcNwpE1cq58arwJFVRq9qWzw1O9TXfEFzbPumoJ6N2j18Xg9utdz2EUNvhp6ZCafFmycp-S6kSjprRJ5fm2aQLPVTR1dWkEoW3WBkGaYN1iQMXwPAlSpaCa13c7pC4WbO_AgJbWOZlxSxwmbZPCy4fwA8ee5dsih473eLqXj-J0ujBPfxxZ_9ybYzG0BSirSdPdvtdQrgwv1rjykp9QQN1nt_s6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=S-bsK_zZZzIVs_5iqCWRpZQDoqYmS-1nxROUagRAQNI4qwwhabXesQqGC_9p5vI-JAM0AkF-G5tSNJu8pdYyTvlZ6y_oOaxtLkahW0E8zQ90Q3I1tm1Mr9T5oqbcNwpE1cq58arwJFVRq9qWzw1O9TXfEFzbPumoJ6N2j18Xg9utdz2EUNvhp6ZCafFmycp-S6kSjprRJ5fm2aQLPVTR1dWkEoW3WBkGaYN1iQMXwPAlSpaCa13c7pC4WbO_AgJbWOZlxSxwmbZPCy4fwA8ee5dsih473eLqXj-J0ujBPfxxZ_9ybYzG0BSirSdPdvtdQrgwv1rjykp9QQN1nt_s6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Quimju90VtmGxfWCP1SzLv6vcP7SD99F1WRG6Bn7v47syWMXTtCEClZ2lYCUqw7MbJGo5yaPth3QMzNGKdHRtc2GVZEux2Rad1Ziickd3b1ZecQ9_8EpPrC-REn_yLMPjZAQlcYYwS2SLBUnEGj1vL2JGXKws8v0qYPpxTgwHEKVPwyVs3Wyyu0EDkVZSzT_sYTe_orTnEIaR4i5n4m7w7bH3JKSTjD71G6t4DDTIuSqt-SQjtATZ-PbVqOvKpfX3BeNRQRyZdaxSk54FTptIvOUFd4SWH7VWlo60KVop0NMjTJAL4d3UmOIy4_AyZ3nh1KsRoqy5Q647PxZvqRwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdBS1kD3MVYbJ8sUIGVq2vs7ZxImy6d-Ggi-iYzvIbAEXMKQt00MA-LJCNjSEs8sn7nkcZe-Vgh0q2Juo6lAzaLKb50_JPvopjesio0nhVIgbPpZDRIJpe9HkzyuibVtsTs4377uUshapyGNlm_JlVYqDiH8Ds8KemmnhsUCGCzm58h_Gyey5cmhpTOzzs_Buoh7jhcdSY5JyBd-r_nP-bD4_8Ab3rGhcCVmWtODN0rw3ur2Lw9zBFlgCR2vopBOm2kUJtx4txFm6yOYjxleqIMjvYYTSXsTAJz3lktaxQg8T29R-91-6Eb9uuuFOfT1oszNRU1mvn99Kk0dBvGf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=MXAkHOkwtqLCXO8zrd4KurrU6Vb7kfOmihw6W9LE24DLwwdGOzW2KfpGZm6CJadItXmr8z9Ewp79xdryfoWPdwet2M0YBKxpeXN2plTbU5cEQ6Ms3NXD7AKvGQl2L4L-aVZdil0hBUyTKHea_E2ke6wymozF8_h4U3p_k-9xY-9F7ofS6FDEe_PFBLrdXR5H6ajcMwgjazuiAUVKWwXwfYz7gGhDQHXAc3-lzVxXKjZDQfwCa4xAftMfDR3B05eBEggXrcIvi41GdGaCA5y9LazugrqIeSmZI1jmXB4ezNouUext7QW_JbK0zyDlRt2DpgUFTUHZgGfO6i959llOiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=MXAkHOkwtqLCXO8zrd4KurrU6Vb7kfOmihw6W9LE24DLwwdGOzW2KfpGZm6CJadItXmr8z9Ewp79xdryfoWPdwet2M0YBKxpeXN2plTbU5cEQ6Ms3NXD7AKvGQl2L4L-aVZdil0hBUyTKHea_E2ke6wymozF8_h4U3p_k-9xY-9F7ofS6FDEe_PFBLrdXR5H6ajcMwgjazuiAUVKWwXwfYz7gGhDQHXAc3-lzVxXKjZDQfwCa4xAftMfDR3B05eBEggXrcIvi41GdGaCA5y9LazugrqIeSmZI1jmXB4ezNouUext7QW_JbK0zyDlRt2DpgUFTUHZgGfO6i959llOiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpKuAI__DSjA2D0cJKsLyl5rgYbkbnwY1gUSYd3Sm0v6frpWx9jiewrD1q7hKYBxvhxArVH2Ie52l8W8mYFg0_vPT_zQeDjPukskxfblR9nGVrL4YeMTDtAtwOWpjEEunRdOjcpk9xvwnd3Xj_LSPuKDoRUT2BN5xJ9zmCdr2519RDkQNuj-Cw1AqbsLQNpzEySlnDT_rBE-rskqITJH2k5DzB5jJeI0Id6VPLBUpUUH5jVmGnxfNN-oV0u35-WyNgejgXp8Ob0FZZKRyPQOEOqlVIUHuJbiWM5DmnJQLmH8yWIfA_qp3R_x-77M8nmI014nVX9AMDuzM0YzxpIRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=J3ZHfjO1TeY_V7E88L3CBGc7KpZy0O63NCKpGfjBKdNurGWvwnMgNfjOc0ZF0hSdx8Q8ONyHwivBsH1fN1VhmsYsXTFiqdEQv1PU5QwuOuZTLQr1Q4C9xYBisfci6IL71hqtR3PALSO0IvZKXqoV85uHy08ndYlKEynkrGcjr351PS4rXON697GOOKWTOYwWGneEtZfae3GMMaWiRaumvqLxeJALD38JGQGUToovx2bZ1wJaaNjudzLRG2INzIrEzD2d89v65k_M2bgd65vQW0FnmCxX-RK4P-FhhP2pVS-isQV_eQfIA_N86hoQUimYzv1ms_kUSdbjnBEtjmUcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=J3ZHfjO1TeY_V7E88L3CBGc7KpZy0O63NCKpGfjBKdNurGWvwnMgNfjOc0ZF0hSdx8Q8ONyHwivBsH1fN1VhmsYsXTFiqdEQv1PU5QwuOuZTLQr1Q4C9xYBisfci6IL71hqtR3PALSO0IvZKXqoV85uHy08ndYlKEynkrGcjr351PS4rXON697GOOKWTOYwWGneEtZfae3GMMaWiRaumvqLxeJALD38JGQGUToovx2bZ1wJaaNjudzLRG2INzIrEzD2d89v65k_M2bgd65vQW0FnmCxX-RK4P-FhhP2pVS-isQV_eQfIA_N86hoQUimYzv1ms_kUSdbjnBEtjmUcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSrBo2P37hM1KAe0VigwL2BwwvunEUDDOSQajky_ZhqCL_B2E7meF1jdrpto6dYWp34KnSyxe0IWElRWu7EoG2CtCEhDDrcqgm8_udvFE1QSYHBucAxSxXD_SzOrxMAxZjgp3HjeVNspTIq-XiwjlutZ36IR2pw5Rm9ArhIpPfF64tVC5ItaU-WfFkbxcIu8qoJBSX-QAiF5eU52fJIgd_JRwqhECjd_SWD8urr7ym7HWZ-JuaxazBZa01eYbWg-vysWj9mL6xyZv2DKjiOeEjJfWX2j02446SwzT_VE_ihK4fIuzgFRjPPYVNEQZytgdFXp55qrCsTJRADQCYUJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkxyPKCJ5T-RghZM08rURwu7nrgyLczbWuiLf0inQaeVFfJ0Dqwxbp3Jl5hC4Hb8w-CWVCQ_hTOfdnoinUkDZx8nG4Dm_-QE_VfkAQg32JTTMdOxvWnLJvd8HJI90Ww7asIalvO4IkaG6geBeG6YB6WMQyaGj-0s8nsXPjr0OHMTy54c1L18C2cqIqTCHSh1QnNnYRAA3KLOGvpn56LZtfASjeBXFacvbYavcEerLb5r-YS66vt2EF8e_LVBxLlE9mdHKlJKcQbF0lo0lyAZc96T-JuDzJDcOaKedkom55Frywb05zPc5tlq67qXbYRp5VZjP3C6eNRicVYJh738mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjNULW1ZzMVeB2FlxPPhNc7T9jMLT1iHujWg20Cq5bElciDDLZdnWm8BkfMESbeDUFeavkbEG6Kt_XYnpFRwAnqc0px5wesefOjmuD5UHdQdrzopji7c28MW57p7rCcwRkKXRUtJEscDrFC81bI7g6j74TMwmnyckKLR7VMJxMDufMe_sISknOAKH7MrA__HrQOunlXVzgUggqyq1ImkV_w-VGpFJapLxP53kgv3xYBqcUU8XJD51O1YsiXIQs-IhheFc7C5aEJSHxR7wGnV_5l4x2oa2KH-ewWRBZL28D59zAaArsogpSF_-vYlcrGsL-VwygSovtvviK0ByTyTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5_Jd34f4zNwjFD6p3_W_HG3tnGcePAshnKkIWEJVF6WuR3hYbyAX_ZBjZ_fTw7jHWECKDnKZS7huulAfGkC_qUg51t0MdVNb9favTDFYNRkMFVZFQVsFHrAF6Z-zt6jU7G5RPdPmgXDmxtiN6_2LVaocvrPvd_4qFHUhoe4RlZlld-L5IxflJ8NpD4RQmU3OFdPU4X_nsUW56KYCGCRfDD1Jhyh92vIL-pW4hwGQK5FNLGNtZrk4VshzfYLEkzH0Af_eZnRM4KjC8oxNXBM8X9rlThTh_jy5tZWGJ-oisawFICq_97DZ-qWKj5qxIGNtKlhSKQ9H-Gz4aPKnm06qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsgQEoJ4owLF1_25Cwn2JEHEloTIRVzYiE_G1NN4v0dZ7NDdvBGWU_qLwvU2qO-bNUH28awomNqXrpqF5XSYV9iLXVVhMtUD8udIIXeXNuLkKVB2qDFtxkUgQWOlVaeb9Mik-pA60UHmlPxGhneg9mABgpz8sJ8DZ8OQtdr5lF4raKA_M4Q1F2F4fpDbw7eY2puHsPZd0dAHCAAZ6W1K_I5Zaz5DMtfPALvfr4HDJ0tscpiarFcrDXl19LP36GA2ZyGyYX8pmteyISgPaLXLxozfQChYHAoW5q4vhE5nQij2GbAvT0QRzBr4GuaRrWTh8V5tGNeIsEs_cqvmbhWlPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR93tkBCsf0e4JY189qd6V6Er4zpwPAbiZwJMG8evuz0o2vqN6un9KvyIj_bl8ClItuqq1yVK9hjFBu6qOkKst0eVcnatqoKBjMxsNa0OOKae2KilVJiZ1-QTNUkXvu-2gIGdxyXneoV4d4NOvfnUuZUDNs2A0iQUAHPKex7OU59Pdo1Q_O2NC8_Jz7HNjvuYCkHi5p1argJZlpBDp4faiuntWXllN03XmULfT7prxuqBwDHW-xp_15dUAX05NyidR6L1pmzH0taXlmV2w9OQPaE2bZZMlyKji4_KK-i-Up_5Wx-6m-VRAKyOlBWQmB2fucE4WIweIj3e3pq1jvGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQKbOOb-v-EpxHOSe_CVj7e_Mtr-rLCSGbmWPJs3NsXkH_A8-Iji6pACanaKkP2rAgJxtdje87DR7fehbCesCI93DrPDLI_kIeXJdhuZM8NIgpw0qcad3QzQZwPBj22JRzrpixmD978DREUNE-9o-sYQrRjkBXZMqN4jxueyRBIHyYev3awfSrAr4xmxqj2UpLQ78N-FyKHRRbDl7C6N9fa7A2NpXTisYuA-3m3sX89qWwRyKjUpYeugYnCiNB5-NW3eFBvWtp9ktmApLruohLcXpOdfKg2XEUETllD68O1w7BfZCyIUNvp4l18vbm2w4ppOXkFXRfhr0yLHDejlQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjFQtrkeO6uGCdbWzbQHySa2vh_i-xvj8j6WxVjvfXo6pMagLPsNc9K28w9mkCdtq2BLKrY0eMxpjbrHURZX9bVtEiJob2GT7wxScvVQEfYLwJlEJFZ7xowY3VGEm02go9S5dflQ7Jztw53_l_sEcUDnswq1SmshUPs1QD-2AKIVVLmSVPUzH-txHoRY_G4FaiTMkc5XghPryJum2-KPBx0IxGoXn0I3QiWaE9lDkot1rzZ1BWuBRtg5-QukW4mHPMunV9BOtB1KV8AIXx6Ig2N_YG1WOF1MDt26w2qw0t2Kez7VccnhFkuE74jk3W8vlhpZhh_3_SPtxghyqbFpkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=hQK87-MLQpotN7EO-vdtHjkpFpUXwDpPJO0bGU7BPaC0Ss1DTmJvvXG7GlUuYnE4q3AbWgTKu1poHiD_-6Q-GQh54Qvp8-T0e5fCjTY9vz1yXCjF-0DIv0KQqoDS-2dF1xBW9LSxxxEBXSatUsq5t5rr7vl6dUkfe1yYCAjvzTQCPAEVtfWkqBDC-FNB5FV4z5tU_rXgAwdIAcprNNbBp0_5K7QGG6FMowchp6FeZlIkglVBLaFoj8iR_l_VkV0vCxVoXnOpDD6uCaOg6KNLX7PDFN9EJ2GGtRQl0MJDyxItcO3xcgfCoDh51WtZFRzQq0TRX7XsNVEeJ2YXGrmzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=hQK87-MLQpotN7EO-vdtHjkpFpUXwDpPJO0bGU7BPaC0Ss1DTmJvvXG7GlUuYnE4q3AbWgTKu1poHiD_-6Q-GQh54Qvp8-T0e5fCjTY9vz1yXCjF-0DIv0KQqoDS-2dF1xBW9LSxxxEBXSatUsq5t5rr7vl6dUkfe1yYCAjvzTQCPAEVtfWkqBDC-FNB5FV4z5tU_rXgAwdIAcprNNbBp0_5K7QGG6FMowchp6FeZlIkglVBLaFoj8iR_l_VkV0vCxVoXnOpDD6uCaOg6KNLX7PDFN9EJ2GGtRQl0MJDyxItcO3xcgfCoDh51WtZFRzQq0TRX7XsNVEeJ2YXGrmzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bks2Lk2RNQrQTYySfZoaUZpDigIS-qXCEnBjTCHS_7USSmcmwHu50bCTXGuMzCWRAgWHzk-fkFm5CsfBbVDYWWDF71SstgrRmucnVUBiGCbTVGsLVUAoNQPXC9d28tc80s4fb0HtMHO_30j8QppCrjVGPcJMtGUpZpj9M1tkSZhoQynQbFJknW50ZfzK9-5weWWCVc6xwvN34NJLMibR4AZc0OmgNIJX8xU5lfDthKBOoKz7qrLLCB-P9DBobzEWtZPm5buatTH66d0m-J9bvVQ-J5U_0155vo2dWmDubHASh_89-AsIQs6LA4XTxhoNFld5c4sOUJyl8kGzNbsLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhIBzCJBC_uWRAmeBclCLj19VYYLRQK4ni-qX32ZsBvzaqKIB1KbMswbYUSxeoPYn6EiCSUaowMysO2etyUcf-pNMZdM8UqGofd2OlMEongftHvBT9FNaaLkeBmZXWeScuwKK4JN6tY_2VW_zi0sLqW91uP23NVOZbnZycU4KPR8QirhokuXNWLoydKQgwYK2nd27srujKCE4czaUR5ZysCPYAI0zgn2tJZkd4Ixv838QbRdzrEGuCGUG4KbBO88ne8_m6WNS5EwClSY-j5rVuL9cRLuvgoqERDbT_60EBepqoHE_E5Ht2zAwvNDgVaoJkuJ0BX5xuK8cpTSOSdRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY1itRmp31gZDZ9o3s2zo8C-AqCjRN53UD8aTCtrwfG-wqNbqkP7O_am_vZc6zJGDA0ZIXhfh2fKkqiRFacda_w9s2Dd3R_rVIgZoeoyFLwv7HDgHKzaymuW1HyRQ4t3tZBvRo6xZrjV6yrpxE6cw9H_AYzKmze4w_4qUIePLxAcUAgAbe7BefXJIbX8TUj5qRxkcK83pBDIV8StBRl6I76t8g0SbqbGp_YSt4mq3UgYEEZfNoOSO66DGEK7tvlUor1zRPdbZLu1__-4FiyUnQOmfFxaMpzvSbSa1tNWjJTXmRknRFGKrzglSt2lbaLVervwUqs3bPuwhI3K7g3FGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=M1adKCdGQUzQPkLW5JEQoRTcvVOT9VIkgwfiGh0kCbTdFIP05Tsxg1RWJmGJMzbszFHde8bY1ILVNA-h6HHUQLfipPnkMlpJy_nWRJ9hugoKgREz2NFRjSeE7ebFezq-HusqSU0i9-WrMJFAAkuaPmWdDgVts_d1WTPmPqO6ITCt1t9XDIhtb_QjJAmWNxoPhxoE_yHhBD03oQQWqoMEiYqNX4C8v-85r7ks2Hd_NdK8FKsUEI8Z6Vwt8eqVceltd3XyXdBxdG-UB9JIiQ5cwlOH-n5BTGWfGHT5Md3H8m0AIwE6lKC97_gvB4o5IAS-PC_4DG0CwMlY5Ij_yNneVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=M1adKCdGQUzQPkLW5JEQoRTcvVOT9VIkgwfiGh0kCbTdFIP05Tsxg1RWJmGJMzbszFHde8bY1ILVNA-h6HHUQLfipPnkMlpJy_nWRJ9hugoKgREz2NFRjSeE7ebFezq-HusqSU0i9-WrMJFAAkuaPmWdDgVts_d1WTPmPqO6ITCt1t9XDIhtb_QjJAmWNxoPhxoE_yHhBD03oQQWqoMEiYqNX4C8v-85r7ks2Hd_NdK8FKsUEI8Z6Vwt8eqVceltd3XyXdBxdG-UB9JIiQ5cwlOH-n5BTGWfGHT5Md3H8m0AIwE6lKC97_gvB4o5IAS-PC_4DG0CwMlY5Ij_yNneVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImopWqLjGuLvaSa3S8_NtYN2SXHEGBssdNvvcHCW3Si5kDNhg8DDwYc9gTQ3E9CJSY5eK1bs_KdLxA1YWtiJvR-Vr5iz0JxNW7ZixTqCawFJ5m3R6GFFNAyTE8n4BTrFoEq5HNzUYEexeVydnBeCjns0bzi15S1CwGfUpSxJUkPlUlOmzlVsR6Ei_7f4FT5v6_kS4BSy-4kGX0MWAeSW8NFVAoLihUgf_R9PRf9unCgxUBX_q21jVh18DBEFHo5MjSP1HpvqxnBlrkAPASmuoPklLbqegQAblSuhlhT6DW6g81N5v2hW_TIxgzUGmWvabOcaYEGLV31H1CJs3QEVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XorCVCwjYNmvaoqrsCD9B0h3-ms1iGm70icqIkTa52u5a-dcHbVEIHa2KaI5NNUU3dwWN7I2HWXnXTJ9u_vsenOQhlNGNozQe8cjRROFR-eXFBBiY-Tk7324k69ZpsNDpz6QflHeXfgv9uq22h7NB-Txx73ajo9rbwxbwV2Q09cyfCzKmSv0gtBCh0zfjh7N5Mg9tFF5B3qx279AFtt0I6-NU0b__dkdmlCLgMFwRMJMfG9XDQmBLWDPVzAxDdfwz8ctoq6_dHY0E3fauMWTy04U_aszm7mFXPgImBHqcWGoDjVl-knspCQiTs5GYijfsx2-i2z7lG6bpcV67Nu4qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1lo7b4R3OO1mYm2mqYAWccQ83oaGJY3O-v_cZ-ydctkRz-HryAfNmY9VBNfVAIvq7Sm9gcQ3yop8xNqzaB7FuGE9YN4H6D9AjvAB8FVpJvLEILH8dpTTLzbRJLILnzNQHpHM0JsfvXm1AKtNWp6YGgKjbSSb-pa1IVPSYBF8DoQNPX8_Y9YEcsCny0aZk_VXXj5OkiZSMeuzWWcXvFFgZwkvd3L6xFLSTUj1tsNvLqWNb7dxd-DgKMtEIZgHR8yBnKI1RraB1eEvSkMqhysvEm9lrcJrEv_v5xdWinfPABXZuT1Z3ErOfR8Yrx-Ba636UQVlP8q1wh1mUqIJzbe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjfgKA4gGb5MPJkAJHqB3oVdiU-Ug4P3wnpJB-D8a6ogiKmpJfHjd8Dnf8JW4dtPec62RNrCE97miMXh8927x9w9upWBcBgP21WSudAvtsHUkXnyjjXMyO4Hn3Fo8dYRN-UIMOkMmlNAuCLLfDkq4Vhsi9AlubuFcxb7H3l0nlp2c3OI8cZNoG1NmBqD23sNaovWEhTCjxDaxpymccpO-nV8WVG2e33dC0GhwpQ9cDPmqVOEZA6GOZUytYnM3nVp6WTcwlsQ1CBCeDj7schBarsyjieley7J4cYy1IdH11QgFNt_5NZdVRee5ARpBBYPH9S17YXX-HSeH5a6b6vHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-t2hnYSzPeKDRUJlsB9DkC0hLMuqrJcQKZxp9OF4cPKOkxVFBIt8DmXpHLrbkFsKfMRqRFxt2seJldylDRfn8IC5vfyyXpwhoLv0HTHNb0rCn5Dx58DOjzktA5j-8Getxc7-B5Ebff0BVZ-KnyGr1vv1jP4C6PHEKqQ8t00vg__YEu8Xx3WEX6QCWKzHJChz7GuwIyNI0mzDp8-TxhXbS4iQKe3opW38xY8gSL1Xd1vqsoNmHlYBty6NIv_YQ9xnP_vKsE1gERv9JX6qoAlaXHRKmIXy9FM_bTtrJbLcVLyVPWgaraFyCjdNLaExNj9gP8ecZCPrnPce8gPzZbfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=a63vKz8Ext-fsXWvPDi8wh3-pYZ47HquXITGie0dTmsEPH_1AknQvUHIPqoN9Y-hctS1bY13pBDmA2xY4obwUKecOjJEhYisqNV1ZRgK3DBWFMiaOiWBUZQUQDp-M0Qp_5bIIL1YyFriUrIGfVeGRWq9FZBzoQOa4mSu6yIl9FKiEyvjBxegkcgD9Kfbo8nk8fLkEI_xBahGjQRg7ZdYXJU-Y6GuML8swNGGCBr-Fi-JjrRXle7n4JHvtS713YYvllV03r51XpA25OcDoo84Tk2wGp7LESLuSNbUJov4xt3mEwZN62cBkfnVD4ZM_wPmhFcID8RmjsUdJwiGqK7V14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=a63vKz8Ext-fsXWvPDi8wh3-pYZ47HquXITGie0dTmsEPH_1AknQvUHIPqoN9Y-hctS1bY13pBDmA2xY4obwUKecOjJEhYisqNV1ZRgK3DBWFMiaOiWBUZQUQDp-M0Qp_5bIIL1YyFriUrIGfVeGRWq9FZBzoQOa4mSu6yIl9FKiEyvjBxegkcgD9Kfbo8nk8fLkEI_xBahGjQRg7ZdYXJU-Y6GuML8swNGGCBr-Fi-JjrRXle7n4JHvtS713YYvllV03r51XpA25OcDoo84Tk2wGp7LESLuSNbUJov4xt3mEwZN62cBkfnVD4ZM_wPmhFcID8RmjsUdJwiGqK7V14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA9tQGD92xnS2pwqZ-Aq5GIttcY2amnhvmLqfrJ7lcckZ29KqhG3gzrC6QzuDyWzU30k0oHDFIr6KWDiy9SUScws3kvhsPIgkGAfXUXgejh_XRJwWlLKwaVjLbTQvLVa61FRmRJPOK4cnD2ToUqg_9gf8KNhpjWFwWtJV-b_deIJyvm6MPgQ-Ip4-9vPs82Qo6U_YcMMty9kzpCBff25UVtRAVhhNc0VehyAVei2Kr5nL_xkFislTnjR9b8V-UGMsingvVc4Ajo6VZGqd1riLUQmLu1CnvKfGq0bKLxSAPyrYXIcwd0hhPPf3-YZ9mNM_MFJStKpgXLzveXulCQRGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrjvXyXTMdHEKvDGmwI0k2TKSz5RWfeT4gKT0a6nc7nmTiZcaAQQH-JCp1QkNukmgBlr57KJu2kGMvrYZA3f1SjolZe1Ffh1W7U98fTh5AGY6GoEmMtuQGNYtBH9deH1ctuo-wKnYDkhW9HAQeySZNjXWiB05Vqh5MR-y6qU_VEH75iO3r-ZDqt_ukrylisG5DmJzs2DgyZRykRq_rXRLL9c5l7qAVVEZpAhdUFZXqowVXa5W_aWXgPLhv1xcPgEUUTkdEgmNip7_jKEsqzDsBuFEBJgmRw7do-MsuF_6mDAv1sMgZgPAerNu0qP5QbjdUE17Rib_DGa3lQA7Hh8xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=iatrpWw6HseTSSSuPUmNyf05mZ8AkTSteJquaFvUE90cz-EQWZNfpwTKjE46pa9O-TfCzYO3r3i74FCMJ43CMhxp3dQOl5iGyujaRUxXExEc06J5ZIEv5CSm8RevoTA7YkjPdB3AjoFKIN7Vn7awmypRqfsJEtYLGWgobJiXqJNeKcXXfjPhk4LLZBtSnYGxcfWTbfITfOCMC-COXrUleNEU2yaJNmAWPBX5WTCQxOTT-L020VouunOGSBM24vqyoE8-0xHOZvC45k97ayzIHIM0e7DJM_Wguwzf3qKrknggHKTIMcFkhZCrhZ-iKrz1WTBn1oVDBq-PGPIYb1nFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=iatrpWw6HseTSSSuPUmNyf05mZ8AkTSteJquaFvUE90cz-EQWZNfpwTKjE46pa9O-TfCzYO3r3i74FCMJ43CMhxp3dQOl5iGyujaRUxXExEc06J5ZIEv5CSm8RevoTA7YkjPdB3AjoFKIN7Vn7awmypRqfsJEtYLGWgobJiXqJNeKcXXfjPhk4LLZBtSnYGxcfWTbfITfOCMC-COXrUleNEU2yaJNmAWPBX5WTCQxOTT-L020VouunOGSBM24vqyoE8-0xHOZvC45k97ayzIHIM0e7DJM_Wguwzf3qKrknggHKTIMcFkhZCrhZ-iKrz1WTBn1oVDBq-PGPIYb1nFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=NoFR1hvm_LGFFClNjHJILYecp-Z-b4h1G5XbgsGmxXgXDiW8d0UUiLPc6SU9kZSzWR5gTA7WKbStc3MwMEXqUY3ljesRKvItQEu3k__M7LdPw0OAT9EFmTlB0o5S-k9He7icuDNylbEjQOxJOAsi7FKvg4HQWfclUMX4x9FeJnbdrDS_PdfW1uvD3oyLi1VoIhGQwxwuXZTXmuZioKkqiHn31_lZPz23Ic6C6JNnSKfc-JsB-vO8vCjtLN-gf3n0jlmBKDa9H8ZjsiEBuHXPDneDcUn36wskaP_OGopdmIEsu4GoY-4486A3G1pTj54-ekFTVOG0Ut6StxU1Ftav3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=NoFR1hvm_LGFFClNjHJILYecp-Z-b4h1G5XbgsGmxXgXDiW8d0UUiLPc6SU9kZSzWR5gTA7WKbStc3MwMEXqUY3ljesRKvItQEu3k__M7LdPw0OAT9EFmTlB0o5S-k9He7icuDNylbEjQOxJOAsi7FKvg4HQWfclUMX4x9FeJnbdrDS_PdfW1uvD3oyLi1VoIhGQwxwuXZTXmuZioKkqiHn31_lZPz23Ic6C6JNnSKfc-JsB-vO8vCjtLN-gf3n0jlmBKDa9H8ZjsiEBuHXPDneDcUn36wskaP_OGopdmIEsu4GoY-4486A3G1pTj54-ekFTVOG0Ut6StxU1Ftav3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=eaCRdCFZDaFFSx_cHpcrODy1NQJpRGwpUoLSjJCHv2rKZ279ZWxYM8Iv2UrYNWoWijsD0kPm53wZvd5-863X2optnNhiAcrjxvZdEzIG6IPTWzBv2ElmaTjtTXws-Fb7F6AOCQS6GeiWnNPJQ6OqtRyFYeraaBFEhBlBQJju4YqwZnN_-jRi8kD6DvWMU8eF2hLM6QcTr5b4TfXcjGx8ZOpp06C1MzqIMcjbjuoMP-A6qScBTp65VFsQ5FpzNSFJMAioR6TckmIhOu-2uzgM7fUGIbL2_Zw9IuTyPjwT5Pw0_zcblEws9042mEj3sgz-wCfMRyVYJBvFUpPiCf-NCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=eaCRdCFZDaFFSx_cHpcrODy1NQJpRGwpUoLSjJCHv2rKZ279ZWxYM8Iv2UrYNWoWijsD0kPm53wZvd5-863X2optnNhiAcrjxvZdEzIG6IPTWzBv2ElmaTjtTXws-Fb7F6AOCQS6GeiWnNPJQ6OqtRyFYeraaBFEhBlBQJju4YqwZnN_-jRi8kD6DvWMU8eF2hLM6QcTr5b4TfXcjGx8ZOpp06C1MzqIMcjbjuoMP-A6qScBTp65VFsQ5FpzNSFJMAioR6TckmIhOu-2uzgM7fUGIbL2_Zw9IuTyPjwT5Pw0_zcblEws9042mEj3sgz-wCfMRyVYJBvFUpPiCf-NCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIIZrP_hxUS7W4qMDoxlAfBz7T5VT3-zqNTGZhYKfi-EWDaPMcXJMjp1koZPRvv5L0mGMuiqSqyu2-9aYZlj8SPP2yn1FLvC0BlcBRqMM_LM9ROOtXIwplrTI2IkjUTfP7YhwRb0jZqacXnNPpfGI8ZmTpq0o7iPhnamkJMjzTr-c6orZtQAIEY19vj3RbxZYP2u3yZZ4vszTAMXGovylR0NNN-WO1M4R4mbPDzQ4YGPcb0s1VDUPncX-mIjTsmAYeEWHlBtds8_a9tSLiMg4SrcUajIIUlnG-rrKmuAqsX7aBBJs4zqghRXRMO_pFQM15rAjCoGw_S96x6x-r93sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=kGiQkMly-7Tf9hTslCp2G-XqZSvht8BLF2qVuiDxvmuOvnElStis1p6e-HjbWeS50RIKgA7kPhgTpOY5Wc881dRtV7UTV-Tv4GGUXqU-z7irLE_WS3YIOhC5wLlOunU1OA-iQOOo8m0eegMSqNmBefwp4m-bGzfCi_lcVT6tVQ081lEe0uMWOM2EBaSwBsHqxvIAZrbAdQrSENcmdn5kOV8wHJFVfbiLIeIjYecjS7huVTFxPqcodIjHOpr3139U2HR33pSC1ODkwsmj8rUzGVIAoxVyiD5m5bTq4Da7wWlslLGZb2EG_4IQs8hysV1d_L0iuFBdsVrBLTg0eRuuqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=kGiQkMly-7Tf9hTslCp2G-XqZSvht8BLF2qVuiDxvmuOvnElStis1p6e-HjbWeS50RIKgA7kPhgTpOY5Wc881dRtV7UTV-Tv4GGUXqU-z7irLE_WS3YIOhC5wLlOunU1OA-iQOOo8m0eegMSqNmBefwp4m-bGzfCi_lcVT6tVQ081lEe0uMWOM2EBaSwBsHqxvIAZrbAdQrSENcmdn5kOV8wHJFVfbiLIeIjYecjS7huVTFxPqcodIjHOpr3139U2HR33pSC1ODkwsmj8rUzGVIAoxVyiD5m5bTq4Da7wWlslLGZb2EG_4IQs8hysV1d_L0iuFBdsVrBLTg0eRuuqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=WYuSe4_w9wxv0eDjhRstTEFzoP49MXsdqZT1uwM2AN6JU8TFe5TFnQRmIUs7QBoRu2HIEZYCIGDcPZPqnhU9LojEQ6wbCbPkzN-LM2PWnYyNTtWLZFsk0uSw9Fc2gpSib6w6yoTJUEf1SHZ4pofMAdu5DUYMA3lMVr1zcE9g08P4NeO1rD0ZegHYgfAKMHuo3JqMTiucnA3IxST4duMvQCpjsa99-iyQfhf7J-de33hWE44EjY-o4mB0xlU3jBhfjQLF-xJRmeFmN-yn6Ec2BzFop1a0sFAOoxzsvMmWoTYVgL0SxzKC4ll1GzO3D1RX1CHs8FmqaULrYUuwx_Op2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=WYuSe4_w9wxv0eDjhRstTEFzoP49MXsdqZT1uwM2AN6JU8TFe5TFnQRmIUs7QBoRu2HIEZYCIGDcPZPqnhU9LojEQ6wbCbPkzN-LM2PWnYyNTtWLZFsk0uSw9Fc2gpSib6w6yoTJUEf1SHZ4pofMAdu5DUYMA3lMVr1zcE9g08P4NeO1rD0ZegHYgfAKMHuo3JqMTiucnA3IxST4duMvQCpjsa99-iyQfhf7J-de33hWE44EjY-o4mB0xlU3jBhfjQLF-xJRmeFmN-yn6Ec2BzFop1a0sFAOoxzsvMmWoTYVgL0SxzKC4ll1GzO3D1RX1CHs8FmqaULrYUuwx_Op2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFY3j2fIYwnFl2bht2i5gd0DUL7qCEZUVD9fWqUvsJpZDyCHwQs_oJrMNL-dvY-F5AFxVyAoyP1Y4RpMYs1cIJnnib4ujWJfUjRTb4Kuy4XUvQKdvPTW4CZ0GYvLHYPBbSZ7itOLRXu_i0Vp_lukW9hJWwjuqB92UZWjZ9xbkQb6mi3v9PVBxunvdlRQ077MXvdw53SBI2NuB5RVEht0X1aLajsZ5YTlVrdFWeNaLDheR_6VXmqfd04bep7vcEhhYYjzam1oESrBOQdcbPppXiJ2ycy8n0GqMcvdJ336-7Tg5M8SaLMJVwdWQOE5AhPflqc2FXRbwgN1gdup2la3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=U_TgIIep1e9n52aWeGwcQCs_JWehNQlNlG9Zj45zf679597PJoF4gmbPPkXq1dOQ9vmwFS5QPX5lp_8fM1VHMH5ht8r5yYPcv1MWdE5_IalAarflKXlGwPZ62VbX1XMgsjkfXtvnF0BksqsixJ9w6eLrWdzLb_eRvu63nYIRFM01DNQCozi45ebKPeO2r40dL1CRyGa5TPFJOVXS9prke1vKlBKKAOpVu_akbU6jnZqazseYsGlyNi7emuhRLhDuNGq76S8cwhZ-gnNLHV97XzhTVIUJf5QFwPi3GBKQK0OM-jqUlZ6Tyi0VxdfrSie7HdY6S8MQ4m7JMDY2I2DM3o6Ri0kaRJqM__20d4xmQ8fk5ebmwnbDFJh-ZYiusm8AsrzgX-j-itcLDl9mPhEefV9Ax93CxgI3Z-VSKeBVUqPXfR5wevj2N4RNfgGSsB8RcfYhkAVrzbC7zjikqfTuhDprWhyjfS7Elao7RJrICFpNdg2DS5veoTU0YyC3MUqmSkMJ2mNhDYyaWDVtPn56a9Wo8N1u6hr6l4vQDkJez0zaoqVp_ls8yoHA-71vUBI1LRMALVvQq93NEJkOAiVZwzaFRBdqkM8W5KwVLoAoaQPghfwWCfi65AhoCwGmnaWazd6yeebB0nKIyQtcf09DDyeKdrOpdsmdctyBWj6B2Uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=U_TgIIep1e9n52aWeGwcQCs_JWehNQlNlG9Zj45zf679597PJoF4gmbPPkXq1dOQ9vmwFS5QPX5lp_8fM1VHMH5ht8r5yYPcv1MWdE5_IalAarflKXlGwPZ62VbX1XMgsjkfXtvnF0BksqsixJ9w6eLrWdzLb_eRvu63nYIRFM01DNQCozi45ebKPeO2r40dL1CRyGa5TPFJOVXS9prke1vKlBKKAOpVu_akbU6jnZqazseYsGlyNi7emuhRLhDuNGq76S8cwhZ-gnNLHV97XzhTVIUJf5QFwPi3GBKQK0OM-jqUlZ6Tyi0VxdfrSie7HdY6S8MQ4m7JMDY2I2DM3o6Ri0kaRJqM__20d4xmQ8fk5ebmwnbDFJh-ZYiusm8AsrzgX-j-itcLDl9mPhEefV9Ax93CxgI3Z-VSKeBVUqPXfR5wevj2N4RNfgGSsB8RcfYhkAVrzbC7zjikqfTuhDprWhyjfS7Elao7RJrICFpNdg2DS5veoTU0YyC3MUqmSkMJ2mNhDYyaWDVtPn56a9Wo8N1u6hr6l4vQDkJez0zaoqVp_ls8yoHA-71vUBI1LRMALVvQq93NEJkOAiVZwzaFRBdqkM8W5KwVLoAoaQPghfwWCfi65AhoCwGmnaWazd6yeebB0nKIyQtcf09DDyeKdrOpdsmdctyBWj6B2Uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

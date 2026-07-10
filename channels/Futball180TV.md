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
<img src="https://cdn5.telesco.pe/file/huH1SWU_PLgyH5k2JruYd6cOsT8i45jhkbxv7sNCIZIr8nuOTWLcpE9L-qNO2UpXxibztjQ7b1Z-GE0YO_qrcmHNYtMzh_qmvgswTbLJhuI3mgIcBLWAbPIC0QW_zm5WnPFwAtBC0LGA7O-oic16q1WyA0IpJS75Na9PKqO-dAjC0AmsthLfutcq2nJOZ0OMr8K79jRwxaUYGU3zYIUGUJaKBlWV_ntGFeeyBy9Xjxm6iyoVwrE4Z8Q_vpcxKdwbFck7m4hIxWs1ai6hpPfBhlPVrscwK7_KmcSbxstWXfAplWOm68xEzNVlTpaT4HusDPqD4olQTQAh21hoaHVp-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 599K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-99421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=g1FCzizUEjfBrQUX3QZWnMgIbogEmVV24ejQrmYtYvJYiihlNpT-wBnzOCHA5xng20zW95GG_CKemqP6lJ_owRk9K3V8M87ZiX6CkIaQkuC5wK4d5vKFIAGGAPdNc1KiQXeQgdx_etN-QZD3C49qMWzYpa5oosOYPGDYWe-ajsHMwU9nY2EAvBfbC2x4AAOq_WMvnkXAg4_MKtuKzgf0YyVqyeFiSRKVfFel2d6Ht5Hl_J7h-ApWSxzxMUxkklaNATsWrJD7cuIqhz1cdXpwzP3_YQHJRiiNflfen20uzaVdAepqRsUwnPcWWahb2deCpyur4d5A4DuqCbSMmcBgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=g1FCzizUEjfBrQUX3QZWnMgIbogEmVV24ejQrmYtYvJYiihlNpT-wBnzOCHA5xng20zW95GG_CKemqP6lJ_owRk9K3V8M87ZiX6CkIaQkuC5wK4d5vKFIAGGAPdNc1KiQXeQgdx_etN-QZD3C49qMWzYpa5oosOYPGDYWe-ajsHMwU9nY2EAvBfbC2x4AAOq_WMvnkXAg4_MKtuKzgf0YyVqyeFiSRKVfFel2d6Ht5Hl_J7h-ApWSxzxMUxkklaNATsWrJD7cuIqhz1cdXpwzP3_YQHJRiiNflfen20uzaVdAepqRsUwnPcWWahb2deCpyur4d5A4DuqCbSMmcBgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
سرقت‌ گوشی سینا سعیدی‌فر گلر سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/99421" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0HdIVlgHJ2nyWevNIM3uf6NypSGoGez2_PrR_Prz7fJ3sd0pvY4JZiOorrE11l8jANRHnllUjPQ0wsRIcbr8cxy7LJF7F3BogLQFT0kUUwk0YJ_gVwJ-Bf6uDYXoFgcLPsVD4JLWrLB6vtQvQkLStKxFPQYrJRJ3tsJHVjCJ0OQXZ1onH_NV6Nmd8CHjt1oyYjL8R8xPKrIHv6UM4kdbSoEMbY9EXVtehP8ZzxNFHD-41cKohxqegRKxld0CA-pGmDgsq9Zd05XDFz5Hh4reISRgXfWiodr8Aw25Atcu7fzAGLguZHokACpUQs6maY5sH4HxBme3moEJLCnLbfkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/99420" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZxiPiKdcvncQ1ZXeV_5mexnXZ99vicN3BrR20h2oCabiFGjMiw0Psp6Ca_ktX5mF9I9kpZ4qEK2rPxZSCJLCAegnkoiofGas5a2m8Yo6GC_8fHIBWYgT72Jz868XEmeoW-KmZ9pCyXfuXE5ivJsBA141LmMJt0HuOLdG0GqXVkfffOoAhcQXkybWAFSjnmPo4ywl8g6Vm8VXrgO_C-sGAwFXS44Jz9C4QIWWccK-cjCYO0uasOSsjE1smRBk8lrzIXfEs0gV85FLvecoYYHIRlBOQ-KtcabmuamJ7PtDMCU8V4hmbyY7qlspqxMmyXFCe2o-UEN1z2uCG-T5lI5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
👤
استوری رامین‌رضاییان که تمریناتش رو بجای حضور در کمپ استقلال در کشور اسپانیا پیگیری میکنه و اعلام کرده که بزودی اخبار خوب در راهه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/Futball180TV/99419" target="_blank">📅 20:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBc9Z1aEE_Neb1AyCiFNIdCE8VJzKiK-EHsj8PZJojr268ZJyMOtZqJt1zNGoa0TqD4KKovXvhMkx0dkmd75bqTCVOTn3LZ14YvXlsbgh6wo9CCpV3j-pJSC-WRQUF46eWnUAnoViqY9WaTD1thzfDI1UYiq4ZJpQEctQmLeSHSMDzp6W4CXTizMgiV0GPOYTmIe1IuNz3a6hsLiSNjT8TBYiuoNbFv8HO-hDCvjrPrIOTvffoiMx-FTW-HFttcpybHGXlzpwS8UjuuiuHLLiQaTPaiZSD41f0igwb-n6ZLrkzAjL1K9w6gvglE9T_W4k2g4bT8OriFjuQvIInRH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مورات یاکین سرمربی سوئیس غیبت یوهان مانزامبی در بازی با آرژانتین را تایید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/99418" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/99417" target="_blank">📅 20:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
🏆
🇪🇸
🇧🇪
تیزر فوق‌العاده از تقابل امشب اسپانیا و بلژیک در ¼نهایی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/99416" target="_blank">📅 20:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هدیه‌یک هوادار برزیلی برای کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/99415" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
استقبال پشم‌ریزون مصری‌ها از کاروان تیم‌ملی فوتبال کشورشون بعد بازگشت به این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/Futball180TV/99414" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/99413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/99413" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHkaqOwmRCl9SiHWV5-CM94OPN8QpXxc1jbMk9DS3tok0z4CgJAaO8TCP9n27qqxlap7Mykpg3grCMUp8QYGMfXWumSV-TM8cpNJCeq5wNKZgWvYTSh03QmD_X4va3a8NoAc9oWRZi-OZWZbtzKnf2yG5Trww-i_EoTyNnzeGf5S6ewWcnXpvF4J-v8oo8Dk4nK6T3RjwbCGIxi6gKHiRx-Kzj2k2wUvarCxLV4H9bZymG6ISAEoT49OXL1WAdI6qZYd7JRkCDVrMCwKAX44JTTIq3fm0FCKKQw5hCUOR0wKCp7YWwWW33tHFTs8_Rr0x5005KiwNCP4vI1d-W1fsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《
لینک سایت برای کاربران ایرانی
》
👍
《
دانلود اپلیکیشن اندروید
》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
19
🔤
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/99412" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0G6j8TuJFN9Fkva4u_7QOa97wymoLPRkVBPyDjTnLgjbWlRGi1BGz5cCs85SBK57i1q_zDKhSFIDg36EEhaqljFygRlhPZR7nMmcSUPBpMNt2ckUdEO6uLBigUWmcHf8hM7IBgoDPcqS7jhovLG8R7Ju27O5c0X-EC_kvNC7S-G7-wR7YzvTur2zeKWusB3_FrfV0_wplYzsmxTlxAd2yAQdSB0KdguELsKVWKeC0-XHnRF1f18ylcGkD5HBpE2xz7NoYQvzZW6TGQeZgUtmbbfJjwbvimxoQjip3VOfNL7oSoYX0IQo8TBVrH8hni6qtB51w-npPpfl__tJE-Fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‏
🎙
🇧🇪
رودی گارسیا سرمربی بلژیک: رویارویی اسپانیا و بلژیک اتفاق خوبی است، اما زیباترین اتفاق، حذف آن‌ها و صعود به نیمه‌نهایی خواهد بود
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/99411" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/99410" target="_blank">📅 19:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfRHVW1phdqLX25BElwyS3Fko2UHaB6_WajR3pI0rmrZ4fVoyxD_F7lQYEmSccEOqdRWgx_fJ0WtCkbKGkMHPW3_9nkrD8ojunHzg66WpumRew-vRxOGuo8Bn5H9mxW0m7nonYWMLCvxEYHNbCgqPwYzP382yrBOjIU9-jJ3faWfD-uHPRGtNJOO7cVguZJ37ufcFzL5tDrmUQneAbf2HvrMGMx7HVpmS5Ryw4Wt8sDGjfe_vfmmgaTqiL8hgiSWKD_dgOrk6hWPYWKuG8_GmRUzGq8wGkeG_O_gZJts9HvjEfq2UJZb4fCFUUQj0QxRXukgdR414cSYbEtU7k-Zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو:
آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/99409" target="_blank">📅 19:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFu6muvZKfrLN4Ol1YM44N2zX77_1Vut-f_utrLPP3pqg6H6dfsMOWnSmfa2k6G_altzxsepIevWcgvu2xw1rbIQtZBwWsugj-IaIdmamE-wVaJ0LBKRGZsjmxXQ541_I_lcaB64fIjlComBOCvS6lyLS-xZ581ZpkzRlTMqYtZEWM9J8rnGWNGuL4ZwQVIC-mCiJG6mf9f-t-1jRCvNIfHj0mZDZTXWNs73_d6msG0IKULYBej3tRI249AHxpm0y8HW7lBMqSuCgBRdrX_t2_IUPTAgVAS_fZR5Ss4qrgSOK0yyGwMSn1ThUjQZY7nCVtgZGYbWA01gNOeBXIZL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
ایکر کاسیاس:
- رابطه‌ام با خوزه مورینیو بیشتر شبیه یک ازدواج بود که به پایان ناخوشایندی رسید.
در سال اول، ما بسیار نزدیک بودیم و رابطه‌مان پر از شور و اشتیاق بود.
اما با گذشت زمان، رابطه‌مان رو به وخامت رفت و به دلایل مختلف، از بین رفت.
امروزه، اگر با هم ملاقات کنیم، احوالپرسی می‌کنیم و حتی می‌توانیم کنار هم بنشینیم و بدون هیچ مشکلی صحبت کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/99408" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC3i39q2Kxf-78y7dxUNiBGyOvwKZgqjqBHi-GWHYpns7XEUxpwA652aUCsV86mYd7kvjYec0nvtiTAppGDNj-pBUvoZ6lwaY4TDQHHMQ2PsXk1n6MXY8oxGqm_Yp9oVRpbjyRgq1gEA8-5EC58-Upr3Osr-6GD75lED-YtoV3O9wGg0q4ZwEJmJmnLovLlr8ISwm9QjIVUVEt1ra_5-dOfhXJL-ujx2-n4hVsgd9AkD8TQmxFtkzDUDT2nUJzLFj5MIqe_QieSpVhoTgyNoPD8RvHyQwo33QN_HzcdGW8oi1XDh_HOz8LlbyUoE6rvw3WTot7DPhxh3p904aWVAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد سادیو مانه در طول بازی برای سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99407" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnWS_BOj8GwhmxlLSByQNoem3AWbBNsheCzijQbsEBHuhEOhbEyu_8hl37rXysPRJ9mISsDzPECf_Yh56D3or0WaxgPPSiWjnwHdpdA0zKblF2Tl0rS7yzAqZszHLkpgM06X4Mxyqu3_N4RYZ8v8rlsM__rKk5P7v1z9cCjtKEQQMdhzV4KlHHSELWFwdlQxPIlNEGTMsbVqGIR_kP08rttHmg2bOJnGIp9M2DtMx1KIwmILsypk8bU5yR0Y4vR1YuMWtL5CEW_iiJl02gC4KK4COz-nL0dMPy_JpsCQFlteq-FAFKxAxRjLqjWx6tdd5NlOhnRB2Sli0fJFFdKRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/99406" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v68KAnF-L7DY0JNPqhOOt5UdUvWEBxr3HILrtX963ra3qGxaJJ4RzsOY-bTgXhcOw9z9stJPjJ4nzrI54lXs6QgUkHXHhr9cfSFK2QM3LWiRCudDYdK2ALFXzL4eueHQyQ2HW-ggxtJESSO4-BJLX6wIox2eC9pYBxRxtXrWrzIhALhhdDlG4NgXn_smMZtHlco7HQUp8CCjqMv8xZxCO2dg65XipS0bBgtC3DFoa2fAdQ3SAio104HDt67nwP6-JOW1zonWdfizoqtjrwOj9lc6Ir2lyZcoZDHc9MtjaR6_2MadqBShTN1a9X3cvVqPo4Wkad_VFTBdTuZchllX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
اسکای اسپورت:
بارسلونا پیشنهادی به مبلغ 20 میلیون یورو به همراه 10 میلیون یورو آپشن برای کریم آدیمی ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99405" target="_blank">📅 19:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj2rz31vgUnenkpibh0eEUOq4t46h-zV18c2zuPeXuD6jEboclh0PTka-VqhNnruc6pi9KAjzuPKgtTTbNMOtJsFfvc9g4asHm03h4bizC4BDfMAFSNhiG_Kj9jmvgTf5838sjG2YNRp7e2ranI6SV-xJHKZaW1YyFWQp8iazhe2PBrSGvWM-i-sNSGl84vJuWYHU-47EdH5bSpesZmYD--FIQuDt_FuJYWWxjLW91U4yLa-OOHvuA3AoJzi6R6jYxG_hc6HxWtdefKT0ZLX1zboe8EPZ_HuFHBaOpo1IBdsF_PcqJaFF-UXK0UXUDFmj9idhDJryaAKqjrFmTCN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇵🇹
خورخه ژسوس:
کریستیانو هرگز مشکل تیم ملی نخواهد بود، نه برای من و نه برای تیم. کریستیانو نماد فوتبال پرتغالی است. او می‌خواهد به پیروزی ادامه دهد و دوران حرفه‌ای خود را در النصر به پایان برساند. کار کردن با کریستیانو آسان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/99404" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECu7ywxPTFYGn1SlxxF75gAn_HDTOU36itdfpjKksqhQ33jDSglRefqhNybnuiJpxcrs6SiIEAu3wWNlgxMjmZJaWLkZDXsvRj226VwfHOWI4jVSs6H8TpH2hgSipfytXoC8qR3YcO-JRS6X1BFz_8n62zrDVF6irSV14lIx5OrPVo5lOXDd4zm6KulQhPBMUbM_MzU7_GWtvO8ZVQsFf5Dr5R3zp-2PxpRACP3XyyU6ynZeWqpOUGkZFf6xJQ-JY55iEcf98_VAnAPbBWIZRPUBn-TXWBASacBWiQ93ZKZTdI6z34l-iV-isJea7kUGbsKkmGwNtxNHd6IlH2W6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی اینترمیامی برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99403" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/99402" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqtUYLgR7msF2j3Q03eGvz2msE-_XU5QAV23ZkDRRMBxvUVAu57FzTfgcoAOcC-8xvnZYHiEwxukfiA2VWUr9wsv7IzkiLA1WIQHz5zR9_CnIyMXkFYyZnVVH2EMTfmgqamt536p3xy4vbJ7jDNBFBViweDXdFCmrdnr9PFbRj5fA40CpEUMSXjZtg-GsRH18dI2udBN1N43xeSaU3XvmlbVbVizq2XpmZhJXa15mKxi8klOixJZfKJ_0tSrNkNplqYyuL_fhIY2DYxnqz7dMy4p041x71ZlF0jlNTuYGHxqaoAcN55YAzIYG5_fxRNG2zhSyxU7F_Dge7_SJgw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین ربات  بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو ربات و ببین
🔥
@TNT_Winner_Bot
@TNT_Winner_Bot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99401" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnJSC96TZo4SrsUkwjR7LsB63B5TMHsdJMSeHa_RYFcRAncDjHS6gS8xfAmkhWPPPH3R6ur2VGVzeFHUfyl0x9EuOSb9oMTJMhEZ1mtbRVfOPbH4SPEhz7u-SJRDsw-2iiAihS7-Tb4Mhp9nqHBOmGZBH4ZRdizJEmzH8sGUtVtyuA2rmIe0-3HlwaRl6IKD1LgIhAI2CqjkJCARb9vRFNTDQVnAtOPrcVnx8ksCWltYrRx0C4r7VRbBfQV9l11HqDipA4bhMhiCB0Yn-3H1c3I-foL0MbXX5xnIanKBdUX9jjjtPkENUOt8RN9PgdMYxRmo1RpHmh6EHb698FD0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر گارسیا، دوس دختر پدری، دوس دختر و خواهر گاوی، دوس دختر و خواهر کوبارسی تو امریکا؛ همه خوشگلا تو یه عکس جمع شدن
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99400" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4zspXmnrFoQ0muCRbLXwfu_6YxSvMsQA6mwDlt18vliFLcspuZagnE0tNhhO_-nlbKLpBji_PjqLAKxLOlNlDuwhE58ixMWByu8qAO9Eca2-YsbofiYcfuW5hbBkotu1AbKadNfuyATAScHUHwWDfmxU1AhfRoW2vJh6NpNOquAkwSIwRkXJVFF5IwJ_MOtCIH8Xi1aDby-vgoPL5Y5qo2ydWAaR2aE4DMLAKBzqbH0-gFInYFQrYxnuPtnUM8guDb_-6bODC00gpZhy9x_v4ZqJnW85uc4Y7LJTYKRs3k_-Ts_aqqsFeKsTu769su7jSzg5she_wtueZejlHVUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری
؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99399" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99398" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
گل‌زیبای امباپه از این‌نمای تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99397" target="_blank">📅 18:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
هوادارای مراکش جدی‌جدی باورشون شده که امباپه دیکتاتور هست
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99396" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه سردار آزمون به میثاقی:
آقا عادل واقعا دوست داریم شما برگردی به جایگاه سابقت، حیفه واقعا کسایی جات بشینن که لیاقتش رو ندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99395" target="_blank">📅 17:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE8l1uO5RGbjE5Ianfx5heefrlsYdABxcp-S81SlwLcXMCvHcFWKh5Q5tK2HjluO4cyYK2NPybbRbIkVSJRNJPVkgGzLvSURUOMlrOaOzs-30Tj7SWuV8Mo9SVEGQ1RN1UKWtw7PlM9V1hLGkZQ8j8wyt26xiVrbKwxicGjak4cGlTRpXtsJ_CnQFdMBK1R40P0hJ0CxY_pPneYUJbuzAHQcorlVZwNbUhHfBETeA6IfhUPzT4iZdj9HlXKt3XysieCLySVDUYMXceUcdoyhB88tXVedP5Uh1rncgu7cojV_1_c5RPKlC3c5oj6W6a_7yLbsOi9oBrUi35_b3aSD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
خورخه ژسوس رسما سرمربی پرتغال شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99394" target="_blank">📅 17:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
نظارت دیکتاتور امباپه روی ۶ تیم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99393" target="_blank">📅 17:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
جوری که جام‌جهانی برای آرژانتین پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99392" target="_blank">📅 17:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI1mjeSPp2onJthtR_G05FZi5zcDlbCwuPhNf8o4EQEwejBQImiVaLuHSizsY7UQc4R4erDagwtaAAazm5_h36tI_xYl8kZyBqN6MsTKF9rHArg6gtwnZZuNJC3zCkkRt0Gbgfc3cX8730djuPtJK8gl4PrT66lE1g57_hnZXwR3ILoQhfHHwRi5qdgsmD4oDt824AfgzLTHj7kxwy0AIdd44QuMMdEDk-FTeUZfpJ7ahEYWMaMA1_gUS0D4gcAqf_k-VTubsqgghgIGFW-as0p5LhhLM7cVyX_NRObkYp4LXJ2GVtb27Pd2cM4EjVLccKPer7ohtPvfIoiIhf4URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
دوسال پیش در چنین روزی فلیک رسما سرمربی بارسلونا شد. آمار و دستاوردهای هانسی فلیک:
🏟️
• [117] مسابقه.
✅
• [87] برد.
🤝
• [11] تساوی.
❌
• [19] باخت.
🔥
– [323] گل زده شد.
🫣
– [134] گل دریافت شد.
🏆
– لیگ اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [1 بار].
🏆
– سوپر جام اسپانیا [2 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99391" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE3BtUnDrVwkRrlc0r0_w6lJ2308oloNT0m66zMYaGCWqx7aAeGjjNTSehIC6nDuCQh4QSIreqSYrQfrX5u-WSgV0XoWSy4jCoflLPwn7W7xvoXOdbV9joakXpFGCukVkjDSSIqhiP5GKPgblji35lbvEb5gIsOcPjz5-PUabbcQWUHJjYOZ_Zcn4tsRjpeg1o2LLEkzHc6PxiJsSOPUOGiYUgNyWRRcOuRF2CNspMo6nZH0X1Z_6kov-kLC0xnvzblgA8dyZoIjn0FYRqmB6Qxyawn3vVSW_AGtiiQLUbbYTX4X5Cy_DxfGj1fjQX8tdbmTeYfP2esxvaIscNj_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اردوی تیم‌ملی انگلیس بازیکنا و کادر فنی به جود بلینگهام میگن Unc یعنی همون عمو
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99390" target="_blank">📅 16:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👍
▶️
🇦🇷
خانه‌قدیمی دیگو مارادونا در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99389" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC4Ex5ER1S_zUMGol7tim1dFUi5E3I9B_-vPfeBvTVN3hynVu9ou5hVBGcWBMHiOOU73Tf7GFXpssfsA7q1-1RFp-IeE5mBy2vrE0YylG0VTRYrQiPYh7KKXcqK7Y9L1lOGah7l5CGBEO2LwMyC_9jvBen-CmEcyHwtOEc51pE3powyccZH_LFqMwsuM90Zb97JK72c97vprmnNQX_mm30JnEOl-k8keXkxUSuXUalHNLSO4ciF0ufMAZ4CMFviZ4jg98ydh70AfgMqsb-gnukGPI2M8GhCdeag_LXOgO71t9qXn8cxO9zPPn9OLXWp0S634Xbgu6ZtjTcfVLWb60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🏆
در چنین روزی
اسطوره تاریخ، لیونل مسی، اولین جام خود را با آرژانتین به دست آورد، با قهرمانی در کوپا آمریکا مقابل برزیل، آن هم در خاک برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99388" target="_blank">📅 16:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoBO8tmhr31k5zDQbNN7IlYIHxg6oa27RbS5re-elHrawPSR3qJ1NVY-hmOSK90nHAFRrVg50hrkffSLk1zFrdalUBS4EbGvKzUOKK1lDMGga1qFdwGG1GH2LfdlNKglTqEToQ8HZind5wy1LAZlDuZ2DcGSEAphh_ZL1wFqr4r5XH_AnWG07-5ocOLMKoYOA-eCSnOgdWBV9dU6cP6jCeAh0kGuqMx85Qov8cHDqPtoQh9vcWgAz2qOrXdPjSTEWuyvylCwXGJjHfAsAKnFB39d0x-8fNWDVpw6u4aPH6aSUMP_TDyKzwP2yxVWgk_e7cIcra7lZXNpieE4P0kX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚫️
برونو گیماریش به طور مستقیم به ادی هاو اطلاع داده است که می‌خواهد به قهرمان انگلیس بپیوندد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99387" target="_blank">📅 15:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=aFhwumocTI-QCA-2bwTXMSZK73pjxIqQzjij3g25qS1vGS-xtiSD7pebKJ_BmwkWkiCaaSDO8bK36DWvJgqqaqVDnTDFTpsHMBVwNbJGgtnhgCdmRWm8zel56oJ53qk2KoqjHkOTfIP12_soYxv120aXBEqcRR5zbSyd2MOApCSOWHLDsa5Vs5XUhR2_8HP-DRVc-GYPEXiblen9YhNe2k8Rq9vEZbjgWywbFAIPDsnzgNWJ4aaTU7oaw1Oz9Cdn27QcUNxe4W3TSKzuq33nr2fblieuPQwTwCVX_raBn7LMWMkd9y88vYvn22FkmmfQuskLZVoisO7yPlPsBw3DTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=aFhwumocTI-QCA-2bwTXMSZK73pjxIqQzjij3g25qS1vGS-xtiSD7pebKJ_BmwkWkiCaaSDO8bK36DWvJgqqaqVDnTDFTpsHMBVwNbJGgtnhgCdmRWm8zel56oJ53qk2KoqjHkOTfIP12_soYxv120aXBEqcRR5zbSyd2MOApCSOWHLDsa5Vs5XUhR2_8HP-DRVc-GYPEXiblen9YhNe2k8Rq9vEZbjgWywbFAIPDsnzgNWJ4aaTU7oaw1Oz9Cdn27QcUNxe4W3TSKzuq33nr2fblieuPQwTwCVX_raBn7LMWMkd9y88vYvn22FkmmfQuskLZVoisO7yPlPsBw3DTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
صحبت‌های ناهید کیانی از تقابل با کیمیا علیزاده و فشارهایی که بابت بردن تحمل کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99386" target="_blank">📅 15:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=OdaAACDkRh6W0a0yaIvAuSf2aaNMAQCZzjSawLEb-Ms43zT9JSTxXTrUpLL0kElZM5H42yieE8cTJ7RAlGu0Rrj9u3g9XdmokM_Awkwd4HE7EFwGFQudWUYznfVDO11qgV9YWpjERwBz2Je1d_WKvckzQJRZeefRwBMbkhmkpnT3CjeQSDvOWCbBTgctureK66TJLemeAhD3cKhFRPPMDg4etJfGylfP2pgTcl0VLkbZoAeow843cABZgawx9XaEanbvAs9mwWr1eMzlZQmmFb93D6ieuL_VavbAMEh5jJ2WJRwBcZhQiATRcQlJbss3iwdPjF-6nHqmEtjbshQ8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=OdaAACDkRh6W0a0yaIvAuSf2aaNMAQCZzjSawLEb-Ms43zT9JSTxXTrUpLL0kElZM5H42yieE8cTJ7RAlGu0Rrj9u3g9XdmokM_Awkwd4HE7EFwGFQudWUYznfVDO11qgV9YWpjERwBz2Je1d_WKvckzQJRZeefRwBMbkhmkpnT3CjeQSDvOWCbBTgctureK66TJLemeAhD3cKhFRPPMDg4etJfGylfP2pgTcl0VLkbZoAeow843cABZgawx9XaEanbvAs9mwWr1eMzlZQmmFb93D6ieuL_VavbAMEh5jJ2WJRwBcZhQiATRcQlJbss3iwdPjF-6nHqmEtjbshQ8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
افشاگری رضا جاودانی از دلایل کناره‌گیری از مسابقات مردان آهنین پس از سالها برای اولین بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99385" target="_blank">📅 15:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlWRQqSyRwiGESJULgIu2iRvsYEJVXxw9f3RBuwenk42reZJtsopmH--dvb9FxvdEQ5eWwhLanhi6-Q8LaGohM7LKW8DU4QA4hQPq60tgzJMFmJz6IBsDh5-WaitpZMu71KWJRty1VlUPaLV5RwoITMTf-6SlfxYozIMvnZTYDwjxBlVuJwjrHYWnFfHNaiXuaMyBQtG_7r5Czel3Q5EmQVxtS8AxnndQsB6yM-xRrofAXPcwG_hs988Qq8mhOsVReG6A14z9bMo42_9k3k6lId0xgQpXL0WMgnez3z_WlvIwEUVtNoNnKQk39sCo6lbzOlC2St7l5eTAZd6pgN0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
بلژیک رکورددار بیشترین گل و پاس گل توسط بازیکنان تعویضی در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99384" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpQ832k54Wrd1dEmb9dug_oMtstp5bvYIafBQu1Lg1LjFG2ECgoeewN5CSkuphWUVo6DacMTRxw3tytGjTLeAk_pJZPbscnthKey5WAY_JXfTO_5VcFeUAmuIJukjYqVjuKVd-ff0dDrJF_IlNUlXltBFIujTfdO5TEsjka8bKUH2m2SC66Bw82-A0sVrlMxnyyxB-rRr7fv4nWGKys8AvIoA3fvbzlqekFBL9tOnw4QUeaYJy8Fb8tourNCxvEahgalyu6cxVJF3ZA5O5FU96VynFWJye2rk8EoNV05PmtXd0wZgWz3xjBjQ1_aTe2nClFME7kXnOdcGAWXdW7j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری شکیرا در کنار بابای امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99383" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99382" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99382" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvSE49ZYG8Vn5PcrVLtMlTUKJCV5ZXeqGLqana0CYayivI5eCpulWHPMIR4WHyIbf6JIBrVHznVseJaeMAlC5ChKzb6E3saSIamMGcAMc9MXZfImUZ6uDqjC581DrP3GTOhvzBoBJ-nyBVjTE5ecu7z_OdUF57F_YEFdJUHySxv0PYkQtQ4Vi5lU1xo3jes8iBMly2FLDSk3f2qftnOWxPdOKRjNKonbG3p1e47biO3LlE3m4xhTV_5_sZ1MHhUL9hPn-KZzQm_HJlfL6vgi7e58DDbWOerAvhmQKNnWLsImtcrFAOURuLjj8f30vZa7DpsCMoG4tRZIBbPkhYGrvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99381" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7Hqvn13Bc3P50Hjzav8ojQIUyOUlVGF-5U0xPelF4WYMs8q0OYzH7A12C1bwTqd67HWtXod4yLmyX-JFmI7vcdcAJ8MXNqBdRKW7d5WO9tfQHdd0qUJ1yQv6d0RAqRkqnBYtjwPmBCHXiknTiP5iWIhq9EsA0LwVlvDOm4TD7CCtqCqWbNmxlbvfeEX6AwKEaCFEgEXYD144E1RrDD3p08oKDquucTfV4G-a6EO_yPQ9U7KN0NnftAZBEvKAfTtrkkyTejKYV94g04GMkyKorR_FzJwcq8tNHuAq6p3D6oEJdTwAe_seaNcRt-BNqj7aiDiTyHVLnPg1bjC7Lf20O1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7Hqvn13Bc3P50Hjzav8ojQIUyOUlVGF-5U0xPelF4WYMs8q0OYzH7A12C1bwTqd67HWtXod4yLmyX-JFmI7vcdcAJ8MXNqBdRKW7d5WO9tfQHdd0qUJ1yQv6d0RAqRkqnBYtjwPmBCHXiknTiP5iWIhq9EsA0LwVlvDOm4TD7CCtqCqWbNmxlbvfeEX6AwKEaCFEgEXYD144E1RrDD3p08oKDquucTfV4G-a6EO_yPQ9U7KN0NnftAZBEvKAfTtrkkyTejKYV94g04GMkyKorR_FzJwcq8tNHuAq6p3D6oEJdTwAe_seaNcRt-BNqj7aiDiTyHVLnPg1bjC7Lf20O1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
خاطره بامزه فیروز کریمی از تاکتیک معروف «آفتاب‌پرست»!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99380" target="_blank">📅 15:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=vG_PFBhR-EfXHm2cyZrrmU1Jqa-63d4RQaa8utOKQi_xjhoiByPnZdwV_7IlcmsNZ3ZchRA_rVV6uQY17tijWRvGXq6Ladrr0LguLDailGRIxJRxCj6C8Eavrcbub0xjJGiOS989MimChxcOvzTJLRt3NlDDZ1jyHDrzF4bNhApqzS3z0DDmAXINO2xtLqg3zs12hAFYGFHwz0BO0HM3Hl41EPq0iDPtKDFsPinAgIj32YcSB2_0CNVehFh7nXrHGUKKvJsLyljJXQwXgzXiF25ruwG1ry-IzXbyIT8nsStrLcjXfucEYAcQlHU5F4CIivPBHC4jBRWBznemjp3mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=vG_PFBhR-EfXHm2cyZrrmU1Jqa-63d4RQaa8utOKQi_xjhoiByPnZdwV_7IlcmsNZ3ZchRA_rVV6uQY17tijWRvGXq6Ladrr0LguLDailGRIxJRxCj6C8Eavrcbub0xjJGiOS989MimChxcOvzTJLRt3NlDDZ1jyHDrzF4bNhApqzS3z0DDmAXINO2xtLqg3zs12hAFYGFHwz0BO0HM3Hl41EPq0iDPtKDFsPinAgIj32YcSB2_0CNVehFh7nXrHGUKKvJsLyljJXQwXgzXiF25ruwG1ry-IzXbyIT8nsStrLcjXfucEYAcQlHU5F4CIivPBHC4jBRWBznemjp3mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
لحظه احساسی و نوستالژی مصاحبه جاودانی و زنده‌یاد دکتر حمیدرضا صدر
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99379" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtYcA-KlYNV5oNO9olrkPKNsdqkEi9xsNWEyZDNiunlQ2CXwchnZVO00gWuPUqRuvBDRyigxGupKLvmrG77H1-qqWhGa57ftsQrC9deOvr2E32rRP_MhvyLPFMSUjvONvkaaFe6N4vMM4OxGeZ8JC8RZOMuJBqMAmdSQPvmI5RaqhL8OXm-N39INiFsgG8506Ba6-RmDFgGW-SaVWN-1eWUZEKNnC1eS5sebu0N_PDpb_Uf9jVAyWLEbAMjkXGtPZ9BP8BVDQsfmThsDEi_s8oX48xNKimtt1k48OMmYy4DLq2g3aQofAoaLZnDJ7qJGLvNVHGbat7F9YgS1yiK58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کلود لی روی درباره جیانی اینفانتینو:
وی تنها یک ویژگی دارد، اینکه به چند زبان صحبت می‌کند، اما یک احمق چندزبانه است و برای فوتبال خطرناک است. او هیچ چیز مثبتی ارائه نداده است، بلکه باعث شده این ورزش در نظر همه، مشکوک به نظر برسد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99378" target="_blank">📅 14:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=kXWLEqnfwjCS-g6-CRestG6TWs3fLdBUm1KoUjJVURWcL6jqHvQR1wYiq7O00QtRpnrct9ArXwUI2S5izYJ7d8JWSyVmIDDQ-t2r-29WK4EA13k_vb_M86-zKwamjtaYjpZN9-h2mCJL79yIZgS0KZ5hYQHPTDh6otagcdnQ9f-2rkH-2LodobYmxJq_jvzMynsuv71fidHpMrncUNsX5EFnC9qle8WPSVn9sVWgGWKUmpQZqPixBSnAUDdl7Qbu_gLlDVCvW2P3aX5FiqANg8d_Z6lGRVzu49tOPAXMUSDa_OKjWrFMXV6bIVv2LMxykU83KGBDBHnxE86hzkWOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=kXWLEqnfwjCS-g6-CRestG6TWs3fLdBUm1KoUjJVURWcL6jqHvQR1wYiq7O00QtRpnrct9ArXwUI2S5izYJ7d8JWSyVmIDDQ-t2r-29WK4EA13k_vb_M86-zKwamjtaYjpZN9-h2mCJL79yIZgS0KZ5hYQHPTDh6otagcdnQ9f-2rkH-2LodobYmxJq_jvzMynsuv71fidHpMrncUNsX5EFnC9qle8WPSVn9sVWgGWKUmpQZqPixBSnAUDdl7Qbu_gLlDVCvW2P3aX5FiqANg8d_Z6lGRVzu49tOPAXMUSDa_OKjWrFMXV6bIVv2LMxykU83KGBDBHnxE86hzkWOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💥
صحبت‌های شنیدنی رضا جاودانی درباره عادل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99377" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw4_cJbxREFZcL71ecLhdPnsghvDWq8a-77isj9HmCGrxmuxD2nrn2dOsTcQv23uywGXAMBvL7tcbDeUOtlKwun5kfjJOnP2qIMYxSkp5FeTx2u7HsM0pWEg-Fg5m6uBB_CqyKeppASovB1bgnJZAlS4psAAhj28fiawd-SgiKR_RoYbNX2ak6tvz1agWtv3SNehkXDSoIhObBUtnpa8DkuL2Kc2Uhq11aGK_zyfNg2sb7UdZjIuZ5j-lp-HPy9fYg9WpkmU3VykG_dmbA4t7_IIcp0_ne_XyV1YF7yONDKWH6xQ3-6ldca5vAzuVfPfd90rVJCA6KK_kxeeIYoUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کادر مربیگری جدید رئال مادرید با حضور سامی خدیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99376" target="_blank">📅 14:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNS66J0WP_5UK1-XZVx0ne5QWgEmswIqFW9NZw3j7FpGVn8mUlMk7Bf_gyJPgHH23XX5xqxxT0Yx973_TNzVPlmFieEYo3DvgdiRVXcw_5Zr_G4HC-zdWcZWtwznFrDLAfs5KQTGoxP1hkng2DkECvy5f4P5OUkKpGdoLyZ7zQfZttTDs2ZnTffI83ET1kDbeb2hYS9r66zBOfpXhlS39_-pMSXeYu-BTBgqQHtqp_10SjpinKgG2xdz-AE7aekAdsXFAIHMwhJZNOUvoRgqGSUXWaJyeMZAlHM0V-uGsxoUBIAPkWtqh3IsAvrM-hLVRs3TaF28a63L_nva0lBUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇸🇳
پس از حذف از جام‌جهانی، سادیو مانه ستاره سنگال بزودی از بازی‌های ملی خداحافظی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99375" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVhNYjj3b0OXaWPHru6V-XUx0TH0_nj6H13zQwCy1VRW6gI2NuqmjS4z56HyjPA0SgkeTAasL1kl1rHlzqeTT5N6nVuCgTsH08paTWOX9pIa-1AAGvLlINzAayXYg024fZTz8MqLsWZc88epouSds274O_MC0ADZeM95ggv5KcxMixGlwMfNN_ho6I07a57-5Y_F4TcGhh81LbQgtEUsYE8gzTh9bDQY2v1WAzhAbKth9ZLYy8DXn-sHzjwHIdsP6GOkXAN2y6AeaaobrXRPOPquE4JfKelbl1ivaJGYiYdBuKjCoVV1DaeSby6TQh2f9eJZfidOiB0YWnr5aDlIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#رسمیییییی
؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد
📊
👀
🔵
آمار ابوالفضل جلالی در استقلال: ثبت ۱۶ پاس‌گل و ۴ گل در ۱۱۰ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99374" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDF8iezXOAdQdqJPZZlvnjE5qOyXGvUWWFhvqxTOzpw4s3M08fYAMI0EfAJSy4XLjBP1q_ohcGVPQy2HmB4AXS4MSHctkYaxeh2anx7wz9JB8zjCAmjT_dET--ldPmXI5T4Xt6eOLeR1OlwWygUC1PHBAlWE7lC3Xc1d6n1iNwZFG-6fvK9JGl9ggSHkIL51Zvg6HMJSvP0w-dC8nHBsJWoKzD4u4GHXURwOwlbe2TJidljPzQuL1cbikdTwlKVPnAgf-DKfoinoM6IR9QmAi1t-0zUaFTl7BYX3GT2cD1JrWM8UkkkoM3_BJtOaXJWfvVjcVNqPrhz2Ai3pthvyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
🗣️
لامین یامال: "اوج اقتدار در فوتبال چیست؟ بنظرم کریستیانو رونالدو."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99373" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-ioNgtcCCClOu_O3-_h1M7aD9FGBXwDtwus-YL_8V58lR7MCy_pUiiDkXzGnFHjg2kcAKk34FrLptI8SJ0V7-pZs98s-RvCEAh7mCIQyvZuz4wwno6OgD1ILzMf-RdOgbrkIXRDcFAvA3CluflqYRHVISPEL5thV83kIhJH-Lt9d7Q69bAd7sS-l-PzoIlyfxyGlCGbBRlokDa0CSVoYbJvUc-DpvC3nAWpWkhiY9VLyEgdC0iHtwD2--gnEV9D6OUBtB706O5v2UgUTjKBuQBbbVgxYHJ_f1LMh9upIzY7puTBg36Z-PZz_fQ74eGd3gYoDbVghUvQIbd2p8O1qdsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-ioNgtcCCClOu_O3-_h1M7aD9FGBXwDtwus-YL_8V58lR7MCy_pUiiDkXzGnFHjg2kcAKk34FrLptI8SJ0V7-pZs98s-RvCEAh7mCIQyvZuz4wwno6OgD1ILzMf-RdOgbrkIXRDcFAvA3CluflqYRHVISPEL5thV83kIhJH-Lt9d7Q69bAd7sS-l-PzoIlyfxyGlCGbBRlokDa0CSVoYbJvUc-DpvC3nAWpWkhiY9VLyEgdC0iHtwD2--gnEV9D6OUBtB706O5v2UgUTjKBuQBbbVgxYHJ_f1LMh9upIzY7puTBg36Z-PZz_fQ74eGd3gYoDbVghUvQIbd2p8O1qdsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
عظمت تخت‌جمشید کهن و تاریخی از دید هوش‌مصنوعی؛ چه شاهکاری هست واقعا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99372" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9GHb_kC9lnwMXnm1XCsxFlxIN_iX38l6-dHeLIctzSF5YdDT5etCpufnq6loKg9EcIGUcd-IpRLWDhj9AAfLKa3gdbrpXjFbLi9X9UHC3y5TYtZ8OFGQYWSInp2LLLRWqekNtvMLsoQANENxBPeBZ0U_BED2sMhM8GSUj8C1I5XAYMp5olGTwezyxzew9Ccp9D4NXf79wnIpBvr0pVYH-hc5xJricvW-2OMdci8AhvlWf3TowtyoDFWDXkmjDDmFytg87_rNtyW3MjzYUVuemQ2SnXMIjKDF-ksQ40VNt8ELdCUwg2uLpX4xlsnLY3mlvT3JNT_rtQF9DRK0smdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🦠
دیلی‌میل: دکلان‌رایس در آستانه بازی با نروژ مبتلا به ویروس شده و در دو روز اخیر نتوانسته تمرینات مناسبی انجام دهد و محل اقامتش از سایر بازیکنان جدا شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99371" target="_blank">📅 13:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=QlVDHYckEQWBUapctVeJmNp4Qfi5to1VvGIZqvyi6HOrYSfmssxwWHT1xuEcLeyHv3i-ln_YTMc3nRpKYLtXX6gQXKqhp8I85ci_-6ym32grZZoJEQdhW5S1T_B5rEVrzgxNaI1ZvxsBTur--uqTzvawH3sxKaQ9wd56D2ldo8GrzTtEcbJvxDwyGS4UxTF84ZdEPyt8TmB0tE549ILXCFqf5L8VuP-EVmRvescT3QQaD0pcdPJLJZYYVbQC9g02nZnWHUADJgvQ3mojNApW8gCrpTXG3TCyyiZqhYSN6xfYCp4hI5FQMlR9yIt9-3fR0EHfCsI8KJZBwBkUTf1onA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=QlVDHYckEQWBUapctVeJmNp4Qfi5to1VvGIZqvyi6HOrYSfmssxwWHT1xuEcLeyHv3i-ln_YTMc3nRpKYLtXX6gQXKqhp8I85ci_-6ym32grZZoJEQdhW5S1T_B5rEVrzgxNaI1ZvxsBTur--uqTzvawH3sxKaQ9wd56D2ldo8GrzTtEcbJvxDwyGS4UxTF84ZdEPyt8TmB0tE549ILXCFqf5L8VuP-EVmRvescT3QQaD0pcdPJLJZYYVbQC9g02nZnWHUADJgvQ3mojNApW8gCrpTXG3TCyyiZqhYSN6xfYCp4hI5FQMlR9yIt9-3fR0EHfCsI8KJZBwBkUTf1onA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرانسه به نیمه نهایی جام جهانی رسید.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99370" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
قرعه‌کشی مرحله گروهی لیگ‌نخبگان آسیا و لیگ‌سطح دو آسیا ۲۷ مرداد برگزار می‌شود. استقلال، تراکتور و چادرملو سه نماینده فصل‌آینده ایران در آسیا هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99369" target="_blank">📅 13:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz1V714W9EFm1pR8v00squq3GEZzxT7XL6JFZZCuvT1pDswRpwnAtesZa2EnCHZ0ufvLB4J5pgJf3Zjfq99VKwbXoIghgKEqSVwRbrKaw4bGy-zjR5s5Cw4FTsJnotSjnB3KTQXjx9qcIxeNwVxmZvMpzFg_nlQRLjryYmvOxQnmwv_T6SEHyW0WsoQhiQ7Ir5egU93k3cnm_7CSwZTZaqNKV9COeftxM1wpz16pIpEEwxwUg_L-dbU5C-42-hqV78JW4tlhHCJKpuuXMrEFMiKC77O5jcOT4yHm2u3Xqp0K0MNNvKyaAs_58Ev0ZimrpnjSLB-0_uK9kL-eSKZmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇾
سیلیست آماریلا، یکی از اعضای مجلس سنای پاراگوئه، ادعا کرد که حساب اینستاگرام او هک شده است و او مسئول پست‌هایی که در آن توهین‌های نژادی به کیلیان امباپه وارد کرده، نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99368" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1CQEJlhMHssX9peuxLM4bLGbo2BVC73cLmFVgh9Tz6pPlt7j3lNZBKaPi3NoTQ69s7A6L1cE8n5egTha1tut9-v141tWBUQX1q0mKxwMgh5W6Fo5XQGPAy0QTOGs6WknU_FsO7e-2ugN99cZY70Muo8M_GDz37-MzLisCzSBYgbjvE4stwUBNUOlnHiHFvf9fi6NlSIA2XMIHNduFxh6BTiqpEWblS1LGWN8dhE0hnmtJse6zExdua6TjmmlyK2ePJKj6k_9CV-of1D8glOScGAifCvL39Oh9HobHf83kr4Xp91114VeBJOQKf3a8u8oub5juEjpxniWA8xK70rXVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1CQEJlhMHssX9peuxLM4bLGbo2BVC73cLmFVgh9Tz6pPlt7j3lNZBKaPi3NoTQ69s7A6L1cE8n5egTha1tut9-v141tWBUQX1q0mKxwMgh5W6Fo5XQGPAy0QTOGs6WknU_FsO7e-2ugN99cZY70Muo8M_GDz37-MzLisCzSBYgbjvE4stwUBNUOlnHiHFvf9fi6NlSIA2XMIHNduFxh6BTiqpEWblS1LGWN8dhE0hnmtJse6zExdua6TjmmlyK2ePJKj6k_9CV-of1D8glOScGAifCvL39Oh9HobHf83kr4Xp91114VeBJOQKf3a8u8oub5juEjpxniWA8xK70rXVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
بازیکن‌سابق پرسپولیس نطق جدید کرده که البته برای اولین‌بار احتمالا حرفاش درسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99367" target="_blank">📅 13:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDYVJ9Zpn7Mao74ft0F3KhF7WDa1G5r43RWVTSxLViv33KqquxmOhZYEC7AH3X8ly9ltGWSEV4l8E0oi8eHmBsB3883lW7P5LHLj-AS5dKk1rf8JG2XWu_dHFu8AnxkS8DZ8sjlTOM9wZ5Uzmg8BS2xX7zu5RlyvmpTFhAm8C3ynASiDErdQ9NzJYSp_VSjp_UHH_sp0hkalw9v2K5czOMILTGBCG93affwJ6j77VjTtL7FMF4GMM5l3FSS0bRqmLyVOuSvwmWneottv5sD3vm1pKAQcGkaF_k-0q67uIWRBH5rE6zvyT_tExtyDjBihGv_Dm_K4jPeRCdtnnUMkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
موندو دپورتیوو:
احتمال رقابت بین منچسترسیتی و لیورپول برای جذب ادوارد کاماوینگا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99366" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=h3pWqiNwR66pqKn7NdHDGMfrzN_5WorHJo9ZGux7Ru4juO4NVcc8K5iMGPJhu42_WOCCKslKtvQ5txNm_9kq3dbER31hUYuy3GN-SqcjMQW7KLOgI2ZNyCYHdWgU9QiDY1OY0uMBHY-KULQ1TZQs5q-IBtXTZ7KzbhflEe8Dbu6K5le4eypzLJhgiQVyp7pcs1GMlTjIvjgXuMjEG2gzj7OLJNC-v2AmLyFQWXypBA1-Ui2Kc7CCkjorIllYyqWzo7eeTzinKTfB69Oa5UNChyh-HGnrVLQ6mICbSC8qK8F5K28UviLwAk237mtTGTmHV-VmV0zOpuNhBPgfRyndbY_J8FH-N9uHKzpeUtYJu55nHZeAoGMT43dp_dpBz3avRit89ya_B4eS-0J2V0fhjQkqEbv4uBpIJXQqAcfoUHXy3AoWj29RUO92d-v_gJxBrFqigIQ-SW0Gxkhls3-osbiCz1AquVVE_2rjbJJtoOZ36QgtU4eHNy03hOk5y8_eNGaZb_-NoAiSfnVet4kgqHvE-MoClrGkR8g2Jm8GeTn5U9JdPwuCwHmv1mHCfPNcHo840CTyrGTsYZNygCKrdE2eke0pD6E8uoXAhOB80YQZXhYSIdHLYfFnulm_MSlE8xWAgRu9MveSrn_9d9iHj_YkC7q_yRl0VKTzkoZ_SGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=h3pWqiNwR66pqKn7NdHDGMfrzN_5WorHJo9ZGux7Ru4juO4NVcc8K5iMGPJhu42_WOCCKslKtvQ5txNm_9kq3dbER31hUYuy3GN-SqcjMQW7KLOgI2ZNyCYHdWgU9QiDY1OY0uMBHY-KULQ1TZQs5q-IBtXTZ7KzbhflEe8Dbu6K5le4eypzLJhgiQVyp7pcs1GMlTjIvjgXuMjEG2gzj7OLJNC-v2AmLyFQWXypBA1-Ui2Kc7CCkjorIllYyqWzo7eeTzinKTfB69Oa5UNChyh-HGnrVLQ6mICbSC8qK8F5K28UviLwAk237mtTGTmHV-VmV0zOpuNhBPgfRyndbY_J8FH-N9uHKzpeUtYJu55nHZeAoGMT43dp_dpBz3avRit89ya_B4eS-0J2V0fhjQkqEbv4uBpIJXQqAcfoUHXy3AoWj29RUO92d-v_gJxBrFqigIQ-SW0Gxkhls3-osbiCz1AquVVE_2rjbJJtoOZ36QgtU4eHNy03hOk5y8_eNGaZb_-NoAiSfnVet4kgqHvE-MoClrGkR8g2Jm8GeTn5U9JdPwuCwHmv1mHCfPNcHo840CTyrGTsYZNygCKrdE2eke0pD6E8uoXAhOB80YQZXhYSIdHLYfFnulm_MSlE8xWAgRu9MveSrn_9d9iHj_YkC7q_yRl0VKTzkoZ_SGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
قصه سوراخ کفش فوتبالیست‌ها چیه؟ این ویدیو رو ببینید نکات جالبی گفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99365" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgAmyDWJFJ5Lg5TsgP3vXfdrH85Mt0JYfnX1dMqTKwCaQDl3IqKgz4YwxvysOXUNo43KUVs8mKL36os-IsfyVv-mETvWCiXXhTy4xWuD_g6GdYhK6vHJiyk29PoulcOrz2g881HYx3ZM4sOA5lVO-nuG-xl8IXg0panxNa4DdXgm8vfInzc2CXsv18zhyb_ys9bo2CSEn8zIxp0ReBt6Ptg6MY3JqD5ZyDE02FncZfm0rOwWeDH61k7Xdp5u6Hg-Q8VKHeBPcdXVThpSaAy8Xd5GGk4DCyd2b_OkBH6QpxvTBbjX3E2nLtSAH3uOFzTi1TzT7G-tUQg4pXQd7NSWyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیلی میل:
دکلان رایس به ویروس مبتلا شده و برای جلوگیری از سرایت عفونت از بازیکنان تیم ملی انگلیس جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99364" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSxJde8CZsiKE2T6e2sawjC2r5CSrL4vSxW8odCisrgiJkUsxwmRDQ1HvoInzcQZf9xFlApxcxIqMvVtAD1hOKrkPOXDh8DfpjecmAPpl0noF6hhCz5GrgDO6Wdfc6PBvIsXaOiioKmYRFTkjhoxfvgEmM1ebYneV-vyvPuKEKjtTR8hmghXWXqmce9VmxXqpwVfnsLnEbiEGVnbBETfJL_-BMMDsESCRibIKISpojaDi4Jegz-P96kXWsv2D_AIzPLdjTyNBCnbmWP6n_SAKsmlihXFglitJ-6FzPLcUUgD2y656_qUyaCOh7K6wnqk2TqyzaW91zDfbTsk-VR7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین حضور در نیمه‌نهایی جام‌جهانی
🇩🇪
•
آلمان — 12 بار.
👑
🇫🇷
• فرانسه — 8 بار.
🇧🇷
• برزیل — 8 بار.
🇮🇹
• ایتالیا — 7 بار.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99363" target="_blank">📅 12:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGPRzuryja145wv_HoLk88iiKODXTmc0hKNvOTVntN74FJBIAyvwOB00HvFllk4p1DVHcBknHpOc59MV9zgDOAi8aauu4ptMUdp9dw7Ncd6NtiZyXCgIIN422dA5A83HIFx6AI1KHqOPoPCrx269-IZlybYAejlwH25qUSMOfMFiEiTy6MwY7EA5A7-rkW_su7YyNrK-rS3f5g0SlTtNvEQuzO0XQ_J7j3yEXym7wEVGXURvD-BL7RJbXjU3i3kemrdC0ZHyhTJNW_7F0vqKVgX9U2Cpdljw7CI6pJN63f7wP2qlzeWA_YPSHub4ePx5dHwHw23sCnqhwQJXpHGVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیکو ویلیامز:
در 19 جولای قهرمان جام جهانی میشم. دوست دارم در فینال به مصاف آرژانتین بروم و با لیونل مسی پیراهنم را عوض کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99362" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOLxYzdNA6vCiwUpd1ix50Jl7_MnRIoLtX180Sd58ifKLrmPGK6re-UpwMhD9GX08ZXAxsGLccZw0ZntE7E5xLIzN_xyzI5hNw86T9WBgk253ihVT91DTZ3yKeNGip67f9WQjjD1BUzQk7O3cQu0bXNTo5kljT9Yumh5ibJE0Ni7PjL-antMvuFlN0KJMrMAF2O-jHhgGntYyFVoDpVfsy2_Nv43VlE9TEaxrHbrmeQN5ubEmV6Am1aFI_Oh1CSZ_ieGNa6u84naxP9EbffNfxBfMFjCdYnwqp4mR9XroTj0FMrxt9yR4zwCtYRkq_YTOIVR8ksYo41wgHJAZ51xTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، یک سال پیش؛ اسطوره، لوکا مودریچ، آخرین بازی خود را انجام داد و از تیم رئال مادرید جدا شد.
👋
💔
📊
آمار و دستاوردهای اسطوره کروات، لوکا مودریچ، در باشگاه رئال مادرید:
🏟️
**• [597] بازی.
⚽️
**• [43] گل.
🪄
**• [88] پاس گل.
🏆
– **لیگ قهرمانان اروپا [6 بار].
🏆
– **جام باشگاه‌های جهان [5 بار].
🏆
– **لیگ قهرمانان اروپا [5 بار].
🏆
– **لیگ اسپانیا [4 بار].
🏆
– **سوپرجام اسپانیا [5 بار].
🏆
– **جام حذفی اسپانیا [1 بار].
⭐️
– **جام بین قاره‌ای [1 بار].
🏆
– **توپ طلایی [1 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99361" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNw0BrR4ySoNGukBevSA1XXfqQDzybLahWmSDfcn-UIZ12v_C6texJSZcNqry4sQXm0gs0DNIZtAV-40-JgxjLq9KGMAcPs3p2iiZR_Qk7EgVyScDAG5i5d-_PekxeOE8NXDSgEXrZZ_4Ys98Ds6cYGy_T-ynKNNgFvFuQ9YsKCIPRws8ETu8NzMh0s25SA1uBeNMYraams69JMD98lVYxgSRkSEPGFDFkA6vcRT1VX2MTWKJW2yUEde4OddQ2e6ebRB3TEbHSx-GKYUsoUBpabN0PCOnDBwU54Uhgr1fYhcud1Q7gy2x0aakxeC199z32IgBeEMKviqgeosY0bNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
استقبال مردم مصر از تیم ملی کشورشون بعد از حذف تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99360" target="_blank">📅 12:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlXfqiq6YbMxdxgqxYDDV5XGw6SNBdn5wc_JPQmh7q4wLJJB50EGYMVSK3fis3tsjPNImOqOlfIFRYLo_Cotf_iwsJkQLswejpqIWddNyufGoJYMhiOi9dSGPCp1RLa61hieLBAzI1LbjfhzSLylreEi81aaGfxepSjuNRDuXeEC7U_Lfb1HwMh4KZIpIkqrav6HYfS6uI4aCapAdKNhAn_N6NQzqC7p2ax0mpgy9gLr3OJXDyV6PKCI45CD-NYZSCAyCEjyS6J_jCMqNDfyE_dfsVIFWlr0OuwZvRbODJ9j0wRo2g8ww26yFlrvaCo4ZK45C3FtyFxrnPpiV0oAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، ۸ سال پیش؛ اسطوره پرتغالی، کریستیانو رونالدو، باشگاه رئال مادرید را ترک کرد.
👋
🇪🇸
📊
آمار و دستاوردهای اسطوره کریستیانو رونالدو در رئال مادرید:
🏟️
• [438] بازی
⚽️
• [450] گل
🔴
• [131] پاس گل
🔥
• [44] هت‌تریک
🏆
– لیگ قهرمانان اروپا [4 بار].
🏆
– لالیگا اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [2 بار].
🏆
– جام باشگاه‌های جهان [5 بار].
🏆
– سوپرجام اسپانیا [2 بار].
🏆
– سوپرجام اروپا [3 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99359" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYVvdtkAcRibBulf3w_zkF6lUVTRxirkDEDlxjIMSoM-gX1AO9ACesocO6SlzHLogVMxKmyJ5dXRbpd-7CicMuXkrpblyno6cQnQ2KYpBaTbtFGHXvi0f82vAbARhWNrbsiT8oRgzmmgzHVoTpJAs_CN5WFJpW5oMMurZ31rnUj0yw2gpcuF26DHo0GG8iIZAik_19ycHhpTSOpVQJCAHGQRFPm0AjL6G4_dKEZ3uyPrc3tWT-jgkhTbGAVTnfl8-JdRsRzrqH5ZFEBhmus49VNu5VjuqOIFYfY11DQpZoN3-Bws1NS0TyqJ0sAu3vQm2QpOQxOwsAhXl9xMAhhJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
کارنامه کیلیان امباپه در جام‌های جهانی:
🔺
🏆
۲۰۱۸: قهرمان
🔺
🥈
۲۰۲۲: نایب‌قهرمان
🔺
🔥
۲۰۲۶: صعود به نیمه‌نهایی (تا این لحظه)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99358" target="_blank">📅 12:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=fBwTatM1skriFs-kx67Fn0HDfrFTYeYRhwZBN8wcZijxshc7bzSJi1ouotCmlhjyV_tHhcWEcBZ6V5aBxXSaF0zxJWUoYki_v7f2OpfgC4qVCWxAa3y1mevEOJnraoYV1EOtCg98SIKb9Amx_DGFK-HBS1AF_mhSYUUCPX7HVBnmnpjA2o1dkaf6LI3bJDA-b-py9nAykclH7m1n0qFnSes_51yTkKR9TNBWS5s_6cc-iPabQ64L-wjhOGLE6dhmo0aDj_8ReXA8EFZJxKt9BV2UPEnVqSDohr89XnZZ0QhnE4WW_iOOLvdZxTjpgKYs9uU4ljUW0znTftmUb6DtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=fBwTatM1skriFs-kx67Fn0HDfrFTYeYRhwZBN8wcZijxshc7bzSJi1ouotCmlhjyV_tHhcWEcBZ6V5aBxXSaF0zxJWUoYki_v7f2OpfgC4qVCWxAa3y1mevEOJnraoYV1EOtCg98SIKb9Amx_DGFK-HBS1AF_mhSYUUCPX7HVBnmnpjA2o1dkaf6LI3bJDA-b-py9nAykclH7m1n0qFnSes_51yTkKR9TNBWS5s_6cc-iPabQ64L-wjhOGLE6dhmo0aDj_8ReXA8EFZJxKt9BV2UPEnVqSDohr89XnZZ0QhnE4WW_iOOLvdZxTjpgKYs9uU4ljUW0znTftmUb6DtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مهدی‌رحمتی: دروازه‌بانی در تیم‌های بزرگ به مراتب از تیم‌های کوچک سخت‌تر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99357" target="_blank">📅 12:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=vF0dImYyynAyo1CvlXPzgKV6c7RsVtiFqqtrHPB3YqY2Kgyyu58sTOpsGux96IN-8N4CNtId_9SdVOhRUVcgKB_2iLDCbdbXvtBA2pEuYb9SPshCQyQcFoAzvrYfoU80wwVTdTGuRaNtIYJdq_Irl6VqpOwPYua5_nR6fymrbEIT05Y2qyfurwL2FEb_tUpTnHV4bgdnMLQiqf4ZUQOWWuhXocg1qyEQT5nisyK1Unn110g4JlZ7vUdmRLD4engDQ8WWRl9fD43Qb2CA1Rebx0ATVHu-eDcPm3oZ_-rt-zLpWD5BcWl_oqH0TVc4tuLWi99jocsWMVN4IXeEVR2_-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=vF0dImYyynAyo1CvlXPzgKV6c7RsVtiFqqtrHPB3YqY2Kgyyu58sTOpsGux96IN-8N4CNtId_9SdVOhRUVcgKB_2iLDCbdbXvtBA2pEuYb9SPshCQyQcFoAzvrYfoU80wwVTdTGuRaNtIYJdq_Irl6VqpOwPYua5_nR6fymrbEIT05Y2qyfurwL2FEb_tUpTnHV4bgdnMLQiqf4ZUQOWWuhXocg1qyEQT5nisyK1Unn110g4JlZ7vUdmRLD4engDQ8WWRl9fD43Qb2CA1Rebx0ATVHu-eDcPm3oZ_-rt-zLpWD5BcWl_oqH0TVc4tuLWi99jocsWMVN4IXeEVR2_-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایتی از اتفاق عجیب و جالب در جام جهانی ۲۰۱۸ روسیه در بازی ایران و مراکش که برای مجید حسینی رخ داد و زندگی فوتبالیش را تغییر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99356" target="_blank">📅 11:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtX-4lL94GDrkYF-unsKEJ7Bd-f79EOZAOsOVNfdCk0StkZyhUDjUYVQbzDmTxfCsMfm-mJSvVGZum1cvuj0R6M8bJbh3rEAmKxzMJ2NyF-dgT7ZbY4BhARb9RWApimxyQpqjAvCvQJ_uE45t-7jmpapUTtBhyvQVOMzTqDN4fqCs3WvOG5xr79AkwFH_-nP1xZzrIw4_4kgy2pptvcSTqRloLNFa9ASrcMkGkC61PIf53FIaI-ZaK4_LCnnlA_MbcLt4EnwSfoNKEdUUbikGe46s68pRsiv2yQJv2XvjzrB8Imt_NWi0K3nwSaVmlhXQ-S83Ecim_33qnpxrY9hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روی کین درباره جود بلینگهام:
جود بلینگهام یک بازیکن سطح جهانی است. اگر انگلیس قهرمان شود، جود بِلینگهام و کین نقش اصلی را ایفا خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99355" target="_blank">📅 11:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=Q9DLFCZqorNuWa9JtHhdlKLIIijOvp2T2NwA5qMtX9_u4B5EVwCyxewTGjc4RsNSMEkmnatVzCUpjWNBaH7tnTO5LDeMwppHexTKnT3fKIItXsTpNxBIP0ZwTPfTGH87IRWCpLIguupsHorrWAGiLMX6V5vl4g1BSyt0R3nG1QyWZ9KzopDtdK1dyIj6__ASmYoIE8rj69gywl0gDIMT2z9IjQ96sUvjYlzcSl-iHz2Ug__YZGLQqH3wfwIXRBSl01hBT0L3wE1roEfIrLafwGZTVRDx7yvv19_9XPVRmcyt4S1qimeRnoJ1vZn1CRs29TeGlxo21wQTtkK25GHAGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=Q9DLFCZqorNuWa9JtHhdlKLIIijOvp2T2NwA5qMtX9_u4B5EVwCyxewTGjc4RsNSMEkmnatVzCUpjWNBaH7tnTO5LDeMwppHexTKnT3fKIItXsTpNxBIP0ZwTPfTGH87IRWCpLIguupsHorrWAGiLMX6V5vl4g1BSyt0R3nG1QyWZ9KzopDtdK1dyIj6__ASmYoIE8rj69gywl0gDIMT2z9IjQ96sUvjYlzcSl-iHz2Ug__YZGLQqH3wfwIXRBSl01hBT0L3wE1roEfIrLafwGZTVRDx7yvv19_9XPVRmcyt4S1qimeRnoJ1vZn1CRs29TeGlxo21wQTtkK25GHAGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق‌وحال جورجینا در جت‌شخصی CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99354" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da77d29953.mp4?token=iwpDeF-IZavCyji5SunkTJKvupPlzbCpBazaEpKL-NOA_OQUpB8mvdXh4Ndr4rs8vo-5NfLIblyvdXUYfpRlxErkIEJFvuCOePGaDb0gcw3qLUYXqOcN33z8v_LHWmSXVlUfcMs9KtO6nmL9a5NBmzYA1-EMIWkKA8Ufp13l9V_5LaZ2RuLaQsQK3Zt_gB_e_MEYhfy5NBI4P0PjsfzZpnIBjOxQL_tQkhIUU8MJ_FXdEzzkdg5HOl0ObjEWAZtHz14uPD759WgkFnZJjOwGwmk_X_lcImncR8VmVCBvO_mJl-Ln-wjxQzqjpgLCOILahHiHiKTzYzaOq4JrUSoQv2iY4TqTWrmSYoabQAeirTmpW0_losUMuJ3kSYFZBHwCv7k4qm4JFCeKz02yTUl9Y2cLBXcgrKc0q846BA8Pev-5WrfwZKGh1_3xnVclWJzJob5hTpy_Z9vfE3ok-NQgLXYn3QUSLeh_9xXhD_1ciVjfku_wwi1oilI5mYBzTArXZxIYb6XgqsDN-cpU35sHn6TzasKsZSgNNFWIxkvJBCPbIXlD0X2e8ZZZr8Z3jbCVUKBhedUThaZLGiicli0wI8lb58Ra_tCqh1OsypY8GRixIWS1BxAwDN4LKwG9rpX9XvJg__SOryb2TsCZ95SNT_U5lxCQecpbZ_TbcYb28G0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da77d29953.mp4?token=iwpDeF-IZavCyji5SunkTJKvupPlzbCpBazaEpKL-NOA_OQUpB8mvdXh4Ndr4rs8vo-5NfLIblyvdXUYfpRlxErkIEJFvuCOePGaDb0gcw3qLUYXqOcN33z8v_LHWmSXVlUfcMs9KtO6nmL9a5NBmzYA1-EMIWkKA8Ufp13l9V_5LaZ2RuLaQsQK3Zt_gB_e_MEYhfy5NBI4P0PjsfzZpnIBjOxQL_tQkhIUU8MJ_FXdEzzkdg5HOl0ObjEWAZtHz14uPD759WgkFnZJjOwGwmk_X_lcImncR8VmVCBvO_mJl-Ln-wjxQzqjpgLCOILahHiHiKTzYzaOq4JrUSoQv2iY4TqTWrmSYoabQAeirTmpW0_losUMuJ3kSYFZBHwCv7k4qm4JFCeKz02yTUl9Y2cLBXcgrKc0q846BA8Pev-5WrfwZKGh1_3xnVclWJzJob5hTpy_Z9vfE3ok-NQgLXYn3QUSLeh_9xXhD_1ciVjfku_wwi1oilI5mYBzTArXZxIYb6XgqsDN-cpU35sHn6TzasKsZSgNNFWIxkvJBCPbIXlD0X2e8ZZZr8Z3jbCVUKBhedUThaZLGiicli0wI8lb58Ra_tCqh1OsypY8GRixIWS1BxAwDN4LKwG9rpX9XvJg__SOryb2TsCZ95SNT_U5lxCQecpbZ_TbcYb28G0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ایده‌های نویدکیا برای تغییر قوانین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99353" target="_blank">📅 11:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX3UT-bnB92Zn5tBzl7xQC4shXFtqfbyqMuCXozWhKWUbdhJnID5S5b9uwndy0bM_CgreC9J2JigHEcYLzZiODmNbfL7G7jFdX4Z-BBMB9SKg7B9ZvKv7fmWXoTUx8WxUVa73o7X-nMW0Ug1GJlpTpUP0Nt8TrNPVVfvxTYRlglkKCHfHtuNBmqUFj8FXJD6F8YjIWdRE4DbFxJGLZINdmjJUH-tpqSVn8BeA-jKsxHAQBaKQJ_GZPZ9Xyv-z-3tlYVwu9F6ljkLbOjfC2CjYou7tXtscu68Gdsr6Gxf7RFJGNemh7QNHoi59mWn-4Yq-N5ePfeH2Mq6VnVv3tyq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو در مورد چلسی:
این یکی از بهترین باشگاه های جهان است و در دهه های اخیر به موفقیت های بزرگی دست یافته است. این افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99352" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=NqP_mW_S_-wHPZpXqEOX-4-jdbfn1LDMRMdXyiEO_dD98ir6wugJ8pUZcwxlwuWM9VDNJ-InQ7qeYh9IEG4-s-qeZVowd0ESTu7r5NnR_AbOtLNw_T7HVhknt3Ey8sioGxWAJrfDtvJufaoaG9Hvx2IzG7ehUAXCJxn21aTzVukX8W2w2yD8sXe1bKYoCd1MPMJYbBgGc4C5hpoVVVKJin2EZU_KICsKmYI08phYH4iBMVvgP-5z1FbjujPIr_ZRWv_fzujFrBv0lHNsbQ3hjA70fOWIrHA0cjyfnRUw-KQbgLz1JcpE_fdxN0nfMHPA8oeIyeiPuI5sSx2WOG62vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=NqP_mW_S_-wHPZpXqEOX-4-jdbfn1LDMRMdXyiEO_dD98ir6wugJ8pUZcwxlwuWM9VDNJ-InQ7qeYh9IEG4-s-qeZVowd0ESTu7r5NnR_AbOtLNw_T7HVhknt3Ey8sioGxWAJrfDtvJufaoaG9Hvx2IzG7ehUAXCJxn21aTzVukX8W2w2yD8sXe1bKYoCd1MPMJYbBgGc4C5hpoVVVKJin2EZU_KICsKmYI08phYH4iBMVvgP-5z1FbjujPIr_ZRWv_fzujFrBv0lHNsbQ3hjA70fOWIrHA0cjyfnRUw-KQbgLz1JcpE_fdxN0nfMHPA8oeIyeiPuI5sSx2WOG62vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
ناهید کیانی: کیمیا علیزاده بهترین رفیقم بود، هیچ وقت نمیتونستیم با هم مبازره کنیم حتی تو تمرین‌ها چون صمیمیت زیادی داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99351" target="_blank">📅 10:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=DZSJ0koDLcNm7sGT5gWBPXC72V89lsvQsbsSnycMiKRYdAWP5hnrvYG0ZN9opACpBbt1fNz6_nW5QVLqtNT4UfZ-CamhlN6AZKQf_UT37RqOPKUXq-HpZpuVTPg2sMblQ4B90A19o7htiknmQvUv4dzV1D0Qx9EHCdEJHaKDI9ZF-k3dTG20G8G3lDjjkGzoJS2EZqJODILJOWAYyqLKuKNQQ0RgwhO1Ag-K8WMc855YrriReZzmtB9jd7PmA1ZDqsjOQIi4OppXS_rFA69B02dkJvMATrSjWOS5UdAizUXfprQPQFXnSeoSNvXj3kIzUycd9rwWxEu9U4GsAwxhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=DZSJ0koDLcNm7sGT5gWBPXC72V89lsvQsbsSnycMiKRYdAWP5hnrvYG0ZN9opACpBbt1fNz6_nW5QVLqtNT4UfZ-CamhlN6AZKQf_UT37RqOPKUXq-HpZpuVTPg2sMblQ4B90A19o7htiknmQvUv4dzV1D0Qx9EHCdEJHaKDI9ZF-k3dTG20G8G3lDjjkGzoJS2EZqJODILJOWAYyqLKuKNQQ0RgwhO1Ag-K8WMc855YrriReZzmtB9jd7PmA1ZDqsjOQIi4OppXS_rFA69B02dkJvMATrSjWOS5UdAizUXfprQPQFXnSeoSNvXj3kIzUycd9rwWxEu9U4GsAwxhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
احترام ویژه طرفداران مسی به رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99350" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfIRHf-zWlan6dzwzYIUFn6Au44QeLIXU-hRVo-s9XXhRd2ZlUvYRZarx0X75IPDietuzWXKaXccRbzhCb_mzJ8ycVS7SRMyE2I3seZ56BpZ4UaURXyv-YyS3TN449p_0MljPdsnusnYnKfwPqgk5K9WZ1eHY3qVnveu5nc8tvPtIl8UD1cRebO67MxoelZPCmiPqY6-VeTT4a3138Mav3-kt3CniNwgGHKh70Fs0xP5_ofhMwCRBfKUXtg76Etns2IiLPNACQ-OQ0OLVHfAz15mrakIZkDNPMk6429jpuFmUgdtpsXQJfGNBRE_56DSjTVkDiimMOOGgBntXftqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🔥
🇫🇷
آمار تاریخی دشان با تیم ملی فرانسه در جام جهانی:
‏• 25 مسابقه
‏• 20 پیروزی
‏• 3 تساوی
‏• 2 باخت
‏
🏆
قهرمان جام جهانی 2018
‏
🥈
نائب قهرمان جام جهانی 2022
‏
🥇
رکورددار بیشترین تعداد مسابقات انجام شده در تاریخ (به صورت مشترک).
‏
🥇
رکورددار بیشترین تعداد پیروزی در تاریخ.
‏
🥇
رکورددار بیشترین تعداد پیروزی در مرحله حذفی در تاریخ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99349" target="_blank">📅 10:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=GZvdQ0t_q7b0y3Em1YSXeNeBS3VDrhSW_CqLm17t9D7QR8bf6mC_uiHrfPQc5XtuaeF32MnNxIYlhyyfrJ1m95p6BKdDDC59U9hBhDoZtDkaQyAtHON6Hy5S2dKOtb8pIp2kZ-tS-68nCd9IAD_KhZx96ERfDDivKZMJyt16M_nJkQk5nwF26BcWpbtnPZqku7yn3e_mdlqVZ9mUcYlPg31DHrGnVdIEybbZbDmgilxD91NrezErm1B_Wn8vgWRTJdUmJE6M4dwc3RtOR7Yu2P_bg2WFf-LjXqz6TT_S4W8qsfJr5OPkqjnvCeypZ6N00t-JdF63CyPq1y6zA8Nm0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=GZvdQ0t_q7b0y3Em1YSXeNeBS3VDrhSW_CqLm17t9D7QR8bf6mC_uiHrfPQc5XtuaeF32MnNxIYlhyyfrJ1m95p6BKdDDC59U9hBhDoZtDkaQyAtHON6Hy5S2dKOtb8pIp2kZ-tS-68nCd9IAD_KhZx96ERfDDivKZMJyt16M_nJkQk5nwF26BcWpbtnPZqku7yn3e_mdlqVZ9mUcYlPg31DHrGnVdIEybbZbDmgilxD91NrezErm1B_Wn8vgWRTJdUmJE6M4dwc3RtOR7Yu2P_bg2WFf-LjXqz6TT_S4W8qsfJr5OPkqjnvCeypZ6N00t-JdF63CyPq1y6zA8Nm0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی یک قهرمان ورزش کشور بدون تعارف از واقعیتی حرف می‌زند که میلیون‌ها زن هر ماه تجربه‌اش می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99348" target="_blank">📅 09:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2516de958.mp4?token=ZreSgZSInABp6QQCBh5cGHz2ENda2K5Zv3RH1FR7U737GeGrhfaoFswT86cT2QqI7ZbdZci2Kpnxz6SfJBbutclDjRSHA_v6VBYIBHD621pVTFlNmC8hw06YZMpQb_NSnBxRjhKdEjeif9gYc1xgwEpUFYZ2umIvwBWGEC1aA2P7ipqVtv9VeZjW8pr-4nhh3jX3Z8uy77ukkL5IX7wJJknPVyqXZrBWPx-4OI1UDMPwPMGjh7DSXi5RVmAyP3q-AXVS3p7y-9HEzwjmIcESR2KalKG-h4LNfU-qriNLA23bR_Sfyy9SBI2-SPtoJWhZX6nvwNpqWIGFS4ThZ4_Xpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2516de958.mp4?token=ZreSgZSInABp6QQCBh5cGHz2ENda2K5Zv3RH1FR7U737GeGrhfaoFswT86cT2QqI7ZbdZci2Kpnxz6SfJBbutclDjRSHA_v6VBYIBHD621pVTFlNmC8hw06YZMpQb_NSnBxRjhKdEjeif9gYc1xgwEpUFYZ2umIvwBWGEC1aA2P7ipqVtv9VeZjW8pr-4nhh3jX3Z8uy77ukkL5IX7wJJknPVyqXZrBWPx-4OI1UDMPwPMGjh7DSXi5RVmAyP3q-AXVS3p7y-9HEzwjmIcESR2KalKG-h4LNfU-qriNLA23bR_Sfyy9SBI2-SPtoJWhZX6nvwNpqWIGFS4ThZ4_Xpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇦🇷
🇪🇬
مردم غزه درحال تماشای بازی مصر که البته با باخت مقابل آرژانتین همراه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99347" target="_blank">📅 09:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=AalmhCa8H1luD3775h7U0yvdsBYoNNkD4uauAdYWU4R5xzxvz3Hfta3A3Mg_UmPqqsFDT14Yza6D3vhmPMn2aFzSQmCoFqvvsxrsQidKEotX9p88rYDbJDXj_eJG1IImgl0CTIo-F7dea1iAKLy3FucjOvU3Y4YtyyCzofI3M2NWhSJHE2Fjg6EGXPHs2yPcZilBvB0D8-MbFLg9xumJXHp31nOY8gmYIL8y0nr6FR6R4pO_LQ9cPPujB8Qmh4HUekwjWzO_H1hPlJCa29_3Pwc2p5DeQa8B3SaAJQBt76TgWe-VuyHm_7KtluUPeJcXao3PPG04UeGY2FndcPluBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=AalmhCa8H1luD3775h7U0yvdsBYoNNkD4uauAdYWU4R5xzxvz3Hfta3A3Mg_UmPqqsFDT14Yza6D3vhmPMn2aFzSQmCoFqvvsxrsQidKEotX9p88rYDbJDXj_eJG1IImgl0CTIo-F7dea1iAKLy3FucjOvU3Y4YtyyCzofI3M2NWhSJHE2Fjg6EGXPHs2yPcZilBvB0D8-MbFLg9xumJXHp31nOY8gmYIL8y0nr6FR6R4pO_LQ9cPPujB8Qmh4HUekwjWzO_H1hPlJCa29_3Pwc2p5DeQa8B3SaAJQBt76TgWe-VuyHm_7KtluUPeJcXao3PPG04UeGY2FndcPluBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخی از پنالتی‌های از دست رفته جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99346" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBqnVCQ1MT_ps7qQhimUkW7d2QrjcYMOCl235mOFOdVLSufGnCcuv2mbyDYhtaDYtmX__dg028y0sLMS6PzFcC9q8Yc0jMGTTtC-E5dnTnxR_pyNn3eH-R7m9mGatnM3ARWw71lgMP7NSQLQl_hiyUmGOZNQmpFlD_lHQg5mf1RtKtZBsxIf6ivaNJl5HqZC6RgPP0ovU1_eh4YPlXAg4cU_dFzyydh9WyJRo0Bj3qMxDA1Y4sPHt_-PT0jyMGYFnPztDtQ5ywDJt3vlsgbOXDBu_km62EtN6EOvRX_aOd8xS3thSIrZwAWMUF8AuKGSVo6box5qTCPUZDegSW10WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
نیمار قراره هفته آینده به سانتوس برگرده تا در جلسه‌ای سرنوشت‌ساز با هیئت مدیره سانتوس، درباره آینده‌اش تصمیم‌گیری شود.
🟢
نیمار پیشنهاداتی رو از چند تیم لیگ MLS داره و
احتمال بازنشستگیش هم همچنان وجود داره
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99345" target="_blank">📅 07:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=eTn_mz4L1RoM4L2EEWK1x6Us59qaDvnxa_4-o7bOCVCLuN15DTgwXC00QaKHeo4U6xiwfxGrEUh0Fwako_3_YYCL3qi0HHQigH7PkeTNjlwikupE1z0WxpO22lmJTm6Sh89f7I7qZCI4VLjhmpzwFW-gKmy80he8O7wnJCmOqEeIKkUYkrUMDMscFL3rjf0qwtX3BGHy124sX1azb0J4DDBDcLEburMhhGGyC2K_AB7mgNv96J8zvkFxm5Tt0f0g4Dd17jum6i57C-aY7IDF8mEmlUVX-dTG9ORMcmrWT37iZTUgJmUeLzrP0PHrpqAi7XEdDEeYt8LIWADnpvvTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=eTn_mz4L1RoM4L2EEWK1x6Us59qaDvnxa_4-o7bOCVCLuN15DTgwXC00QaKHeo4U6xiwfxGrEUh0Fwako_3_YYCL3qi0HHQigH7PkeTNjlwikupE1z0WxpO22lmJTm6Sh89f7I7qZCI4VLjhmpzwFW-gKmy80he8O7wnJCmOqEeIKkUYkrUMDMscFL3rjf0qwtX3BGHy124sX1azb0J4DDBDcLEburMhhGGyC2K_AB7mgNv96J8zvkFxm5Tt0f0g4Dd17jum6i57C-aY7IDF8mEmlUVX-dTG9ORMcmrWT37iZTUgJmUeLzrP0PHrpqAi7XEdDEeYt8LIWADnpvvTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
📌
افشاگری کلوپ درباره انتقال امباپه به لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99344" target="_blank">📅 07:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq05WxOO9ItWV5V6oljPqp9aDG36-oXSFyY-uWYOu4ld93FvFA6zZJQ7OXeMZRVpceEeaD5QUmbtJweS2Ut9kw0TAQAFTTOtkBIkFkgUU3OaaUltMCmHBDTh_ZIgOihu0lzRGjrJQIXFGbvV7a_v3Sz7N3F_qewDV_RhR4mLVGNXnBwAKyg1knL_YWFcj5fmeG7bPP_tHlud9TSYITZ0AxsIv4tIF5HSqCS7QablWX-pzIOlaDT5EMn-hqHHFqbWUpuI2qBW_u4qENUsUT2yXghZ_mL8hDbAZtLPKpLNsIFzcarmHHLfDM7ZH6IwwL9mSTk4mYUzz_Jj7f7KDDwheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Legend
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99343" target="_blank">📅 05:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5BPyXLcadsKG3y5RhOYNxobwh6ocxqvrfY4HV00hv7jfotkMlxw7LaAgk0ukuwtu6LbDorwgGjnb7qXUBOPC4rjZky0YC-hd8du40wx6s2rq1TOkeJ4UmTxB3GgQQbhtUe1l3t4yls9I5_JU4ilvk0mjhMTR4KviHIg5cH9RStfwgM5J5ZtTR5P86UOtHzO9kqHXourCTv1Ml9OqoqVrYY_sUlComCOLDVPW0uLpD0zlvSdQrsC-YDCF12fy3_5FjBRCwjIoI8ySHOSVJwwIxgg6Cu7odJutfj6OB5lBP6lF6IghXtYq3rQ--PngeWM_WQdhOQs5y861qiCkG5D1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مصریای کصخل بعد بازی با آرژانتین یه کمپین راه انداختن برای آنفالو کردن مسی، بعد از 511 میلیون نفر فالوورای مسی رسیده به 512 میلیون نفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99342" target="_blank">📅 04:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUrl9jkXOxbA2H4POII_vxFPV03D75UMkLtGLUlTq51wqwPmPAX69_HbUdu3QVW2KAUi4Br0dy5g2o9RzLgJIAhbV3eipZQ2ELru_5MMDhC1TkiGIkwknmQXIz7FXbRnoTMmy79__WxY7VhNyeEMDNUkwuFf8JIO7AeET-8oUXT4IGQ5JzOgcwiGSHVjeQVOTvF1WmOm9KJ-8WhzXepuPceLU9oUeL8tf9uf3XbNkzGVC2A1fXdtn9z0Rf5n-vt3M2k5t7kMPYRrwm9GA_LKEeJuOMuyS6OGeon3L--ff6QNxLOAPshXk_UICT7XnnxYteHzammkeUU9rPJKYmTuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irTmDpeBJ_AMui93hOLTSRLDiQ62yFtIluGr3cdZICKJqMWJ3OL3t5i-vd6BBec8lj0yf_2oyVsB8HzILl90GXu_99EStEJUBkoosXvQpPSgzCO2YBD-OemmDCNe1YrOLV6w2WuKbZV2S_6LvFWEpLdNngzUevTPRvAmhFQb6OJ5LxOZoKr9tWXOxpQQ6BuzvGVRg7Rb28zUFW1LFEeUnhPONlZAoZyVvEL0Cfd-vcPm2lkIsXgmLJIbQQ7EzvbIr-Oo-9EBiOWT_z4rdOjLusf6XvoZOjNaeYCN3hm7fLeDIvnhiY3O--aPCaUCtF8AjJf7LleIALqbL-VCfrcKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBrj4NhLmkR9YkEnp5btavPUa90h9ENFhDC_b7Exu9oMznhmErrnjineXHC0qkLzrwdUrilP7O15nVw3kxy_Rwawvkt34-NZePW9W_shKfbQHEyIuJ7J7GU0UYeGyhvqZCTz66fzN3mMw9-5qWzPrKG2JtyvyGrpJFt-knsVjRpbTTzm1vzrfqfcuKeVIFsotwY7oN40zHZiOMUuUR1i0YptnL7EZTD6K3WSUFKKhgV-aARzt0bOrcea5H57cx69NKDGFSjjgYJpGJ86PlNa4BhgDWQS4XAz0k1FIXEA-ZuMsdRnvqJluZhzpEUdGwPyyfMD-LqSqOrFcv7TLx_0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6SdBwGlMSPpoWzE49RAJ32oYx_HdPaLwann-U5JlsbuNuRyznlXnkorwarhFp7voTnNjAXfjC7Tb6c7Gv3Hp4ViMIdg2ad4B9rUDkZjckQAiycE3c3vjBkgpIZyj7MJ-xbSqnD3wufuOMp7o1hNJm5WMnMPKAEQqzgKekybhYfcGxCfzKuE46Z83sOITNBG9WhX3-GJzygpWY3lw-VxurOilK3CIeNlU84IU3NhOktufTDpcRSpUpc0cvPuoQzlo-_6uTTipcYSK5W-tHknazsrSXMLrMvWl-PBb-dk9AH9PpdDcrgHp3RlixuFI5WwVa3uH7QC39oULzl2MIxt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aGGeac5eRfKVlH2bg0ba1k1YTbDHYGqrVvrc3aEifgldsvfa5HibAga6Ws_eBcuKa6y3WPbcma35Azx_njEuBbO3EEl3MObiydycTHAEWSBiEHVeOge0nfNtras6brEwbX3xLiZeMJgL9R7xoTUiMrpKtS-U7SyaOJcarKCXKadDF_ykVwlCYHuI4fnARzoQYzBE1QyU3e4W03DOTqQQMlqoMKcZb7FFQ95c-R8COiwqVpgjflA8X0bO_TAPBbRKOe2s4V7mth5R_J56mv_PM79XyKTpPfji5FXM0y78VC4xrhCQst9ZN5GVCVTR4m9kOlmYQIiPlZctdpk0ljrgzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/99337" target="_blank">📅 03:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=seKGhoZ4j52i986tnlw5LuPMIMdt_gJXT2tJ4i8D6JiNgu15CP2esXxsdDpYovYcw6VsXaPtThV6PL_aRS2h_GaaN8JPQ5Q8eZmNBezeTsW4zWS3ijtIPkSgDCsCRNLmiSzvgyShzs0M6-BB_urq97UM0WHRGFJiMZa8Y7tSY1UWZcdvW7Q2X4qMXnukURfn-7jFGg2P_-o0gbfsyb34GPEcECA-8DkBvP6J2tAazdG70gOh5y0189FP4pIk2AkIrxUIFdIyq1MvyYErHgBROLMhT4DB3GRLS0kMOkebbWMSlP-w3_2-8qCdAb36XE-hqomtC1zypfxRfMF9HWXsWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=seKGhoZ4j52i986tnlw5LuPMIMdt_gJXT2tJ4i8D6JiNgu15CP2esXxsdDpYovYcw6VsXaPtThV6PL_aRS2h_GaaN8JPQ5Q8eZmNBezeTsW4zWS3ijtIPkSgDCsCRNLmiSzvgyShzs0M6-BB_urq97UM0WHRGFJiMZa8Y7tSY1UWZcdvW7Q2X4qMXnukURfn-7jFGg2P_-o0gbfsyb34GPEcECA-8DkBvP6J2tAazdG70gOh5y0189FP4pIk2AkIrxUIFdIyq1MvyYErHgBROLMhT4DB3GRLS0kMOkebbWMSlP-w3_2-8qCdAb36XE-hqomtC1zypfxRfMF9HWXsWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه نداره از دوره بعدی بیای آلمان؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99336" target="_blank">📅 02:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f8503771.mp4?token=bPMbwWT7edl12kEcjME-GUMm3JvbxGHG1X4tnZjfyNAABHLvb5JPSgqRcex3LUHfvAzWiyhVERIGTPG06QOT4gvbiYG94gAZlvULG6VOonUfo1PYRMeiKiR9m7UEX7GQF9kswoGiziUu2-J7VMMyFpTwRWQe1Vzu3D8PKD0Q-ih0hk7pNuayP9b8hA2exnWiFsf0CLLHMir9AX-Fwqdkh4z2QlEZx4iansvhwl2S-B73XO2xMe2Zl0mshrpI1VicQTK6bwFtGIDbG9jUtgwjO05HGXAlo2uwRpvGJN8iK6t166LVticyxwQ0ZBAqpuK9yTmR0FnLPLa9jnX7-i5sPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f8503771.mp4?token=bPMbwWT7edl12kEcjME-GUMm3JvbxGHG1X4tnZjfyNAABHLvb5JPSgqRcex3LUHfvAzWiyhVERIGTPG06QOT4gvbiYG94gAZlvULG6VOonUfo1PYRMeiKiR9m7UEX7GQF9kswoGiziUu2-J7VMMyFpTwRWQe1Vzu3D8PKD0Q-ih0hk7pNuayP9b8hA2exnWiFsf0CLLHMir9AX-Fwqdkh4z2QlEZx4iansvhwl2S-B73XO2xMe2Zl0mshrpI1VicQTK6bwFtGIDbG9jUtgwjO05HGXAlo2uwRpvGJN8iK6t166LVticyxwQ0ZBAqpuK9yTmR0FnLPLa9jnX7-i5sPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
برسونید دست گزارشگر صداوسیما بازی امشب مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/99335" target="_blank">📅 02:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpDx4BfJ36FwcvcX0Wyh1h_wbV1N5O8JvBo5VkHq7Bvabai4IniDoSqCtsB7qOHu2fJIwWPBHSjnjHIxHPkj4oVfR6j6BNRRYSxyaOU4FuITpjeetS8dPWA61EV374HfL-4jHTmTh_pKJIfHmoZ80aTBq6-xFnT-vnBe6jni7pnYCQqZA6ysDKrDVxLdmktSze5LIG4DXkEVCzSVoJ7LPqUD4C0nPnesUZl3jgcSm9YD_WSfKsxujgRelqjMdpaCSJeTOcemW9yVI5nMOiUXLM3j1VNuiDbAl83-OqDDxn_WCQpd7_kycA2Xn8q_umU0hL6Hu6zD83paPHVnRit2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoOXLLX2ZSWLO93ybcuDe49XNzmS-M7xOvyZeDwT8Bcxy_hbXusHHDlOV-PCUc7vLPS-0glU4N8XEjiAnexci-ibPhAfwIoEhlDKGIcqY5PGRKRJJFkO4SCyZI7PrvzXlRKeOToA5P10JiPVmKG4HEcUKXSNrn-DqGFTnWu9kp4vAVUoouReQGEwtEy40LflLpaKja4Bt4lSU4mgPeY00S6l4Y6TxehRxzrm2aem8duqV2OGSlL9zYEqZebe3Fsbp3RtVAOcsBaw2sdiMSxlX4brm8xqBto5hFuaIqYOY36yBfKSSGMv6EEnCoZe44WVbNDtYl35sXVYCJbaaKXc5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
🏆
در طول 60 سال گذشته، تنها 4 بار پیش آمده است که یک بازیکن در یک بازی از جام جهانی، هم گل زده باشد، هم پاس گل داده باشد و هم یک پنالتی را از دست بدهد.
جالب اینجاست که 2 مورد از این 4 مورد در 3 روز گذشته رخ داده است:
🇦🇷
لیونل مسی در مقابل مصر
🇫🇷
کیلیان امباپه در مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99333" target="_blank">📅 02:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
🇪🇸
#فوری
؛ بر اساس قوانین لالیگا، بازی هفته اول بارسا و رئال در لالیگا بدلیل داشتن حداقل یک بازیکن در مرحله نیمه‌نهایی جام‌جهانی به تعویق خواهد افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99332" target="_blank">📅 01:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeCZsO3NYfs4eH4akYhJ-ljV0y1sWQnBRupfJ0WOHrsGkUFSF1tu_b3Ac9mCo38SV7TRxNx3ENDKAiKjf2fYVuG1ffE7yc0Jp2ixZDWtmwLOc4RfXw2OUGmBXlngE8tnx-PDfGMFmWzbVOalpKEbcMEF7ZpUGY78wO82MQuKzxXx1-rk_R8cpy1cIu7BG0tX_mG4h2v5GJc949I0DgHY4zwBOsCVKetgWfDgxGM7hFVacCRhzTj0XjyrrMzXOrnJPRGUKq450BXldfskkzUsloy0mKzaM12YycM0iWhmEn4DsyFtTZpyJ35P9_mMVx-zbQDm_n8hDcZPb3G3qZeFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🏆
| تیم‌ملی فرانسه با قضاوت داوران از آرژانتین تاکنون 6 پیروزی در جام جهانی کسب کرده است، که بالاترین تعداد پیروزی برای هر تیمی در تاریخ این مسابقات است.
🇫🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99331" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9ICLoVxWFKOsqswU5nOu9He2bV4gdA0Pz1a19q9h_vOU-tSfqAoDvJqPj5YOqp5cZTHL9D2qkE9nqwLn9CHbQOOTrpD_1lgmlk4JDcv9PlDxwVfDglQEIcM2u90TKY_8nDoq5FsOyX1nmzK6BH-opQ3T3qqt5JiSHcK4__e7GIBKRu9bInka_1aUxRkLlhRK6IOfsOeTUFKtYQxE_k1mrhLPYXLLs3GXNpwKuR45C9aMDmBoZ-0WswJJrM4AAxfupswqTO88_9wKCVXcOS7rAI4EZCS6VNAMJld-CqogZNCFjVj_9ZEiDMtSTMtCx9yLFhSv4yaQ2f9pnhby76uoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
کیلیان امباپه: از ناراحتی اشرف حکیمی اصلا ناراحت نشدم زیرا در زمین مسابقه چیزی به نام احساسات وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99330" target="_blank">📅 01:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
Man Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99329" target="_blank">📅 01:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIP-TO39MbVhO4fWeXPWtEDRjAPCDg83MnnkxvONJGTWS2k6nS8kdGuAnkTc5VUQf71oH6O0Ju2vNIa_lbJITbpZCsNxMptsl2v1k8CJuJS60aZLCIUhkXA-7tOYGPTChpmjXmZysMSJPNT_lyPoARegePdJ_qi-505nu6E29-lr3J_8gxFFROYVg5gHfqmh-e875YzuYN-jJcyVBeEIOYLqV1VysqUfbDR2clSbyC1McZdtJdGYpy8rr0lXdHQymqX1u2Nlf3898NW-fbb6hM9yhPSzlvT6HgWs4cXNXLPk0imdlYRDWEmhDgCsu9KebQyPBL1odXJQr33ftW_3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
M
an Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99328" target="_blank">📅 01:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCLjc5N9Pw8OgEQQo4lfU2WasqpVildVm7MoUF2LMIaHF9piHpBWHizEZ7XMu9pgtbaTv8lKyB2_qnl0xu-6jb1Ft4eFTizNaSjgoSRxck9Kp5vpxHfCtLZuYaGC9F0xC4PPLb-xz0_lx4q5HXq-f77CCRppJD0TjZHAEUwufG067KDPfqpOGsQ6qwuRik5ia3h4oW2Jbb-FGabqvbWi1aDR49D89cLdUCKykWGL9g8b2CDYm5SSscqHFFdVyfHV1ILbwrhIJ9qcvLZE2uraH-vpiRatP1izxO1vH69fxD6qVeoSn2_fAuIZzxFexr_uVxS_nDu-_vfoRaDrBUyhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99327" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3H-gUZJHXkFDSH07Rsf-e3uTekM-dLtmIJCLe7OzU4akQ15UxJClRBlcCADgrVyMJjlUg5gm_uM7vqJYp-lox5-A1qk6O096zNt5JReN9DaVKf7JyUaj19GQolYbQriCdEMWHmfT-pjQi8Q8FwFY4gBQLc1_-s-FmuF_1vmZ8v2aLD4i2ssLkshaihlrlGNVNTwnwJ_PTyi_e6ivKA08SuSPykHgEThaWd61ketv_irq3ivcnt0kLJPR2-hO_bZedWX491Z8EeAkqWVHUO7AThq4-bEIPj9UwfE7I-AUNFFy2ystyvxgploO6nhFe0bvwlsqCwf9yCzZnH4EBcGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمامی تیم های آفریقایی از جام جهانی 2026 حذف شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99326" target="_blank">📅 01:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99325">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP5GBWHF0S5itPzrX3ppKb8s9bJM8I5Asa1qMi-x95VexeyUhsIXlvflc8ALT24dB-S_rtA5dV4wz5NIuEf11v3Rs0ut-9NRLufZbJSUi75KinUPY8bnDULdWE416RoW7kCdubg_hb4-g1eL49hLoh8tZ8-h5_eWf6i4v0j7C-Lhqq9SHhxd54Xtie1dcZXfFcYizuak1FeHfjY2GPKvRSClmvWoihVrb0IEgPlAEL1MB3X3PlDAV7AoD57UftQQt9aAzi_ExqEGCKfxMrRuln4LlMmIW2yKFmdeus2kcCCYsNegsS630jvYI5OBy8tc9krUJhst4EnRAfN8g4cZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان با یورگن کلوپ بعد از پایان مسابقه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99325" target="_blank">📅 01:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99324">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlbWktLOdfyclrcry2z4SC9EBd5EwRtJ5ewPFvM6RTPQOuTN2oji_Gatj1TaeeqSaPma3jfQLhYQL1PAhyMCiXSvMYJdXKdpPxc-iAM_Zv7LtJS_rPs3z37mKCZKlvfMVJn0rixRjugzY6fRe7ZkYVx0jjEwX2SyFCiJWYH3v3jYUDgS5PvGqxk_xpqs36_GGueeNO8itsTUWypisnb1R9b-rLYdFDXmkUlHq0AlNInC9VAGp8Pf-R8Oflo9KQIIG3rQeMmdjUfN1JALkylLua3Kh0nKWxMS2Bz6fLmBcKAdL8oMYaBmJdJlz0Sf1UF3l0mKa1MWq5wBIsA0XV_nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• کیلیان امباپه در رقابت‌های سال 2022:
🏟️
— 7 مسابقه
⚽️
— 8 گل
🅰️
— 2 پاس گل
🚨
📊
• کیلیان امباپه در رقابت‌های سال 2026:
🏟️
— 6 مسابقه
⚽️
— 8 گل
🅰️
— 3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99324" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99323">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV361NgXPjyIqitGcmvkD2gd__6BjE7MKNV5wkErBP7qjAyhI1-PqVGvp9xaSR6q6AGHkysC1FlQOUeZhGtDoqf76GUBjW1X9YyLRZ7qA9EFzPjGV7fb91a0lFGCVEY_tCldTM2tj16aOu6hzYeA9w9oeyAqaXp8Wi7nGvVlLAupk7P1ggak5FBRKqrKzLKA61v-QDRXCXpk4V8QyySA3OTZp5vw3zizWWVFMer2WGxpNaqWEEWalvH6gxpknaUh5VLZP0NkBgJYSQwvlAJQ8bfUmr-ppVC5zRIFdQGY02uRbAaaXgUOQTq6AWVvFzAFiwUIalDJMktmSp7-iIT1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آخرین آپدیت مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99323" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeNTYIdkb1rF-c1gv5TibLPWsk_B_sLXtPOZ2IApzpKBVR7dqAkF_2U9Akxpeso7R44Qo92lvduc-RmxKbdWilcygVlJxJSuh1fcEcRdXMHfUB25TQ1wXhPYj9wIHEc6EBvPIX1EK5DUt4Dkqh4MDCWAjpwHg5iveux4KO8eUp2uAn-JIs155utBj9raozI26qcMY8bhPyyublYbtMQWSBbqBBbR1bDEdb4ckfSYV8Ka-YzJ60-ZzoWAconvGIvYfYZVS0uRayVHnkcb-1uNNotDbUYdOdOZ2S6Q0JPU6MrxwS857d6gr45AWp33FHnXUKKaj4u5ryxbzk9bBpUyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 بازی در جام جهانی؛ 20 گل، کیلیان فاکینگ امباپه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99322" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPLW6lGy5_3m5Fm6OGv_wOZE1rnDoKHWWepe4fdsee0v2CG2Z2Q1F9hZ6pPolKZu_s59aI5WoMcnRGPlyftk4X9o6W2066TR8SCWITKkfzEPfeTuTgtedZctzhIVJNccKPk2fq880qClj7tccCrdGZf4EPhPzKc4ns-teHCat9Xsp30Q3qL7pk5AEunESK46dQdKqw9KuuI_BQ53ztaw8w1HVlvGZ8qo_qua-BGSil4f2wpVjw0WthQwuMJVissBlNpesrETTQZo06gGiUf4wqT4qjvlDARG0guRPXjyVMsY73d-tEIcdQDkuMEzvFLv6zheqJHWpT7RZMSgYfZL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBSE0rolBMycwjx2ZpxlhdOYwWw0o6xKf-XhK6ORF136zxXCWNILq58hyczmYd90zbj043j1WB4ih6Dvy2QWJ1mxEkWGHgxudbwqiDIAq-jB2nCnepqJNuvVS7ioL4tozGaLTx_t9Emqqvy64YhxofYNJxu4_ft0llPi2Wb8S06CfK6hfnC4abkWTlL1I-W3VQI4qasMSfcvcljmYHx3P0AJg7KNuNbhHWMTbQYr5Caz9IBPmufc3ti8eYuAS_fAoZZB9HY8qHOrJWJrnjCKzQ3_1wavuOrznoOhFmh55umcwhSJHQQFnbAmBs4p-tT44rH77J_irGPuOgax1XbxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTbahQcy49ER9tb722r1Zmx0Jan0b3dTEbSqwEP7Lmud7eNK3M4JplTMrOKMWlup5l_UtkdVa4aTWL468I-uhDqSQSrWr6xlQkv9xCp1qhGADZEmU7BS1l_W7rVBRXBaF3mdr_eBCuqVdxesxkLOjYcgjtekyVivosYG32q_A4pkaBEZvq-Me3ZQ-QYBHNvdTlNjMEqqzbb5KHZ_FTPIvJ8Luzv04j7w6jAaR4nNq5fLfS9ZrAkVgcx8p40AuxHlQh2ALBsgNLbUa2E7-37sv_K-1GTVK9tsYZXdekSSa7T-mzo1Uh0prwCXbVuRYbBHna27925RpAebvCuWcDUK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JosIq5qXV9JGmnRK6dKni-kspT-Y-j0kYOlQon-Gp6wu4McJ_3c-esS7enD8c1Ti-vp-n9d09goDYW4-vFDyCwWTm2BxOEYadhCtB71A5qx6PW-rrrdGO5YlCZIs14TFFcm1OO-HFH1tAPQYEfEU2txVYW1CPLHx45kYZIb7XQtjQ-34DNP9py_71f6ZQPM0dAlMG-Ggi3MGUO4tUaSiNf7mqvJ81E-jPJp7XjlIDftPTUCZU7tbNTq5-Qd0iSB-amD_e0F_bgbT2YCXejgmIPOc8-7SDDFKZPXL5SeMUczAQDrGDu4ieCvqYxR4SAyURpXFb5BHo8rgET0_2ahA7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🤯
📊
🏆
آمار گلزنی مهاجمان فرانسوی در ۶ بازی اول جام جهانی:
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
کیلیان امباپه
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
عثمان دمبله
🎯
🎯
🎯
🎯
🎯
اولیسه
⚽️
⚽️
🎯
بارکولا
⚽️
🎯
دوئه
آمار فوق‌العاده‌ای از خط حمله وحشی و عجیب و غریب تیم‌ملی فرانسه.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99318" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmghIZg3XfSFVu0_4HctfkSNzzX31yv1ZbhL4z-9qc1Jcwd4tQF8bPDsVSwVowN5da-2_GxFn8tNvgHZzjpK6n2olIUhRPb_eYkkvVTfL3dWEZ5fyo1rBCTMHt4ZdxCawN5OE9csXKxAb6NqyrqKz-FUtadtSGWE2RwKYf4Rigpkz-JQ435SVFz3bJUIdSU5yV5r6xxehc47UomSgQV179v24h9iZCLRbURFmonlmGP_E2nNQPmh6NT8goeh8H0xfrATZ4IpPU2QTSMQv2QXTl8XfxVpyRMcOuEaZqM2BhSYxW0L5RFtZ4dZlKwye2eCfdqbvgypQQPKPj_0_Yy1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه در 11 گل از 16 گل فرانسه در جام جهانی 2026 نقش داشته است.
8 گل
3 پاس گل‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99317" target="_blank">📅 01:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYCJjRs5PEeptEd5WuFqtcYPvsbbtEhXb7ajpk_K1dgsAkERfWgLTGw8wxSttvUZbJV4DbA-4036-rOK3ipPyS9KkcJIJhuiLh_v9hcdsaU_5tcrcJKzWYDmJ4kUyWpcoe5Tc_ImuugY3FrINp8MYLOC185VskSkQna3IHRWzCOQWdAbNt132Dzq33s3zsnGB2jzeQBCpmpCBARVX2A84JMjTzJRQj_Gl9sCyLzV7MsyXRiC2Iy50FbepCdFoVdCvL7ITbVx68H2zHIFz8VKuuW3K3-rEu0JScjiBgyTRBXGgDAnHf_Q6rghfXei4uozPzDPDHzKnpbO3kU2nvZLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
کیلیان امباپه همچنان در حال تاریخ
‌سازی است
✅
اولین بازیکنی از سال 1970 که در یک دوره از جام جهانی به 11 گل یا پاس گل رسیده است.
✅
اولین بازیکنی از سال 1966 که در دو دوره متوالی از جام جهانی، بیش از 10 گل یا پاس گل داشته است.
آقای دیکتاتور کیلیان امباپه.
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99316" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99315" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PqfvE0ESLu7-i-Nj4excOylKf80QksryRv-eqNWFOVPPIKXD420wZG2Ec_s8eGiseUxLRIqlP2p3toc6Tw46cLR_qJoVsoBhCsObyAU9w8RCFkdsP4EOrQaM_oFErAedy6BwwMQa0Gz2cCx-u_TVG849f54be1W6ygIQ6V9KVS8-p3jl6uXbF56p4CLcgnmPYz8g49cLJoUbpRaEM7P-2V9l5bvYn3bDQgYMPG1gvjwCDB18_B6lI1duREeHrNnFGO1kS7lQww7ox4LWsCum8nSnAc4Jj8CMIMtyFdMHrQ5GUHKm8Iya4MpqySTXlhjV0uw2BfPYzwEac-ZX5V8lyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99314" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

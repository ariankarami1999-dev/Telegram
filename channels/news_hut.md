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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 22:35:21</div>
<hr>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTohZW8wjm2EtGsK0flKrBe-WwZgSuqttwSNHzjK8iFqTcxtnOYJYct-Z7ZmaSCI11Q7JcQXIE8b1Q6EBJyRknqDAvfAPIOgh9EBfTZ5F83FkDitKDVPCk7wO7qblziZT4i51j9oyfT30BCMOUvb83ogob9D4RvAiRpfFJ2CVE-1zY1uniuNJW9UuWiC-tKJbosNwkXCH9B2MEaHc5MlGxHqu8AcXNdFpcF4EPnBDm6oKqI-kVq-CoemDrRSRqbnAwyU98mkj7rruhjeCYuji-XKi8FTYgvCLrJNePnJI4-BWEeUxyV4mQVSAeBT-HI-KftOirAUUHcLdfY-p-8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_OqoopYPj8H8xYW6nqRttfG73Wr2W7oM758EkYYu_fFDhSdg3WoVtbX3JZdeyZMZZJY2jpojCroNY_QJzGiX7aFIoPhWEBEIAWvr0GAAja_sxIwIaHnNC75W30nDZY2M8_mWLrXXU5-x34XaD_mlnp9-Im8iOCrAJKotgyGrihgLkmnUTFeO_AUo0_L08Vq2vQXOJKlLD0bKdIj7Ii7-oNu2qXBMQBTOPeiDZfAsiPO-5jZbLMXxi8dt7MLNGZnoTxlHwgc2u1v7OPcqe2UGB6-DPLEdDskWJjZnegB2NytdVYxGvCKScRiK6KHAEzK6mEYCVr2hSmsMa3qfLaoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AD9yVaPI6UnIBgEgc1CH4WTut6R9vJdMCs-HCFhlr26b9oNATC4acEdLsNKNbfd4tiyjLOAOOy1s6XGQa0cv5Pl_BSvDuCYGflZm2vu8PNMTMoxOZMAOPL9U1kFnXKnposf3dh_hGtNYX-Tr3xw02ENjzgqyM5jLxypPwaKzjoZOKe-cCFv1DD9TljWemOlQUfyLYz4v6XtN2nW8kIQ8gDO9ey69I0OZ4QocMIqua6-P-ehLvNa2OZkDLdBEcaV2wOYlq8T1t8DnjIQUDk3Ae-LmPSDUGMMKfoqMI_JKN2nS1698Da4UhC1L4ZMw56zaaJqVFPjSZoTLzy6Cr9-dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-1Yp4S9Ue66-D7Ym2yCu2WPztDJS2Ixh2o0yNABCJCMuilRg7rVER7U9iD0EmVNL6y04Aw3_6NVpWDRFkru83L_xcx8PRf7P-AjUtGIV3ba8-sSCYFFdjDjpELSe5DsR7XCHdYTYUDtpwBAKhic0PD__n9nacdQEKWEOkarlE8im7jZpVfjtU7CJikj238E0Fb596MXQ54PvCE6mFXkiREpY12Pt0d3DEsoyd2SoTsW68U4kaebbul7VJ2Fx8D052prYSdSLGzaVoKHYQ3_hw8NJpwPNoMmgee59I5tuas3WUihUhP-ghh0vWEStBsnIrf6hYMyL08TmCEI_kERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l43FwaK9il68Ce9HkJAbVy8vE_x-Iw917uamSbHRjXz89GyLoFTJrwn8-QXBaskw9M8aYzc9Ydo6JKVrTVAWH9jywvsc1Kljb1CwMF5hdCw1h4pSPICo8cI8HvuaOeOHlf1eaqIz6hzLtMoW8w4d6JDPO1wSOB21DB99hwEflZweoveDDoMqwXAPjPx0tyxZ-jC-CI3uTYsJGV0V3VKzbPZ-483RU4MfeFB4_00qFsZofFrf_r9cM_qW2v0luzm4u1lHATpYQc7asIui4tk5_RhlDijWqZwtWjKqMzc3lLCH30KcL5jR5MpKcBV3fu-2x_YpbnzSmLI-BREj7IfY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHL300cIlVUaYCdNQVCb9e9LYYEABLRiXnnNjMqPfb6E6PTxZQnv3nIce7xKuRZJbKWXOAsMxkJk5OLEBD4btDsSRDBQMnJa_GmlGoy_Y6OFgMD7C89YwM_SAl5NYlAAfbAqfgBvOA5jzZvqPnX8lw1WbdLcNSIH2B8bLRrQpB1ir8oktP38Fghsjlpciga9-LN6NvaN4w0RQcbTGcnfj3N6weUbwq03Wv9ZL0LIZoweJiP2Kie9EJlaiE8vG2qfsnyxYw9Q1C8eg1JGNphDxSs8spqj9kO0dq9mztLdqCpEeWDvKL5oa8TS8yMgSTML7ETjAJ3fPe768K2sBbHHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMiydK4ANPGpw0Kf6FGyrtF0UYIqqknDFJkqlFPQJrERMkk-leuez9PxYBW4vAxVb8Nqxno4-jSoN917RvbReiHynIKvDuMSN7taulFpFlRb15K_jw0-qhshB1Tcbw3Uv0zfBcAIPE4EkX4R8xQcYIPJgfGo39I1P6WyVLvcHRU13olUiq_gHfwVw-TrROTPUrmesjRA4hKfsxhawmQqzgZZLttDohNyCI5trYU0H7cERebxebSpyyFZj81bQJYTMmviHoikTs1shHDe2ipl4OKk7nskv2djmBpZ3D42TZ6WBAeKTg2sqXS36Ki29agDS-w05RoH5to44D8rzExvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI4THY7zX1FQ2hC8X2wtA6a5KMda-Y4SjSne-U4moNSOC0D0TnCKvncIaEli5VMt7Wz0NCg34dacHP3ldZaDqI191CIoCj-q9D7UVAhyW2hjv1I2Ux2b1uwiAyW79FsexrEbr9k9A9HKMA7lyAcA8lc40fblWC0Ez3QiMubthTG_bHMA8muSg1CAaEMjdnbDfreEYToOfw5YpR9tzHskIPuSYCJ2Cm1eCiojg0-4lb3eRC7tsNty3VQcwuFloBi6ZcNjaw7Io3zR9WA03AXC24eSoGTktzUuTbWOYEB5T8NUlUzKDoUpHk-2-7ZJsreLAxPj6cFCD0vP0Kh63AmLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_Sru8OnES2mmXYYRR8t4Q1nsJAqRExvLM6JWhAo5BgSLgt6K4Pt0FjEU3S0MizCYUSU8o4qebsAwhD6WJNxJluZrysi4-6PPQFUNnwjYYxqHg-A_cO56kEcAdzJXGAHTGRsmSx4IdtaMm7cA4awvXrInQEsJi5qfDC_F5K_ktRjta_l1jjG9FEw0kfFOP9QRTGyiX87Zyb7se7S3TLMPWq-qsak1Xn81xvNhQN0UH0TUjZiEPlhFQxllEvIYnU9J3V70jZ7OKjbhYNjHL-Lb5deUajG1fmgbxcXw2CFSzpszres7n-PyPioNUv1bYE4zoL8PZhu5nGOxgM0SQj2fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvIcKFXRFfU7HsjkyK03zA8DJaIaYe-o_Ay-WoRrvswV1hhTvpu9yYpExz6oVHeIiyHYlWliC17OC2QIAOYkHfrrDUSweG8XLXt4rMiADkyfC5NqDj6_Rds41khXimqzFuwxB_vhcjB6_G6Ppq9Gl-G5xt_JyzGbqCGStlPBKpLa3pX8dZoN1vscGYK2mMFJRk8YpU7J8cC8lTtGskhkuWfzbva5GFOGNvGoZvUzogWPKhoqRvMGWsQ4nyoAJd62JtgjUcoDS-DCtd_F_CLvbe1U-1Gno5TizByn_9AHasVR2_keQzW1CAbbuFe3bkbHgqZe48ks0juqnSGCvzNtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYSr9IL_wR7WVqQsRiJqnBvWpZM0d8-n7Oz6HSur1iyrfzwdqYXehNJ_IO9Qzlmzl-FySsBPABOwp0eiQ2qCh7WAA60HU47zqKbfBTtHHS9gvkwF70CV9lyiq9Z8QrDu64lKpEgq_2C5gGidkm9qcYCiJVDhKWC8RQvEHszE_YJYRlxhOhhen0GHw5jiMz3Fv_S5BZAp6Tc9MfN6loWnZEDCwJmqnOIT8NguJ2fYa9JLeCx_-dofIXztB2ixbz16675WDxr8t09eaEzqF28P-gKCrM17wYdG4CCFEv_FF-3CMAAW8ges2Na6W9vVoIKYxjyFUzv_LmWtWex8UT5QkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8i9oIunnSbap7rsNYW-bs9XOGHcZww1u7TjF0yNP--j_TIz5TEJlOmyalR9KO3DJKBfsp4NO-ES36cYdhrvd1y2qMe9BzfX0ZR9UQmQOHL2SjA9BEV8_09GgCtqdO-DChIJY3s7oC82Owl2Zbyq0yDPfm4j7VqFw7lWG9tpfT0-jRx4xRO5Rd70UHcMA4Vsh5cyzSyLGwIGZGLn_Fg3ewKVxzIEividnttit-cDxBFOuSOnxJrCaiJunsxIb2q2YuZSMoAQAVSIMvu5TGV5X5ksmDWMQ2ZZNZR9jbU43L-V-UpGjGN80QSRWxApgKK-zwjs_sSPaR9ULOuzkv9_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S1e0-5MWZItydZrcpSjhm3E7HiZ8vy0ewUDS1Z272tkGwTlr7tUuDXKqvEcwbeyF8JhmOPWibOmzZU8o01y4znNPIRulhcVWRPVlR3mTJ78gW5LvfjRgVxxzzEu5PWcVvtVonTc54MiqXeARcG2ElB-th-BeFrdyd7to9X_YuYnsvIjy3chliI_zl01CitIJlVY42nXm0dIE4IsMD9RZL6w1Dkm3Tp5SRIOn2GnnFkbSAxXQYqB2GKkZpfg1SpAOa5l_rchpHKOlOPhzd5psjTAkjqCLaH7Z5WCAXHLWl7f7y00RYqgnQ_c0QHRQ-DEAf-EE62x_qr_M3hVQeRjN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aZBwuN8zH59H7csDNBde709-jrlbVfT-lu7j0-xHxRv3_0bV2NImQc8aveoV4xEgZEBObjuqF5WArHkpPozvyfWFJ99biOIyxum1Qe1VnfaRJY3E2EON1sXSokemoHEBuLNelvMfN1nqCnqR3-ki1ujKvYXRCkBJ_FTMOn9FbAHJ5FDu_vmFaof2rEi3POT-Jw9-8URXPpPm5FG72lBgDBadGpFPcFCZhUlTuY5Tj6mIqA5raUW4JSzznBQGH9ieNYUxa9WvGctvUZBf4NOGKEzbrgYXJZcCLmyeYxnKeTHl7ucM8q932cnJoOelDSsYGr6d3diJPJz-EgtTrsjuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aIiav_cUkmsS3AMc1weJg_yBPE62fkOLcBQuKldjMQ8c7f2Qw7JjAeZDlUtdVWdWo_NukiESc3xSx7QpgwRRktcljbZ7KT5Y_rYDCof45Ul-BeQ-QBS0_etHIhTAYZaauGraIsHwU_lVipUJkG4fOSC38Q9jQfkvZQjruHNAPIpQ_igQSrWxJOIXrPqE1BIzNSWWyckNNuLhMaoETRPreZc3OG2E-QzHEGzQcqFR3svgVEfSVCHRixf2fA6Pi_sqHpTQWA6Xv6E4Ag6AZqJFAAdub7z5kpHUceEDKDVxBy3MMMb2-ArEBXwUXLP4DgtCM8pe8YZvCXFiN69kROlrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juNDBaxb5jFu3c3bdmSM3QkKjSab1FBqVz3HL4feKGtCWfJq0jLbVN3ceiFZB4SLo4OieZ2eHtwctwPBCA51Ali4z7IK6mw_hHHAsh-EnBpnAZEowmmutrxL_NxzborDhOY0qtAILBdafOc6IUmAtIBIXwijN2npHet_Por1QCYGPcIw9Z7mK5I-4WVpRqWyaEs403wS2dTnyA-cEhfcVQNBJKotALY1BiHOLUqK-AQl55bI1CmLyMchfpmsbpyYBfUO-uHXiPPlA-IlcxzBz4BTbnfzAT-PDX1rOWAwOD-R1oU-xWeegXTsSjxvK_1MgP3XhFo3JHUr_FGGqBhgBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9qPeVYJ24GLS7hUZ3OaZzQdVD1oL68ME0IKOFimgCfkxsZZhFitJpYxWg0d4naLc4bm9Bq_w9xAF6uEU-rkHXpn-DEeETILuWJo2e1qoco0R78L389i5mzyOCDfssYY0fych6uusXuSxLBVJjlFvlJYzkhrR6GcHw7T0grfWhCl7-75RfXrJxmz2bk69YaOXn-SQEgZTzeJLX6AHy77Xn_KKmDdcbCS_yIwRdgc-S0mpZQW76zni9Jd8G0osgZXQSV57BolUtj6B3i-GUX9k32eZIwMlQIVP42g6UGveLo7JN_ECzaWoY9iUOvWJ18YOkL4eCOL7H55PIngFDtaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNwEQN8AoLtGpcqnn0NVl0RVi8jKvcIhdTm0tz--DnM2e9GHUoK8NE_dVzM2HH70XcB_6X1YAOpCvevcHOqnE01YeNmTb8NdNVufQUIB3QckVvnyKaokciNI98Tqq7ZjyNODUjP4Ip5iCZn-rqFJubEm2_jHdz7zEV7T1oBE0YkdvjWQ_pf6cO9fJi7naTian7NFnnYR6zfkYgSCOiQkGwo0MuG5cUEsZE9S66pnSji9jWcbgd-F_b9ffW2RLCdkVxk8dpkBqB6z_DWOF81G4GRPPBrf4lSw56a0MTjtjiARLw113L3rCHetRj3Z2UVR4KQGkNR_2rQEo_VwvRRtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPr0g8sEQZ-Hz5Wi7QMeuyOD64ZGlJfgNTYUtit2tM9B7G_2YKJGwiogPWz-Ro7TKZWMG6DjW4RWDWFb9HYDTKa8colkt7Voui51l19CSAJsK4WQ8suoY2UvLpk0503RaVi9LqtxyMD4owL8nLyYyE8jkTNmb9ItkUDUhxsPfFKEghjStoH0BGWVM0dXTpLmOZmbmR_yPd18CjKnF55lWJu9jeONSuCP9H7qE7wGj7quXUMFhZclS5p0tUP0kfqvRLbRnA0DuDvs8rLn9ZIKyaFrKVnkq3kL9qUyVGRNAEN9-OTCE7pV6tWfJ_P_dIyrHT7h2ZHQEOO-1mYQDTbhxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFyuyERvfouZAViN6X40RqtwPZNuLvsSm8FOT3xA3KXrYGiajaRCqaeQJdmaULF814jAeqKMda-RFLAUFSnsL2Y3sNLrMMHjXQMG3qpi-wp0mN1Up_ywnmlw7kggr_mMTkEqMfYvfx61F_ILbrd0GJ5-lnwI597Gi5q8i0LBHFy3S0H26D-BM9_VnS1LBumwOGx_aqxkWkyu_2p-q3eAGwSW-YI0ydgf5Lth5RFiPvqlq_3KYAhsWFxu7u8s35ziGPym0TQI9KGXA44Lv1zix0wQNm2oVD5UiI66MQyaMdiSibnkxorRMpFDBPKywgFUxkyp06DCbl9HBFfLDbl2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=jZ_CDZHDVlIV-86tmXXg1XQhn9_qy74yqoVUMt-rTX7KRjdj3kd-j_XgSHvw_M0HlpFcwuQaRItmZxJUD3RSAgdBpGnJeF1tk-wLX_lIs7lXPDlpJQkHVJrABKlin1tRg2jmsyQ_LwYIsrJIr6Tp_y_4oWlNnvyK_oTRY6QJ8FmongfXUOL5ZKaHpd8cyKV0q8dE6v4fQfJj6OkYZAXWTlHV4SADTsnka4HNCQjssoqJja_wRpFqqjm3zXjrVg2zNdezXKIxq0eSboXnyTiEKKzFWzpkCBg5NzlyAc2DAAcSV9v75BbGIJacHdxIgsJP98LS7qxD-JhLf2jQkwBHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=jZ_CDZHDVlIV-86tmXXg1XQhn9_qy74yqoVUMt-rTX7KRjdj3kd-j_XgSHvw_M0HlpFcwuQaRItmZxJUD3RSAgdBpGnJeF1tk-wLX_lIs7lXPDlpJQkHVJrABKlin1tRg2jmsyQ_LwYIsrJIr6Tp_y_4oWlNnvyK_oTRY6QJ8FmongfXUOL5ZKaHpd8cyKV0q8dE6v4fQfJj6OkYZAXWTlHV4SADTsnka4HNCQjssoqJja_wRpFqqjm3zXjrVg2zNdezXKIxq0eSboXnyTiEKKzFWzpkCBg5NzlyAc2DAAcSV9v75BbGIJacHdxIgsJP98LS7qxD-JhLf2jQkwBHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ldbb6KTqtnHSF2KORAnriUG9xrgGsEgHRL5xNge3txLgG5XqQVIiFWX5PwLfLPHb6Rf5EzVW6ywVu-iKqKNxoCLJXc3Y--PtfsiXzE8381ocGfYi-efJtUEeJ7jalTU8x3Bvs2M6TsTcEQonNB4wwaSgQSJLvX6QnqcQFiJKsAMYgnmE-LSJ4_HTnzu2_apej9MX321pX0bfIGNCarOh4-BvARmWDOmHTyzbT55Yy5kyN_VLO-SVAaytcj_YEXJr1igBYup51T3v2g48B6ssdRLmIJeNtIG1HZrfIhKfiF6HdR86Pl7QFBlqcplFvr3EIs0uyRriWD2_vYqFBJOXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=J-s5bYrpx4FhflLjptQPd7jLYMOqkTdaJGU_6hkEPv1VG9lDB8ZQzVUU988U5Q_7siHkhw5_kxjKD35_BK0k1BRfbo80PoQni_13Qalup34QuFuwXD8M39-hYZMctWk2Nvddjf3WN8mweOPNBGIiLJhk31xT3B1z663H0hmfYTrcefq0gCMLI7y-9K3x5tz8fhT7UTiYL5R4JMOxR0D03-jAfw67R-fiOHQEJ-disV7q0DP_gDBJvjocxhdHUR0jWt4NX43fKkhjh2QwShJKoeGiSFtdySRQYt4mLh4-Iwn9L9kYDATiixEDhEewlHD3nw5d789doITF3vntLqEcyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=J-s5bYrpx4FhflLjptQPd7jLYMOqkTdaJGU_6hkEPv1VG9lDB8ZQzVUU988U5Q_7siHkhw5_kxjKD35_BK0k1BRfbo80PoQni_13Qalup34QuFuwXD8M39-hYZMctWk2Nvddjf3WN8mweOPNBGIiLJhk31xT3B1z663H0hmfYTrcefq0gCMLI7y-9K3x5tz8fhT7UTiYL5R4JMOxR0D03-jAfw67R-fiOHQEJ-disV7q0DP_gDBJvjocxhdHUR0jWt4NX43fKkhjh2QwShJKoeGiSFtdySRQYt4mLh4-Iwn9L9kYDATiixEDhEewlHD3nw5d789doITF3vntLqEcyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6Exqx9kHMrRBO4gYvLHmPQircCBkrJ81v-FM_ndQOWUl_1pXRDn-LnDJ6jLJ-0Wtyatsxf6CpLIJOB_hA-8LT7iLkKwEt7VMpal1ZA6NKQXmi0dLKc70DLJXkp3-TAu9BdKOf9LC0JQ5wqE9YtiPa4dDvY4wEDlp0XMU1QRGheKVOWO37s7ZhEBzKF3zHD3hr2ry0NVjrgXjHEa-fdSZKQyFHC1BHzVG2LYAyDKSOIG8XX3K354VMvXXWpHmK7WrfAxvC3ZnhYCK8TLPCC52SVtwGnbp-tOpvBnZmRDfXynPa_vbIpZ-WpG1KCJdJKqIN0bBbxpFhCCJlXB1_PzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmPKwdcV87ZupdmOqhJlQCgtS0QiltYzmnGDu5pu75If2ZOrfhTQJJExLRIg8xIYdjDzcXUuVaFTLjFFpool3gL-5uurNJ7mc0nwInopUSwir5di8P5-fBiChzGB1fHNgYpLHT7zFId-ofoOdbEbfBKn4Mo20trYxLKqlQF7B413CbYOPTbQihqeHAgZVF4yyf49QvYGHha7DHCYtY163IhiIOqynQFQmtSH9Pjoow6urgWyTHxgJfpQkiqO8L0LllMRBduVeE1RGgG2ziRcGcD80PGWTKXATyONbBVxtGO9F6l-HrEUVBhK5kG8pCNFrxiU9g2C2UlQMZkpfw3rEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEoWHKxbjIUO0op_Z7CS_lEFzfRkIkHQ4-zN4ndTbe50VquibfJfrlkpMlrkiHzOxxflGC2WxLlLze7Daudi914jpWmtC-0_ZIchHpT2WCKioEaw5QGV9cIiAnPLdYvI5YnqLaXFSdg8OR1o5DeZqQ1Zn95fIyiZjujfgXQub0Nrg_BJ1qElX5Z2SSLQhhIY3up1Ar5MXNInVnpTaHG81d1IdRf-zHZ0edyhpobRihRgXjpObr-sdVSEacbmjMRrZv3z4U0NNOedU2C0SHuJ1o_9dPK-FSxbNJr6ScwEBhF4eZnfTOutSCpjqv6tAXfQ_DkcKxIeQl1aGy9mm4jQ4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfHkwKLrtFuVmmiLy2SteoPyqNet1zTToF44eiuAKh51tA6BIHTVtx7KIo4lUqdrfCC3WAULCd72Lc3ITu0N5PbR2XQ7VU_nhC1s73gyeplY_b2pu8UrbAm7M8_BCuV8V6DhmQdSpRsGgxs4GjmuuaUIDWpQ3dalznVL0XjulQ8fp7OzJP0-miX_z9fY5-ktlJk3ySK4x8fa8loOyYmEHjHd0P8iLrQKZyJrRYIDWV7cMZ7OiSw9pVA7XOxkQKy6NgU0OYGXyF8JEsnk71rc38GRMa8qmRoqY9aW9k69LT0CKoRZNlHflCueMbx02c6k9TQEyY7vZiESY1-BB_wtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCP9QzdeWaRcxxqylxeB4Tgn813pllH00M9sPYMLDFbMbE8squWF6IghLVheUSXH4bbW-u8qUxp6-g7APhREeZErBAqCOqrzY2rb_EXlcHivsIV1GZhTGwCbL0kGfdVsgsGAotYurgcYFYJAx76Db_Qx7McVwzqV8SRvwhvfoRJ2b67xzB7pMbtEeBdpZQKk8RgMByHzVo2uQMotm76CwjMpbcVIJhCuR8Qcw4uXHbT738KMu_6PeAD9ZocIJX2EPHOdDaGQQn5OWMG9LCERbrg81nV6GCkvSMpAXiyMvL21NAzA92bW3MKQXulEcCc9wbc-EoVEwQ9XF8U_D5fhNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbALkQe6TXa0ikWMeWqtH4a_Ghk9hEu-C13nIXyXu8z0lfY6hcsq5J8oe2onlvKxkYHbA2aBpqlLMhP2IF9DePwMUJS1gymghwbZPcFRYmGvWIe_Zq4VKGeZkCwMBAAGwBx4SlbipIpFic440lGjzK3uCOEFRKoyskWaPI7TLw1dNYirtUwg9y-Ro2uFvH6QOvdHGt5IQr3II7rOgMvT1jo6qhEPHHdrOXOUUNy6EFUPqgggg1PfShIg4qeB9srC381Gt_tPJiwRgZz8V7MR2oIS6vaJstrGktF7sJeovxMdd01B1bk8f-tA24csiaaKTl8wkGxTZ5faa_j4Z36AFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqIHTc43fVnN-RclHVWoHCecD-uiiqJjrbPl0MpgvqVYpK7_yCtH2DVl3Kno2SxQ77lUWkeTy0lRP0vrnCQfwTjsgaIM_QiLYvcm9sjjc4zhniq4QowBsYLKu0klhfe43h2AyiG7nDJgntvbe9LAx0ELFMNhs-nwkTA5ZVwksrl9N8Hr5V4prqSmoYFWLBXv6EBL27dMhoxY8SRIMRuNN630FcUWmK9AnkzVGVf2XFcujuq9xQg49c0hC6J28ygIW2VQESlycJjjtbNGYG_PUG_Ps1ulHuMzYkp89kcxGPhOIvJUvpYaGBbJGP2zfqyYgKA84LLe6qYo5QsvpSy8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=gbUWpEVne_unj-SW0HpzBmQqHMybbeLXcqFj16Ibs_X0wMS4QVLlcghm7oAuqBO9-dBj4NfHEZA62rUTTCv_hdMI3Vc0Nk0zo4tTxYOKaYQSagXvrhbAiQ0zeG3dW-mEfUoCB_jtFm3UESeopWw_P8RSeVxa-Tw2-isDjOfvvgavxjFuCD5Nh4_PT3HdAEEiFX_7pOE1CBhco0SLt1i7TrRLoOi8_WUgJJThKBGs5U1bhmrgIrGhYk33vNpRIZ8OOZ5JlBYl2-6jwUEpQBNveSfXx8jXzjWjjznjIq5XxKWCQFLiKO8SfyK4xAdH7tJZ2twf4IK4o5qKTljUL2Gz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=gbUWpEVne_unj-SW0HpzBmQqHMybbeLXcqFj16Ibs_X0wMS4QVLlcghm7oAuqBO9-dBj4NfHEZA62rUTTCv_hdMI3Vc0Nk0zo4tTxYOKaYQSagXvrhbAiQ0zeG3dW-mEfUoCB_jtFm3UESeopWw_P8RSeVxa-Tw2-isDjOfvvgavxjFuCD5Nh4_PT3HdAEEiFX_7pOE1CBhco0SLt1i7TrRLoOi8_WUgJJThKBGs5U1bhmrgIrGhYk33vNpRIZ8OOZ5JlBYl2-6jwUEpQBNveSfXx8jXzjWjjznjIq5XxKWCQFLiKO8SfyK4xAdH7tJZ2twf4IK4o5qKTljUL2Gz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abYhnQSsMajGdvKTUYb5_MF3rpjVhV_cZG_vHVdbttq7heYNm58-x2_NUEga-lMucxgjqVpC-I4xklQcXgVeZyQ0oPqGm8kLCrP0xyHHEO9qSfFeN2mzcPwAbB6HQa4ACWJkI-OaggF3GgqUlU_6ZN9DKiLvIkivaqCaAJa5ZaLcaxEgKkil73qAgethViJPFtE50fYabgDwJRhr4jbAVaXRtINir4M4c5rhGU6HX6mnqTr-fdRshluTvUth6lyrcFS0F38_Q6hvZZhPioqFNAmcx6oYKnHs77iqhRGTXOjyS0DlKcuz0_BtHO7AVC8Xi6_cXI9U2Ltw1EbR09a6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=XS-KmiUjWt171LURBg7vW1hV73vKwjxeRaSJn60rHheeiIlJ8paZIX-Zd3v1ee5jr0vvemTjJWZ5NtukNs655VHRyxLtefBX_NbQ4UbWdVLy6UZOnr49dU6wkvZNV2ej1nDlcFFK6UifEmOvHjGgsLxfzNnYYhXiI9BW7V3yG_5cBYOHiAipV0YeqcvH4HLH4424ch3aw6NOvchFOno3A0DNyjVwuK39HFbQvclL92VtKLcbuL9fbmJmdKsEG6nNpm2Etnpr_yu1r9PmWFsYMwJETadvdUAv6xLCC9WuMhDjAhUgV6jmL8uBbfhLJZQjYH4W7MnpxTSuYfWj7OurLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=XS-KmiUjWt171LURBg7vW1hV73vKwjxeRaSJn60rHheeiIlJ8paZIX-Zd3v1ee5jr0vvemTjJWZ5NtukNs655VHRyxLtefBX_NbQ4UbWdVLy6UZOnr49dU6wkvZNV2ej1nDlcFFK6UifEmOvHjGgsLxfzNnYYhXiI9BW7V3yG_5cBYOHiAipV0YeqcvH4HLH4424ch3aw6NOvchFOno3A0DNyjVwuK39HFbQvclL92VtKLcbuL9fbmJmdKsEG6nNpm2Etnpr_yu1r9PmWFsYMwJETadvdUAv6xLCC9WuMhDjAhUgV6jmL8uBbfhLJZQjYH4W7MnpxTSuYfWj7OurLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FobfccYTa4Ni5XXrNMP8_vos7SpiWX3IaA_xWvYTEO3nzmIvu0zdnwBPzf5cZkCVahKLShheIGn3KqSwqa2TnAN2EK7Yr1aPvTLwT3KlV9OtoKcqPautGcVxGeQNSFyqpKMPH9z4RY3ckeQ9w-LbuJdpXej9sdvCJy1DkEnensNgprmY9_LeffuMPMsnHVtaQsYugy7UIAxUeOGLY5fc3_TCSeg3H9u3Je0r7QU_4O6HylSjeauzx-ihtzhrkuBpC91gXHtKxw_XBjao9JRUxQGqvt8j3dxslVJ8VCmWbsJeagpnLnu6hF0K0Cr32rEwlh5zD7NNW1CywX1addeujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKFDrsmA8uLSEcltpDtoQ0D040QXL58v4ckCpS2zhFqvt8yoLI3ybR_MQ2UpjKYBx_AkNvFQn4_ZQleinWIPOaSASGQ8GUuCjHxeqSCla0DDPnH_iZJpX1EUrduiGhH9SFeyGTZBLP-tLCyp2E6x40kwONs2gVzbfPn_eBdqAgC2rzV1VNaNqYcpXAiMgrCxOIgTG_RLfR8j-NSowQtk2YtaohV4rcd2zSewkd3I5mEHqjqJWaN18_hWJnKrVz3HL4yZGOPa6Gpm3XXRhHwolfnoeUHKn_bTDigSnSHtUc7v7rCOFycuho9_xlKYq87LaDOJp0RZk74mfD-2RgkqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoICgU8kWhQ6oFmp5fBnxfWIwKoS--tvQnHuJWkvByw3C7Xtz0iJd3d1jcOOQMjCOcXTcKgaU_4tLQ7OWFruEEXayCInUwAOgzH70HzvRvg_vFevitotKHBpzK0zcxV2SaX8H-wDNnak8BRLoOFLzTVy9SN2D2qgYtUG3jSsXJ_ZGKLdP5bZjiMvIfGDbTOaCl5B5sgvRpsSRRzNUuWE4naBQyDnDuETGmXtJsmo0gTbXCuG0rsdWVoP-Bg9EPfL_aUtkJ0BP6AjHMlELTEvj2a-xs8SVqFnlKjDihHFbja9Ppo73aubSBp-yen5__BBj9U-T2Z4A0BPR6FJft1aRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh0KB1SqftOpLXmkkszZW7rGZsnpisu8vwnaKzir9WaIZnNh8qvkz1oYYrq3R_xrhvKBFx0kHH490UbELu775RKphTl4Z2yiuMd3EmQfrUE_XiLL7Ikw1AEMXCnWcybXL7kqMIRditMvD6uoJEGqulJRKzYtbGze4L8LiH2Ki3kc9mSOdUwFfmCYlZ-Mx_SXVMfZl54uCnneDSBG8q9VrANu0stb4dUUjXqwHAW5-m7InHLE387el1j7hfn-v0ifr_MKTFFoEleiy-TrPQCUQWAlcuMtEotq1fek_o2tXRHQ4zjyvbJQ-5SPhUpLtNK9IkHTbq-FHoModuX2wklgKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=Cd1becQ8h4CuILUyxtS0aeB0FG_ZIrBDR-Up6txJT0NPq_85q2TgcbC46PylIXsYCKKvjpRTyNBozSRqoG4-hJm9mdN4WkE9-oix7XAO3-7PmPiscbV1w7HxoNd5TvlL6LoaZYSTHM3evMyJZiyyR17MbRQxSEKPu06WKYSXbGU2Rhuvjdgbtu_DwTtGUim_iXey1zU_mXEW0ze_eKvsVH1u_cqqJb6wu_fSPsS81w9ijCeixKonqmLpLUrr7KpBgarP848iHy6CCIEKqFTKzoSrV52-fb_NGVGSaveh6A0n1NVK8ief07saaMW3JTymCwBFcYl9UqCR_bEfo-rlXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=Cd1becQ8h4CuILUyxtS0aeB0FG_ZIrBDR-Up6txJT0NPq_85q2TgcbC46PylIXsYCKKvjpRTyNBozSRqoG4-hJm9mdN4WkE9-oix7XAO3-7PmPiscbV1w7HxoNd5TvlL6LoaZYSTHM3evMyJZiyyR17MbRQxSEKPu06WKYSXbGU2Rhuvjdgbtu_DwTtGUim_iXey1zU_mXEW0ze_eKvsVH1u_cqqJb6wu_fSPsS81w9ijCeixKonqmLpLUrr7KpBgarP848iHy6CCIEKqFTKzoSrV52-fb_NGVGSaveh6A0n1NVK8ief07saaMW3JTymCwBFcYl9UqCR_bEfo-rlXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ57mXCLI9WoPycyw41lb_9INlo5Ln80GDfSGMjvkdJFuvWsY-dowzyhLEZr8-Q56lhgSzLSm5EeHra4yhjlzcW-dI1-mDpv5TB4pVAdxNxZiJthQJoLuYR8CuZGL1f0_6gTJpsfUAbJexZKNmWNCGyMac7-acS1FMr580BtIDHrYeIb4jDBiXwVlrBABWraNaltH4RNUzyvuITtunwyYPBGP8wR1VuL0weD8pFXkU-mpjCgSttiGE5tGEFFxd0SPGS1nTtfR790I-5O9aW_3Y78SsQxrZM84SnsAboBhffiM1niHaz_fINPrd4wuuyGuHgxKWuRXN9W8Ah__b88jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8dGQnjOSaW4KRGQdMzb98ZSFcQolj9KWJ-zD4ePmmSIG-iuz6Q5bPrCLmdfqWO-bRVo16FMmyAUQVmg0VjD_7y1WPcJKoiy3suB6IqFEFpq-e4RMpHCjvttfMr6jC2kyUnpE39bGh5hjHsq6NeIJBp-_ddOUt9LpQHeNn1_xpgJHbt9pIa6F01Jd6tfTpK51CbpmdxnVGAnakzFSzDkIO01Yg6PCgMIhtCZQesqKI5b9oiaEoL-SKTq8A_lNWDMRGb3A9bonmt48QZdhuWCq40YYHdFQtecbSWDcsa0-6-LAGO6KDzeZ-nGQs6OwKblzLKPmIL3TC8rEAz3gF2KFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTV7mZQKI2XfP0yH02C5kD9a61tjjRDRnmkLwxW73XrS-2UijAQPY4O-azNj_zANXBMhKhSWK7BNP7IsV-4LFQALk81lq_SF2ImjspBlpF1Pkv2ZA_uR78pktb3pEpDmLxaurp9JwKW_sKqnkD2MH8vcdC36bO6mttXqY59Ywgb_g0SSMBLqbPgH0N71Hi200PH2dzKb6j2E4mw33d3vajYm8xhxkQBAoKdC8ztFvmnRMMzwZoKi3EAdcqcBiC2vEW8DCOFLBWCrv6KHUyxPHRE5OC7m0HIzonoL4Ajn34VVXliC77_hPOm_r8S0VZ5QW_j0lBqxQLptYw3sfJymLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d12HqQs3jTxK9mbwFTrkddvX3y4_2YYujk8kx_PSMT-aJ7a-_NGUEmdieBO91noHAlbq64K2Hdcp1Ix9HIn5ynayMib0X3zf--MzZQLcb_2tMfx8muKaV8grJ5tKbTXqMJm8W_5OvhfUakie-6jNwybi0WACv6ATPbDj8_sStpV2hxhaVCJZhqXqxGmcx7AJEjbdMYpIJJbZWders8QqBJl1BiFNoMn19TOAdgj4fAh5RVt8iVggW86nOzLdBRPOpLdPKsvU-XnGB3UuOQo9Ku6wmk9IxVt0kBps6T1ZNO_U_5C4afpFnafNv2Ke6BS3iWnelG21mx9hLWz9R-qTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW04Y3ZjrmCJ3hptRiW9JMCIWsObH_NcOoy9DsRU9r744V5gC-Q5lDTVTjn47q-txV2FD4YbHgBATkU2P_yEpyZRfpyyW7LUt7QkxeQDNSCv8yM4ug7PEcVDKbpEFJTHV5UK_-b1rsOgIDalt4uWk3FbnEVi5kNLSZoYzJTHCTdiyhjQm0Uiys_ULtWGLEyo1F1T3uqUF5mwYg2GJmBgCedrPoaF9h9d_iYIpfX6h48srMueLC8pMCpfr2LO57WMR1VORpH3HapV8l71ye3y-FzeQT_81nGO0wiP0kJLqF7NymBBYhEnXeGCn59xesAMkf_KYlBF6ywJ2gI8HSa88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=CYr28EONPgpMTWk6VaY8_vDHX5B96eMJIHWrJpONJJVd6uDYCZm6sY0aRPeEpKztHlRB4ulyL-woU3nxZHHwqqTxK6d7WgOf4DHbU74Lyz1BNxq6O8sPEUGfV7L-tEBuP_eHg-ac5SNtL5fiOZ0tpqhS4yLCebl3n53V6tmUE7qMWOxMk0gTZ-5Qm_fVwwsFJoZhnBG4UlTBzYK2IiLpIiW9s9RkFGF0-pgLK7-WWtlMpjvtsHgeOaFBqADmPhjM_FZsEn6W94yeHtGv-RgKcFApHVRwxGVaH3KwX5gZKpb1Lg-B2RENZ7kA_dVdGLMXLcG3uUFHmF3V_sAOdxA5moWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=CYr28EONPgpMTWk6VaY8_vDHX5B96eMJIHWrJpONJJVd6uDYCZm6sY0aRPeEpKztHlRB4ulyL-woU3nxZHHwqqTxK6d7WgOf4DHbU74Lyz1BNxq6O8sPEUGfV7L-tEBuP_eHg-ac5SNtL5fiOZ0tpqhS4yLCebl3n53V6tmUE7qMWOxMk0gTZ-5Qm_fVwwsFJoZhnBG4UlTBzYK2IiLpIiW9s9RkFGF0-pgLK7-WWtlMpjvtsHgeOaFBqADmPhjM_FZsEn6W94yeHtGv-RgKcFApHVRwxGVaH3KwX5gZKpb1Lg-B2RENZ7kA_dVdGLMXLcG3uUFHmF3V_sAOdxA5moWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFi3LkpF1tO99T4nL2xTeTRunLp1c8cMBnwa79Fkqwek4w4RcpMBpTkA47K4TOg8-4O8_zPj3qU9zUF-Fzd4eb7FaoulYRMm9cl1YFGgTwB4wCtTenIf5oCxxEp5TRrD0TtnTpD4Poy45BRyE0f7rNS2Mo6pkjLhMWRnztmXl0FQMBLbwraKne_ZYYHg-MAI5OplH31x0W5MEUhDepl-BF2ie6_1kQpmmamRekdFhJfmh5eYBErhX4bQPloVMsOtZ9UU_mbgJWvgi__oNecAMjVQ0ff8e6aT7deYuUX3AKhr8JzG5hRuWo6erLdfEXhqogNqdVZmPrNSSVOFLXazLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouTi4Io81qdLplS596dyF8xvYf6FLseMjx-QRU-ep5MSQVErK2ajLFvmswHK8FNL8L_zR10M6fWhovRVowM8vvgtgiDwi86l3JxCjHE3o7CJW6a8f6Pw9kaTn3kvrYIV-IUb2mJisap97UQdvMBgT-iMk9StEYuTK-X7GpIZDb9YwVj0mRAe0hhfIRDfb1scQzW4kT8OU6_o7_M-zX84dq7DxbPxHUicw8BRek8im9Ke9NCn3lstI8RVFBPlbgcqrnnty95r1psLJlMMzX8rDvf55ZabPW6p_E2XIYYxk3W54DQiKF3pRugGetakVd-CdG6KlyIPkJyLzbK6CA9dmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=hhee2n81NZ3J5rCAkUImTwcnhswmpx-ztvyUPO-QOe6OrlPyTrRui_aqsuoT9GrPO3SSlsC6xbhtTmoblCJ31eyLStbd8tXr0RUR4VAHXrg4HVVpfg_nWJXm4Ij7C1kE5tOGGEuWke2eyig-wvUWWkpieFNDAavyv9HnjgJ0GFe7DEAyhZLSoxCrw6w40K02nkecZHEePuAJ1ZOuBoyvl7Feat-RSHU9REpQ34I4rIlmWlpvZt-koP3M30zePDQ4JELRAAZ9DUplc0GTVIbMW5ISaC4QrmvmTf6_epDpkWv97cbVhSiVMIkYKqgXPNkOHncawAvY-Pam7BEX1SOx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=hhee2n81NZ3J5rCAkUImTwcnhswmpx-ztvyUPO-QOe6OrlPyTrRui_aqsuoT9GrPO3SSlsC6xbhtTmoblCJ31eyLStbd8tXr0RUR4VAHXrg4HVVpfg_nWJXm4Ij7C1kE5tOGGEuWke2eyig-wvUWWkpieFNDAavyv9HnjgJ0GFe7DEAyhZLSoxCrw6w40K02nkecZHEePuAJ1ZOuBoyvl7Feat-RSHU9REpQ34I4rIlmWlpvZt-koP3M30zePDQ4JELRAAZ9DUplc0GTVIbMW5ISaC4QrmvmTf6_epDpkWv97cbVhSiVMIkYKqgXPNkOHncawAvY-Pam7BEX1SOx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=En5y6GvrQI_xCL2CMO-ibw3-2wWo4_kHgcV43ILxVIHRDKAD2OgQujAVxSRI4aCevRegqWLopyQL3jtejLuyOW-v-HqsMEi_5Bayx122ojV0PDe7hOfH0b-RG3hllunNu165e0bT_7xIjiPJ6Tm9hgpnjhw3Xzws1iZMbFqSBNhSgFmHdgicHop4Xj6e_bw_D1UtaPW8cYBwxjKZ6KK2ZgIa5iNMLALRT6HBncFcdm-XaQXCKSzYYuLmiBAZ0Wad0CGDHZULIMtedMDQP9RD9CuGCCucg6UHyLA5NYuaP6WONUVvsFXz9iKN_CDcFDb1Emz15P5gPaMW_RZHa4VmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=En5y6GvrQI_xCL2CMO-ibw3-2wWo4_kHgcV43ILxVIHRDKAD2OgQujAVxSRI4aCevRegqWLopyQL3jtejLuyOW-v-HqsMEi_5Bayx122ojV0PDe7hOfH0b-RG3hllunNu165e0bT_7xIjiPJ6Tm9hgpnjhw3Xzws1iZMbFqSBNhSgFmHdgicHop4Xj6e_bw_D1UtaPW8cYBwxjKZ6KK2ZgIa5iNMLALRT6HBncFcdm-XaQXCKSzYYuLmiBAZ0Wad0CGDHZULIMtedMDQP9RD9CuGCCucg6UHyLA5NYuaP6WONUVvsFXz9iKN_CDcFDb1Emz15P5gPaMW_RZHa4VmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=uIu8-27b7JLy5IYvExhwV5zcKDr7lokgbHs78vG3KPxys0hTFcBpNcAdLaAZJFbctIo5EIXh8Ri4Y39MxrjAiKnuQnIDXF3jfPbA6K7wRukoGQavl7iwQE9aHJKailpltiYx2MY9agdsLyjH7Ot5WmZonKWCB5lUdpVB0APVDOQBOnsHN4zimfKSka7Np3UHBWGt21sbVXnn_Lap_wGCp2yn5EcomF7eohna6bWkJxQDrFpGq6o4LKo6kjLgz2i6Ny2XktPULQAgSkvr1WlpNysreaA7da9kCtSP1ymCnhCnSVJ_qyX6a7reQBea6D-LcE1r18AoxXiEBqx_LtnyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=uIu8-27b7JLy5IYvExhwV5zcKDr7lokgbHs78vG3KPxys0hTFcBpNcAdLaAZJFbctIo5EIXh8Ri4Y39MxrjAiKnuQnIDXF3jfPbA6K7wRukoGQavl7iwQE9aHJKailpltiYx2MY9agdsLyjH7Ot5WmZonKWCB5lUdpVB0APVDOQBOnsHN4zimfKSka7Np3UHBWGt21sbVXnn_Lap_wGCp2yn5EcomF7eohna6bWkJxQDrFpGq6o4LKo6kjLgz2i6Ny2XktPULQAgSkvr1WlpNysreaA7da9kCtSP1ymCnhCnSVJ_qyX6a7reQBea6D-LcE1r18AoxXiEBqx_LtnyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muuqwu7YE1BL0akVyjZ81pJaK6sSD_AO7xaSgw4Qx4Cl8PrdNuK_rTKbuYPcd-y_p2yTU3ixnD286vuoSq_kfEQBpku1Zv-Yq_1tZ6EmXVc40DvJlYGOoobBKUROYnqZ-KNkQRY9JjWJAo5yYYuGO-r_8Y9oGTG7vOlk5Q5EOJGuWMfC2Rv0PrPpqgJSj-9z2ZsZf_sXFhP6bXrjvLnXjrkS7DCZP0OcZsYzOzwU5xd0LxRfPIEw58SxJhCcY7vTP65PE_3LZBmh37sqrUfikve10-aW6SZMn8ubXQhgukAsOmXTTG0vXLVrmG2x1e15Jd8o7LyWEOoi0DRoerxRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

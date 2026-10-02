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
<img src="https://cdn4.telesco.pe/file/fHLXkwzH0hD3G69sbKAdLyzoor2ZwBIQol5HGgQ-wT-mLV9CXKESdE7KvHkxqBkk9sqA-mCmVACdsQbmQoxVVKVNPdVXe_cPw86YBgMLH3y3dyljIVyEuEvCx537E_ufQAw-_iVbVJzU-XXv-HwCR6QyQp-wkhkB6qNuxCrVHSXDO0nj2Ta-TToelaszzW8P3tqj8_M3yZzz0YhZDp3IaPBYp66gdTlp3mKmJXgUNwGs_QpHav7uPp_qtvk5GQYSaB4n047ClpY62mJ6XM3S7NO3UN6Ye4_oneDnzPsqi_DzqA_cMLYMZi2FdD2JG-R3g2bVe11H9vhGUqt27RgLkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed16bd6292.mp4?token=nc4QAtVzzdEMnwpOWGCS7v18BpxdhYS13DhbkPf0dwEkVgr7lQs3sNmLE5GBssZVQt-X7V1lFWDT1A3DeT3Uv3lIrjfTOAjOj8iEnTD4l5jnABXrsh2uGe5LJbTE2AA4ovB5vAl-gr4nduuqHNLO6SAL_yAAVeLC7eD71B8Yli8E2dMemlZCBL8XjCBDCLZC62M3nb1jvlCXi9dZTXKPca6yfTkCyzXGKzoEsemLP5u0Ot2Dq_JYDpiecfWzN9O9LNNX94uErIYzXOWVC9cN-t32hewCe0XjTKINBS6ggsTXjSsnoiKpzQA7IBQQUniDcOXViHS9QL7Wc_D3uvH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرياض تشتعل بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/naya_foriraq/92342" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مشاهد للحرائق في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/naya_foriraq/92341" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8140b6c5d5.mp4?token=BvSwAf3LIoaZPfX4jANzLU6lz7TRT51MmQGIuyO6MOSOJ9vLnsxosSRbRSIveueI4kWiIYJFfi2Q4w0CnaAH5O2zLKdoYzjSCXklHezdxWhrKA9J7Tps1Ed28Eae6DpZU6mFfmcpUcu_-oRXpqhVUrJbtmq6JBqNJ6ZUe0mjWhBo8gewq0dnuSaIIaHjGPuwnpyiNaQ6thW0YX3MpNpxwMl29qtBf2sqqZJ2wCMfsvOxdKgmUbb27dJZglykNytMwqusH4cwVAArDyhLE66ST49THa1XuFs7X3wZp5xc978BGnPCRiRd_CzVUKBJPyw92c0wIBmu0w0E8HZGzDiVyEI7kpACrvXaG3cvPcrAXt3rXKL1BbJHEE_74lq4d0U23m0-nmf0C0YlRRb8O4ZE382V39um-HKnzgytVmS3ZzQtJ_8QyZoBDQ6DRkV9B4bbrrD5PlGSmyfejcbYNoFCYKWTGno5GNHdH_ZzzDrwWgkQD7ZYLD8ERGov1im42HDMUbwbCPYeOu7lLddXGB6f7Aa4Bcrs9EzuDrkiCzoehjSO23NpmtjQ0Ra8q72loh0VG_Vz0YTwMRMhdRgaDwAZIcePPYhOPgEaVQDFgqpd1kF5lpHgPs_1Xov1G4vq8baP6P_j7OmA8DrwSpDS6sDfYeo9Ygf_nDSnPby9TpKkwMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/92340" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=k1gVigThzAE_KGUHmhKhpA3rcf1gdgYdaIbkq1pFwC9t1W7hOW2slgV9GKAd-scNJ0qWSbbcohjop0p4GvF1VjK_a3K8Wo2DkMHREH-sEUPgWdL2Yk7KcPBgzEWgmsdave0la667S41oU69IV1BZs5N--oe32sFlA4tGMFTkSOsoB2_vdX-DkhnGZVTCMMUVBKAdshoaed24CUWBjTUP8sgAFvUg4EtEKUXOmYs3Fwk_Eq8gDF6JJcHddJghhbqQjc2nQhgl2YLp_2GAqiR8HIcHcnfUPJ0IsQg22_ehgtJmGeCriRI5MHpiWtneosh4iCDP6JvAajoz8qB3h-URIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ab0c8c4e.mp4?token=k1gVigThzAE_KGUHmhKhpA3rcf1gdgYdaIbkq1pFwC9t1W7hOW2slgV9GKAd-scNJ0qWSbbcohjop0p4GvF1VjK_a3K8Wo2DkMHREH-sEUPgWdL2Yk7KcPBgzEWgmsdave0la667S41oU69IV1BZs5N--oe32sFlA4tGMFTkSOsoB2_vdX-DkhnGZVTCMMUVBKAdshoaed24CUWBjTUP8sgAFvUg4EtEKUXOmYs3Fwk_Eq8gDF6JJcHddJghhbqQjc2nQhgl2YLp_2GAqiR8HIcHcnfUPJ0IsQg22_ehgtJmGeCriRI5MHpiWtneosh4iCDP6JvAajoz8qB3h-URIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العاصمة السعودية الرياض تحترق بعد هجوم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/naya_foriraq/92339" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfeNkJJwjiD3S_R97xp6xLQJMEsQexQ1xQLvyAwjRJBKQ8c2FegrN-vMCKjUjgNMyPK4-vyHdKOK_JPQdKCX9KDw1gkMoxIrSZFWJLAPOukbQHK8tqn0YAY2VkTP8hGC5_zgQHO6bM7h9AblPk6tAlselmY7yZUMg0wU3Q3yyI5glr1Kkq3RCB3LIf3tKi3Xq63nkTvo-FYarXRlPgGd4nQU3b19uUOktUJjWF11G4qwS4syoSAVtZOhrs2qBXFLXJB-Kkvg20KfgNibrRAFK5zLTG7SFgSFPiZJysL3CK7890URY4-NlqSgL3oECm5LRTzcsBJawCuy4xtB0VXHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐖
🇺🇸
ترامب:
أوروبا وافقت للتو على إطلاق كمية هائلة من مخزونها الكبير من زيت الديزل. وستبدأ هذه العملية على الفور.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/92337" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">إصابة ناقلة نفط ترفع علم بنما بمقذوف وتصاعد أعمدة الدخان منها أثناء مرورها عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/92336" target="_blank">📅 17:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
مصدر يمني لنايا:
طيران العدو السعودي يبدأ بنقل جثامين وجرحى الجيش السعودي عقب استهداف مقر التحالف في عدن من قبل القوات المسلحة اليمنية بالصواريخ والمسيرات مما خلف 17 قتيلًا وجريحًا سعوديًا</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/92335" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=CEqQ0RFTZK_Su9QhmZBXfT25oiPxuG03PLkkLcD1ZcFQB21l3M9Ny6me_WNYkmuNh7UQDPnyfC36lj0j-6kbvAov0A_oF6MgBZNLQEXcgnzvR4bZIVj0YZ2gr35Z7lxoQuupfSlcRR59n4Vp8dg6FgprQiR9wfxLW16fWt7N9pZ2onZ0eNhkwTaj7gCPl46BPJ-Ln0FLp3e-x1U8LyqXZB85mkDMgQMZGl8AiK07dqCMT43HUPWrb37kxo2Zcelt19PiMBh_BxGTyxkS3q5cmfw4wMjSkiyaRAdQRN3e2UF7ZKNJFiJ6tQbiLrMrh4hf1VMjjRGcZt7QC_YzUAgH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c980ec8562.mp4?token=CEqQ0RFTZK_Su9QhmZBXfT25oiPxuG03PLkkLcD1ZcFQB21l3M9Ny6me_WNYkmuNh7UQDPnyfC36lj0j-6kbvAov0A_oF6MgBZNLQEXcgnzvR4bZIVj0YZ2gr35Z7lxoQuupfSlcRR59n4Vp8dg6FgprQiR9wfxLW16fWt7N9pZ2onZ0eNhkwTaj7gCPl46BPJ-Ln0FLp3e-x1U8LyqXZB85mkDMgQMZGl8AiK07dqCMT43HUPWrb37kxo2Zcelt19PiMBh_BxGTyxkS3q5cmfw4wMjSkiyaRAdQRN3e2UF7ZKNJFiJ6tQbiLrMrh4hf1VMjjRGcZt7QC_YzUAgH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعراض جوي كبير لمروحيات الجيش العراقي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/92334" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتنياهو: كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/naya_foriraq/92333" target="_blank">📅 16:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتنياهو:
كلما مر الوقت، تتضح الصورة، والمنفذ تبين أنه متطرف إسلامي. لقد جاء لتفجير الطائرة وركابها. نحن بصدد التحقيق لمعرفة ما إذا كان قد أُرسل، وكل من أرسله سيدفع ثمنًا باهظًا للغاية</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/92332" target="_blank">📅 16:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10465af39b.mp4?token=Y_u3UUwcBUUG2zWcResdIu7yDB5ewKrl7LBuCURpN6yyIWEN2yNEcAFeEZ0Oym4X8fASSsYA_t3dkoAdu9rI3jnIP__OhwZxGcTX64A9658rxG2yTgv-hEp-4xHr7TKDbVBPX_Sd1q7IzcdTqM6oFuBTUWYzbPegzRTkLacBIGhErmsiOUA8rXi4-Pez69Tn977U9epwCpg5Ch3Z82quTWtPN1zMfM-05yum87vPfzZbHWDZwy3SPmIoyEL9eQSqOziLL55IQQwhcvDbk1z47DMdHOr12cA3sctjfTHt0LeWW5nYa9_rl9SLLdgHvtbQIh3LfjWNdd_RbfQHDzB4BGuAMYIeVHd9cBP3RhwdeH8xGYPh_ODi9QX2JVqo0_2utVU0JQ8afemCfKdMRQ6e-GOHo56k_e5li5o6zYBEjDmmvH3aDJWvL5AET0Syvq5Qz4JAkvHgFjVXTPGYMHyeOOGQShxhak5efQ1Vs6VgIKXI76iEDAxYhQikFb_z8Zxn-jHpj7qja8idIDIwsFlKHJjaRte0faLeSb7EcrusfWDsjdK1jYMkcxIoCdR7qQuSMZBQXoY5guHM7HK_k2PxCCNxtZVN_kMllbp3bKOKwJDNMVFnEBD8LkmqkLxlpktIFSL3dFad75RutnQmQEEfCj30MzxdyXAf20BWHTZRMsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10465af39b.mp4?token=Y_u3UUwcBUUG2zWcResdIu7yDB5ewKrl7LBuCURpN6yyIWEN2yNEcAFeEZ0Oym4X8fASSsYA_t3dkoAdu9rI3jnIP__OhwZxGcTX64A9658rxG2yTgv-hEp-4xHr7TKDbVBPX_Sd1q7IzcdTqM6oFuBTUWYzbPegzRTkLacBIGhErmsiOUA8rXi4-Pez69Tn977U9epwCpg5Ch3Z82quTWtPN1zMfM-05yum87vPfzZbHWDZwy3SPmIoyEL9eQSqOziLL55IQQwhcvDbk1z47DMdHOr12cA3sctjfTHt0LeWW5nYa9_rl9SLLdgHvtbQIh3LfjWNdd_RbfQHDzB4BGuAMYIeVHd9cBP3RhwdeH8xGYPh_ODi9QX2JVqo0_2utVU0JQ8afemCfKdMRQ6e-GOHo56k_e5li5o6zYBEjDmmvH3aDJWvL5AET0Syvq5Qz4JAkvHgFjVXTPGYMHyeOOGQShxhak5efQ1Vs6VgIKXI76iEDAxYhQikFb_z8Zxn-jHpj7qja8idIDIwsFlKHJjaRte0faLeSb7EcrusfWDsjdK1jYMkcxIoCdR7qQuSMZBQXoY5guHM7HK_k2PxCCNxtZVN_kMllbp3bKOKwJDNMVFnEBD8LkmqkLxlpktIFSL3dFad75RutnQmQEEfCj30MzxdyXAf20BWHTZRMsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92331" target="_blank">📅 16:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=dLm_X_Byi0LAJuhSR6PRKewFDmbBKaiRxoayqMtz0PdZ3XW2hUOs25eblQmJvOUx8JlgUVgv8M2w_3Iu8grkPPuqZi-V-2UGiztUEUVMdSQGsjHnxTH9XTgzwfnemkb4nSDymaZ5ZK0UMXyEbcBu1a2Q3CPd3J6FDnUD1bUETauRz88JP40HpkOdNPweRdRCPsFL-iDTmVPRh8ywZh-1L53IS9mwCs6L2fU20ZB4EYj6BihtdH4J8QRPnm2cdgCFdF49kCpqvtDgDUp_HjCz5LbBScwWGu0n3O_bdlvVkNWVpaH0V-JNNvx1Qw4au5SOfMBpdYDF_vUdU7Sje5n9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc43b2c991.mp4?token=dLm_X_Byi0LAJuhSR6PRKewFDmbBKaiRxoayqMtz0PdZ3XW2hUOs25eblQmJvOUx8JlgUVgv8M2w_3Iu8grkPPuqZi-V-2UGiztUEUVMdSQGsjHnxTH9XTgzwfnemkb4nSDymaZ5ZK0UMXyEbcBu1a2Q3CPd3J6FDnUD1bUETauRz88JP40HpkOdNPweRdRCPsFL-iDTmVPRh8ywZh-1L53IS9mwCs6L2fU20ZB4EYj6BihtdH4J8QRPnm2cdgCFdF49kCpqvtDgDUp_HjCz5LbBScwWGu0n3O_bdlvVkNWVpaH0V-JNNvx1Qw4au5SOfMBpdYDF_vUdU7Sje5n9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسراب كبيرة من طائرات الهيلكوبتر العراقية تستعرض في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/92330" target="_blank">📅 16:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">المرجع الديني جواد الخالصي يطالب باستعادة أموال العراق واستقلال قراره: لا خضوع للإملاءات الأجنبية ولا حياد بين الحق والباطل</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/92329" target="_blank">📅 16:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=Z_ardiKbRytr4XWLRMJ6nS2SVtZRQCeBB_0nb6hVJYUiOOVK1I6DlXaUNC2ewbilsDPdKHbqQyEy0pislWGXRsudU2sg4pnMD-C93lIb3LcxaSM-a2zb1j6-Afnvjew5P-FbWpPA6EWpv5fTEAK-lxvTPCp6wkrCq1lvkCsngSnxp3SDs5V-6UPdT-gFKLA5zoFgGwoS7zxXQ-tu9pkKwJ11QgcfMldeG-UNA5JblztHlQ2hg2WgjdKPWzTgReP57efZbPpkeo5Rv9KknZCcTSuwr1RebnoULDWCFh1wKoI18yDztbP5hKEL16bwFs5XBCh-hAkxros5WmgO3OuGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9479b284ba.mp4?token=Z_ardiKbRytr4XWLRMJ6nS2SVtZRQCeBB_0nb6hVJYUiOOVK1I6DlXaUNC2ewbilsDPdKHbqQyEy0pislWGXRsudU2sg4pnMD-C93lIb3LcxaSM-a2zb1j6-Afnvjew5P-FbWpPA6EWpv5fTEAK-lxvTPCp6wkrCq1lvkCsngSnxp3SDs5V-6UPdT-gFKLA5zoFgGwoS7zxXQ-tu9pkKwJ11QgcfMldeG-UNA5JblztHlQ2hg2WgjdKPWzTgReP57efZbPpkeo5Rv9KknZCcTSuwr1RebnoULDWCFh1wKoI18yDztbP5hKEL16bwFs5XBCh-hAkxros5WmgO3OuGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توترات في مدينة الحسكة السورية: الاكراد يرفعون رايات كردية والعرب يرفعون رايات تنظيم داعش وسط مخاوف من التصادم فيما بينهم خلال الدقائق المقبلة وخروج المدينة عن السيطرة</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92327" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngArDXOu7oOjsAc9h4qZP9KvVgBhcvj0lw2IuPYPzzQwJi-cwmFu3kAyaIH-k1WNx1kh2NpMI_FMjYK9N0nqcVjW33_kHOFQ89NPSWSmGZZml3agkxdWIpi1i9RNDUD-RvdaHoJfQf2UpIjuroHKswebbn9wqmEbW1ZGHTNLcRGNiN4b6hI5V5P8Wbos2YH9dYcH57FrXsoiorgN1aQGo_VHI-o8P2hBDOcQLBAvwAChrMFFmtC7MYqpNZTPwBgdZUK7BfMXtd2BLghtYRo8T10kvlFY2ih3kqbFrwlcLzO8jyrgy5eUymG2hQnd1a9oYLRWRKezb5UdFYCDRAiuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب يوضح بخصوص عملية التون كوبري: يوضح الجهاز أن العملية جاءت في إطار واجبه الوطني في ملاحقة العناصر الإرهابية وإحباط مخططاتها الرامية إلى استهداف المواطنين وتهديد أمنهم وسلامتهم تمكنت قوة من الجهاز من ملاحقة عنصرين إرهابيين في إحدى المناطق…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92326" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
القضاء العراقي: السجن 7 سنوات بحق النائبة عالية نصيف بعد ادانتها بتهم فساد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92325" target="_blank">📅 13:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية وعناصر إرهابية في مدينة راسك جنوب شرق إيران؛ مقتل عدد من الإرهابيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92324" target="_blank">📅 11:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4622935e.mp4?token=FyNXv7tulHN_TC8Uk7OQmetOHAnsYW1khhQw7fzBkFUrJy-ph9Z_2d3eFIV0KXhgfpgD-p41_F4wJ3E6--Mhsqs85DbF7zO8_h1sRUiPNk10BbJ8MOjHTCDosokNLuk_zdrZXvYSU_NDsxwtCmgvTJVes47apFoHu7i8gXamAt4duH7VW8cV40gnpNCLzNSQhiYcMw04CTK155PKrofhuYCWepoXVO2JKkJpC2da_U8ocx8ffCqcci9kdf_2Vi-c4jtwLhrW_VPOpcUkh8kACca66BM8rhC0G9L1FxVMjH0B_Z8b7pSseGIZ7aVP-uRF9DZe58RrDcTWr6yoW5JDEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4622935e.mp4?token=FyNXv7tulHN_TC8Uk7OQmetOHAnsYW1khhQw7fzBkFUrJy-ph9Z_2d3eFIV0KXhgfpgD-p41_F4wJ3E6--Mhsqs85DbF7zO8_h1sRUiPNk10BbJ8MOjHTCDosokNLuk_zdrZXvYSU_NDsxwtCmgvTJVes47apFoHu7i8gXamAt4duH7VW8cV40gnpNCLzNSQhiYcMw04CTK155PKrofhuYCWepoXVO2JKkJpC2da_U8ocx8ffCqcci9kdf_2Vi-c4jtwLhrW_VPOpcUkh8kACca66BM8rhC0G9L1FxVMjH0B_Z8b7pSseGIZ7aVP-uRF9DZe58RrDcTWr6yoW5JDEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران القوة الجوية يستعرض في سماء العاصمة بغداد ومدن عراقية أخرى بمناسبة طرد القوات الأمريكية من العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92321" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e49c4705d.mp4?token=gCzAiReqLaGk7taDle5o0VnKfLTRj6fwFFq8h4jPSCx-1XSqht6u9-0oUrbEslmGCh8AsxffPm9-fnwpqL1TT1YSoxZTUFO7GrapW0CDmU6RQLMPBahohhnb5KZp-UK5hsyzzHkwPW7Apmp94CCe4_73oBtFrWoo_ZPv901PBd4ts-F3dN4hxrcknxyp41Be8eYe4s3AYjNvWrbw8bN7_lG7kZJtgymr-od7z31lWJ8eFfcn0LN2KhVCAsmpfKQqJI-JnT3s7m6tAqhCY5wHwh2bIik3E3TYni62ZxmskDr_AHpOnbxCdlKS96NWB14R1Ya0Sy3dTO3BVEEWcJ6hVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e49c4705d.mp4?token=gCzAiReqLaGk7taDle5o0VnKfLTRj6fwFFq8h4jPSCx-1XSqht6u9-0oUrbEslmGCh8AsxffPm9-fnwpqL1TT1YSoxZTUFO7GrapW0CDmU6RQLMPBahohhnb5KZp-UK5hsyzzHkwPW7Apmp94CCe4_73oBtFrWoo_ZPv901PBd4ts-F3dN4hxrcknxyp41Be8eYe4s3AYjNvWrbw8bN7_lG7kZJtgymr-od7z31lWJ8eFfcn0LN2KhVCAsmpfKQqJI-JnT3s7m6tAqhCY5wHwh2bIik3E3TYni62ZxmskDr_AHpOnbxCdlKS96NWB14R1Ya0Sy3dTO3BVEEWcJ6hVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران:
كانوا يتعاملون بالمخدرات، ولكنهم كانوا أيضًا يجرون تجارب نووية. ولكن هذه المصانع التي تنتج المخدرات، وهذه المصانع النووية، تعرضت لضربات قوية للغاية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92320" target="_blank">📅 10:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888df7398e.mp4?token=CocDS7rP6mQ7JGcP4wZO71QemAloiaq2nZZeht2vgN-udu-1QEvLq6Cnb4-LhokWpk2Lebbw4bnlqm-ueYJ_UtK46rCzoQf8vczaZDsaCK844HAWcyfFq6CmkJj-QJ5VmP92QcJ2YiKjCFZ4asuArl8XOy-1w8ZGLbIBXUQOi8pFHpoEs79RII83zItPYaLnBQm2h06gdqGehJddr3ZUFvoXaqcIjL2DvPewQ7hJagykuwCtG5SoeoSn9rz-bnoiDK3H2MK5OlKmxofeRrEBimV-imWu0qLlKbw11q713KxbwviWa4A5kXA1IVLVlPjuxJts_kuNPm5D2qTPV2HWYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888df7398e.mp4?token=CocDS7rP6mQ7JGcP4wZO71QemAloiaq2nZZeht2vgN-udu-1QEvLq6Cnb4-LhokWpk2Lebbw4bnlqm-ueYJ_UtK46rCzoQf8vczaZDsaCK844HAWcyfFq6CmkJj-QJ5VmP92QcJ2YiKjCFZ4asuArl8XOy-1w8ZGLbIBXUQOi8pFHpoEs79RII83zItPYaLnBQm2h06gdqGehJddr3ZUFvoXaqcIjL2DvPewQ7hJagykuwCtG5SoeoSn9rz-bnoiDK3H2MK5OlKmxofeRrEBimV-imWu0qLlKbw11q713KxbwviWa4A5kXA1IVLVlPjuxJts_kuNPm5D2qTPV2HWYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تحطم طائرة إسرائيلية خفيفة في منطقة وادي عارة جنوبي حيفا؛ مقتل الطيار وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92319" target="_blank">📅 09:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b61da074c.mp4?token=GAgc6TgTWEW4rz6jesBTxJw_dyvH0wzegGanZxAYuvmGBx5c1Ix5xZwN0bQqaJV4wSvYyGdsjXyxryCFIInbDJnB567FyD3sh0E4kjOXl-EsEvH2_n7dw6jAla-TEkm-3eOTKzmhE3scoEAnLqDKYpUoJ8S4JCqvO9e9DkQp3M2X2rgLK4LqF26QX2jbwVy0XKE0_f8m9_NI6sitfuM8x6JzJXW6wOIEMCHhOR2pk-Cdo9d-T0w9S2Cd8ScyL0_DopnlLo2nKATUZqZDeK3jE_NDxz1Dk_klUmu9iJAf7wTJcpjTFQA0ucIPjP3uS2bOvqTNad0cI799Ce_FzRBHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b61da074c.mp4?token=GAgc6TgTWEW4rz6jesBTxJw_dyvH0wzegGanZxAYuvmGBx5c1Ix5xZwN0bQqaJV4wSvYyGdsjXyxryCFIInbDJnB567FyD3sh0E4kjOXl-EsEvH2_n7dw6jAla-TEkm-3eOTKzmhE3scoEAnLqDKYpUoJ8S4JCqvO9e9DkQp3M2X2rgLK4LqF26QX2jbwVy0XKE0_f8m9_NI6sitfuM8x6JzJXW6wOIEMCHhOR2pk-Cdo9d-T0w9S2Cd8ScyL0_DopnlLo2nKATUZqZDeK3jE_NDxz1Dk_klUmu9iJAf7wTJcpjTFQA0ucIPjP3uS2bOvqTNad0cI799Ce_FzRBHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ثاني يهز مطار تفتناز العسكري في ريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92318" target="_blank">📅 09:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
إنفجار ضخم مجهول وتصاعد أعمدة الدخان من مطار تفتناز العسكري في محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92317" target="_blank">📅 09:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb911b96c5.mp4?token=gbqL_67u59KNCyuDSpLpLjz65hqOuXA95zfEzeuJpmvJYe_u5xPYkYonX6H3JsbtugZ_VbpKQNCEgofoTdgarQMFOQlAbLaJRGKH8AgIg0eDmgAOUcliVUGqAhLVXxRWTRhUnxQNjp_XyVJGVtfMpRbSRSG0ahfxeLpmBwVUY2PWvhWqRt3SK7ZTo-3MUJDHCJrJORyDQ1w9amVH5agfwtgslOXGCKPcI9esO-FuEO3L2J-BykcKAXWsK0CwCFoc6ZV6jmhlvvHu5aaTOG6TpCr7YBJPfJmx5QPfu1ibPzxM4GaPWYhBWBAsiG-SI4Yk74kzZCdW9EdmGXxaZPW2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb911b96c5.mp4?token=gbqL_67u59KNCyuDSpLpLjz65hqOuXA95zfEzeuJpmvJYe_u5xPYkYonX6H3JsbtugZ_VbpKQNCEgofoTdgarQMFOQlAbLaJRGKH8AgIg0eDmgAOUcliVUGqAhLVXxRWTRhUnxQNjp_XyVJGVtfMpRbSRSG0ahfxeLpmBwVUY2PWvhWqRt3SK7ZTo-3MUJDHCJrJORyDQ1w9amVH5agfwtgslOXGCKPcI9esO-FuEO3L2J-BykcKAXWsK0CwCFoc6ZV6jmhlvvHu5aaTOG6TpCr7YBJPfJmx5QPfu1ibPzxM4GaPWYhBWBAsiG-SI4Yk74kzZCdW9EdmGXxaZPW2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إنفجار ضخم مجهول وتصاعد أعمدة الدخان من مطار تفتناز العسكري في محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92316" target="_blank">📅 09:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=eeHfQGSYf33okbZ4R-H0fRxorF-leaXdjxJnsi2XZm3rKTm38A-zDHZ2bbAggTsXdcuRB3lQ7t6RB_Te861rhQwjHJSL_XPU5ggTIgFpopLy5g0Glc-WOKUaokiNu9rver8IPj4Hmpl5hBcm0DM1h3fVlOTBebccSUFaPxyBBcnInGTmYmO01yc85qNKqTTR4a1R2MIc7LZW_IHUrMWtHdx8B-Dt5-ApaFw9KtkwN8-11eJ_hY9gUAk5UbrPppW-ke3rIWWsY_4gh8ikhTMBIErbTzk9yLD4d3R_e_nzc_qTCOEJI5JdkF6883Eubu8ADWWZfGRZvQC_pfjGxYYClw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edffd6bce5.mp4?token=eeHfQGSYf33okbZ4R-H0fRxorF-leaXdjxJnsi2XZm3rKTm38A-zDHZ2bbAggTsXdcuRB3lQ7t6RB_Te861rhQwjHJSL_XPU5ggTIgFpopLy5g0Glc-WOKUaokiNu9rver8IPj4Hmpl5hBcm0DM1h3fVlOTBebccSUFaPxyBBcnInGTmYmO01yc85qNKqTTR4a1R2MIc7LZW_IHUrMWtHdx8B-Dt5-ApaFw9KtkwN8-11eJ_hY9gUAk5UbrPppW-ke3rIWWsY_4gh8ikhTMBIErbTzk9yLD4d3R_e_nzc_qTCOEJI5JdkF6883Eubu8ADWWZfGRZvQC_pfjGxYYClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مستمر لتحشيدات مرتزقة التحالف من قبل القوات المسلحة اليمنية في عدن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92315" target="_blank">📅 04:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=sneXAORIaUffRoNzydobacw2ZFl_2x1MBJNxVcE6Ftc0w3VnzRNb8QQbfIfHTvgKs-tW_GnO_OSnpwIphBqRzsctPTXtQC-GuBB90lwBDd5GV-p6QCZrC7bnfO9t9n2eTW0zF__i9qwjiYhHFzf-J0VWaGYInYwxWX-hKIIXd9sXzeChoM84BAq9MWJEw9RdfbOAZFFVYSjexp3BHygp6tOurRUdaFhjggTb_-R-RcR0oTw9nVoGGrZaRtwo5H8ybKzlJVl4O-P7V_vhxky4uV3n0-CT0gTTa9nSxh_9tcf3nS2ih728E-dKgNRVrWhpIBELsK7Q-RMHrBKASOSKwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39cddb5e2.mp4?token=sneXAORIaUffRoNzydobacw2ZFl_2x1MBJNxVcE6Ftc0w3VnzRNb8QQbfIfHTvgKs-tW_GnO_OSnpwIphBqRzsctPTXtQC-GuBB90lwBDd5GV-p6QCZrC7bnfO9t9n2eTW0zF__i9qwjiYhHFzf-J0VWaGYInYwxWX-hKIIXd9sXzeChoM84BAq9MWJEw9RdfbOAZFFVYSjexp3BHygp6tOurRUdaFhjggTb_-R-RcR0oTw9nVoGGrZaRtwo5H8ybKzlJVl4O-P7V_vhxky4uV3n0-CT0gTTa9nSxh_9tcf3nS2ih728E-dKgNRVrWhpIBELsK7Q-RMHrBKASOSKwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللحظات الاولى لاستهداف مرتزقة قوات التحالف في في عدن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92314" target="_blank">📅 04:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">إعلام أجنبي:أرسلت الولايات المتحدة مؤخراً بطاريتين إضافيتين من صواريخ "باتريوت" لحماية منشآت حيوية للنفط والغاز في كل من السعودية وقطر، وذلك في ظل احتمالية شن ضربات أمريكية جديدة ضد إيران.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92313" target="_blank">📅 04:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=LmsEvWzmmUCtCfV6ShpxHbcYYmHv1pNl45rGlIWAWwVLOj6VleNTMRl9DQw8EUQ-xYAHw0XzHlwVI8JjCqa9urgizHREphoqDMQ05kPC2VHiXVtBw6OJLQRiADyqJcVmLIj0MmhiNuMTWkQKqURDxvPt4Xk6FCXEawrnYIkMe9qHEj4gJMi4l7_6ecEaW5_QcLubJ-2AK1gofaJDR0CcFSlNlvLR_nutoFnIcbVSA7HxCm2-Dzj8jBBTAaEw5n66yAiJCF8Lx5y0CUB4aOUfzSKOIAaaU3I9olHn1gkfGTnQo_oMLaJ-24jBPbwT3M0rwHWB47XGHjj48iaqQl9EIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f52287c44.mp4?token=LmsEvWzmmUCtCfV6ShpxHbcYYmHv1pNl45rGlIWAWwVLOj6VleNTMRl9DQw8EUQ-xYAHw0XzHlwVI8JjCqa9urgizHREphoqDMQ05kPC2VHiXVtBw6OJLQRiADyqJcVmLIj0MmhiNuMTWkQKqURDxvPt4Xk6FCXEawrnYIkMe9qHEj4gJMi4l7_6ecEaW5_QcLubJ-2AK1gofaJDR0CcFSlNlvLR_nutoFnIcbVSA7HxCm2-Dzj8jBBTAaEw5n66yAiJCF8Lx5y0CUB4aOUfzSKOIAaaU3I9olHn1gkfGTnQo_oMLaJ-24jBPbwT3M0rwHWB47XGHjj48iaqQl9EIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92312" target="_blank">📅 04:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قوات التحالف السعودية تعلن اعتراض صاروخ باليستي أطلقه انصار الله باتجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92311" target="_blank">📅 03:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=vwA9Ng4jEsRvK7mHhddolzy29nipe9-Tq5ANLyQ1wXzQ8NLsg2y5i8l3KSjkPB2lAd7S108S7s-JI7NBgmfeDRBfeeRPLvPEPh_Pjgea7W_iH1ewi9d2f9Wt67sPV6cUJrKDEjOHPbeK9XqVmQmw9xbu1nCqnDd76qQeyQohZhENNKm6X9wnT0c6M77nO7If9gnpuyPyOt54IcXR1kH3E-Ju49oxvyndPYvcJobMQ8Irdou-qavVmh8hdRq4l7Shi25dXXliD4W30kqUKPdcP1YuRti_WIupin0macljy62D5-PnNPB0DPYA_1ZvtzqTo-S_59UTm-Ga5nteVrnccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8b51349.mp4?token=vwA9Ng4jEsRvK7mHhddolzy29nipe9-Tq5ANLyQ1wXzQ8NLsg2y5i8l3KSjkPB2lAd7S108S7s-JI7NBgmfeDRBfeeRPLvPEPh_Pjgea7W_iH1ewi9d2f9Wt67sPV6cUJrKDEjOHPbeK9XqVmQmw9xbu1nCqnDd76qQeyQohZhENNKm6X9wnT0c6M77nO7If9gnpuyPyOt54IcXR1kH3E-Ju49oxvyndPYvcJobMQ8Irdou-qavVmh8hdRq4l7Shi25dXXliD4W30kqUKPdcP1YuRti_WIupin0macljy62D5-PnNPB0DPYA_1ZvtzqTo-S_59UTm-Ga5nteVrnccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92310" target="_blank">📅 03:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=I7KLKnfvvnQ7_lK_NNjzaP_0tZkozWHv4JzUqt1Xc-qV3Q9odH6EpQpMWlnzmdgp4MkRpQF0QsFpxVa-ByqMHShWxzv3eOgfjiANlA4mnnX7X9ccb4c9j8qDV1X9aQY0xDz5LzMNDxt82P5jeD0ql1Lay6Wa8jT6FmA7RMc7UX3Fty8cEfxxKTRVRNn7VravBETnUHIySEGwWXnRhDsg0RaXKgbTrsBrGwKVOp3ChDb2wlGpnAXhD7sz0_9JoBnQ5VinyJdYzW1VwJLwUTIzqWqVwBO-iW5AFf-wB-CnXv5H7pBOenmjDjubN9h_a3UDp5SXigVRdCU7E1oR3R7QuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47ccb5bca.mp4?token=I7KLKnfvvnQ7_lK_NNjzaP_0tZkozWHv4JzUqt1Xc-qV3Q9odH6EpQpMWlnzmdgp4MkRpQF0QsFpxVa-ByqMHShWxzv3eOgfjiANlA4mnnX7X9ccb4c9j8qDV1X9aQY0xDz5LzMNDxt82P5jeD0ql1Lay6Wa8jT6FmA7RMc7UX3Fty8cEfxxKTRVRNn7VravBETnUHIySEGwWXnRhDsg0RaXKgbTrsBrGwKVOp3ChDb2wlGpnAXhD7sz0_9JoBnQ5VinyJdYzW1VwJLwUTIzqWqVwBO-iW5AFf-wB-CnXv5H7pBOenmjDjubN9h_a3UDp5SXigVRdCU7E1oR3R7QuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات مستمرة داخل معسكر قوات المرتزقة السعودية في عدن</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92309" target="_blank">📅 03:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=UR8SetR2cIrtWOpgqAlrAxu1iuPzZ61kz2GnEZbKCYGpWGc5xuBkYtI6-i4F_D3eM7byQahNhh5ZfEvBecdD3KvY--fohTyDmwjdwIgyQK4FZbOAk7uVb67jJIaL2x8oZdYyOMcIjMtVcDBO6zKLrefgWXrxlu8jedcFO2SYICa9m_qXJTTh53arMbduvmGMEj5Aa6LO9_Jo2yqgw-hdGm13YMCpp83nrI6lby_w--Qh2KiiCYjeDtjMxd6b_dtxcbpaYCAFfy4O9AbIGulm76rSNOr57DQ4ENZ2mUF9XPnpcClncqNJbvWnMvIPdNfi_sabxexUH8K2_FmbwqKdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a01896a2.mp4?token=UR8SetR2cIrtWOpgqAlrAxu1iuPzZ61kz2GnEZbKCYGpWGc5xuBkYtI6-i4F_D3eM7byQahNhh5ZfEvBecdD3KvY--fohTyDmwjdwIgyQK4FZbOAk7uVb67jJIaL2x8oZdYyOMcIjMtVcDBO6zKLrefgWXrxlu8jedcFO2SYICa9m_qXJTTh53arMbduvmGMEj5Aa6LO9_Jo2yqgw-hdGm13YMCpp83nrI6lby_w--Qh2KiiCYjeDtjMxd6b_dtxcbpaYCAFfy4O9AbIGulm76rSNOr57DQ4ENZ2mUF9XPnpcClncqNJbvWnMvIPdNfi_sabxexUH8K2_FmbwqKdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف القوات المسلحة اليمنية لمواقع مرتزقة التحالف السعودي في عدن</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92307" target="_blank">📅 03:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
مشاهد أخرى من الحرم المكي تُظهر إبعاد الحجاج عن شخص يُشتبه بحيازته مواد متفجرة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92306" target="_blank">📅 02:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb7qt4bSlWfQe7TUmvwzTiz7T5d-H0Cb6RViuCDuUxH8a_Ga6Z1Fc6anwRChoilc_I37JbDx-kdychPqeZ70aK2_Nxz0UFftLuFEkkpdbM_8n_M7Hd5jtmQzWdsWH9B2WJ3LUHsiNHu3qEK2XiCwtxvUJGjxDJzSURZn2_TDKfmomgtQ5_vox_uAgupnQNstjT6phrGFHvd3HRlA4vqzlKJ7rtNbSL9gaLM_75078ifzIWrWwrhRLfiMWmBYEIfcCRpo17wxslSR7cIxVi9fXzq1MuxploK-mSFFAxcTOqwT3eq7nmjj_85uhLaljVtE5nY11j1RWO1-LrtVtPOjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد الرياض،توقف حركة الرحلات الجوية في الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92305" target="_blank">📅 02:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=fLPRVvqPw3LtmXTKOiHDefeVBF9Q4aSR-fwlE98oBOm3irz7S8ycgd2n7ZUavM-hXuOf2aggvQ9UyHiGotjtlhcckdg8pL9_t-CVvaH4LpX5AqFiEqrJHX1C7wejBmwd6aNmbNQpigMw1fxCCX2EBxcu2Xh5gCpHe3mwE4UT_lv9Kr4EyYZ6mUtU_L6sS7qe26rxDdGyMmxZ-8-FfSEH3nPurp9nfRgvFV9aCl-wvUFVl22PZIzw0pCy8CI9tQDxIadfWxZIW3QRlVlOatpRwmeOjrxLK01BzR85z479YTFzVm8aEMFycmUI3xRjiTwKcGrNT0x4Q98OtrwvLcl5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ec9b5c12.mp4?token=fLPRVvqPw3LtmXTKOiHDefeVBF9Q4aSR-fwlE98oBOm3irz7S8ycgd2n7ZUavM-hXuOf2aggvQ9UyHiGotjtlhcckdg8pL9_t-CVvaH4LpX5AqFiEqrJHX1C7wejBmwd6aNmbNQpigMw1fxCCX2EBxcu2Xh5gCpHe3mwE4UT_lv9Kr4EyYZ6mUtU_L6sS7qe26rxDdGyMmxZ-8-FfSEH3nPurp9nfRgvFV9aCl-wvUFVl22PZIzw0pCy8CI9tQDxIadfWxZIW3QRlVlOatpRwmeOjrxLK01BzR85z479YTFzVm8aEMFycmUI3xRjiTwKcGrNT0x4Q98OtrwvLcl5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:  إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92304" target="_blank">📅 01:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=YE_gy8OguvyyLcdVZDMg4SKfgLvPjOOHUIMOqxmY1NKk7DXgCsu3aeXAzv-ScpPdJKcPB8jFW1bim6zXJl_oWytkPxaU4hxoOdat7RF4me58VRf8FFCASC_y8AiH-vMI-Ng7ClFCt4T3IOaXezvVg71pvaPoK6ToEd4naaDys5HNpnxPzvH1sfYY2dZMDUtnMU8__PP1p0cxwgV3P84hZwSyQpkJ_UR0to8AQSO0_aKVc91dZET-WIQ_7xV0rePZTl2uoZJcfJvLTgkEgTCJWOEvCqwf2TQ1So_ZcA0k60H_lfPMqFzhgd6jRiHMp7Gwt8u4KTvuD0EBJ3R1SPwhVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0492e588.mp4?token=YE_gy8OguvyyLcdVZDMg4SKfgLvPjOOHUIMOqxmY1NKk7DXgCsu3aeXAzv-ScpPdJKcPB8jFW1bim6zXJl_oWytkPxaU4hxoOdat7RF4me58VRf8FFCASC_y8AiH-vMI-Ng7ClFCt4T3IOaXezvVg71pvaPoK6ToEd4naaDys5HNpnxPzvH1sfYY2dZMDUtnMU8__PP1p0cxwgV3P84hZwSyQpkJ_UR0to8AQSO0_aKVc91dZET-WIQ_7xV0rePZTl2uoZJcfJvLTgkEgTCJWOEvCqwf2TQ1So_ZcA0k60H_lfPMqFzhgd6jRiHMp7Gwt8u4KTvuD0EBJ3R1SPwhVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن إيران:
إيران مستعدة للاستسلام. سنحقق الفوز بسهولة بالغة في الوقت الراهن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92303" target="_blank">📅 01:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=N89h7Ekr1HGJw-bLjTB_EEirOKosn8a6PYsPAg9YaZTILl5BYDZ-63NHfgdsLO4V2GxjtpkJq3bAUmCP9uMsGW04CPFnGJ9hr4OUQlIm5X4g_oxU3JzvZHbrxKYcA3LnsZX2bmnWP14KjFn0paXLkc754X6HVatKWk7CIbpTu9DUubNrgT9m_X_hHWDCTDmBNZFJU3BYSU2jH29q7CbY3QX3ZCyWbf2JZvS_wAEVs1zIgWIv0G-IjefsKHFUnej0gPhgzhnrxbDcCzj-5PqBoyj-GYCe4lvrpb5UMObCqyI1YAB-ZikLT1hSS-jwoN8vJaacw9DYgt3ae5B-6hcHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a92eaf392.mp4?token=N89h7Ekr1HGJw-bLjTB_EEirOKosn8a6PYsPAg9YaZTILl5BYDZ-63NHfgdsLO4V2GxjtpkJq3bAUmCP9uMsGW04CPFnGJ9hr4OUQlIm5X4g_oxU3JzvZHbrxKYcA3LnsZX2bmnWP14KjFn0paXLkc754X6HVatKWk7CIbpTu9DUubNrgT9m_X_hHWDCTDmBNZFJU3BYSU2jH29q7CbY3QX3ZCyWbf2JZvS_wAEVs1zIgWIv0G-IjefsKHFUnej0gPhgzhnrxbDcCzj-5PqBoyj-GYCe4lvrpb5UMObCqyI1YAB-ZikLT1hSS-jwoN8vJaacw9DYgt3ae5B-6hcHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
بالفيديو المتداول من حالة الذعر التي اصابة الحجاج بعد الانباء عن امساك بشخص يحمل مواد متفجرة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/92302" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92301" target="_blank">📅 00:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇪🇬
مصر تعلن دبلوماسيًا إثيوبيًا "شخصًا غير مرغوب فيه"، وتأمر بمغادرته في غضون 48 ساعة</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92300" target="_blank">📅 00:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=PDHVdL8OyrWUdiL319rAE5rZi593vyVTN_qjc2e8WUcZknpUnbIvIbdjWK_uWoOWtdEyntNJZl6rB4XmyIU6051BcajfHVSvJM0jqAXb7mpm3xZxFU95ZvlKChNKGp6MSTHDhtvWAbDSFndJv3PGmdGEKDyKPcsTSmdOD8Yp5rtUPUNwd2Wh4nBRVqO8LECeqlxF9dzp0jYzda2KU4-jj30wu3m1In0bNKpM0OfZ8E204fad2xHZEu3Q4YGBwrj2ij_EyAU0ZLDV0Uk8n3rcTHZznYeFpxZOQgAWQAJjBn67NcQPb-P_jUwQuFFJXwFHVBlc7G-FeKo6flB0nVNKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b57ca628.mp4?token=PDHVdL8OyrWUdiL319rAE5rZi593vyVTN_qjc2e8WUcZknpUnbIvIbdjWK_uWoOWtdEyntNJZl6rB4XmyIU6051BcajfHVSvJM0jqAXb7mpm3xZxFU95ZvlKChNKGp6MSTHDhtvWAbDSFndJv3PGmdGEKDyKPcsTSmdOD8Yp5rtUPUNwd2Wh4nBRVqO8LECeqlxF9dzp0jYzda2KU4-jj30wu3m1In0bNKpM0OfZ8E204fad2xHZEu3Q4YGBwrj2ij_EyAU0ZLDV0Uk8n3rcTHZznYeFpxZOQgAWQAJjBn67NcQPb-P_jUwQuFFJXwFHVBlc7G-FeKo6flB0nVNKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السلطات السعودية تلقي القبض على شخص  يحمل مواد متفجرة داخل الحرم المكي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92299" target="_blank">📅 00:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=eyNzZRk_q92c_X5m4TDdOXECBm4RIC52eFR8JdQ-TuQ2KR85xxe6UExXkMdKM9N2U5eIutfmQfr8LBBfdY8bSKZIUrdS8MQFjhxAFpeChKr3N82VqcE1Fi8j2HsG2f6RPaB6pAEde3cK_ma-hOqPbjfL6P094OXcdY2-cU8rSgm3uAFwRrQe_fKNqmKBMCBd1i6oUQe9K5a_z2fdloTleWWn2zu5NdRKix1r8imBRniwmX52miZkgv-O9r5KT7PJ2yXYe0bq9UkcOejgA8TnAs6PFaWMVZmtEnXXtQZi8yImqwornWMhK9bbmG5H5TWqHO6_-3awl9nQDAjQ1LqDWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0add1fe8d9.mp4?token=eyNzZRk_q92c_X5m4TDdOXECBm4RIC52eFR8JdQ-TuQ2KR85xxe6UExXkMdKM9N2U5eIutfmQfr8LBBfdY8bSKZIUrdS8MQFjhxAFpeChKr3N82VqcE1Fi8j2HsG2f6RPaB6pAEde3cK_ma-hOqPbjfL6P094OXcdY2-cU8rSgm3uAFwRrQe_fKNqmKBMCBd1i6oUQe9K5a_z2fdloTleWWn2zu5NdRKix1r8imBRniwmX52miZkgv-O9r5KT7PJ2yXYe0bq9UkcOejgA8TnAs6PFaWMVZmtEnXXtQZi8yImqwornWMhK9bbmG5H5TWqHO6_-3awl9nQDAjQ1LqDWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92298" target="_blank">📅 00:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇸🇦
السعودية تسمح بدخول انتحاري داخل الحرم المكي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92297" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇸🇦
🇾🇪
العدوان السعودي في وسط الاحياء المدنية بالعاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92296" target="_blank">📅 00:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
‏إيران تعرض السماح لمفتشي الطاقة النووية بالدخول في حال تخفيف العقوبات.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92295" target="_blank">📅 00:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8GSvCZ-9UzRDwM9gQH1wveXrb0X7Ly2pBwzCI3zAP9nKYpncLHLJXabfq_qQui0hRDPMCTRXNLxNHB34xso89419XtZxd0LbDkSOIw4IjvGSLqVH8aMVGMUyd_KRvgNGVXBuqlJ6mChNmTDfe15Sh12y2WbBgnM519PdvjBWXktDnE_iyfEAOt8fGAhnJWywzrmYf20h9ddIyoBcbdkC6z2FvReWgcbX_xfYEdTKDYJ2siNEUj6u1SUrILARYPXrZl71HpMt1VOnUeLd6szXVgfUjT51ZohpgULkw-NnQMdgLA-cvXCk9-l9PKAKH3hEfh_b6IZDVs_oc7yp-BNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
من العدوان السعودي الذي استهدف عاصمة اليمن صنعاء.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92294" target="_blank">📅 00:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75906a072.mp4?token=fGriO14fqztplMq7KYgSFlkkV6niC_rLLt7_efTb0G7mX7m_GwzsuvnXbPv8yYy656pMaEJUmUKQ1xtmew6cLFEv95dJVTvMouZD_9b7DEH3LaQOwyc3zDXINF6JM63AYqVn1eWoX0eYBmHTFUHvyiZ7UdEfnQsC_587PargiVcnHiGwlbnjQsAobw8wpswpHgY8mDjMhSnPjlrqPPQTj4ZJWbX2pZzMb5Q2coDvcecRrzB0U4UKHjQrMgF80K7fpEaQxSUWtHIK5x3xZ6X332BZ9JFWqSa3kd6CJEpV1-7z4pU6TYPDMoywqlcD5JZwOMd953EZmwDKOrS3IZoicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75906a072.mp4?token=fGriO14fqztplMq7KYgSFlkkV6niC_rLLt7_efTb0G7mX7m_GwzsuvnXbPv8yYy656pMaEJUmUKQ1xtmew6cLFEv95dJVTvMouZD_9b7DEH3LaQOwyc3zDXINF6JM63AYqVn1eWoX0eYBmHTFUHvyiZ7UdEfnQsC_587PargiVcnHiGwlbnjQsAobw8wpswpHgY8mDjMhSnPjlrqPPQTj4ZJWbX2pZzMb5Q2coDvcecRrzB0U4UKHjQrMgF80K7fpEaQxSUWtHIK5x3xZ6X332BZ9JFWqSa3kd6CJEpV1-7z4pU6TYPDMoywqlcD5JZwOMd953EZmwDKOrS3IZoicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92293" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-7Xix1FbsM9gle3LDWIJU035xfzqHyW9_ttKU1bGwkToUhimz48Rts-ZgX7ykejCrY5zB713F0SmYRrobLI2buCvTk7ON6ZEMnbbfDAPsAZvcXd_uMa0Z-zbFK7TjKiD7KcvYQUWzHH_5ApWa47-Tg7tGeoeLYd35wF0bubkLPIElW7ssksTYgcpDUG7uW5noaIJjd765VvWI9bgBx0ul6BhZ9BYItnKpwzhHLExOJRKpTPeuMpWvNuNS8x_ylJh0HS50JEHQgupmoe5ZINmELfjZuK1feE1uczj7jKnMnBMpgHErRVq-6FsCn7uoDJZ3DR-Jgnr5QpVH178wtgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على صنعاء الان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92292" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doyFQ17YVPcgEOVSZkeZ-F1vFpyrh_3f9Jx9Xt0kFHll-8yx8FyNKA4PSW4FhXeQ8VKcftE7gWEcQW-xd9v_q10QkrH9iewY7IWBI3Q7Z7II3QgjQ1O-Anrl5cYK9WWOYAC14O1sSbEBN6VyoLvPQ9y4f3wdaZ6qPLC-rOiXPZaw3whoQPtV1cxGg-BtXgrr7yJvx9J06RdpyqsyhpW1Untexm96WSPx0jV-f8osJ1zJ-l3kxi7zdioW3ZxBPDAlRfLFG7VQxnBV2d74SW7P7D2kOL_d7gn1pzO3qmiSy9AdurjfqoWrj1xJTqDGA6v6pyVVm3_OTjXKoBLX98qJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعرض سفينة في مضيق هرمز لإستهداف بصاروخ من قبل بحرية الحرس الثوري واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92291" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9xqHdiwQz7ArrMzOjC-22T3KarqRvbY3BdD1s5eg-kEyO9w6UWjYcNlqzyU9L23NToY1iwxCAoIAKeGIyVyPIsY2xP_Fh7YY66DJHa7Dqi76LUVK_MnetUqih8altKpkTo8A5meghMXC9yzFt5RGGTzLhBmAP7lNxHhgcMrV69qXhOYDS-N6M6pHz0Ru9My1eIpGpr7VO4lPZch2RnPwX2RPVis9h3Br-gIzqwSSebY-eeSlyPuYXXd9KXOMlOnEGfKrCzclGWPXQuX0QTHL0dX7rqepk5wQoMaAvkNSIYAWIEwu-9JwzW_YCRSvxzaXZGpQIJltvH5YCYwnLLbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
انفجارات اخرى في جازان نتيجة هجوم بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92290" target="_blank">📅 23:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇦
🇾🇪
صاروخين تستهدف جازان وخميس مشيط.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92289" target="_blank">📅 23:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUdhk7UY0zSWY2eQdUjLtcL0VAad9iU-8_PEXAhactrL2PJeCpjxonPwcPCf2DOMmW1ROtLUTnbsgArwcv7cYAURFt0zsFXAam2BMsqsMMmBvBaQOgS_CRthlvjdAElNY_izUtv1FGKE2CMyBuhOeXt1MnDreJP82QaJuc-dpNHb5qqaUmwhd1YqmIKeVSiK2WMG5wioazMWxR0ykp9chNDNeRwXHhCLTVlNPppaOIwz9TrXkeI8ohRjOd4L2rEzq6zSfv2SS9PyeKztwM7j6rCHKzyi8zaLsqhD678Cx7SODhhRJeV-dCdeffwGYOY7SEHb9XXwjU1tmrbFHUWU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية بشأن القيود المفروضة على حركة الطيران بين إيران والعراق
:
تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة الإجراءات والتحركات غيرء القانونية واللاإنسانية التي تقوم بها حكومة الولايات المتحدة لعرقلة التجارة والنقل الجوي الإيراني مع الدول الأخرى من خلال تطبيق عقوبات أمريكية غير قانونية خارج حدودها، وتؤكد أن هذه الإجراءات لا تتعارض فقط مع المبادئ الأساسية لميثاق الأمم المتحدة والقانون الدولي، ولا سيما مبدأ احترام السيادة الوطنية للدول، وانتهاك المعايير الأساسية لحقوق الإنسان، بل تشكل أيضاً مؤامرة خطيرة لتقويض العلاقات الودية بين الدول، وخاصة بين الدول المتجاورة.
وفي هذا الصدد، تُذكّر وزارة الخارجية بالروابط التاريخية والدينية والثقافية والشعبية العميقة التي تجمع بين إيران والعراق، وتُثمّن علاقات الأخوة وحسن الجوار بين الجمهورية الإسلامية الإيرانية وجمهورية العراق، وتعتبر القيود المفروضة على حركة الطيران المدني بين إيران والعراق منافية للمصالح والمنافع المشتركة للبلدين.
تتجاوز العلاقات الإيرانية العراقية العلاقاتث التقليدية بين البلدين الجارين، إذ تقوم على روابط شعبية عميقة ومصالح مشتركة في مختلف المجالات. وتتطلب حركة ملايين المواطنين الإيرانيين والعراقيين لأغراض اقتصادية وتجارية، وأداء فريضة الحج إلى الأماكن المقدسة، والسياحة، والتعليم، والعلاج، إدارة قضايا النقل والاتصالات بين البلدين بنهج مستقل ومسؤول واستشرافي قائم على المصالح المشتركة.
إن القيود المفروضة على حركة الطيران بين البلدين، بالإضافة إلى تسببها في مشاكل خطيرة لمئات الآلاف من المسافرين والحجاج والمرضى والطلاب والناشطين الاقتصاديين من كلا البلدين، تتعارض بشكل واضح مع طبيعة العلاقات الاستراتيجية وعلاقات حسن الجوار بين إيران والعراق.
...
🔹
تدعو الجمهورية الإسلامية الإيرانية، مع احترامها للسيادة الوطنية لجمهورية العراق، إلى اتخاذ القرارات المناسبة في مواجهة الإرهاب الاقتصادي والتحريض من جانب الولايات المتحدة، لرفع القيود وعودة رحلات الخطوط الجوية بين البلدين إلى وضعها الطبيعي بما يتماشى مع مصالح البلدين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92288" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
تعرض سفينة في مضيق هرمز لإستهداف بصاروخ من قبل بحرية الحرس الثوري واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92287" target="_blank">📅 22:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن استهداف خميس مشيط باربع مسيرات من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92286" target="_blank">📅 22:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن استهداف خميس مشيط باربع مسيرات من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92285" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب، رداً على سؤال حول ما إذا كانت الولايات المتحدة سترد في حال ثبت تورط إيران في الهجوم على الطائرة: ‏"سيتعرضون لضربة قوية جداً، لا تقلقوا."</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92284" target="_blank">📅 22:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92282">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
‏إيران تعرض السماح لمفتشي الطاقة النووية بالدخول في حال تخفيف العقوبات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92282" target="_blank">📅 22:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92281">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPOJqE8UTbb7lj9P2d3ohTV_BHmVzByf26dI0R46G2dlcbf9RK4gS87tKU7rdi9B5bDwoXAYsHN3OIMTF8mDoRpbdHTkrrFVz0LeM-aEhtdw5PKzPVrt7bOCgzqUWgpb-KhtgTR6VzajSZifYf3Rpa0dUnWBCL6MMtRN1GNz02UpjAu1hVQfxTSKjzeABQTJbrd8Q0lBaJAZkQ_pYkuk89qvMkNRjvw7z4rjLoTKqxrRcV1Ecckg_lM2-WZHcV4BD1I5NIRV8QqB37VSYCSIIb10eTJ8Of4aPmy3qy8qEMdwu78uUkVkozckIVeEnfWy3oR1_O261B-4tlG04zqcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تتجاوز 101 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92281" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92280">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29f31a6f6.mp4?token=jYe3l8PTC7uRKzeoXna7HTHHPAYO2TF7VYuZmezIDdMu3Q4dip9l7m81UUWeyVAmJA7Th_v-Pr_jwzxtr3pn_BXjeUqCFBKMzpNiZ3u_Z738bLUuQGzEEdkKsov_tWLYy1PYuQ18lF6968LQZQx3mCq594vrhm4t7R6H9jK8pK74R6hGU3ZoDRI8o_wifSUcMJ71-Wo55t8rj8OATicX69ftgq4GrurI6bTEKx-7EjpiFCG1KWFg9CZDfGVuSGrtObmytObOERESqvF9N7cvcgJE1rL3IdETyS8qXdeNgXceBhqesfcPW5q90WaLketBIEXX1ETqsDdSV7kr6I2InW4rwt9a2ERbOIfjetIzMf0FyUCGTZbTCNukUw0GDrPRdodsKdsIpCPQzBghc-6Ks10R-WTfCTvFuQJ7nidR-rI068bbyqJQBdTzRb483pAVevThKzdgtHe6EAL7SegJyZS1FcA7bRv6nkk69eZPO-PXsJL6O8Vb_j9cUgnArWSRRQ0cWeLFlsuopIeH3vUf2rYkxsprEJBdnln1qfcsnRns0LeUVuUhrs8j1IL9llYXa-D7AT75DQV6Ut2Tv0f61Hke13GDqFPLz-bJYBOIcQHE24-8K0Dfm5gHsIzDuw7unxxrRk5IXxCY0-Tdu8Zgdmh9Tu7wrnpZQGa0bJbT_L4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29f31a6f6.mp4?token=jYe3l8PTC7uRKzeoXna7HTHHPAYO2TF7VYuZmezIDdMu3Q4dip9l7m81UUWeyVAmJA7Th_v-Pr_jwzxtr3pn_BXjeUqCFBKMzpNiZ3u_Z738bLUuQGzEEdkKsov_tWLYy1PYuQ18lF6968LQZQx3mCq594vrhm4t7R6H9jK8pK74R6hGU3ZoDRI8o_wifSUcMJ71-Wo55t8rj8OATicX69ftgq4GrurI6bTEKx-7EjpiFCG1KWFg9CZDfGVuSGrtObmytObOERESqvF9N7cvcgJE1rL3IdETyS8qXdeNgXceBhqesfcPW5q90WaLketBIEXX1ETqsDdSV7kr6I2InW4rwt9a2ERbOIfjetIzMf0FyUCGTZbTCNukUw0GDrPRdodsKdsIpCPQzBghc-6Ks10R-WTfCTvFuQJ7nidR-rI068bbyqJQBdTzRb483pAVevThKzdgtHe6EAL7SegJyZS1FcA7bRv6nkk69eZPO-PXsJL6O8Vb_j9cUgnArWSRRQ0cWeLFlsuopIeH3vUf2rYkxsprEJBdnln1qfcsnRns0LeUVuUhrs8j1IL9llYXa-D7AT75DQV6Ut2Tv0f61Hke13GDqFPLz-bJYBOIcQHE24-8K0Dfm5gHsIzDuw7unxxrRk5IXxCY0-Tdu8Zgdmh9Tu7wrnpZQGa0bJbT_L4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من ساحة التحرير وسط العاصمة العراقية بغداد، حيث تصطف النعوش الرمزية لشهداء الحشد الشعبي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92280" target="_blank">📅 21:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92279">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇸🇦
‏
الداخلية السعودية:
قائد الطائرة ومساعده غادرا المملكة متجهين إلى أبوظبي صباح اليوم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92279" target="_blank">📅 21:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92278">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5a-lvORcjvFOGmxRVC4ZTTaMPHWcEXi2gtDg9ANWwx8fHvAQKHXmq5qCrPA-aExMkkRKx98_GT05qpFtDV0YH5Bhm7dQKM9yHIj1MBhVYC7h4geMjslpgMjBcR0-U6HIWrbLsjvHUBGbCtdJSGUXeXQ7o74WqJOJthrmL6fFMVXlG34niQqDiRJaPwqb79fsjEaLXIyVfehN8cJK6oyHbj8ets5dxUVT_ojHLy018FXdtCekkmR8Xl2_bxZsLWAv9dq-E0mP_Yfeo_8haK-n8ettvPRcrAELN55xd4aH0bcx9qTHybQgMkEQpzTBChpZyT2JcJymFi66fxKuezgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: ذكرت، عدة مرات، أن الأمر سيستغرق 4-6 أسابيع للتخلص من التهديد النووي الإيراني، وفعلت ذلك في ليلة واحدة! بقية الوقت هو فقط للتأكد من بقائه على هذا النحو.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92278" target="_blank">📅 21:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92277">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da0c14d8e.mp4?token=l9ACZF8WZTmr5JhkTr1TZG_fQ19Omk2mB4GT-cB6S7k3dazHOftv9_Qv31tQBlGSi3YVhg3R0qIB4oDqEDWeISSveac2Hqahy48NBidqfipwJPIZuXiCZ2qDaYNei1P8_Nr65xiX9IErAQL0SgjQtvdkKzvGAN-BaBCQPtMJam2MK04PFHCkN7XqvR5rYyH1wCNYxWeIXu5LD2WbzMmGeHUVPRbQsdpk6Ifqc2g2d-atZKBuBuTU0f_ZUUGrvV0Hfc0xtNE5ViWZ2UKTrPf0o2QmQt6LqkDb4v07NLfy87iYBB2F9p5QLJIZSCFTauo9CWvyqMTT1-nDpaH1DEbQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da0c14d8e.mp4?token=l9ACZF8WZTmr5JhkTr1TZG_fQ19Omk2mB4GT-cB6S7k3dazHOftv9_Qv31tQBlGSi3YVhg3R0qIB4oDqEDWeISSveac2Hqahy48NBidqfipwJPIZuXiCZ2qDaYNei1P8_Nr65xiX9IErAQL0SgjQtvdkKzvGAN-BaBCQPtMJam2MK04PFHCkN7XqvR5rYyH1wCNYxWeIXu5LD2WbzMmGeHUVPRbQsdpk6Ifqc2g2d-atZKBuBuTU0f_ZUUGrvV0Hfc0xtNE5ViWZ2UKTrPf0o2QmQt6LqkDb4v07NLfy87iYBB2F9p5QLJIZSCFTauo9CWvyqMTT1-nDpaH1DEbQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات متواصلة في موقع الانفجار واللسنة اللهب ترتفع.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92277" target="_blank">📅 21:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92276">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
عمليات قنص نوعية لوحدة القناصة في جبهات جيزان تستهدف تحشيدات العدو السعودي من يمنيين وسودانيين - 01 أكتوبر 2026م.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92276" target="_blank">📅 21:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع: ‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 47 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية من شبكات اتصالات ومدارس وغيرها فى محافظات تعز وصعدة والجوف من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من جيزان.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1256 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92275" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فيلسوف السياسة  بمناسبة الذكرى الأربعين لاستشهاد الدكتور علي لاريجاني، لنتعرّف عليه أكثر  #نسل_الشجعان  انتاج نايا على التلغرام وفاء لخادم بنده .</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92274" target="_blank">📅 21:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rw3Ohz7uGOrqNtsYmufhYfkVwg2vOuzGyQ2hdNVjtiPqPKStfb5YTDHVsWMMQ2hd6PO5PXSPQPFJKrMkhzuIlDqdD84TQuGWFdYDNxS52oP8lXT1rqz1x8seA2hF5OdCRT7gw3JJD1p0UnOp20VrP8ZnkL63-Pbq_Ly8Zs6k3qRZKviMgwAAcSHK770DogupVZ9sgva6Sp6Gdxm716Et_Hv971lhPx4mNjap-vhyC7mqdDACGv1U9KK-4GKdnBfB2pEZuGW_gmuF69iBZrWzsLo9BKzwdh9btiYydKV-DgdYLJWR-zjYML0-9su1uBM_Hq_1cfJxZ1N65YuaFxxYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWaL5WdtrC3yxs8AOe0fcDoq_0AWAVGdANUakVxukhgxdDqoVrEtyHzYttWqwFuDe3txsSxKCMHKMu0W2zBCATwKnIBhbrjbN--m_EfjYIaQVfxJNMk9gLT7sUl4mgudZXvGwTUdlTn6oV5TgfEfh-ipPUJRQkk_sqpdryKb_3GCRhLJmjaks1cel2YwkOpL31PwriyA6O4KAq-2CLCqdpqGdByLZCINz53mXpYPSo78pMRQN-Vcrdp2GPjRVyfnZ8OuvzBvqw5g6Fc6uZr-DqizK8hQTPSRLj98XEOaei7WWdZZL1GtLWEjtqnV8H3Bf9VAFJCZJh0kDuUbMNIW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szDohnN13_1T4f9NQMKbFsbZCFwdrWAwNVo96-ySXnOwky868Wx7eI7egBN0KeudCQnkD2ExK1W4ll5DBTWbnwlx0cNYDvoFJChqY10yp005DoWYYsUo8E8r0mNMvCB-4tOYymgAQLzmBdnIP8kk8ojSD-vwPlogvVChb_h0v4qd0l9qRhKqhZLGSSxqbkS4pBSRL_1rWaSR9V9IENIbAsAoaZGPC6VOUMtFicy2acN8jjM0xhzIkQqETpbLIGsaZVEhWqrNcCKk5BhQ7rzjGZfbHDL2XRQ5UnlDu4RRWh_qEfF5Q2ke9XRevomnm6bXgvLQAgkUPZRiK_iCjy-cqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNSbYX987m8q-hBDwBKBleKT0N9IuwJpDmzy12z33qCb6azvtZ_3PRownT7w-TuYR29YdXcfJKQIp0h8-ard7nQ2jfmkVj92yP3W6Ky-QAeE5sJdRCIxtRnwn9y_T3mIAivB2LrTC0lVkSqohjAENOklQSonXlnSRzK4CPwD4MG6I9NSRBlbrwifYDg_OJm2SnSLRRPwxSrJp_Wm26ZhsfNxoKKMNit5vHVcmfnNnm2ZIV5Fg80F0YHKoiFo4V5_QVALSbndyaNeuRbR7xmcEe0uTkckgj98F0qIhOmSKDDX5g1DyZB0oC4E5dKMW_-nQz34oWc4aV3DPV-C8Mgcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gh8f8FLEta861-POStvN_IzpaHt97rlx3-VZoeDzNT-b0EVoy96COFHCmjgetSicC5TuAZVDUs87uu6B6jyZnICqL_Q82V7HxAE6zg58_ylVZ7grjhbAwvKUT4wkF_gW0Va7dnUBYRlCWWLpKhX1jDq9XHOJNbm5UYG80cC88z9GHtmy5f-uLAYoDXQoSwfiLeWqwkT0NB-gwvmlSkYynNE0MwIYTK-IO30NoqHAucSM55R8wI1Ru56LgiY-jUbw1fVflTN3neoyj5goxDDR-UCF2hDFGwOIF-ourKWWlKawlBnY-or8cWaNTK51WlXzuiQyW8IA8zsD28yLJOwKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgfAGafkiJ2jz5QM0tHX8xrPnq8OPvgMN0-RksstIZotL3LX7mqun6WVP01hee3Lew5CPb0wuRvzmbo7vV6Gcr6VckWDBBKgluuRFJ9gXcaYwr0EAqhq8zZGN3MiZV4vgIbw2PSCENHHNs5kEvpFLSEM21dsCSO9pXDtaNdJzUSHez0jVnjZ1HdpZVqacck71s_jQE-g15LgwrKp746S4tKsn6-lATkfDrIb-O844iZMoJo-I88gqN798SJhcfTMBputLgKyserSSRk5X3h-Bew2boMYIvgtTN4y31XALMOtWa8fkGrkzRvBim0IA-GHFee0debmFHzIKZjTv3Cg6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
كتائب حزب الله في العراق تطلق ثلاثة قنابل في يوم واحد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92268" target="_blank">📅 20:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
🇮🇷
‏رداً على سؤال حول ما إذا كان للطيار أي صلة بإيران، قال ترامب: "نحن نحقق في ذلك، وحسب ما أسمع، نعم".</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92267" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: الآن يجب عليّ اتخاذ قرار. إما أن توقع إيران على اتفاق، أو لن توجد بعد الآن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92266" target="_blank">📅 20:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترمب: إيران وافقت على ألا تمتلك سلاحا نوويا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92265" target="_blank">📅 20:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
استعراض جوي للقوة الجوية وطيران الجيش في سماء بغداد والمحافظات، غداً الجمعة، اعتباراً من الساعة العاشرة صباحاً، احتفالاً بهذه المناسبة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92264" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQgZAkhkb7feBUqY9GatgsEkJmSeY5XMpROdhU_taxQpdM34iSXBj08L5TYkP8t7pyeROv4TlK1RcKHVueU9_4ggIzkK7gfkq9DLIOFeqhRwRCd12Y5Fb_25lcoQR5hslEkxMQ1lRPe-lUzs011XOu_7OMUsmVQ4P38zaeWeyxf1xNqKxiEIc3rLvyihejx8rWZ_o-UbCOtAX-3f8onl2izY_ZjZ8WfEO43-Tl8OO-pccoeuoyrQuuiaLk_CTezqUP91ABnR-S5izoDuxPjGdxVzF_4f5p0IkhHQIHIFe4XkAvBZG0_v3hWYYDm1GOtxDpBDGzOZOuMNYH1QnPwW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف باستهداف مباشر للقوات المسلحة اليمنية لمحطة الطيبة الكهربائية وخروج عدة محولات فيها عن الخدمة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92263" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278f98e7c2.mp4?token=Nwe91Ga-NEHqwh1qqFQFz8QVCDgoIKrL0DsA3SI8yjeRAB3TfVLz3vJ9f6-2FuBEINZMvEuUZItWlj6uPQAcJquJlQJrczXqc4w6bW9A8f7K_n8rLjeMNXiMpWIbV3XSHwlICQEeJkwZFfJmT3LazLAtvUTkGEy7FXd4W716RNUX-rzadf1dQ1PbB5t8Nie9jfseJByYA5O8skofgNV2_cDr769eMSXBgVXiC0fI7KXDeY3AkSJwxPlwZILL9b05l7xJTS_PWvY13TpPoq893f32epl-ys5zyRUSQMuvgnu5f1OXfmMNju0PeG0SIyGKxJhNExtUC6gZeY4laKDA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278f98e7c2.mp4?token=Nwe91Ga-NEHqwh1qqFQFz8QVCDgoIKrL0DsA3SI8yjeRAB3TfVLz3vJ9f6-2FuBEINZMvEuUZItWlj6uPQAcJquJlQJrczXqc4w6bW9A8f7K_n8rLjeMNXiMpWIbV3XSHwlICQEeJkwZFfJmT3LazLAtvUTkGEy7FXd4W716RNUX-rzadf1dQ1PbB5t8Nie9jfseJByYA5O8skofgNV2_cDr769eMSXBgVXiC0fI7KXDeY3AkSJwxPlwZILL9b05l7xJTS_PWvY13TpPoq893f32epl-ys5zyRUSQMuvgnu5f1OXfmMNju0PeG0SIyGKxJhNExtUC6gZeY4laKDA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب
: إيران وافقت على ألا تمتلك سلاحا نوويا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92262" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a2797024.mp4?token=sl_uMkpKc_jG56WuTuGh_AxbX-1QbJWAleyzY5c1tBgBKZ3XDfwcrPXIez0R3eKQdVZhqEPyL9uewCvfwxlQSJ25RsNkHQC_JoAncVACdN5qQyVBoVGC2NtPfeVNoQ6eA693rTWEwu1czK8I8umHjThW79HUbIzOb5G9_th7owSg4todF6-GCO9d5vKYhIz9SD4zmZaUSIF7Nvu5Zj5_kHSVaKm3e5-uuUueo85pqsuEpTWdWJn2DHtyfCCGcB3KpxS_vTvj6I_pB8QKqkal49nbEOL7tM6t6F9HLsKDqtLtNewVVtFQ76wq_iN7wkkS9e0va9aKlo1Wc1H3CzNFMG2QiCPndU342rqG0BV7WFJctFTTw7c8tzzwmfhZuXR2TIVqWNGg7jsUNG-V2MgnpVrw_-W-OvLnFD6rfatpzJ5XLAbs1JnhCZ1vHUMisZvA0kuzX8UnskyrlAdeqaQR0tqtdpcaP6l2sNHFHXQ2aNezTbEjHdtmSk9YiBqv7LzRmmn6Whz1mTCc5lw2UkjpzH852_7gHVCSse3kg0NrgU3_OkieAskGDSLQSw0hf6UOiajTkz1iLODz22Gobwm3zlB8m9WTsp98jO4REwoJJ5ZbEw_-ifZZy9WCwyYEssuX5rcnjazK5jGxj5WlSQHF8YYDBSWTl_Uv4aIWtxVORfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a2797024.mp4?token=sl_uMkpKc_jG56WuTuGh_AxbX-1QbJWAleyzY5c1tBgBKZ3XDfwcrPXIez0R3eKQdVZhqEPyL9uewCvfwxlQSJ25RsNkHQC_JoAncVACdN5qQyVBoVGC2NtPfeVNoQ6eA693rTWEwu1czK8I8umHjThW79HUbIzOb5G9_th7owSg4todF6-GCO9d5vKYhIz9SD4zmZaUSIF7Nvu5Zj5_kHSVaKm3e5-uuUueo85pqsuEpTWdWJn2DHtyfCCGcB3KpxS_vTvj6I_pB8QKqkal49nbEOL7tM6t6F9HLsKDqtLtNewVVtFQ76wq_iN7wkkS9e0va9aKlo1Wc1H3CzNFMG2QiCPndU342rqG0BV7WFJctFTTw7c8tzzwmfhZuXR2TIVqWNGg7jsUNG-V2MgnpVrw_-W-OvLnFD6rfatpzJ5XLAbs1JnhCZ1vHUMisZvA0kuzX8UnskyrlAdeqaQR0tqtdpcaP6l2sNHFHXQ2aNezTbEjHdtmSk9YiBqv7LzRmmn6Whz1mTCc5lw2UkjpzH852_7gHVCSse3kg0NrgU3_OkieAskGDSLQSw0hf6UOiajTkz1iLODz22Gobwm3zlB8m9WTsp98jO4REwoJJ5ZbEw_-ifZZy9WCwyYEssuX5rcnjazK5jGxj5WlSQHF8YYDBSWTl_Uv4aIWtxVORfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أنباء اولية عن انفجار كدس عتاد بجنوب العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92261" target="_blank">📅 20:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
أنباء اولية عن انفجار كدس عتاد بجنوب العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92260" target="_blank">📅 20:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انباء متداولة...
تم ابلاغ عدة شركات طيران عربية من ضمنها القطرية و الاردنية بعدم السماح للمسافرين الكويتيين من ركوب طياراتهم المغادرة الى العراق بدون وجود كتاب استثناء رسمي كويتي يسمح لهم بذلك.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92259" target="_blank">📅 19:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعترف باستهداف مباشر للقوات المسلحة اليمنية لمحطة الطيبة الكهربائية وخروج عدة محولات فيها عن الخدمة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92258" target="_blank">📅 19:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c3fcb712.mp4?token=TIccFBHwN_hnVwgJLVsoCr7TUDgbbXB4MEmmbzLcwCfgPP2YKXP3sRddYbWj_F70_LeM_kEGJcTm7rHzR5b8ZeK1dSJ1jl7F-jfku9Ne9l4VRIxAeDleQYqr1gXXGNffnEuUGu4PeLs30cZEV1cWZ7dSURvYd2iA_Nb0HKs1RUkaFyga3IW_SPGOJCW-UBpMlURJ8gYbyLlEcCstAS2pUsWgdJ4oohekvYXsgiwDmZLn3usOMEFr5bcupIZSC1oHRbvAUdFOKVu3psNGUjlKOHInFWGz95AMOjYtjRTQGHjBXhWL_CiR-V5GG6Zf5GrTeD4AYw50XyldAJhV0BZZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c3fcb712.mp4?token=TIccFBHwN_hnVwgJLVsoCr7TUDgbbXB4MEmmbzLcwCfgPP2YKXP3sRddYbWj_F70_LeM_kEGJcTm7rHzR5b8ZeK1dSJ1jl7F-jfku9Ne9l4VRIxAeDleQYqr1gXXGNffnEuUGu4PeLs30cZEV1cWZ7dSURvYd2iA_Nb0HKs1RUkaFyga3IW_SPGOJCW-UBpMlURJ8gYbyLlEcCstAS2pUsWgdJ4oohekvYXsgiwDmZLn3usOMEFr5bcupIZSC1oHRbvAUdFOKVu3psNGUjlKOHInFWGz95AMOjYtjRTQGHjBXhWL_CiR-V5GG6Zf5GrTeD4AYw50XyldAJhV0BZZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين:
إذا تعرضت روسيا، أو منطقة كالينينغراد، لهجوم مباشر، فإن مسألة استخدام جميع الأسلحة التي نمتلكها ستطرح على الفور.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92257" target="_blank">📅 19:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRRDzOUiQpKIzCnN1U0b7CXZUGDZZbHXL4jm0BfpDCu9A9gsDY2eQCJ4XHawzKKzKyZk-PR3zY6ulVPB2zaBYgkM3svk2dwpAnPwU9C6nXQKDi9C0s_66vLk9MtfqHI6mCpXmuT1hmPnQBsvjr5DBsp93zrtDMNQVusE7Y3hJh6CAkRl4RHU6hK9ka64B3fUNscIRhBiled1DcqwbflrL0fvK50SGLTgATNLa7YUz_vOJxPTQLHpD_eo_e-Qj4IgV2v1ScbQmH9W1J8d0h3xMMOEmaFjhX3pKphOqCQHcvGSVNsg9oDVWFAy9QC6gTVtacauKkOWXD2N8k4Efp6Uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سقـ.ـوط طفل في بئر ماء من سكنة قضاء البعاج في ناحية ربيعة بمحافظة نينوى والدفاع المدني يستتفر لانقاذه .</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92256" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASrQclgdAnqmHevC2PNRygOlaaclktaWx1lsnFqJejtxhClWVyuNVzyMns8teuKsAagnlpXM-8uckXzZ7kFsGGBksFY83fyrYFbLSyCJ0R_XwHfTGDdBXoO0NWAWvSqb0IdsM5iuUwTzynUhMblaXgPQoEPJ0wqxbchymMzVjaqU9WleQrlAu11is5VWR7B1RYRys2oSLZPphB-YEes8MBM39cKuckZDOVgzqSCXrV9gnBLQeLQCx-hnCAo4ydKdIzMr2HBrzyuLLTiPqPR6QTQ6ib0m_X0LtW9l6bkd_s6UCgmlr-4OaUwkX6Dd-gu-uvOGVMJf0eZaT9904x27LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المقاومة الاسلامية كتائب سيد الشهداء
:
بسم الله الرحمن الرحيم
في الوقت الذي نبارك فيه لشعبنا العراقي الصابر إنهاء الوجود الأجنبي من أرض العراق، وقطعه مسافةً مهمةً على طريق استكمال سيادته الوطنية، فإننا نؤكد ما يأتي:
أولًا: نجد من الإنصاف أن نتقدم بالشكر إلى الحكومة العراقية، ممثلةً بالأخ علي الزيدي، لما أبداه من جهود حثيثة ومساعٍ جادة أسهمت في تجنيب العراق اقتتالًا شيعي ـ شيعي، والحيلولة دون انزلاق البلاد إلى فتنة داخلية.
ثانيًا: نعلن التزامنا بالاتفاق المبرم بين الاطراف المعنية، وبما جاء بخطاب القائد العام للقوات المسلحة العراقية ، ما لم يُقدِم الطرف الآخر على مخالفة التزاماته وفق البنود الموقع عليها.
ثالثًا: نتقدم بالشكر الكبير والثناء الجزيل إلى اخوتنا المقاومين في جميع الفصائل الذين جاهدوا وضحّوا، وإلى من استشهد منهم أو جُرح أو اعتُقل، في مواجهة الاحتلال الأمريكي للعراق منذ عام 2003 وحتى خروجه، مستذكرين ما قدموه وعوائلهم الكريمة من تضحيات خلال سنوات المواجهة،
رابعًا: نتوجه بالشكر والامتنان للجنة الرباعية لما بذلته من جهود مضنية لإتمام الاتفاق المبرم، موصلة الليل بالنهار لإنضاج بنوده بما يخدم المصلحة العليا للبلاد.
وفي هذه المناسبة، نؤكد أن سيادة العراق واستقلال قراره الوطني تظل غايةً أساسية، وأن المرحلة المقبلة تتطلب تغليب مصلحة العراق، والحفاظ على أمنه ووحدته، وتحصين ساحته الداخلية من كل ما من شأنه أن يعيد البلاد إلى أجواء الصراع والاقتتال الداخلي.
المقاومة الاسلامية في العراق
كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92255" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
اعلام العبري:
أفادت تقارير بوقوع مشادة بين وزير الخارجية التركي فيدان وممثل "مجلس السلام الإسرائيلي" آيزنبرغ خلال اجتماع مغلق في نيويورك الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92254" target="_blank">📅 18:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
الحزب الديمقراطي الكوردستاني يتهم جهاز مكافحة الإرهاب بقتل مدنيين اثنين في حادثة التون كوبري وتسليم جثمانيهما إلى ذويهما على أنهما من "قتلى داعش".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92253" target="_blank">📅 18:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
حاملة الطائرات روزفلت غادرت مع مجموعتها الضاربة قاعدة سان دييغو متجهة إلى الشرق الأوسط.
مجموعة الإنزال البحري مايكون إيلاند غادرت سان دييغو إلى الشرق الأوسط الاثنين الماضي.
أكثر من 2000 جندي من وحدة المارينز يتوجهون للشرق الأوسط على متن مجموعة الإنزال.
بحلول نهاية نوفمبر المقبل ستنتشر في محيط إيران 3 حاملات طائرات ومجموعتي إنزال.
مع حشد كل هذه القوة في الشرق الاوسط سيكون لدى القادة خيارات كثيرة للتعامل مع إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92252" target="_blank">📅 18:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a54c8a6b.mp4?token=Ei7_h-6p9r4DaiQU_SWCtG9kYyz1EIvCKLTkRtTz9gz3HpjNBUkIykG2d7IgbdLMu5AKh0Lkyn-PcaEwizCe98HSuElrIti4CIb0nf43L9kz25ZpZM6HqQNJ-yxZurhWxIDrogK8kOLi-0sRqmsYssQ52WpYg930ucLCmeFGygmeR5sNw7rQqcsUxXF3MjlFheDTFTXpzlk6VPytyDALcrz4Dm-M_d1a7Ly-fZBOqt9fGwlXzcKV9t65EGyPjZaL2GeY5ia_7TnsDQFii-EBQfQbkjiDO1_Txo_j7nwj2C5qtY-isUP2JbNpYoRco4AxxlgVNH5HyNjcIJ-2zWNzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a54c8a6b.mp4?token=Ei7_h-6p9r4DaiQU_SWCtG9kYyz1EIvCKLTkRtTz9gz3HpjNBUkIykG2d7IgbdLMu5AKh0Lkyn-PcaEwizCe98HSuElrIti4CIb0nf43L9kz25ZpZM6HqQNJ-yxZurhWxIDrogK8kOLi-0sRqmsYssQ52WpYg930ucLCmeFGygmeR5sNw7rQqcsUxXF3MjlFheDTFTXpzlk6VPytyDALcrz4Dm-M_d1a7Ly-fZBOqt9fGwlXzcKV9t65EGyPjZaL2GeY5ia_7TnsDQFii-EBQfQbkjiDO1_Txo_j7nwj2C5qtY-isUP2JbNpYoRco4AxxlgVNH5HyNjcIJ-2zWNzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد تظهر التقدم الكبير والسيطرة على مرتفعات جبش حبشي في محافظة تعز من قبل القوات المسلحة اليمنية بعد دحر مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92251" target="_blank">📅 17:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEDueof5HSl8sDSB_cOlp5NbVywHWptvqTYOL46-Lp-82qBM9gnYXwij9HikNxfOt6UT2gxICMcCaIqRrINj3zotj9XoP8RT0rXd9rahzNXfbUd1U0ZKA0oqF0AYmnI-4qqt_CFnBrhAVEjVeAeiM-Sss_ZkcadlJbtU-0kBsAg2gOIxfiiqEAKNxFvGwmxT0rGqGJd16TWyQrvcpn23pHrVGgt0XlsK7ZcKLvppVAeBsMv-HCOdiWMKCP8WaWyyE5m35c5Q6scdZnszJjiePazrVOJ43vorGqDbpzbJgnFyZLWtIqLpgSXNXQ4YZAZa4oWovLkKDKBSs15tQIITYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بيان المقاومة الإسلامية حركة النجباء حول طرد الإحتلال الأمريكي من العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92250" target="_blank">📅 17:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5l4T68x-73tRF4C69PEkOXemO5hUg8lrlpexkhiuJF_QvQyLY5CAkIrPfquPzKw9d-LOdiZWhsrd0TGanyvI5h9p6PUlM_cVQ4p18vmhD1c8ond9R2n04zqBf5Af7swJUABZHVC3tzzej4yp5iXWQUgyN6IwkpsuNFHx76P3xQ1SwFq4eVdFEvpMQzkx4_d96dZWPn3Ve2ukVqPVYU_lkKSswnrgZARIYdulRN3dPBn8WHijMR8d1tJqUFpaPRkXA0sG3cVEK-s92k9APNH3e0eehPVo3TtJKShlJYi5YVC2p680PV4GsugWT1cgoC14ej5W_uPFr0nSgRhyNskFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تتجاوز 101 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92249" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0hzrtaoJtl-r8_q9chrAWbmSfJplrqdrtrZSfwVmY_tA4IGftOU0ylOT-9L-B9ZT0G8t2jWGIfKLlq3BUZzQsC-Szp_iqIw2S-wlrme3jDJCkQ2KXGFsiQeIrwlXO_lwEGkSIblKus1dT-H7e4s_zwHbhGHt5HF7YZoK-vdFtFLL7jy7BBHL8Nf_5QG43Zhdw5xeQ2G33wlPyUj1jfhvTZPmWWdvGL3at1c5-SGSVvmJOXVTgvVTZmzPGmlT9EWoxbaiInKvpMikFf7irPXljrO4wKHsuu4OUIXkq7V_iL1008hahXZE-i3bpe0cNd7Kkzga5Vah7y7jQsvNRtTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/picCco4SHnbDs1J1mDCaocHBicmEddAHqPBsxoPFPJfNZ8pDLtso0HS5S3lL3ICmenyrzsyW6gA_92WtZM4B8SwroM4BupEJyNFGwsAGkQeOF2xocsSa66eqgR2QJtdSMHeQHf2Er1z0QNFWuKWnonPZ1FUo88WtHwbZQ0M57nXm2G0CcmPA6PnzsCOOat9WGhCigfgOPCS0JmsHP_EPuJYRmaiatbSIMJutjiY7XLC7dOLIhk7X-urArS2IRGBLdkjL5MLVIHwH-yFRs2eJwNUgm1zy8eTWCXk4TymTXnYJCaPH9bVjWJz8q1jJ95olzRqjK5CtiHhXaC8QGZTMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ED9LyyAPKvQi0B26RHvyE1od_G_MunXA2oC8P9CRx3pxvDErEl5JJlNyyXl_dKPUVLHxcqW7Pm8aJGMAg-6p-k25o_A9MWVUe8qjKg9ojlgCOYU4qFncVZqsvMPNnIC5eYDHy-xahkag1xJLeC_UmHwXQC4uN3EXNXwkIR_n6_91fwI-_AeW6IPChDiFyP5hmP3c5vag_AnMcIO81uX7Nu5FxxvsMzRAEWT0YPf2dq0X2AXG06ZdX8olH4Oox38Smfr1NKeJYRXIsXFZkSf2r6ApI81Famj7TsZFzEdBUQXXqdX0j9eDeULRq1em4OaEGIU9V8J8ydjZqRR9myjWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZ99jUuldTZ5gGLZtdn-snUs29ztiQ9K1iF47mtBTPKLtQmGf2jHpi8UnA-cEh_0AAguuiQ-cY9brtZ8lYkOmoYC0JN-MnJik0Pt-xiD7684lTuNWvlbdVFwxz36lltM43S8tz4_7cq4LRPaWORPjQ5-_xVCddb4GfW6qf4zIZIoy3I0cFIRls4ffcSwJWXJU8rR5SutaUFv0SGQ7XYnwkzZxXoCGgY9lwbHBigsNdPFrbe90loRR5LveP-mPzd1idt_uuAmevICBQ1MeLPFVbUE6NWW4W3XAVp7CSynApAn-9R-XrE0RhokNGyYjguMhca0hFDr-HySrIfF5JyMFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
مسيرة كبيرة لقوات الحشد الشعبي بمناسبة طرد وإخراج الإحتلال الأمريكي من العراق في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92245" target="_blank">📅 17:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2lIUYQ6oIVTSXiSU5nHCcI4v5bT5OSndM--Clf2JGLvIpC4gAA8N0KehOPDXWu-GEMD_nqWgQt-SCMZsvYTOS_Fov37gdBSlYjl35FyJRUPntPsCo7WQCDYpoJ4IpGdGSmW2iU9zr00RkEtRl03-wKku4qa39OPdIoIvoeOKwV1UkdAuzpzq07H5fVT81bLMviSTovAKjRi0aPFanRPstT5wrxd-nA-mP1z-7gnMQV5PxpTvxtH63H-GzfyT6Re_nC6tRhBllNFeoCBVesn6-q44Ta7WlLHyqnjRaCvvbnPyY50cs8OeJ_XOTmdiIlL0eSw2lJrfeVRsLKPWjsdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFN8FYVPKvwrujL6Fc7T31rcaw4NPKSKHVk_OHL9XditCtfQmrtU1HdooZTmItuJX3ioe_NyX0-AvrcNF1W2j0bbur-nHRlWksuLepfu_R9GkfM023gBqxyaNTIFjVBHBMdzG7dJUROEltNE2PZNR9eNxCwhPY-6eCaqonVzV0MfigLSzOgkN0Gau-Zw14hRQaICUPExW5AvW6Zd7dpLIC1TE8j3il4DZbOinNfhbEO08uyxjgFEI7AqCC68eJFJJVDO64xrFh7-z8UGjSpAhwnG1QPj_87BJ_RXx9D2qMZKaFbQUp-90INRt0u08JDDWHb1h_JWMeYOGO2sN6UZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkhD8j-rSGtTpm4x9ijyEVBncFxBcWFPNOSIyaylMU8fvQhkJKQm6UxY5p8LlgQ6hXwtq-c8ojSGtVuSE2NfqVDhuk2Ur3qc3q12iZ8mmjxPv9IRR2q7E9tsUe7WTRICFv6dXni3zCwiMovpbDTy4GxNDmj1tvSfgQyc9v1dSRCo75zWgaVMnV0cB44QSuj3Auq3YggISbAl1UGgBcZl_UwZCQsev_RMb0gAKeiUo0sv5mluZwo4xhIO5jZmtbsx-gBXlaH00UrbkkGZbFb5p5MS94ijB9MhJciGweS3F-trJu1-NgF9s4sve9xUuLZ5owD41JhJsDOVr2h5BfoHZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
إستعدادات الحشد الشعبي لبدء الإستعراض الكبير المزين بنعوش رمزية للشهداء، في العاصمة العراقية بغداد إحتفالاً بطرد القوات الأمريكية المحتلة من العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92242" target="_blank">📅 17:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
وزير الأمن الداخلي الأمريكي:
ناقشنا مع بريطانيا تهديدات إيرانية محتملة لاستهداف مصالح أمريكية بالمملكة المتحدة.
كنا نعلم أن إيران والحرس الثوري قد يحاولان تنفيذ هجوم يستهدف مصالحنا ببريطانيا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92241" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">القوات المسلحة اليمنية تشن الهجوم هو الاوسع منذ هجوم الساحل الغربي على مواقع المرتزقة في تعز وسط تقدم للانصار والسيطرة على مناطق حيوية مهمة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92240" target="_blank">📅 17:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=CqyTLo07PoFJHm2Lyk8eIkxXV5BL7gwlU7RTGOQvnpGztVmabjEbUjKHbobSdnwss72iP5MFMtOQELQVyT1xIVA4cCpOivdapdiLRXjEcBEj5KwAeoBnXAh2jbrvVL40f8rHXz8BYeZvM71c18EevDlzshvJlakusKZ9VZ1gRxBaAZtagBTNJ8WxMSrYOwtnXm6eScdhfUm1gWNW-25hv9f1-8YFizabFL04vL1FrXdqBMf3MejGfKm4CnxjOsc_7Qthfo-VcFhXghOslhLgoYBkgMqk1Oz2inPcWZugHDhYd3sgiAyEgte0riUtEEuqq4hkV220mEw_HXa8KqVMeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=CqyTLo07PoFJHm2Lyk8eIkxXV5BL7gwlU7RTGOQvnpGztVmabjEbUjKHbobSdnwss72iP5MFMtOQELQVyT1xIVA4cCpOivdapdiLRXjEcBEj5KwAeoBnXAh2jbrvVL40f8rHXz8BYeZvM71c18EevDlzshvJlakusKZ9VZ1gRxBaAZtagBTNJ8WxMSrYOwtnXm6eScdhfUm1gWNW-25hv9f1-8YFizabFL04vL1FrXdqBMf3MejGfKm4CnxjOsc_7Qthfo-VcFhXghOslhLgoYBkgMqk1Oz2inPcWZugHDhYd3sgiAyEgte0riUtEEuqq4hkV220mEw_HXa8KqVMeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
إستعدادات الحشد الشعبي لبدء الإستعراض الكبير المزين بنعوش رمزية للشهداء، في العاصمة العراقية بغداد إحتفالاً بطرد القوات الأمريكية المحتلة من العراق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92239" target="_blank">📅 16:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
حادث إنقلاب عجلة يستقلها ضابط برتبة عميد ركن ورئيس أركان فق21 سابقاً في الجيش العراقي وبرفقته امرأة وهم بحالة "سكر" في منطقة اليوسفية بالعاصمة العراقية بغداد.
"لا يابه دمجوا الحشد بالجيش"</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92238" target="_blank">📅 15:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇱
نتنياهو:
من الواضح أن مساعد الطيار كان انتحاريا.
قد يتكرر الحادث لأن هناك مؤشرات على أن إيران ووكلاءها يحاولون شن هجمات ضدنا في موسم الانتخابات.
هناك ثغرة بشأن فحص الطيارين ونعمل على معالجتها ونتعاون مع الإمارات لضمان عدم تكرار مثل هذا الحادث.
سنتمكن خلال أيام من تحديد ما إذا كانت لمساعد الطيار صلات بإيران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92237" target="_blank">📅 15:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92236" target="_blank">📅 14:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92235" target="_blank">📅 14:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su76omC0vKR8dPwj1Hm37pCBxO-Nu2XE12bkQM2tXpZZmwbC2ReMuiIeZQ8J0keJG-8vkA5x8JQeCi9Lq70zQ-qEeA92y_FaGMj9kvx1kg3gaBve56i06BtTKcFHd7PyhbEu5Nm7nTUryAKdJ-J67OUoDcXPtFHjTdVLFtKMN8u_YWGcfUWQpczsOak1U-6Mqw_YMN4z4oSMZPrYm1cxKwpAbtRYNIBptCGqrk8eXZgsppg4tU31lSSDEixwoby0eJLwJC6iksrHAyQBpXG7pTdR2lQVAsbkxxbeBSWbcmCKY0cZZqqESilSQSaJ-9JwZcdpgYvfS9C-Ls5Sf04mTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات الطالباني تخلي سيطرات كفري–سمود، وبرلوت، وكلار–ميدان، وإحدى السيطرات في منطقة سرتك التابعة لحدود دربنديخان لاسباب غير معروفة وانصار البرزاني يتهموها بالخيانة وتكرار سيناريو كركوك 2017</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92234" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇱
بن غفير:
سأطالب في الكابينت بتسليم الطيار المخرب، الذي أراد استهداف مئات الإسرائيليين، إلى إسرائيل، وهنا سيشعر جلده جيدا سياستي في السجون، فحياة من الجحيم تنتظره هنا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92233" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92232" target="_blank">📅 13:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92231" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
وزارة الكهرباء في اقليم كردستان العراق تعلن تقليل الكهرباء لعدة ساعات بسبب اعمال صيانة في حقل كورمور.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92230" target="_blank">📅 12:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92229" target="_blank">📅 12:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92228" target="_blank">📅 12:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=cfYimV3yC54p1MmQpY0rae7l0FjT5RgUeJk6Ti1lJNplIXH6BeFnVkOq-axAXrtY157qbyvk8d_E6l49sf_YSVB6Cw-VldcPweinmMJWpFGDEegKaFPj9nfDJbfnbWGrdYOnmUsWOtGgi1oiqt7TrXwOHAQm188hiK9aIjtYkvVw51i6cvSL_K-1_ie0DR0ifrKxQs2ze0qg6tS8H5Jpej-_lMgL5N6Jtz5kVyhtpqf8eYqOVVAVyV_AHSg_NaGMB4ZJTV5sQqRNu5zYVtQSD_5GaMJuOh4MymlA0yXjLaZYLWfGytOFZEjovyj6E1AMgmfhawD3r585gRr-VKlj2wNMGqUlSN5P7GCX0MaPDKZ9S-luctv7DgNVKXpmtBsJDGoYVdqGnototJfW9_0E71c1kQqOmI4gHHcu1axq__BsKyY_eTONUykDBMNkDXcQU5nWUzEWFKrVbx_je3T_NRqxwsXCvSTOaRLYuJuUTNlkWfUv-V-zqOdbyBXUwblbh9qAiIjVXyb6YXhJfV-dLuBQi5m6IXi3Uv8peuTCNBwrB425RWO1K42GwjsU4IXXUnW-O6XzX_nIARauuX-S7fjecGtr-MhF46IQc55WX-xuhZHTbKXlQ5_NvPYrLreDbn-wBk4m5--ZYEEsreNxD6UYn1wwuuXe6b5muYC--Fc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=cfYimV3yC54p1MmQpY0rae7l0FjT5RgUeJk6Ti1lJNplIXH6BeFnVkOq-axAXrtY157qbyvk8d_E6l49sf_YSVB6Cw-VldcPweinmMJWpFGDEegKaFPj9nfDJbfnbWGrdYOnmUsWOtGgi1oiqt7TrXwOHAQm188hiK9aIjtYkvVw51i6cvSL_K-1_ie0DR0ifrKxQs2ze0qg6tS8H5Jpej-_lMgL5N6Jtz5kVyhtpqf8eYqOVVAVyV_AHSg_NaGMB4ZJTV5sQqRNu5zYVtQSD_5GaMJuOh4MymlA0yXjLaZYLWfGytOFZEjovyj6E1AMgmfhawD3r585gRr-VKlj2wNMGqUlSN5P7GCX0MaPDKZ9S-luctv7DgNVKXpmtBsJDGoYVdqGnototJfW9_0E71c1kQqOmI4gHHcu1axq__BsKyY_eTONUykDBMNkDXcQU5nWUzEWFKrVbx_je3T_NRqxwsXCvSTOaRLYuJuUTNlkWfUv-V-zqOdbyBXUwblbh9qAiIjVXyb6YXhJfV-dLuBQi5m6IXi3Uv8peuTCNBwrB425RWO1K42GwjsU4IXXUnW-O6XzX_nIARauuX-S7fjecGtr-MhF46IQc55WX-xuhZHTbKXlQ5_NvPYrLreDbn-wBk4m5--ZYEEsreNxD6UYn1wwuuXe6b5muYC--Fc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار يهز محافظة دير الزور السورية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92227" target="_blank">📅 11:54 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Ap2dIyLJJxsjTQJa2uYo3f3HH1Y-D3UitnQ1yWnV3-eyAFhB2SOBv2AF96Y7uiExZ2MurwzbgRKpW39u-IvVTFcuzTVJDFFU-X10jyzEL0D1Z0wkO7XSdbL9byqWMsiA_71d8XhiFpzo2YIsZlZPpKbx4d4Fj7a0NF-eLlbI2KSkrNI6FNxbfZoARZn9nE0yIpVSERBcSQ3YagU7ILxJo9ns7aONpe26t-kEPZlrcak59158LmSeZYMy_10somPLqv5muMONGsMkm4rV16hdkqxf5UvLO8Avt1CU7SGcjZCvkjVEvyc4WFdtJ5aL1xYwtnmPHGOv88b6tAKvcNXhnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-6810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1M_TANJoAIQhWOyhiaAsy2jtomelBt_cFN9Y6vX2dpGvYO8to8Eq-EnDICOICxgmtSYArzVufaK5ietHCMcb_83Y_o2FThz97BS5Tftfhn6hMjTQA_1ekaz48BDjr1fLPPBT6OkRFqCLHMXFBS0hLx4ypyOQvkHe8U0vktuIopuDYSvyqcQiJUJPsvHufg9Ts-ybdg652jw_jQT_SdCFRI25J2ohu2J-E8M5wTJ7YTVli_uOJ43c0UN7Q3W3aNS8Nyo1OpSO4-wEISNPRZxLTynDqfrX2ifE3AXd_daf1zmwjSxxzScSzpFFymabtaUrb22XRZUdhTplV-noY-IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام آگهی استخدامی «خلبانی » ارتش جمهوری اسلامی گذاشته.
یه نفر زیرش کامنت داده « جنگنده باید بیاریم یا خودتون میدید »
🤣</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6810" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9CkvVaVmzpIvxMcsldzN85wp9cchB41V0pCS6D8yN7VVFB57jCL2CLRaZ-wPYLUqq7kOYq1Wt7j4ykPeG0P0SYzhtsPwXjZ0hiDDSlXDIpYW7EPjeo4AzzHKH62X_lT24ubinWBzn_KNSy2Nz5xGZJfr9AjIoiBDWia1fi3yMh_yBRl_PRXq112cZbVxiBI4PTI75lSQ8BLQd6PxCgWVXNXymZlKZXNB5IMpf4l9k3wlwxFWOi409MZQtuixXCeMNHz-575EDR5QLWwCADR3r-Y-wgM2SqlaRSpa-9CG2jRss_P7k4obMIELciHnKsheJjNzfYuXTmelrUXI193Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bB61r_car39sjP5Vi2QY1koQWemOUKVXjs25pVySVR9H3m_m4CCBw72dj8RCwHNtbLqW2kE5Q7y1K7fhgij8PNvLEY9X6V4oSIPY7zP_FXqTGd2OKtfSAxEOZXU3dRWVYs0ftI6pYD33_x53186lLy38VUB-usYauRWn-_Ivlmwd7MzdAlwtD_Nx3L2oxDpd2Us743arT0LAiKUc06tM7JSeFYGuxsz2qAnKtCMgJpT93OyTXNeArKQgYYHkyJQods9XaPydW1QW2dNZXCd0LvF7UdbxWGh5Y-FGhuoqeNpGuQYutR12wEP5XItN8te71lzTkk4dodCA-NkNqYOedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pv1u2uUleHFzW9Xw14Dme3Fkbt6DuYNptbaqbvmHQon6ZQ3Qr2QqrqO7QU2LliFgEowY45EDbxksA-XZcxDBC3oCVYmLkcbk4bUYuOLV_6yMNOJEMIRSVdNKm64p0jkLR6NiNwPoiKcRppT9t6h0FP2Y_ZdYDz7q8nesVhYOYna3_QVPm1dpniCpSMeR0yElpSnxg78TvP19kl3hvYdWcXQjuJNSse_HRmi6XrphSO56INHShOoN47JMNFfGN8BRLyXjpDnQONB5j8az9kcEuwbJIwyFxwO4wgdcaGfr3ruEuPg6THJMDGUn6WTEA2kEY3H1Sc-SPThiQW43SktUlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=djR8uCNR-UwLFwfklD7tKP9FAhR7M9FLyu0wV4nnOicWQ2CUguXiG6EpQhkwA0zVGwT5QoAqdkpqBIiiraaDlJ7ZNaLcKHXqbrbhxERFS9jv7ktR9M7SgaSYGesAcZSda-ZXCEwbtdBLtyx3_mDlEzP3aqgYtppgPpkU0j98Axyx-IqMI5NRGiC-fnkapTpqsEiIhzcM6nwhkPNEkuJT23LIcd7einZHlqtRZHeMive_TEPJM9D5aj9z8HbPAXcPyF0iJ-yBtoeshelmDWMZmBP4lwPyfsS-SXCfF7-N89YbfteQKzPAJ-26oPEm1r2oyKzcSPzwLKPdQDi71yf3FIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=djR8uCNR-UwLFwfklD7tKP9FAhR7M9FLyu0wV4nnOicWQ2CUguXiG6EpQhkwA0zVGwT5QoAqdkpqBIiiraaDlJ7ZNaLcKHXqbrbhxERFS9jv7ktR9M7SgaSYGesAcZSda-ZXCEwbtdBLtyx3_mDlEzP3aqgYtppgPpkU0j98Axyx-IqMI5NRGiC-fnkapTpqsEiIhzcM6nwhkPNEkuJT23LIcd7einZHlqtRZHeMive_TEPJM9D5aj9z8HbPAXcPyF0iJ-yBtoeshelmDWMZmBP4lwPyfsS-SXCfF7-N89YbfteQKzPAJ-26oPEm1r2oyKzcSPzwLKPdQDi71yf3FIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HToD-m4hufu_X1IIc5b51DafvkDO2_GMeD_Se75Ntfz24NT-5ya5nM1pTV0L7VKsxi8CraTcEoh1rGzr-CO6_kEadqXYAKv16QmQbLU8I30llX0eFL45XEKKnmx8Z1qzxgQUJKamAm81xV-gQg2dhMNmSdat1zaZxKnEwrnlkPqlLXTgbRxuvwje5xjksBgjJ4329NEl1NeIVVDr1_RDhTEwCHlw9JQaYVQIf8rieG2W9sd2fWyZ5r-9yp50iDNgLyVd9886tZ_GihOqFzICMDB42Vxvqz65JRFZl5O_8t_Mas9BE6J-jwLGYJRd4tQs1IfSDo8NzXlD40WeWIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1ykXoZwX45pNc1-7eEf92IhhgVvrUQeAdENiHWRYRAF1huRh8L3gVreWBW8yDJo9Sj6FBxA-Z5kKXtH1LXFchoOeaBiyObb8AuGEc8Aif3K0lldAdFuiYWNGLFU2M-CBsjIkx3spSTvJ40jjpGV1BWp5CR5M8zBXYL7I_K6R8tudy3BEVlQdBvPTvCJUiTEmPu59mGmQGArRtOfn9hgLCIQcm2g2DdlvO3HS7_gm8wPYuL36KtdOzSMOWl3WDCuSRS-EOx5wKXor50KZ5G9F_ikNTSgWVpUg6Ve99I1nzEEbDpMVYaJmRPWEnoWeYjcU-BU_ROj50hp_qFx81ha3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUA-GRoYMIBI9TymAgSvJBc7czbAjaXPo_t0tcwYndrQjfLj_ZGVvLTs5221VHszc6Ri2NY2tIywF4Sy6rEXWLE2r2bkJdbcqQR2QPaf-ZkLCZqhbzeL4D5v53Q2VYKZ5L9A122plctIFjfP35WSeaclWnhpE6faUhHX1xWISwYJqfhr4SABJOPqHCQLRUtTne8WtD9Ogq3wGlrcx-pOLm0rHCIKxOgUb4RBaMvhV2LAGw4MdrTKnoICJTprg9lm5TPJUnR1RDQoHQ0ZPLAShlo71qX4rfoSqy7G2ONrFulGxqJ54vOCURdv2lJ2FUklywh8Ex_tgjdEm7R9nMthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2qYD6WTNndkTfF4NpcWV0t3EfoOu9M0mwqzACQbp8eBapFo3XsHxIOJkBevlsKmLUqy5WZazvM11GlaCbUJ8ndCLrgJ7jERFaZojg6EVi4QItjjBJao3YSgkBWv6H-gFV2KW5_UgALyX-_Py1kGHnzeh0N3K-t_Hm6W9iOBOZAtF1IMOUpDEWgDjwFhjD319TG5q4dx4zYUJ80xXQIj-V9Er-CKeXwepPGTybIUReOr--hhgICSkb3DglZDBPrQ3p0BpB_WkMAtjsgDxjzHRlHKBLzdk4xL-ZaAJqmd_lQHPUQeigCTlVyfGm9heikVygbkE9ChymL7RRW2CP0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd3RkBWqcri4HCg_UQwpcEpgDkJptlaCvhmgLVu2V45EGmkQDf8A_2ktxkX0lrtmYyW9nb6P1BoWaZrbxpfrAmRzOqgM0abo_H1zGF39hzNm5-6HDjOSY-McbxxWZ625PKBC_-HsRjC51_gfx8ZrzpINUFWXhYpzFJv6mjhkhOUrMYQHz7nGobrgCMiVpWiPf3YdZHq8aDbropgqyX0d6eb68tS83nrUnMwuOFf8ZrREtmBoIpuwZBuDyA4RvtMJieVIQ4d1zQFQ4Ber1vOePq75jFYzPZxFJRiwbGJZ088XrpSLw8qtU4XK-zf6_cDS8ledPYfi0xKo66mHPL2zrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9j3UuFb1QMqAUta8VHk_39Dkqzns1bpuqgmaJax-D2STttc4KsaIXksQcW-iat8xu6RWm_HgLGbZdMmLDYagtNWvYXeTnqsBuH76nVwzzjrjiSwcggW_EogNW7ZWxM0uoDQUJihfAPay6OEEdkFFEl21DAtZdd7YbZth5SUai0Z4DlqlZLwE1IwBSWh6LJTyrDB3zHZnycW5V1rLIgk3-QCS0DEh84N4tCV4ri6BwTNX8RdAV3T1pb5Uz92Ysu1_jRMRN6sL4QM_9y1TYXSkZOsHEj49DnuVMixDrC52clnyUBVx745h9YiTRXJ6DZpFF8WoWzREsqpVpnJiCbiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYodyObeSVmYsPptnSFXg5TdmltXyWP30h0c14PqCJcGIzh6LXDMJL-6aS8WP2eIc8OqjjhixZB3daZGvg3fBfjSDzSJXC0zCHLU1Z_oKUFyarL3JgK1jXJ4ZH-DcJ6PCHM4R46PdoTo3x2fElOj5PVUrHv56UmfUxqp5IRuydq8B3nMBrWRby05idH6-EiwvndFaqMX6b0pLMx9fkEuqt6B0j4bkqfqDSS5mPc1L_Nni1mqqRl7GSFujHz55PwSeapQyWupAvtIxVTFVGQcO6i1lq3BoK7xTS3R-zgQqP5t9SYG_VJYkuR4-ZynBdpD0p6lxGBuZzo0pC4cRM17pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIYzVOiPZeZWurWeEHutdYIRyFhgR1xBwMXqUONrIrKabvCDzqiB3XyCZox3rqY0PhJ7jQUz7N9ksXNhKVFQeiIC3w31cKmBb-iILZzx3DAqLsHPguIYFoa-tCfklNo0uRzgjF_QHPLiMt1-8kaHH7KBA-vNjGfydtZv25682UswLDduhnrvbEVcaKpCQj-h9eh5HkBi7KuEtUPif0AoXlBNiVuSYbjvPcx9O5wg-5eOGYQtP1JOpK3mrQWdwLb0UAkWXMtUp90CNDcMC6kAintRn9PzA0OoxmvNJyYaVz06U6FflXuICjjtvZ8ttKoS6P1iQvvbUtjOixz3Ip06SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=bz7xNUma3-AvwTJ2llUXkSJ49BviB_KJ5LPbbIx_G8dIZrZ1iQj3Dee-u2hMPMpclLr6fN6jWE_QGjbZmjZwAMHHUaK0EbT8sT7utsO_AHgN9PypD9qUWoy_n-0gu50LEcnGwepwHu3bzs2LtcdJ9dp3_GSJOinRZ2mxF1tYPltGm1bWPDaYERsZqDkpC248QCBleNmEu5hLyv1IgXELxW8tBbvSJAeocz6w0pZvX7cXRFjrkfRzfNMVL_gtFjB-_tqAtQ5v06YECHAj9qAKT_2mWDi3VmLj4IocfeQq1EIvgw3eMFI5Hzurl1zA_egdkp3fm97RBf2mVE9d4JP4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=bz7xNUma3-AvwTJ2llUXkSJ49BviB_KJ5LPbbIx_G8dIZrZ1iQj3Dee-u2hMPMpclLr6fN6jWE_QGjbZmjZwAMHHUaK0EbT8sT7utsO_AHgN9PypD9qUWoy_n-0gu50LEcnGwepwHu3bzs2LtcdJ9dp3_GSJOinRZ2mxF1tYPltGm1bWPDaYERsZqDkpC248QCBleNmEu5hLyv1IgXELxW8tBbvSJAeocz6w0pZvX7cXRFjrkfRzfNMVL_gtFjB-_tqAtQ5v06YECHAj9qAKT_2mWDi3VmLj4IocfeQq1EIvgw3eMFI5Hzurl1zA_egdkp3fm97RBf2mVE9d4JP4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=u0y9JmPHS_aOr63R186j0FpmAQXbrYGA1vCN2EtarI8OFRgXQ5M70xWS29sCWw3w34crdud3pm6nyahNiOdwnG__W8vgLqXCoI6kEsCwOCfeidgTw2G7RgmiOee3-IxsKD7oPCmcqu7KU3NAH0oyduyS16bJg8X_sInmMVigCXxrKiRgeXqqO18lOjewZXjxFWkO57Y2UuHTACpSO7Wtk6FCcj7ZPzlE_TiZXSeilE74PPetToPRNQ7mc-zK_Fj4gFHgwt_rM-b9q73ubVekYkZlcw1LdDpQwKh5Ji0KWmZ0QjoUHuKck5pexfhdmRvCeDlmj5PO-35tSv7ZXcavF5u0myYACT2yc6B1_03Ib1vHH9NBXFXSLdYlVA-7yHCEpk7w9dgLPBd8OIdo4w1bT80RNBUzWESxhucLtaUWTtgsgXB5Ga6SJFPOnmuq2-xsDd-icN9frAvDZj6bNh4qLIEgFRG0W8p6GAN8aN-8JI7WNqgF42IvioT0uTJyDN74qcrCDNMR9nBBb8DpVNPoTdk4f4pbZ99-FsJPcjVJJl7GoxOQ7eeatTisPz9r4RddUkuMJ0JAVn4nybjHAGNapzp7sXFpkV5HXhN9dxJFZHwyhFK2QlsdQhJFTKOeSFbBfbii339tSNtXD_FiIZdezQko64lCtyQjoLfjofTFydA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=u0y9JmPHS_aOr63R186j0FpmAQXbrYGA1vCN2EtarI8OFRgXQ5M70xWS29sCWw3w34crdud3pm6nyahNiOdwnG__W8vgLqXCoI6kEsCwOCfeidgTw2G7RgmiOee3-IxsKD7oPCmcqu7KU3NAH0oyduyS16bJg8X_sInmMVigCXxrKiRgeXqqO18lOjewZXjxFWkO57Y2UuHTACpSO7Wtk6FCcj7ZPzlE_TiZXSeilE74PPetToPRNQ7mc-zK_Fj4gFHgwt_rM-b9q73ubVekYkZlcw1LdDpQwKh5Ji0KWmZ0QjoUHuKck5pexfhdmRvCeDlmj5PO-35tSv7ZXcavF5u0myYACT2yc6B1_03Ib1vHH9NBXFXSLdYlVA-7yHCEpk7w9dgLPBd8OIdo4w1bT80RNBUzWESxhucLtaUWTtgsgXB5Ga6SJFPOnmuq2-xsDd-icN9frAvDZj6bNh4qLIEgFRG0W8p6GAN8aN-8JI7WNqgF42IvioT0uTJyDN74qcrCDNMR9nBBb8DpVNPoTdk4f4pbZ99-FsJPcjVJJl7GoxOQ7eeatTisPz9r4RddUkuMJ0JAVn4nybjHAGNapzp7sXFpkV5HXhN9dxJFZHwyhFK2QlsdQhJFTKOeSFbBfbii339tSNtXD_FiIZdezQko64lCtyQjoLfjofTFydA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciL21iWx3wcJqE_g-eV54NnD4yH-cdmNqAZ_4x8_rlTyoQL-rxNhzIVeEeTNefyNj0Ii7iAE3QCxAR3NgJMPOuJQfxyXarYIIAlHaxHMbH9zDCKEY0giVfgLYbvSLdhXay4cpZASYlMwKgdENzzLXL8CNw1xZeq3t1El-D6gSRTqDAILyKeZ4z2jSt9oDiGKr7hm0o6gVNVZYk6rWLx96xhXgsBJ6qcfhoEZuw1Tcz3TBQHQyhSOKhfDcTH2Fdy0nlcCKGzkPALR70izDrMYrjnttuGEhf1SrwPbJJn5zUkp30ZlxryQ6QH09Qzmrl8nMPwYWgUYCqMXWmIGhNXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltsTBCjprbkMijRN6h3VLjUyi_iU9NPFk4Swd7ljM3BmmpDJ5p6dNvfAVj0nj9juYaQELSh6Ydx1HF-BpWy9kXNHvdykGzCOF2wURE_NsmD9axmr5_0EJhVFDcH_-ict5w0fXmh7u2VjPopGPdn712Wk9R_Zy3xFw-tcwYS7BwX01ltq31doSy_gebVSQXcBKIKKs8w7Gbj3khjT0RYvyZSBG0_KWdztvUdibWKBcYW1oxa8C8EWBsStO8mvfNGYSZXDeKuNrusnxNCkixlhPfhC66v8TJ6fuc5K83zioz1USO2ldfxZIrEsMGR3Z-kiqsu7xB2SWeous8o32TWH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOgV65OMh933qi0cm9t5NctATPcPkZ4_E-LKob9QtEMfr3Y7QaHwJCtTM3Odyd7MtjXcLvfgIqHsa1cXUQ5YAKcizxOJABzmjwgJFQNc-Rc_-uSs5_3LPwl7u6-OvZ4YT2KybdETMyB1C3pBLHtBxASkw-6bSB7TIlf2FXcyNHKoKbrEXnPTQoNg5iu-7OtfupSTPa7jNZNbgcq87ke_RKSF2YW10aFkANesWTMFjZ9rySPYuMrM0OwDh2yJdEp9Jh2DQPXv0kYTMWv8Tm0msC1FrMpJpWrNvzPC_Of-IAYWYtlBPF-vYkOtoQyk9L5LnfaGWNsQFLECOQi_VkSq2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=cC8uAad00PAyOpGK7CsoTI2m6Mvqw4pP4RiHk0DbucH7jkDIcfybzmL-WlP5gV0nMMfDNA_KVZD_c7suzJW7uqhOwuOHThrv9REE3AyjybJueptz90NtZydGaud8kfr5nBGcsq11RY-mOkaptAspcIMKjtlvafLP5N819ODYPmIGniq2rtnhJTjyBhqI2lU736hECO4iYJxB_50qvEqEw1HiiLMC5cgxJryr4XGjn1FTCFiHf9E0vQ4YckWhUnQgwQM8YLeAMihVBSKL0Hb5KVAbAhqXGEKX9LQxD0HY8Y-NWWAyvpWVwnBBwM5ugb4RogPFtsXvCxO_Yg8IVV7IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=cC8uAad00PAyOpGK7CsoTI2m6Mvqw4pP4RiHk0DbucH7jkDIcfybzmL-WlP5gV0nMMfDNA_KVZD_c7suzJW7uqhOwuOHThrv9REE3AyjybJueptz90NtZydGaud8kfr5nBGcsq11RY-mOkaptAspcIMKjtlvafLP5N819ODYPmIGniq2rtnhJTjyBhqI2lU736hECO4iYJxB_50qvEqEw1HiiLMC5cgxJryr4XGjn1FTCFiHf9E0vQ4YckWhUnQgwQM8YLeAMihVBSKL0Hb5KVAbAhqXGEKX9LQxD0HY8Y-NWWAyvpWVwnBBwM5ugb4RogPFtsXvCxO_Yg8IVV7IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=FGQPiO-K8r6t-p-n1fG5Sef-UJiv2cZWJQD157PzuJMkTqKhACkVJHIW-bPSOFkhgEtDsy5nWhxuP-ZKkyXRhT9BJqtNnGWQUDbybl6MnL5NMSq9WNzUKltk00-gclk1NR2vGqSNu-O1swHv7qSBZnuRd0x8AZ3cYYm1slIpaumr9nh_gsr1_0qqli8KFv0I82sxXawLg-1CMRx6Z71_pt537kpkVdjCc34nYQmJluAgXq3ZhcEHdYxyMgJVBxYeLIKm4rttUtJlPi3AdEVqi7xStWM3AepmunB_Xs_eDGmZ8ijFe55PdZVk7v6ScC61P6n4fOh4I4k4S3oL-nEVHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=FGQPiO-K8r6t-p-n1fG5Sef-UJiv2cZWJQD157PzuJMkTqKhACkVJHIW-bPSOFkhgEtDsy5nWhxuP-ZKkyXRhT9BJqtNnGWQUDbybl6MnL5NMSq9WNzUKltk00-gclk1NR2vGqSNu-O1swHv7qSBZnuRd0x8AZ3cYYm1slIpaumr9nh_gsr1_0qqli8KFv0I82sxXawLg-1CMRx6Z71_pt537kpkVdjCc34nYQmJluAgXq3ZhcEHdYxyMgJVBxYeLIKm4rttUtJlPi3AdEVqi7xStWM3AepmunB_Xs_eDGmZ8ijFe55PdZVk7v6ScC61P6n4fOh4I4k4S3oL-nEVHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTB-ZRKlQfVEzHghFvM5VlWm23B7eMpoN7MH-8ySIkolhmtZjWZeIBbyUFHbkKtm1y-MnGtXlXRgweqgJf564_2xABQp1uoqgxu9pFyGGWeaAPwPv-8JIbJlZpT1k5Td2XczZgIvuOHEaYsj_mjkKErOdEzpKhv9WiG-cI3oEKOlc_310CJOKAv2fXiRvAgr0ZP8sNU3CbFKnLipev_DJjmQ9Vk0HMr_DbGYLsvhcvHkNdx7h1SUU1KakikHTjcI4vFDWM4i-ceCVGdFEUFzBcWUl2yRtUFv6gddN0UXr2FU6SohRkHgrs0AdMSDwiinXeJ0TFnDJaw8DadSj6ag1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Uwy4ftK_ZQYuBA9KsU-a9TtGQcujM9jVKm-dw9PK2D9jkemob9aeGXTNa0KBOVuiPycRq807fb6yeKPCMbso_SVTnR0mdOETxQn54jMEBswqzrroKPC6SVmsH8Ia_nUyJPp7HWyvuLDW6M-t1oT62tyw7kkYTjqEi40ywBz_pisrBTLogu1K9xe6_SrrefVNKxclvVENPEs8EJvvy6fnYXXBd0HGH5LtPqz69_pvu4HmOHkS5QFybor46VioC1iDckUwvReYfpMX_aZ9k34AvHxzUY_0DieRTiMbkA1Cf6R1rmNlcnvk8n_Kaah2YCRR3Gn3VyEoDGmX74TxHM9gDJkncw33QjV9ZfLa0dYamEouPh8qs0YBPrxi-znR7FGjLDkqNZoEYeH_RMGegL742FmET0vcT0dn0SaeHO8JMh9JW8Bb_IFf1wYAbzYtIYZGeTQMnsOAVghQUXRgg6IjMrMCtm4W0wI1PUC5d2ImRgZLG4Gm1iLvFXwNahLTcbMzKfaM1HZKLc_-Fuqz9K5S5HHx-WdURsx69YORmtO_MXRn6mLuN_5nBSAmHtLAPIGHz-dLdd16xL3HchtJaSHbuIybX1RtTSfNgQ70nLTxiGfYIsiypeMMRZnhwf_4ZfztFeWiv-0kX7eDxlPzUhaiB4URPmUrKdxGrE_WY-bz6As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Uwy4ftK_ZQYuBA9KsU-a9TtGQcujM9jVKm-dw9PK2D9jkemob9aeGXTNa0KBOVuiPycRq807fb6yeKPCMbso_SVTnR0mdOETxQn54jMEBswqzrroKPC6SVmsH8Ia_nUyJPp7HWyvuLDW6M-t1oT62tyw7kkYTjqEi40ywBz_pisrBTLogu1K9xe6_SrrefVNKxclvVENPEs8EJvvy6fnYXXBd0HGH5LtPqz69_pvu4HmOHkS5QFybor46VioC1iDckUwvReYfpMX_aZ9k34AvHxzUY_0DieRTiMbkA1Cf6R1rmNlcnvk8n_Kaah2YCRR3Gn3VyEoDGmX74TxHM9gDJkncw33QjV9ZfLa0dYamEouPh8qs0YBPrxi-znR7FGjLDkqNZoEYeH_RMGegL742FmET0vcT0dn0SaeHO8JMh9JW8Bb_IFf1wYAbzYtIYZGeTQMnsOAVghQUXRgg6IjMrMCtm4W0wI1PUC5d2ImRgZLG4Gm1iLvFXwNahLTcbMzKfaM1HZKLc_-Fuqz9K5S5HHx-WdURsx69YORmtO_MXRn6mLuN_5nBSAmHtLAPIGHz-dLdd16xL3HchtJaSHbuIybX1RtTSfNgQ70nLTxiGfYIsiypeMMRZnhwf_4ZfztFeWiv-0kX7eDxlPzUhaiB4URPmUrKdxGrE_WY-bz6As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Vm8A7yLF4f-pCpZDn4zcdEsPhVxNE8GoDltGQ9SSZ-ySRYv1bKMWT8EPgyQnU1e076MRjenlBLHm_ihW2p9UvW4axT_jv70Vh8IQHRohE2tQ72NR5QHmElWz0bFN7NSnPhUnzpMIFBlTVNWFIBZaXQTbtIFATDF1MxUs75M1zKVQNXvOERXxM1y2ZYVZqaHBFT3cpnfTKk4Xj_sFgxrtoPbcMo0MXx9AZn_YYdqU58suirWK5Cdrpmd-322Q4QW34kEd4l4NeKzD2LyO4lfz8Cy3KAXZZo8Z1Q9LQzI9DpGWLuV7F61jX3bLjs2ipPI_2sPFBhm6i40qaJVcCly7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Vm8A7yLF4f-pCpZDn4zcdEsPhVxNE8GoDltGQ9SSZ-ySRYv1bKMWT8EPgyQnU1e076MRjenlBLHm_ihW2p9UvW4axT_jv70Vh8IQHRohE2tQ72NR5QHmElWz0bFN7NSnPhUnzpMIFBlTVNWFIBZaXQTbtIFATDF1MxUs75M1zKVQNXvOERXxM1y2ZYVZqaHBFT3cpnfTKk4Xj_sFgxrtoPbcMo0MXx9AZn_YYdqU58suirWK5Cdrpmd-322Q4QW34kEd4l4NeKzD2LyO4lfz8Cy3KAXZZo8Z1Q9LQzI9DpGWLuV7F61jX3bLjs2ipPI_2sPFBhm6i40qaJVcCly7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql_v_GdvXsswJvzJ3Vv7HH3PRQS8VVw-muGku4zsckb8747cFN9m9M1XPoWxsJaSJQlcaDU2bsqwzrursb7PqGMi0DIPDwFif8bUvG41GRvYyyjuc6H1Y2RXWOYJgAZpI342VHHFTu4fpI4kyNxlfsRecpTvGWn_dQrtTFdStWI5XGKBN2DHn3irhpr08uR61g8odCyotBHChwXsTPs104nUHMZtcjd-s8Y4INcSH4ukIEYxUfBbWWZj4IMz1zXoBz2pH3IV6tE7lfi7HXmMksbqpu037iVgQnZphG0rQarn20y-MFGDd9HLNvcrVp12u-Fz13l-9TE6SC-tMPSScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=XZfDpnbJU3csaMPnYCaudZNNLi1igIq9f-SplLu-zbYDfIVdg9WVgoR3hO0I41S31K45ZWk1FZjo81TjseAiDue0fpyyoSf9JS52jL8irfW7iNEEHXm0HkIXKHa71XmRkvSAN3hLL9fp31MyPUrdrBEd6EDco9PYovDwLdP19Q0XIwYjnJz59guxycl8vXSsHi8ycGoMfW0Dmd99Q0nQcMD1aPrcoaF8FhJZeMPTYb7WP3P3Y6kVXvaCMt2UPvXjnXo8cND6oWjTTQ3X9H0W00BDjuhB305XwIfQszltgoY-yCh948xuGv4vZH1V5NlkXnH-lAwNJ0bpWaZSlfY6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=XZfDpnbJU3csaMPnYCaudZNNLi1igIq9f-SplLu-zbYDfIVdg9WVgoR3hO0I41S31K45ZWk1FZjo81TjseAiDue0fpyyoSf9JS52jL8irfW7iNEEHXm0HkIXKHa71XmRkvSAN3hLL9fp31MyPUrdrBEd6EDco9PYovDwLdP19Q0XIwYjnJz59guxycl8vXSsHi8ycGoMfW0Dmd99Q0nQcMD1aPrcoaF8FhJZeMPTYb7WP3P3Y6kVXvaCMt2UPvXjnXo8cND6oWjTTQ3X9H0W00BDjuhB305XwIfQszltgoY-yCh948xuGv4vZH1V5NlkXnH-lAwNJ0bpWaZSlfY6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFhwnWv8uyGEkFxsGv_VhgBsxpvBHJjkIrv1UcmOVqBV-CGcZibDto3XHnGDDEkxi99kw3ccevGHJHO48AejbXjGPOrWqfE3eIFicSWV2kkX__8ekgA7zqqnB7P6eEpC9i2h4M_x9kZSFIC9gCTPOXlJKHwPF1NAut0APLMeTmcE7qDmp8XiXT6eukWoyY67QxPm58s-9HF8P4BVcDDqKpedEzit84b1dJgCsovQrKZfVSxJs2qv0onyB-rX0jYnsvjafl_cAYaW3hsnGC3TlA6fkHXJMhCGCVPkKtSmquhmsVZkMJqkizbBx2cga8EA3zr0P6HK7KZme7TBq33ZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoYqMbm2Ub0sJx1eq-P4D52PvGKFdVMdk5m15WUTUQK21Fnp6qVS10OCxVxmmlur5rrQPy6HO8Goe6y15LeQWJ1gsHysMNbfrL3cQopoKiarKR9IwLekcoS5KRs3ie6GO9S6M-nlLLtagQtXGTtsU_jTR-BnMyfjAzBwPt3nmtbefYT4yXFqKbri7Gn2TPA9Q7R_6pr_5Lu16zOK5iTffLdbfhhiOLQ7k7_zRGbEzyfMumAPX_1c_ywaFLpHGeLMX7-4rSS2BkAppmI8c02pf62AtvpOJWjSnIAhJlh9kE-xdbdqgdcRbVuiaCul83j3zYoOuky8647GCLcDLfFeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=JwmwrRUWcpPJcKLjoHDGeWsjza3z7pHDZfAvoICr8rSYle-qOPJJVXkZG2DSn_huwH7hl0lLBYhv8nWDA21XzF5vkatUei6YI5WOvuM85TESCcUpQl4oNbpDGaYLWq_PqfBFE2PU8EcBk9Ilmt9aYMcHei---tRgzFVHwEywDsP8btw7O5ZS0-pys_d5jl1Tb_KJgsmdY3ZMNj2hEh4OnEsTKyJpooVivy_OOGhCCNdS_h6KUPk9nefdM0Yl4GulLq8KwYsFMr4T3dy_-5PhvIoWdl38YPUOEsTF47s6YAcaYnyuY_CKJ7Z8tJRgVngkP1A14ztJBFI_wOXSDrivXoG-eoXiONwyA9kZ0xXAyYFmKxi-JUGxszQmqM1s0CmhVlBtJhfE7cYPGpDwalCK-XJzAtchCK598h3dYhD6ctKZQV2QghSYisTBJOuxiIEa1Fh0iZ5CBfFSeJ3YijvhkvRqkVXdQq1dKIsinYFms89_r_H8MdY-LLee21z9tZt4nI6KHJ40KpMM9OJM6-FKqa1sTXjsZ-sBR62-diFEfXbo3mW_-YwntjDn3mXpE437puLbhfYW9bVbhzowAy3n3ZiaaQ3cW6681-zYieV9QRsVbXnOogbvhVZyPEcjc06nlh9zzkkhHHfpoNSjDEwIy-EsgEjr9o2Me19S7IbsV9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=JwmwrRUWcpPJcKLjoHDGeWsjza3z7pHDZfAvoICr8rSYle-qOPJJVXkZG2DSn_huwH7hl0lLBYhv8nWDA21XzF5vkatUei6YI5WOvuM85TESCcUpQl4oNbpDGaYLWq_PqfBFE2PU8EcBk9Ilmt9aYMcHei---tRgzFVHwEywDsP8btw7O5ZS0-pys_d5jl1Tb_KJgsmdY3ZMNj2hEh4OnEsTKyJpooVivy_OOGhCCNdS_h6KUPk9nefdM0Yl4GulLq8KwYsFMr4T3dy_-5PhvIoWdl38YPUOEsTF47s6YAcaYnyuY_CKJ7Z8tJRgVngkP1A14ztJBFI_wOXSDrivXoG-eoXiONwyA9kZ0xXAyYFmKxi-JUGxszQmqM1s0CmhVlBtJhfE7cYPGpDwalCK-XJzAtchCK598h3dYhD6ctKZQV2QghSYisTBJOuxiIEa1Fh0iZ5CBfFSeJ3YijvhkvRqkVXdQq1dKIsinYFms89_r_H8MdY-LLee21z9tZt4nI6KHJ40KpMM9OJM6-FKqa1sTXjsZ-sBR62-diFEfXbo3mW_-YwntjDn3mXpE437puLbhfYW9bVbhzowAy3n3ZiaaQ3cW6681-zYieV9QRsVbXnOogbvhVZyPEcjc06nlh9zzkkhHHfpoNSjDEwIy-EsgEjr9o2Me19S7IbsV9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W44y0cn2x_st7-5WExCyl2WenAJz0EHw8J85dIZ6DEKFPcens-b85cx6Cojo93hxATPnIWXN5kfrikfDIALIcyv9_NaycnVo95Eff1uhycHalTukARWSrLls59kyUsEV4iR3iIUBcc8Dban2I9iXOQxv2itwUh2LYE2wgfboRWSJEu27WpdjVTatbn7Hv7H9JDvSxRABRWxnBwK40thM26qhdPuv6hjsenJO0IZake_Z6TIkI_pEWiECx-VB8iGWe2o52ZKL6Sikkslo5NNMrFZnZflMlBwkg7JhUQVq6eyHgVg0rGy-cY1-dzOK5548wb_CPMRNlHlPLzM12tSh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_YSVqKXWzqrC7s0vf7yNRH2wlkDLhgKSkEYdV0p0mo7XT6mE5KX2fdblHSyvCMkLu-_GPsOyyBLPf-GdgbhAPj0sdrkOh2hdZVA0gOu6aNLjycSoAMWyhZgnenP_16FYfUUmE94Co5giaBZaXNUpV-I6PxPUs09Za06JumsOCIYkncHzu_RrEqJBWpqggCPKjO2BjjCeoHD1PcnfHuJHEgnuhC4Miu0mCpVVoPWxPDUPJjZkPkRYLfj-Z3ZQ1VnZZ4R70ovKhQFhVg54ntxP_nwkAbVartszRjPkbOOuFkzMQTpgDSSpFgGkd0MIjKcWpOnUVqztVwYco0MuJYd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=aNVImH-VWbBKvWEOhfOZJ9zr5196kbzOJgPRmLMAdNY95vxcN9EJ7EFne3OUodyq0RZaCmGXSr6DJEujTC-Qw7bvzmSmxplqBbPwjfoDkHQD4kKpOn2JIO4P7Y4n8Q1anDNjphlHbvxc0q1A0C8qvir-9BryjY95ng1yJzN3VtYgtOe0DxnSAoAE5r6YJO80KkEYERacizQnCpzgrbaskfzqbKI_Aig3MvCoU1N3rOV5eNGyRhNzDNbmH876ZMIq-NwulB1SGGi4ee0gbQa4ls2m-14UwZbyMXWAucTDH8QJ7z02o8fRZblBGCKWYe6k6h-vs8F3Vou6t62VM6QZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=aNVImH-VWbBKvWEOhfOZJ9zr5196kbzOJgPRmLMAdNY95vxcN9EJ7EFne3OUodyq0RZaCmGXSr6DJEujTC-Qw7bvzmSmxplqBbPwjfoDkHQD4kKpOn2JIO4P7Y4n8Q1anDNjphlHbvxc0q1A0C8qvir-9BryjY95ng1yJzN3VtYgtOe0DxnSAoAE5r6YJO80KkEYERacizQnCpzgrbaskfzqbKI_Aig3MvCoU1N3rOV5eNGyRhNzDNbmH876ZMIq-NwulB1SGGi4ee0gbQa4ls2m-14UwZbyMXWAucTDH8QJ7z02o8fRZblBGCKWYe6k6h-vs8F3Vou6t62VM6QZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=nVLz6eUVSJpOW1nj9Kq742VS8s78QHXVY58T088ojqJt7mOBQzsbirZv0jB0fQB4Gp3giiREqjAZyp8CCCkiDeDPI0QlS1ZIgIQ1G5qiLYq4k1nj4G02Em-_l4Xz2P8DE_7-4yaL1ABn8VW_c9l1Xslpk-DQkQMd-lVcUZwN63g3ImvWdTnBNxbCxcy0AWuauShowuhg5ZWtsj2JUPc-fALwO0aEsaPFVzcBvmVqbHI9OtUcnim52ucjzHaHBuBH2y8nRz9wOWXNQ4-ulsTFGCThOX143CDvisB9EpqV-GBZln-lwm8k_2UvyxjoFJqNqH9Q9aEY0872t24FUDMdGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=nVLz6eUVSJpOW1nj9Kq742VS8s78QHXVY58T088ojqJt7mOBQzsbirZv0jB0fQB4Gp3giiREqjAZyp8CCCkiDeDPI0QlS1ZIgIQ1G5qiLYq4k1nj4G02Em-_l4Xz2P8DE_7-4yaL1ABn8VW_c9l1Xslpk-DQkQMd-lVcUZwN63g3ImvWdTnBNxbCxcy0AWuauShowuhg5ZWtsj2JUPc-fALwO0aEsaPFVzcBvmVqbHI9OtUcnim52ucjzHaHBuBH2y8nRz9wOWXNQ4-ulsTFGCThOX143CDvisB9EpqV-GBZln-lwm8k_2UvyxjoFJqNqH9Q9aEY0872t24FUDMdGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ivAW50KZc9wmuvtPq1d0Ll9lh-iSvEV7ULK6IKUSJTLntDcMRTe7z5CYfAYduVgVzjUEF3asak6mm0ArZkkhCCd6EyAq-HWHgkbXlAMX5Yw4QBLlMYegbQP_RGWiQPtCzLqcx2I1Revs0Oe2QrTRGduBPrns5CwgFZ6z1feGWevZUkeRv7K_ld_21RATkonPB67jFoBPh1OdF2kqZPZbrxKm0n3hmIMyJfjqRJOyvN-HLHsblO--iMOVyZEh_XdMjmW7ByOCFM0rq5JJhIjmUJV1Hg2pvfNWsLExbMV2DjmbhCGXiabN6yBcR_7dNwcpAH2truHveC6h2i4Gt92Ezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ivAW50KZc9wmuvtPq1d0Ll9lh-iSvEV7ULK6IKUSJTLntDcMRTe7z5CYfAYduVgVzjUEF3asak6mm0ArZkkhCCd6EyAq-HWHgkbXlAMX5Yw4QBLlMYegbQP_RGWiQPtCzLqcx2I1Revs0Oe2QrTRGduBPrns5CwgFZ6z1feGWevZUkeRv7K_ld_21RATkonPB67jFoBPh1OdF2kqZPZbrxKm0n3hmIMyJfjqRJOyvN-HLHsblO--iMOVyZEh_XdMjmW7ByOCFM0rq5JJhIjmUJV1Hg2pvfNWsLExbMV2DjmbhCGXiabN6yBcR_7dNwcpAH2truHveC6h2i4Gt92Ezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1S0oLYrrAfTreoYlnTJuaMS6kES5KcYGmFF6HNywP1w19iNLaYIwc974RRKApX6OfINp3mTB1Nt8hwYbjHQuK7MtvzvF9zH15hBKkURl25cvnxRxlce53nCAFAVtKT7zyQlhyPrEFuyIee2vPC58kSdRXpPl1w2Dw8xt2B2caM-NCdVOd5YYxB7cQICF2JuBbpipJPekZaW6-45oN-CDLIr-HiozEKELPz7RNFbVTbAe12dHflRLvZ2HYNkv5HWAhCpiat5-nYQNabv7uUxwaOsNvULVPUdQVi2BWYYHgdyo_rHWxYeGkA3cC2XMbTvaVLHwCdkbpZUHG80ncpQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro4Ijn7CgYSQK6wJDGExie-eCS1NbuqsP9I28ZSTxONvG8fJmHhJc9APvkZ0fHXJIhTACoUOzH2CoV4aD2_Egxpo81MIvd1xSuwO1HnAmAf9EDw-Ql814ggFFf46PAgvSnFwCirX458_44_kNQcAHTuQOrsCoAX2tE7rUkPMbWC9s6vekKYSxoD0uIqXCqKYGfXFQ3TBKPSmjXg9HXP3GzGPq2dz23oxIEfF2niNPrx6xqhNPxrurHUD7PxOIRVlJEBkdgE4Ul6YU7RVyElyeeCU7cutvvAniz-vaiANrYU6OsBjnu9JiLzrt05L52seUoVXd8mdHJdO8uAEGILgoAWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro4Ijn7CgYSQK6wJDGExie-eCS1NbuqsP9I28ZSTxONvG8fJmHhJc9APvkZ0fHXJIhTACoUOzH2CoV4aD2_Egxpo81MIvd1xSuwO1HnAmAf9EDw-Ql814ggFFf46PAgvSnFwCirX458_44_kNQcAHTuQOrsCoAX2tE7rUkPMbWC9s6vekKYSxoD0uIqXCqKYGfXFQ3TBKPSmjXg9HXP3GzGPq2dz23oxIEfF2niNPrx6xqhNPxrurHUD7PxOIRVlJEBkdgE4Ul6YU7RVyElyeeCU7cutvvAniz-vaiANrYU6OsBjnu9JiLzrt05L52seUoVXd8mdHJdO8uAEGILgoAWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=m2wzbzb8dvyTn6ByDfxuRVKePCiTpH-3lf6jVxGMhHv6xvfI3IA76Bnb_1ZZ2G_q-cY5-H4cMfLNg-5-_E0P6FgMF2cPqwzGVY5uxOch07Xtci3Yf7vQ4D6FCPSBf-g1VPn-EEgZ-yCWqeMPK2AdfUnmSbnzbQES8IR-Ve3Eod25fFBw13_V4CQzPX9r6j7JHzAwnxzih2_Thuw9ReO3uEZyBv9xvz6qIAkVIA9aWSjm-5RrH_q-ZQjdxa4keF1WGnTl8ka8VEtJdCYTvrlD6wRnIazi_TlLhvHaDrWSIgGw0S6WpPPuNuyPgdwzfFrrtYGPNIZQhJfyJAFCB7QdTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=m2wzbzb8dvyTn6ByDfxuRVKePCiTpH-3lf6jVxGMhHv6xvfI3IA76Bnb_1ZZ2G_q-cY5-H4cMfLNg-5-_E0P6FgMF2cPqwzGVY5uxOch07Xtci3Yf7vQ4D6FCPSBf-g1VPn-EEgZ-yCWqeMPK2AdfUnmSbnzbQES8IR-Ve3Eod25fFBw13_V4CQzPX9r6j7JHzAwnxzih2_Thuw9ReO3uEZyBv9xvz6qIAkVIA9aWSjm-5RrH_q-ZQjdxa4keF1WGnTl8ka8VEtJdCYTvrlD6wRnIazi_TlLhvHaDrWSIgGw0S6WpPPuNuyPgdwzfFrrtYGPNIZQhJfyJAFCB7QdTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFaePQ535aZJqt2w_wEZPAtdR0NPEiQpIGP0Bik497ork8UHZWaYqkqXmWFYfDIAJORkbqaZ8dqo2z31zMEyigPImA7EpmhG837iKR3mA8wgYeHOJiSPZtnq4Ca0LUOP6abn_E9SMx1SBtK0zjaaM0gX8fi4SLTt_yaze85KrH7i_YMnt4ByOrwHYJabloXiFb0udPWgFLo3awboXEVNXIzpuhVfkC0g7ftXdt0jPhD7_GEM-wTHHLFbR_v8q42enjWuxvkFcEm5T3Xl2lP-4MBGGwkDMWEJ9ckpvu98nctLMZB7kzcZnLeHwvlC6Ms3MacbrJceNluGH41sWEiYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Ei9mmexsdAGhn8DwyAqDTP94ile0loL70rWVLuT9vcE6-eyG85L_1stg_8Lw315GOB2XoyrG51vhBZfCONOjRcduIFcOmNMrQKsce72g8qLvsQHjtB3SIQ7J3aFUx7_JcxzzN5b5PqV8KUxL3PZEUNNtn58Wpyt_lqrM5bJpVMrymLZcIveecW5TIdMG_Zy-kSstVeMNHRtUph_qeopEoM0nA3pF8uR8Wkd6O2StQb61MQxe8dwD33z6fRhzIzihiQag6f3bQAwbhyofGeaF1ugCObhMCwPIqltB_kXYNEHIoQVMHbt__tNsg-jkHVUwmu_TOr56iktb56cmWp_35AcdpY-8Avd4HNn0DggA7ipKwnU6G0DIdnzyVr9rUlHE7IoGcZbBmewBj07NEx0QTOmvePmlhVvVvNzz_GS6IGGqIRZtNv1XEAD5jI7gK_6fIApvHCe5u8ZkxLsPBRQtpIUt9tFuILREpQpfLfpRdb1QcAZfjCXI5nzgHy48c8oW8bc0Qfx3vsXC4TocWKk9ClpEkoAaQ_yAkc_lDw5st-zAlJF4Cm86uIrot-RyuZ_5KfOXd-pe78LUIyxGspUn48c2tBA8kDkkBCDuwmuul2ewnWfJDlKGYFuluTWLxpiivyHeptsOmVP3OFcm639z5yDk4yU7JjkH23HKEjS3IU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Ei9mmexsdAGhn8DwyAqDTP94ile0loL70rWVLuT9vcE6-eyG85L_1stg_8Lw315GOB2XoyrG51vhBZfCONOjRcduIFcOmNMrQKsce72g8qLvsQHjtB3SIQ7J3aFUx7_JcxzzN5b5PqV8KUxL3PZEUNNtn58Wpyt_lqrM5bJpVMrymLZcIveecW5TIdMG_Zy-kSstVeMNHRtUph_qeopEoM0nA3pF8uR8Wkd6O2StQb61MQxe8dwD33z6fRhzIzihiQag6f3bQAwbhyofGeaF1ugCObhMCwPIqltB_kXYNEHIoQVMHbt__tNsg-jkHVUwmu_TOr56iktb56cmWp_35AcdpY-8Avd4HNn0DggA7ipKwnU6G0DIdnzyVr9rUlHE7IoGcZbBmewBj07NEx0QTOmvePmlhVvVvNzz_GS6IGGqIRZtNv1XEAD5jI7gK_6fIApvHCe5u8ZkxLsPBRQtpIUt9tFuILREpQpfLfpRdb1QcAZfjCXI5nzgHy48c8oW8bc0Qfx3vsXC4TocWKk9ClpEkoAaQ_yAkc_lDw5st-zAlJF4Cm86uIrot-RyuZ_5KfOXd-pe78LUIyxGspUn48c2tBA8kDkkBCDuwmuul2ewnWfJDlKGYFuluTWLxpiivyHeptsOmVP3OFcm639z5yDk4yU7JjkH23HKEjS3IU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxIVm2EViSSZEak2yeh4Yfg1o7sk9PwUcdjeQpQpdCp60gAzvd3x3RyB9dD3mkB2iLZmy6AzkxXmj4sjJN4_eZufy4rMvZhdV7-9d0q3MLSuRrgklNw4Xoy_rEUxtPx7LmzLOgL6RDgL4KPFp02O9JOkAlgW6YJYOo2D_OzsiKI9pArXojj_jwpW1itzlamFvArSFk3N7AJgIaXdMayefOBAYUmcjEgWRIl05FcISZtNmzLPm-kg5Kw2auLiNGzGvrjKozwSDiyMVpe9eRrEdriXJDCDNnYC2c3zzJV_K61c2bf6tW-Fp0xNNipz7-WXV44m48SUZyFbb5QHLUJVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WsBCBcgcNHacG-SyNinkRqddEA4TTwfvuQv6HqZrbzPQ5YUi41UlftEhTKb5sO8NgKgCDAOeP6n0lcPCr1MPv5uZLFOQhVZJIIP9frLz8w0egTA4JjOyHrgJR4MPYJXud5l1S5U-W8amr_6iduf55ei6wJxEABsMRqdYu_s4DGX3QJMoinq-0DAXd7Tx-gzxKCgJsCz1PmtnIxlzC15iOrUHApXKbDNe30hedA6U_b0Wcp7zvDGbhzYByUG-fjH110JfA_HztvbssTf0Ht0SLfXwYkAI2GNsGriSFfJBolPlNAHDjIjVLaSpGayLmWe5d3Kqtyz_EJ91xx7X1hBOIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WsBCBcgcNHacG-SyNinkRqddEA4TTwfvuQv6HqZrbzPQ5YUi41UlftEhTKb5sO8NgKgCDAOeP6n0lcPCr1MPv5uZLFOQhVZJIIP9frLz8w0egTA4JjOyHrgJR4MPYJXud5l1S5U-W8amr_6iduf55ei6wJxEABsMRqdYu_s4DGX3QJMoinq-0DAXd7Tx-gzxKCgJsCz1PmtnIxlzC15iOrUHApXKbDNe30hedA6U_b0Wcp7zvDGbhzYByUG-fjH110JfA_HztvbssTf0Ht0SLfXwYkAI2GNsGriSFfJBolPlNAHDjIjVLaSpGayLmWe5d3Kqtyz_EJ91xx7X1hBOIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu_vv6cvoKrHdiSe1RE6n_Haqah5232ivkD0ErN2UhU6GTBy0wdYAfizEry340q267Y-xbfBW80StXKJS7k_UW8SMHOS2yPZ8s2ikfnvKZKVi2z8iktJC6mIo6qK-OK9sVdM1L_NzbzynLm8d5RMM4CHbGF-DldXGKZJBPThZIT7VoNGXcciE12i_wmRvQzmAnANTpJFB7mtudyKk3c2QzoxgSLyrXhMd7iR7tUAtH_cf0RpgSFagviWPHmcsaf4uUfaIQskqJCJ3jQBUqKOi7AIHkrgABFHZUiJLOzwNiBUhkv3pY7KtpATSMHR99hEvjtkFCnAVrPR3KGjr8Ldhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0erLR_u61_5mxbOplYjTxT07ZL1hLKieGM3dmI7QOv7IVqSv_hB56HQKUxqhQYsQQOsAMCTfqg-K_CdQogIAggTPHZ-D9vfb58b-gL4wYuodrJjQTqmZeEZ5640v7xxqy2x5GaBpkjz6DHwpNSLGz8V5tl4JcjAYIb3zNYwGO1U_rEVm8bB3T5bAlK1D83g6X4Vdu9njVSKdxCtyOGX5-Q3m6aPsCH_Mcm9jHYRhJ-9QWvfXi16wQuUwJFWNnpw-6ByoWJrZQ52fdL9bHiTBJi5TTYm1MiC4IZei8LHw_t5JfZNGOl1Fck3OvFWn49B5lPRlOiK8YdAKVWmhFo42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDPpj6EupKl-V3ZUqA5pugKOUfbWY4R6T2611GDUBKfUVF_xpIq8iu3dS3rVkqUOwZ1mk_8v07tF_dpQSKjp2dG5PoKzTUtAvAlWUylYHc69OKHRqyUhTaAdVQg38NG_N69ShGjIS8veH69lsg69F2ifzs2P5zCQq0UeqsA8B62JHsZmyp9eIAD_Vl2yh3YpJRPjVgZ17kNdNvkv1ZYlxNFoCqnEoEzuNLea_ya8IFqYBvn4FkuwbrCCYFD5Xk4b4MrNLgkk6iis9rQR0bVyftV9axtXbnxupYLtch7yBN-S4PhnBbnXfDGij68qcvfaaMfKE1sVRsHwRWdT9TpnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IMPQDBXtD7dQWggunkwzMJhmU9oiejsLTHW7-wIvKQQOYve7PN6cTMNwGBpSiDeXvE6M_v-BKppIyeMSXOqBDosTrphd41_rHpmgpOaHSw218AQbcZe4aGm4e5LKFp1_7c6TZu5BnWCh9t7pmTf3oawexIvoErn-_20UlXOC4KD-iae2QlKOuUW2Y0JROrdHJApj5zbm7mBqzeKlmctRohatbgcZdyFBW0ue0KhW01e__ReXGLtMVLbnWWaAXhn-u3f8WK3NA75Z6Esgg3R7EXXXu2EWd1woJc1cvyHCtIeDRQThJD5uRGHWG8VEC_8SYhqPftDEqeoMMxBBpZUUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IMPQDBXtD7dQWggunkwzMJhmU9oiejsLTHW7-wIvKQQOYve7PN6cTMNwGBpSiDeXvE6M_v-BKppIyeMSXOqBDosTrphd41_rHpmgpOaHSw218AQbcZe4aGm4e5LKFp1_7c6TZu5BnWCh9t7pmTf3oawexIvoErn-_20UlXOC4KD-iae2QlKOuUW2Y0JROrdHJApj5zbm7mBqzeKlmctRohatbgcZdyFBW0ue0KhW01e__ReXGLtMVLbnWWaAXhn-u3f8WK3NA75Z6Esgg3R7EXXXu2EWd1woJc1cvyHCtIeDRQThJD5uRGHWG8VEC_8SYhqPftDEqeoMMxBBpZUUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHqUmtx3qL8XGZCOqcqWpSyZCAEZCzIt3LrcmZjm_9mqyz0-Idt24TrybtIQm5xFncEZGl2ExxHw39rLiVmNTg2W_QydGGfP06LKuQcThNwRPNHV-5K7e_rMVqNvSbY8uzTkdq5TFQiIrTihGPxt5_cZ6Xk1zNwCeotZ6rDQ8MZTjSyUVa_w9tbW7GImQia8q7z0qatpRpuxLa9PCedHtW-zQGDoQb0N0TJBxtb0d6VnRjRrZwrX0glSoDVig1RULEKRBHmgSSCs541fvXfob6M9GRcF17CM6n0ZXK-IYPVe6zSQ2WfLaECg0uU1TdrUggkD3gY9jtJjAAcichE7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3wL2u9ILlz3Nh6_Frl2zWCKFsGY6Dich9sI-ZxvXwgt7J8WHtlGOwRRSA53d7L9v5scZc7L9Hj01pOxUecHH7LcoSLrcnnQBQVvG-bhVipjtdXpIg5eCRIJHSASiZLtpqli1mcMxFTU3Jvb8vF4sTqTotpNu67s5X0Z7ZNYZUEYkGiIy0ni74DhSPhPPeZn_w9lME_kV5ePZKagNkGKX1yNNBzMNO_NW0Cg6smYum_Gw7e2xNDxLz22vNjXlLQSGRFhD2WSUIaCVKPzdw0_bCymySCh4dZCvWuuNAhSL9XTry4KBHiTU9r4hP8wMhnM0p0bhMeuAVssJ9vF4zCO7ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu3wL2u9ILlz3Nh6_Frl2zWCKFsGY6Dich9sI-ZxvXwgt7J8WHtlGOwRRSA53d7L9v5scZc7L9Hj01pOxUecHH7LcoSLrcnnQBQVvG-bhVipjtdXpIg5eCRIJHSASiZLtpqli1mcMxFTU3Jvb8vF4sTqTotpNu67s5X0Z7ZNYZUEYkGiIy0ni74DhSPhPPeZn_w9lME_kV5ePZKagNkGKX1yNNBzMNO_NW0Cg6smYum_Gw7e2xNDxLz22vNjXlLQSGRFhD2WSUIaCVKPzdw0_bCymySCh4dZCvWuuNAhSL9XTry4KBHiTU9r4hP8wMhnM0p0bhMeuAVssJ9vF4zCO7ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=EFp2J-lOlO-4DQJwSen7dKEaN0XMi6oLubptuSIPm6W_V1e1h9nqOCmimsliqthbBFs3hneurMk0YFELvLqpN5y5uJMgsNmLMxGuICbW0aSSkQ7ybcrSPaxhMY4Mm8Fref6mK4kn6pydn4x1mL_sP40COAFK9hqzstRzEPljgNbAExIOWLlcDTGp1azWtALfByja1qo84bS5jXNPOtgtBcIo-Hfgivq8C-2iso8syiSMCkHy4k2MSx5tCuLhXvuhnE5nAZ5H9oDCoy-PukESPBT2Q1aipBttecJD4DzacqF4zfWMwUwqvdmaEWwe1KDkXK2WGz73upYCVXpzCLktyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=EFp2J-lOlO-4DQJwSen7dKEaN0XMi6oLubptuSIPm6W_V1e1h9nqOCmimsliqthbBFs3hneurMk0YFELvLqpN5y5uJMgsNmLMxGuICbW0aSSkQ7ybcrSPaxhMY4Mm8Fref6mK4kn6pydn4x1mL_sP40COAFK9hqzstRzEPljgNbAExIOWLlcDTGp1azWtALfByja1qo84bS5jXNPOtgtBcIo-Hfgivq8C-2iso8syiSMCkHy4k2MSx5tCuLhXvuhnE5nAZ5H9oDCoy-PukESPBT2Q1aipBttecJD4DzacqF4zfWMwUwqvdmaEWwe1KDkXK2WGz73upYCVXpzCLktyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ll9XlEVMxsgE8rC1uYKUWCGS7JWLapSkelOKzu5S4fRR7vB6q1ODoS9AE8-qxaVa3UPc3FTfFkxHTNA9CxyOXptTEl20ETHchXAX25-Kxy4S_PqBJGZW4N4EN_p-tsJ5_7kMAdEYAETEBGvUOeYPdIQNxT_4sGyML4hF-NfEOBhAN_yRl1cNqs5QRHhuuXS781MiWkTbI-Y6jqm9AuklTKH-GvFRT6PrWMPj4cl-OSHnUrv9vsyxzJz3J4LneDGTwIQhXDPr-lx_G0rubcu2GXJH29_7TF_7ejxmtcDrHUMFVZj49GEaAzTDfIuWGYmL13ze1k35IlitWDWgwlawMbnxVwxPl3ahLKoJCk-xK2rdtYU76dXxslF-lC1KTL0AzR9pKPQN3unifuBf5-Ffeu6h-6JBDyAXDMP3sDZRKsjxmMJflnXqXQ7s-_3QxXUoF0DHMsLrxAWGIuyum6rXsVzo3jfGbd1XK8HP2nYGLu5L_atfQ3kjDyA1r6fKSVTyAC_RbWhMOrVaSAUTR9Of2Gzrc7LSe53Sj1ujC8exEhImRstBPPd1jXa5jHP8EqvT9Qq59oiwuiR6W3WOWMNRUuL5l4CJj3NUTtSsfOSmtp7sPsstLCLcv3TMBwN2CIq4_VozVu6V8l4MOiaZgO1V-pwDtIxqcViRMsdtbmsdS2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ll9XlEVMxsgE8rC1uYKUWCGS7JWLapSkelOKzu5S4fRR7vB6q1ODoS9AE8-qxaVa3UPc3FTfFkxHTNA9CxyOXptTEl20ETHchXAX25-Kxy4S_PqBJGZW4N4EN_p-tsJ5_7kMAdEYAETEBGvUOeYPdIQNxT_4sGyML4hF-NfEOBhAN_yRl1cNqs5QRHhuuXS781MiWkTbI-Y6jqm9AuklTKH-GvFRT6PrWMPj4cl-OSHnUrv9vsyxzJz3J4LneDGTwIQhXDPr-lx_G0rubcu2GXJH29_7TF_7ejxmtcDrHUMFVZj49GEaAzTDfIuWGYmL13ze1k35IlitWDWgwlawMbnxVwxPl3ahLKoJCk-xK2rdtYU76dXxslF-lC1KTL0AzR9pKPQN3unifuBf5-Ffeu6h-6JBDyAXDMP3sDZRKsjxmMJflnXqXQ7s-_3QxXUoF0DHMsLrxAWGIuyum6rXsVzo3jfGbd1XK8HP2nYGLu5L_atfQ3kjDyA1r6fKSVTyAC_RbWhMOrVaSAUTR9Of2Gzrc7LSe53Sj1ujC8exEhImRstBPPd1jXa5jHP8EqvT9Qq59oiwuiR6W3WOWMNRUuL5l4CJj3NUTtSsfOSmtp7sPsstLCLcv3TMBwN2CIq4_VozVu6V8l4MOiaZgO1V-pwDtIxqcViRMsdtbmsdS2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=BafIbnVLPaUsLq--sdHJ081ZqxUKqMaQ4BZYgYnne3M8FSlIYvGpFq5tqZQO2Lyx9wKA3hdajV94L4_zZ7jkAXb1e6xUhdI_Gth_GSwIUz_bdvW0bzUUb8y3AhRMt2rBs59kgRVxtVaqj2GK1E-GKVt7VDmWwBRwkyUolD6UqjVsoVO_C5RHHEPaPZbaSIvCbh6Tv_gzrnmeNZJ1F-LF2QMPQxEodiAhO-3J-w0uxi_seMbW2J9GHTAFCIl4Aw2SzXxtX4AVmYw01c56SCh9WG-rRBez9OhtVKJbwPgxnTQiRFFTXrWtizNydnrdRZmbVa7wQuvPC8EC57vOhe9Wng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=BafIbnVLPaUsLq--sdHJ081ZqxUKqMaQ4BZYgYnne3M8FSlIYvGpFq5tqZQO2Lyx9wKA3hdajV94L4_zZ7jkAXb1e6xUhdI_Gth_GSwIUz_bdvW0bzUUb8y3AhRMt2rBs59kgRVxtVaqj2GK1E-GKVt7VDmWwBRwkyUolD6UqjVsoVO_C5RHHEPaPZbaSIvCbh6Tv_gzrnmeNZJ1F-LF2QMPQxEodiAhO-3J-w0uxi_seMbW2J9GHTAFCIl4Aw2SzXxtX4AVmYw01c56SCh9WG-rRBez9OhtVKJbwPgxnTQiRFFTXrWtizNydnrdRZmbVa7wQuvPC8EC57vOhe9Wng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLO52Df2894TCpuSnbZNpNhnzLJh6BOdVWQIku99Tlv3Vuqrb-CZrr_2645-OPGbJu0CDeLyIHk0GwxaYSge50NPGiwnI-eA1lIzz6RH2T_qCbHvUcE39osvt4xOs3DcUOfDb2MluQjkYLQkUylSWFw3j3Cn0Vz0yVDAuzZaM8J6j50b74sNkh9bJuKkRp1dPTFlmhjG1y_vU_y7UO05MGD-_UUqjzVXZ6_pATDpgmvAlmafiUIPqQ0Z91LIDNuDbuMoiLAckb3ZAMFlNNYK95NnpVbrZ8yZPTGIijC_pRLEmEWFIQCF6BA1KcnFa4IKHUsvVeRCJa_N3ytbxMxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=vKV_1C-kB_qWUJch3JPwSfVJbGHp9bKtvoGWWAq1u2ahwuHzKaB2X1D5z5jX7xJDdiPrfwkqj0zfpvlwMe3VAWxc3G-Kj4QZvmKOVxXlWA8CeRli4mMCoT69c8eddz6h_Sz5SV8i_SgELwiy1m8cf5dkcAuH-nMJr135rbAKNSva2bbwd9DLvFPhwwY2n_T0vU1uS1hginpKGAjKXSxeUX0ZPu6j3I2VXORKhwaNYHgdT5qvEdPeKQQUFOEAmJfFjQqYdFlojYIcN-SNoeh2GLu2c0KB0_eBbCTTQ8cXbPtelGMLLUTj4-wXoQlfMDcDuCyB4dj42hvmmFgMA5kGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=vKV_1C-kB_qWUJch3JPwSfVJbGHp9bKtvoGWWAq1u2ahwuHzKaB2X1D5z5jX7xJDdiPrfwkqj0zfpvlwMe3VAWxc3G-Kj4QZvmKOVxXlWA8CeRli4mMCoT69c8eddz6h_Sz5SV8i_SgELwiy1m8cf5dkcAuH-nMJr135rbAKNSva2bbwd9DLvFPhwwY2n_T0vU1uS1hginpKGAjKXSxeUX0ZPu6j3I2VXORKhwaNYHgdT5qvEdPeKQQUFOEAmJfFjQqYdFlojYIcN-SNoeh2GLu2c0KB0_eBbCTTQ8cXbPtelGMLLUTj4-wXoQlfMDcDuCyB4dj42hvmmFgMA5kGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=efxa4MsOZtSblZ0mMueD_jiMSKW8najdFGbaHUbAwHeJxqDr2mwS_-lHzwPCBN2YqqyPIjAqfwhyuO9FWRemSyu-NFxM2KDhCCaQ_p0XsUpbl652IBX5I_Q2R8M2oBEn0no1dnt9F8S2mtq8iPYd1ylUlZXPFiGA-0gMJksG_ETf2KBXVt1j0OKLK5bXDz-pgNC2cecmIjC6D5bHd_ibMl4bnNNvOPkDxJA8fciCQk4v3mETve7S25Acl7ZzeLGYhDk7OoaI5KF2yHYTrw9c9Qh2H8rbWMeto4L0KKQUkjURZ7g2rs2uXIkJajMFpt7enos21B345WfFc_LFEYTpuoZLoPFkYD-YDnFg8eZpbzU6nmg2gwnhQpJZU-VNat-VemnC8JSJxMzcgxFQMsxcuGTW_bZUU55oHX4AHX_9AxPpadPKB0OaWaBpU68FaDsJd4mVAivUx3ejo62dDiUkNL9_GXl72mqGq8MitN6h-daDk2iIMdz5lTp1dcCFL01wzoQak71AA7kSjgmh5f7JHkeJN6n28mKdiP-Esp7dwBWzTIyHotf6C1ChZlOhI22HSkybrUkEqeZhgY5k9MXoEzMy4Xfgj92fYUPUmk_DM6pSdY9OyfrQ7PsmXQ7HU95LdIk81hpFOekvr8upqZuV1DXqkkCtc3z91IRa_K0x3mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=efxa4MsOZtSblZ0mMueD_jiMSKW8najdFGbaHUbAwHeJxqDr2mwS_-lHzwPCBN2YqqyPIjAqfwhyuO9FWRemSyu-NFxM2KDhCCaQ_p0XsUpbl652IBX5I_Q2R8M2oBEn0no1dnt9F8S2mtq8iPYd1ylUlZXPFiGA-0gMJksG_ETf2KBXVt1j0OKLK5bXDz-pgNC2cecmIjC6D5bHd_ibMl4bnNNvOPkDxJA8fciCQk4v3mETve7S25Acl7ZzeLGYhDk7OoaI5KF2yHYTrw9c9Qh2H8rbWMeto4L0KKQUkjURZ7g2rs2uXIkJajMFpt7enos21B345WfFc_LFEYTpuoZLoPFkYD-YDnFg8eZpbzU6nmg2gwnhQpJZU-VNat-VemnC8JSJxMzcgxFQMsxcuGTW_bZUU55oHX4AHX_9AxPpadPKB0OaWaBpU68FaDsJd4mVAivUx3ejo62dDiUkNL9_GXl72mqGq8MitN6h-daDk2iIMdz5lTp1dcCFL01wzoQak71AA7kSjgmh5f7JHkeJN6n28mKdiP-Esp7dwBWzTIyHotf6C1ChZlOhI22HSkybrUkEqeZhgY5k9MXoEzMy4Xfgj92fYUPUmk_DM6pSdY9OyfrQ7PsmXQ7HU95LdIk81hpFOekvr8upqZuV1DXqkkCtc3z91IRa_K0x3mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2ykUqYBityrrutQlxheGcEZNYB8-TO9f2PJxWWfKh0smM_PhU4VgXtoz9IV1K9ejZp4B64_xGbZn5SuTk8Lx54ifLVhmvp7JRMmrkLAMnjSvCU7Kpobxbcxele8EXsmGWqFmIQqxc-2F3BGICdSnCzFA-HE3qjM1sW-mVM0PgKxr2TSPCoBb5I6cFJHuiewH46-jH9Cn1SzOxaMkJTRdnKC4XN-h1JxeRF9qfsUh1bDuLBbkpcR96AJQN8dYEX_82Q7T6BNWLI_8PGoSD2L86pYzx4p-trE_l181jgjBivxj_A7Fkv3CUDWDCD1Eulq9HSAWgmsdUWod-PPenx0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZgrAodcjNCp8pCJ501AJkUdmHQQaygg9EqDjH7PFur4JhL5_i99NX8ndnC0q8QjN4t76EWlo92zWRw8QauMmFlLSqeX1hrcgMilcnNAYUJB_9JubAxYZFfCTVXLaHP4D6MqlPI9R6_pApFkC66sfNIruZhq6OyqXDIvKWjd2_GdkkFEiRVxrs4gsxC0DyunPRjSkN8pxKRbB8QmdmyeWclhGVAfYvb3LJ1xAH020nOpJ9hYIser5S3flcQ5C0IPIM3qSKDI2qobCV4WMY3CZpRvoXysVEXDcefeCq01PquAMGcBuIiJpaopb145wqsAkgpMZI5UaOI1qqUYbET1KtlpQY0GTJoTAHB_C5le62bX_SJeak_ZNnaRoE-gqb7SodrzlcX6VKWHgMFF3EjRvyJBN6N1Hqg4IYCMBGQWDhXOKpU5WtFgQb7812_5vcBCGbYX3rK-JxSDOBZh_MJ61Dygy0676-AYmrPalnXcBm9NylTElBZnqvf2xNIWdDDOAqz6phueAkVX5hwu-oK2O0cp3L-9K6prqcVooIqep-wsioi9YT0-8A5TvNq0y-WCcbN3XX9WPAgAScYw_q4Uva4AJWf-YzeTyrXTtn4KjdsK3H13C0EnqsWXFfpk6SCuA2kb_qcc1OzwP4iS2p-g0PCGR_CUcc9BUw8RY1Iwn-z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZgrAodcjNCp8pCJ501AJkUdmHQQaygg9EqDjH7PFur4JhL5_i99NX8ndnC0q8QjN4t76EWlo92zWRw8QauMmFlLSqeX1hrcgMilcnNAYUJB_9JubAxYZFfCTVXLaHP4D6MqlPI9R6_pApFkC66sfNIruZhq6OyqXDIvKWjd2_GdkkFEiRVxrs4gsxC0DyunPRjSkN8pxKRbB8QmdmyeWclhGVAfYvb3LJ1xAH020nOpJ9hYIser5S3flcQ5C0IPIM3qSKDI2qobCV4WMY3CZpRvoXysVEXDcefeCq01PquAMGcBuIiJpaopb145wqsAkgpMZI5UaOI1qqUYbET1KtlpQY0GTJoTAHB_C5le62bX_SJeak_ZNnaRoE-gqb7SodrzlcX6VKWHgMFF3EjRvyJBN6N1Hqg4IYCMBGQWDhXOKpU5WtFgQb7812_5vcBCGbYX3rK-JxSDOBZh_MJ61Dygy0676-AYmrPalnXcBm9NylTElBZnqvf2xNIWdDDOAqz6phueAkVX5hwu-oK2O0cp3L-9K6prqcVooIqep-wsioi9YT0-8A5TvNq0y-WCcbN3XX9WPAgAScYw_q4Uva4AJWf-YzeTyrXTtn4KjdsK3H13C0EnqsWXFfpk6SCuA2kb_qcc1OzwP4iS2p-g0PCGR_CUcc9BUw8RY1Iwn-z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rlcBzkzS8yQTUBl0hnOUpLz7P1Ru-fPpgiGg4aqRTIgWnPimhb9hSJ0znEAPbQNV1OAnQf_CdKc6a57YSeuPDz765R-CJHf4YouXdem-PCmpnk2RSEhb5uuNU5wVrDkQdbsyzw57XCPC8uUF3hABbhatVoECd7jpmISgB-gtZ1f87iBLWWysTEvIGZkOPkv5OP-YDdHHo9DtCEo8HHygq1MQdgqgwUyzr9QYNHxmxmCfJ3oZnipZnRUMNMna8GucE4rbv4S2L9T70X-1eZdZN37_tZKlKLZ70WHGJUFGIrqeTCezt51veZA9UN8pwVYkTIIu7b7iEGyoQ3I_x2bG7xmt69Q_wMscXVh9y-TXKJt-aXZmscKGEEh4W0xpC1PNzgHg8DDMI6SWgMoc0l_W0SIOxrK-8nwU-5_OkmBjiN2OEG4DktmLQw5zjN2WPj3AfvDLX0TDikXMs34ltm-KGZOngX8Xb_bw-oGbTay82ud_IXNQe0sV3FNU6k2zpsqhO-ImxISUn7zE_Ep4fVfxVDtAzF7tTwsq9zr1YaIanwpV_uujp31CsvHeT0Sm3JhmZM-1_GDlhLudzwbY25XuQ9R953xGyoLB2Z1kJnr8Vd_LSrgua4yp-jHXMRa53V5LzlIztbmTTtqp4QXKheUqqjEzCzhrwsi6bkFJSejzsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=rlcBzkzS8yQTUBl0hnOUpLz7P1Ru-fPpgiGg4aqRTIgWnPimhb9hSJ0znEAPbQNV1OAnQf_CdKc6a57YSeuPDz765R-CJHf4YouXdem-PCmpnk2RSEhb5uuNU5wVrDkQdbsyzw57XCPC8uUF3hABbhatVoECd7jpmISgB-gtZ1f87iBLWWysTEvIGZkOPkv5OP-YDdHHo9DtCEo8HHygq1MQdgqgwUyzr9QYNHxmxmCfJ3oZnipZnRUMNMna8GucE4rbv4S2L9T70X-1eZdZN37_tZKlKLZ70WHGJUFGIrqeTCezt51veZA9UN8pwVYkTIIu7b7iEGyoQ3I_x2bG7xmt69Q_wMscXVh9y-TXKJt-aXZmscKGEEh4W0xpC1PNzgHg8DDMI6SWgMoc0l_W0SIOxrK-8nwU-5_OkmBjiN2OEG4DktmLQw5zjN2WPj3AfvDLX0TDikXMs34ltm-KGZOngX8Xb_bw-oGbTay82ud_IXNQe0sV3FNU6k2zpsqhO-ImxISUn7zE_Ep4fVfxVDtAzF7tTwsq9zr1YaIanwpV_uujp31CsvHeT0Sm3JhmZM-1_GDlhLudzwbY25XuQ9R953xGyoLB2Z1kJnr8Vd_LSrgua4yp-jHXMRa53V5LzlIztbmTTtqp4QXKheUqqjEzCzhrwsi6bkFJSejzsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=h617qlz5BhTpt8lHhsqXG0ccySPIj5ImmP0RHgiHFa6thc-VtK6OIprCQ2UMfNV1a1QFhvKPQvOYSQC4fr5wVQPJVYgRvyf9jbnfoEi5RudMlMdSBuZ_uYo-6jGu8ecgbbbpC-dye078pQGuHws3hrCf7a3JI_sFBOMHPx0jLVzyDH44kiE9B7MpdPxx6mmfc1cS9lLUgzLJqKf-CSzo2-NlWqBEn2VNj4UFnNo6GQkVGORRnyTWyJ0rBjvX9QlorYyRMLT4Ihsq0zuYlgjgeIEEcbElw3Y8ORR4fyYUcd_RSIyQyWbRQhS_GhWyvaNtX8Y8vk_URcGu47xiBZ5y7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=h617qlz5BhTpt8lHhsqXG0ccySPIj5ImmP0RHgiHFa6thc-VtK6OIprCQ2UMfNV1a1QFhvKPQvOYSQC4fr5wVQPJVYgRvyf9jbnfoEi5RudMlMdSBuZ_uYo-6jGu8ecgbbbpC-dye078pQGuHws3hrCf7a3JI_sFBOMHPx0jLVzyDH44kiE9B7MpdPxx6mmfc1cS9lLUgzLJqKf-CSzo2-NlWqBEn2VNj4UFnNo6GQkVGORRnyTWyJ0rBjvX9QlorYyRMLT4Ihsq0zuYlgjgeIEEcbElw3Y8ORR4fyYUcd_RSIyQyWbRQhS_GhWyvaNtX8Y8vk_URcGu47xiBZ5y7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=iowbOn-CjB0i1i3aXaYYECjiR5rA4Fp9sddGp5LINNZB5sKo4qxff9JYwpqvfI3r7icQSQBx_re8yx2GC91XA6P6kIcrL7H2_3haGtt2wtsqYbBzAHApjRApvgwMGV6yHYdEmUclleyGpkrLw1JwGdWZYYlWPGOAg_yBQiL5uYrBsFndnBbu1CqD6TeHP82NPU4BtLEyHiB7NSST1ICT5DpeqlaVA9zpZ6e0siLGQwmzP84HVR_LgXTaOkeMHl4ZYyDROe6-dgQ2hLTxzn6pqnLRScAbIXAoB6gnleTr7MFKza9h7-hHx-iWnIc-wFeBGT7h2_l-_VZWo_OXoVEWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=iowbOn-CjB0i1i3aXaYYECjiR5rA4Fp9sddGp5LINNZB5sKo4qxff9JYwpqvfI3r7icQSQBx_re8yx2GC91XA6P6kIcrL7H2_3haGtt2wtsqYbBzAHApjRApvgwMGV6yHYdEmUclleyGpkrLw1JwGdWZYYlWPGOAg_yBQiL5uYrBsFndnBbu1CqD6TeHP82NPU4BtLEyHiB7NSST1ICT5DpeqlaVA9zpZ6e0siLGQwmzP84HVR_LgXTaOkeMHl4ZYyDROe6-dgQ2hLTxzn6pqnLRScAbIXAoB6gnleTr7MFKza9h7-hHx-iWnIc-wFeBGT7h2_l-_VZWo_OXoVEWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sws_fPYjk0QNib3vmSlPJrBgjUQswTm8hM58aU6l7Fskr5TzhwhFu219xOSE2kd8TyvAGFjTB6IfxYGa24KCtJJYybbWOLffEni5nuGuzUjE3KC2-1oPeaaFPETe3MD68JA80uBWKYKjEtbllePPtHeWROsrLVqYiGxIZL1zJ1BDPob8ltmOQb5Pog-a6DQhUOKrZ6ZdcTqXeOVkrP9jKvJnGuiuUc_44fTdl655wZYFwS8IIlxEJBzz6fpI60nUmwjQUZ4ctr0wF14F1YIQS888bmmqb8DxsqjPgCbRAhdeR1zO4HmW_ftH6qID4HZ4YtGh2A9irGrl8q8Pr2E9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=sws_fPYjk0QNib3vmSlPJrBgjUQswTm8hM58aU6l7Fskr5TzhwhFu219xOSE2kd8TyvAGFjTB6IfxYGa24KCtJJYybbWOLffEni5nuGuzUjE3KC2-1oPeaaFPETe3MD68JA80uBWKYKjEtbllePPtHeWROsrLVqYiGxIZL1zJ1BDPob8ltmOQb5Pog-a6DQhUOKrZ6ZdcTqXeOVkrP9jKvJnGuiuUc_44fTdl655wZYFwS8IIlxEJBzz6fpI60nUmwjQUZ4ctr0wF14F1YIQS888bmmqb8DxsqjPgCbRAhdeR1zO4HmW_ftH6qID4HZ4YtGh2A9irGrl8q8Pr2E9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KYmQgwz-YfGPs_1mPOcolP-8qTO2Dx6KOySw3CL7PPcTgxLfvlTHqSsANbOOEFDKWAogEdamxn6hk299vdHTscDbiWRlAgaTMNtmjB3As-GDfdppu-NyYuzC_zQbnsksZPd-ynRMsnipweWGpgXZE192rO-YImaH-Dsw5wB-3f1Kx_04tzZ2kERtFpi0GzMYHLvrqnQmxFAJFMowvytwzDACpMRDWjjpdqyMHbymt9uihkqH05_TGWNOU7t6aaldXQGwyZiUn38f-qwzHx7CznyrzxjwSScRYFtQFbmvmUdhuRT-5jHkhtu9JEVND1Fukdpxe4H4X__E2kHSsiggKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=KYmQgwz-YfGPs_1mPOcolP-8qTO2Dx6KOySw3CL7PPcTgxLfvlTHqSsANbOOEFDKWAogEdamxn6hk299vdHTscDbiWRlAgaTMNtmjB3As-GDfdppu-NyYuzC_zQbnsksZPd-ynRMsnipweWGpgXZE192rO-YImaH-Dsw5wB-3f1Kx_04tzZ2kERtFpi0GzMYHLvrqnQmxFAJFMowvytwzDACpMRDWjjpdqyMHbymt9uihkqH05_TGWNOU7t6aaldXQGwyZiUn38f-qwzHx7CznyrzxjwSScRYFtQFbmvmUdhuRT-5jHkhtu9JEVND1Fukdpxe4H4X__E2kHSsiggKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=j7wtmaNtUCWM9mgVQqNBg1CcnPn7a5ngt44UZGN-EOdW-NDE4dkL5DNQna21ROk_v98d16euv2l2cxZJeBPJ2Q3OTcR4xb6HQcv4KYHu6HE6QOkLDzIjRTjhFPcmixnb7O9OZgtfVbE45Hp5Mry1ce0vEt1OQVFDnWPYv4kqv6D5gGN8IBbe-lyl4ageBgBZ5qOZBO6rqeFcAQXZ7qaX2OpQK-CZ4bPteWHb4T0oIGZHxbevykI9quAmDuYFWT-QIWYegqnIQK2VRS9G0NibZVTou_kpxrEU66sUuumGLsKNKhlrOFpWQaND_9gVZ-OtyC91Hs7NyPSpDESAo0yaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=j7wtmaNtUCWM9mgVQqNBg1CcnPn7a5ngt44UZGN-EOdW-NDE4dkL5DNQna21ROk_v98d16euv2l2cxZJeBPJ2Q3OTcR4xb6HQcv4KYHu6HE6QOkLDzIjRTjhFPcmixnb7O9OZgtfVbE45Hp5Mry1ce0vEt1OQVFDnWPYv4kqv6D5gGN8IBbe-lyl4ageBgBZ5qOZBO6rqeFcAQXZ7qaX2OpQK-CZ4bPteWHb4T0oIGZHxbevykI9quAmDuYFWT-QIWYegqnIQK2VRS9G0NibZVTou_kpxrEU66sUuumGLsKNKhlrOFpWQaND_9gVZ-OtyC91Hs7NyPSpDESAo0yaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jPDGzlMrmiY-TIIXkZRPz4x-fa0JD7nYno4vZYcs5joK0CqOxW5PRZdf8c5Wb_EZ4x5QgVAKLlx_o3NuDfEZBPPoFZIT0Wrv_WO3TiaTSQ5pWwAP7irTU9-HNF0w2luVNAf9_VroqbcWrkbkGumXGP2eWdJozQ1Y6JhLwoZVgrroLpZ7HdUHQCWDHhH2GaG3FJXiILCeArG5UxHsD5CwqCoQ1NjssQ83M_G65i8LILJDalLi11LecrkV01XmDWDL7xKTFY1sV-vomwtWGtBeoCTheASQRiCI24vIZkgpiUA_PlqNFtK_PcvIQNzP3BjDzroYLRUtadyvKWI427GnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jPDGzlMrmiY-TIIXkZRPz4x-fa0JD7nYno4vZYcs5joK0CqOxW5PRZdf8c5Wb_EZ4x5QgVAKLlx_o3NuDfEZBPPoFZIT0Wrv_WO3TiaTSQ5pWwAP7irTU9-HNF0w2luVNAf9_VroqbcWrkbkGumXGP2eWdJozQ1Y6JhLwoZVgrroLpZ7HdUHQCWDHhH2GaG3FJXiILCeArG5UxHsD5CwqCoQ1NjssQ83M_G65i8LILJDalLi11LecrkV01XmDWDL7xKTFY1sV-vomwtWGtBeoCTheASQRiCI24vIZkgpiUA_PlqNFtK_PcvIQNzP3BjDzroYLRUtadyvKWI427GnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qKfwi0EocYzreHxmR5xBXG9pqkiC7A_d5wX_Q9XQqlLLt-fVEnBVBtPjhX5eK_oYR-NF1Oq4dki-acvENR00gwiaDdQKMrJoK5okXKMXeQmAIErRl01xg6mUXf-FlnUrpPNvvNkO9LEGlzJtcXwnj1iUHq3MAu7K7_yq7WGbHPw9HEKf39hmp_rg8_xRtpnSryXOq2pkbpa5ik5lgTpyKDGdP3la-YkLfm4hegeDTFsc7wjjHlxjeJncrs9ugk-FWc16_7eZlfJqh1oM0DPnoOT8LM45g-B1r1CuhVCeG5sUkvZsbUfIYGSMrkPtEXypp6HbBy2ypbjmYWLD8NxICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qKfwi0EocYzreHxmR5xBXG9pqkiC7A_d5wX_Q9XQqlLLt-fVEnBVBtPjhX5eK_oYR-NF1Oq4dki-acvENR00gwiaDdQKMrJoK5okXKMXeQmAIErRl01xg6mUXf-FlnUrpPNvvNkO9LEGlzJtcXwnj1iUHq3MAu7K7_yq7WGbHPw9HEKf39hmp_rg8_xRtpnSryXOq2pkbpa5ik5lgTpyKDGdP3la-YkLfm4hegeDTFsc7wjjHlxjeJncrs9ugk-FWc16_7eZlfJqh1oM0DPnoOT8LM45g-B1r1CuhVCeG5sUkvZsbUfIYGSMrkPtEXypp6HbBy2ypbjmYWLD8NxICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKkrlPU3QBSZVBMcfuY5hw-f-jwrmyRoBZlFVef-fHrGARKrmew3eHsKenKFixTZGHROaPCvu0R6JV-yFvowcyhxlf1QfWRpcC7iCG8KFu6o5cnOsAhR0Qjgmgb6rsgNt2mC9AwMHvVMpSiA_0wlBi40XlQ6J6LiaxkyKBDHqil5HDVNKbstq75qOCI-iCEG48AMRwQXoVemzUt11aqYGk3IDWWHne48oWSpZ_aQ6zmJPwbyJDE25tcw71gjpEL5H0iFb5P0ApkbK9-DpUYs99_XFtypBY05FRDp1miy4wETd6-ahy-CNoYdfW7aW8uiYKarmB32znFaWWqT3pBdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=QbapG6RU1anBL645YVwkST6hdMYjK7uhYotVpCa1Wc8m_lud6nIQmJYvFD4qLrI_6ZVaOdg49LcJMVxfJdMPBkq8nl1BXbsVVHQlZW8ylpx9GEYzYzj_KZTC1wGj8le0wnapqfOXtbL1iT-ZndLwYXNZyZC2W4THb-_Zd6uHbCH-e347iSAoEzfYSHaz9w5E6sW5CEwDbChaOC8AjbOXrELR677QF8T_7iR-03V8FH5xJgRMlMXtf-2O0DreLbZUJhmU2uMdauskE1Jj5u9sr8NY7QtXEEgUsi2yFFybPN_MivJxekHmrfnNLdEKu72F8gThzMT6CdqzC1_HCfDEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=QbapG6RU1anBL645YVwkST6hdMYjK7uhYotVpCa1Wc8m_lud6nIQmJYvFD4qLrI_6ZVaOdg49LcJMVxfJdMPBkq8nl1BXbsVVHQlZW8ylpx9GEYzYzj_KZTC1wGj8le0wnapqfOXtbL1iT-ZndLwYXNZyZC2W4THb-_Zd6uHbCH-e347iSAoEzfYSHaz9w5E6sW5CEwDbChaOC8AjbOXrELR677QF8T_7iR-03V8FH5xJgRMlMXtf-2O0DreLbZUJhmU2uMdauskE1Jj5u9sr8NY7QtXEEgUsi2yFFybPN_MivJxekHmrfnNLdEKu72F8gThzMT6CdqzC1_HCfDEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=rP-3UQ2GDbEDCzts5Oq-TMlF70QOVBGLVrOioT2_OaJaI6ETn5orlXt24LfZVyLC-01xfG8q3nkRTTZvRk-yACSQveflOVijs-xyPW-7WxdxpqaEoJE2POb6fmHAImM6fAzSt-m0utWN2BSkBXBKcSSxq2LGwW5WwK_SWVCoFT1VWVxLsAY9YQVqwSGcoRWM8oYKlRyVeYiLM_qmxLS4C1iv6gUnkrWMsLRO2dmtc712AchVtE_icANVVSnyVJVl4kiMsVYRDhUsQZVfl3JnD9mzZtUO5sFMZPVbb8jUhFeMfPV1WiPteVFnYbyGhS6rMpgrK2DUOT5cN8HEcYGnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=rP-3UQ2GDbEDCzts5Oq-TMlF70QOVBGLVrOioT2_OaJaI6ETn5orlXt24LfZVyLC-01xfG8q3nkRTTZvRk-yACSQveflOVijs-xyPW-7WxdxpqaEoJE2POb6fmHAImM6fAzSt-m0utWN2BSkBXBKcSSxq2LGwW5WwK_SWVCoFT1VWVxLsAY9YQVqwSGcoRWM8oYKlRyVeYiLM_qmxLS4C1iv6gUnkrWMsLRO2dmtc712AchVtE_icANVVSnyVJVl4kiMsVYRDhUsQZVfl3JnD9mzZtUO5sFMZPVbb8jUhFeMfPV1WiPteVFnYbyGhS6rMpgrK2DUOT5cN8HEcYGnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=QzhaKZ5g_c4UWD3rFXhFhgQUZTXdWNi0CmVqEGsbOQK_juwL65qQCoZ8SRX_YvdaVRK9DRpaUnpf6jbksLmfskic9n9GT4cx5PjSa9x_QQS8sYn2YMQ1GqMMS2Qub98tx6HmQKqgfvRxzOWmn9NAS4A5vj4BXtHn72aQl3ZnFnlRpOG64rDYu0_vmfk4Gzi8s9kTqRpTXf1fYrHWDG-8i-alaoUC7wg5BfZvMDMVPTnpUdap2L0wSl95U9mFZYFpjz34YPsgc6-wnLj1cTyLFh49RilseIOdPqk52Lcy4yhP7pBfNGv2y95uV4j3lfDPKds112Urggfjk-IRBvP5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=QzhaKZ5g_c4UWD3rFXhFhgQUZTXdWNi0CmVqEGsbOQK_juwL65qQCoZ8SRX_YvdaVRK9DRpaUnpf6jbksLmfskic9n9GT4cx5PjSa9x_QQS8sYn2YMQ1GqMMS2Qub98tx6HmQKqgfvRxzOWmn9NAS4A5vj4BXtHn72aQl3ZnFnlRpOG64rDYu0_vmfk4Gzi8s9kTqRpTXf1fYrHWDG-8i-alaoUC7wg5BfZvMDMVPTnpUdap2L0wSl95U9mFZYFpjz34YPsgc6-wnLj1cTyLFh49RilseIOdPqk52Lcy4yhP7pBfNGv2y95uV4j3lfDPKds112Urggfjk-IRBvP5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=f_gCcbtgYlDzDSFWGo7MgwgkVpry9ft6VDCIysGNkquSHpXqy8qUxWaKdwr85mR_EItXtmxTC9YJCn9_Epui_RnJNIH9LQ8rOHGk4SRciVjSCN-fmvJoHd9OI8PRkOVQF-AUoq_DIH3DTvd6GarF6qDgbwYZzcvnu4TxIZK3xLVvcenCtSzWBfwF9z7xxArtu6iCM8wHJa_9KDNE8PnnDVB8YCPqS6H3khGgLCAXBsHeUs6yUzj_ytGv1LTM8TG-yQaZsphemR4Rf_xPrTguw1QiMKU47d2xpvUlq-TjZFj8gXXsSg4UcXm_gsIycWtcRX1nM-VE-ylZ8yum68uFzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=f_gCcbtgYlDzDSFWGo7MgwgkVpry9ft6VDCIysGNkquSHpXqy8qUxWaKdwr85mR_EItXtmxTC9YJCn9_Epui_RnJNIH9LQ8rOHGk4SRciVjSCN-fmvJoHd9OI8PRkOVQF-AUoq_DIH3DTvd6GarF6qDgbwYZzcvnu4TxIZK3xLVvcenCtSzWBfwF9z7xxArtu6iCM8wHJa_9KDNE8PnnDVB8YCPqS6H3khGgLCAXBsHeUs6yUzj_ytGv1LTM8TG-yQaZsphemR4Rf_xPrTguw1QiMKU47d2xpvUlq-TjZFj8gXXsSg4UcXm_gsIycWtcRX1nM-VE-ylZ8yum68uFzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blHfy1GkQ6rd2S8EXVIL2IEx2M295AALV3VnFS8EcLpfd3fLePpxe1ucnr-3IL7F81Juj0EIvgcNXTIG0WxvRr7XX7k_xjt_UGcQAO0Ainb_jr2xWgwufwsVH36-pqdlQmXx_wfkZaIsq2RtTvontGYgRTCyDfs-ham4v6JOtHDJZ-qlIED4ep8lIFPMa2kN08LCl4HWPdPBs54kuT4dvTnJmkq6baNq5o7gGDZ2McVbb9ZSZpOMoXPpW4BU0pSmADCUTK_mDISxAETloci07hgORSyxJio_zTqPMGYkc7rsgrS1t8VGeKK3hrPIRR19qUdIsbZ-X2CyBVk8XD6_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GWw8XQVmhV9Xgyz8mVmSsG0XL-EszOoo0Ma8XIrKTkLHjHD_AFmaL1olg3ISiaof1l2RrEu0Oxe95_gON-1JB0nCh_H4-NkFjOf6BhBVTfjc985pz_82D6VNFWPx2zIs3E8cCIlJDD3iFlhN1kPxuw7whupiuYhiyxL8SJWoJdvcYyJqgu6mmBqH-miE19j46QaifosF4m0rWUS2we4U99yMIMghxSpZr6c1dWfTpYbzMNkXJfHbI0kOIXH9CAJKgdslS28soEDXYrDfTHeBqz-eAtprOgTsIZSKs-bDTUAaAypIBWvb7_WcGLEqjbKjHgWoK6568TVrevIub91GOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=GWw8XQVmhV9Xgyz8mVmSsG0XL-EszOoo0Ma8XIrKTkLHjHD_AFmaL1olg3ISiaof1l2RrEu0Oxe95_gON-1JB0nCh_H4-NkFjOf6BhBVTfjc985pz_82D6VNFWPx2zIs3E8cCIlJDD3iFlhN1kPxuw7whupiuYhiyxL8SJWoJdvcYyJqgu6mmBqH-miE19j46QaifosF4m0rWUS2we4U99yMIMghxSpZr6c1dWfTpYbzMNkXJfHbI0kOIXH9CAJKgdslS28soEDXYrDfTHeBqz-eAtprOgTsIZSKs-bDTUAaAypIBWvb7_WcGLEqjbKjHgWoK6568TVrevIub91GOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=PaJta51XhDcC7V2FUHwI1gk7ZHb7uyuQnjnX9ADW1jT_0U8bEHtOtDtriFmPE0xaWcNWGwLkdVe9KePy43zURv2aivAOZ7XHO1q5h1E5jeaEvDlQuPgAsSKickXATLSXmJf7_Ix7k3KnaPhBq2ytwQTVoAsnveaUlyPkJpPluLy4EVM_Lfhp2kAs5EdJd6i2Vom6Npi2q5hMYBHhs8mSybWA0Y9kAy9Hgy4MQfumYme9girDqK2l2q7tL3vrTB8SV2RVY0myH4JNezVa1XYgufxwuJwgJphZVzUNGEaeZCLV0DM_07twv51JzyFJlfAdSL_ZLcoYEmiTQ9jqVc0Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=PaJta51XhDcC7V2FUHwI1gk7ZHb7uyuQnjnX9ADW1jT_0U8bEHtOtDtriFmPE0xaWcNWGwLkdVe9KePy43zURv2aivAOZ7XHO1q5h1E5jeaEvDlQuPgAsSKickXATLSXmJf7_Ix7k3KnaPhBq2ytwQTVoAsnveaUlyPkJpPluLy4EVM_Lfhp2kAs5EdJd6i2Vom6Npi2q5hMYBHhs8mSybWA0Y9kAy9Hgy4MQfumYme9girDqK2l2q7tL3vrTB8SV2RVY0myH4JNezVa1XYgufxwuJwgJphZVzUNGEaeZCLV0DM_07twv51JzyFJlfAdSL_ZLcoYEmiTQ9jqVc0Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hm1omu6CUSPU-O9fys-9kwOB5d98OLioFWHRnvunDTCekKnNI1yF6YznyBZnAAYxdDOu92aA05Iz2kDouGPOMFqpCFVwB_Tl9xpS0R0XhvKpaMQVt5fYccFqq1L6njyWN7GSAgprp4w6eTr8x_mkFCUmXzAj9gNMldJVO05KNS2aKEzcc77Ma1GVd9ZE38mOechpZb0u7nlFU94Em55Wu_Wqsogau7be5ubALdV3uZfKlxA6fWfGrVdCo09bWkVmF9XTbfvSVLcVbMt8JkiPa6UBQTmJ2z6NlAmpxwq-HqFENMtJGeyB0SDAleXcGeAR-Q5IOdmruK5dyztcVAVzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsK7vFad6nwHnhhLBpq96YLr8hJ__2DK2GmCATMQ9DCPtX9y5jyCcXZIg-N7MknS2tHZohEEDXXuvR7Gba0zCP2Q64FCOPr1I0aUJ30EtSFvZ3PGGTDlHXKH3CGnYmfcmFq8AmzE04WIQY4CVAZaJpjTOgTdZJuKWY7u4ODK9yPPZ4YXHqSHhkVQn6ny-5Psml7RdDLQzGgdRoG8gRXEhUDJXpZT_YfGF9UIMq1U8VyhxfGfb1QbQFwsDQymNaUfI3ZcoRQkeIFhw_OOUNifO8ph7zghYtJ5EXnw5K67H3jps05gm-9YIpS1vUuxudhdvg1gZloY-op2r2qv6IKQYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-6810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1M_TANJoAIQhWOyhiaAsy2jtomelBt_cFN9Y6vX2dpGvYO8to8Eq-EnDICOICxgmtSYArzVufaK5ietHCMcb_83Y_o2FThz97BS5Tftfhn6hMjTQA_1ekaz48BDjr1fLPPBT6OkRFqCLHMXFBS0hLx4ypyOQvkHe8U0vktuIopuDYSvyqcQiJUJPsvHufg9Ts-ybdg652jw_jQT_SdCFRI25J2ohu2J-E8M5wTJ7YTVli_uOJ43c0UN7Q3W3aNS8Nyo1OpSO4-wEISNPRZxLTynDqfrX2ifE3AXd_daf1zmwjSxxzScSzpFFymabtaUrb22XRZUdhTplV-noY-IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام آگهی استخدامی «خلبانی » ارتش جمهوری اسلامی گذاشته.
یه نفر زیرش کامنت داده « جنگنده باید بیاریم یا خودتون میدید »
🤣</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6810" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9CkvVaVmzpIvxMcsldzN85wp9cchB41V0pCS6D8yN7VVFB57jCL2CLRaZ-wPYLUqq7kOYq1Wt7j4ykPeG0P0SYzhtsPwXjZ0hiDDSlXDIpYW7EPjeo4AzzHKH62X_lT24ubinWBzn_KNSy2Nz5xGZJfr9AjIoiBDWia1fi3yMh_yBRl_PRXq112cZbVxiBI4PTI75lSQ8BLQd6PxCgWVXNXymZlKZXNB5IMpf4l9k3wlwxFWOi409MZQtuixXCeMNHz-575EDR5QLWwCADR3r-Y-wgM2SqlaRSpa-9CG2jRss_P7k4obMIELciHnKsheJjNzfYuXTmelrUXI193Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HToD-m4hufu_X1IIc5b51DafvkDO2_GMeD_Se75Ntfz24NT-5ya5nM1pTV0L7VKsxi8CraTcEoh1rGzr-CO6_kEadqXYAKv16QmQbLU8I30llX0eFL45XEKKnmx8Z1qzxgQUJKamAm81xV-gQg2dhMNmSdat1zaZxKnEwrnlkPqlLXTgbRxuvwje5xjksBgjJ4329NEl1NeIVVDr1_RDhTEwCHlw9JQaYVQIf8rieG2W9sd2fWyZ5r-9yp50iDNgLyVd9886tZ_GihOqFzICMDB42Vxvqz65JRFZl5O_8t_Mas9BE6J-jwLGYJRd4tQs1IfSDo8NzXlD40WeWIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ey9tcDhwFTWW3wMXL75_2zInQo2WGCO-5ytDHzW3KoDesfzynGFRvcAQNDSyYaW4q7QcW9By5XazufXrtNSYolc7JF9l4yHPbgL6pxVGy6pCJ-Biv92niSfTDL7dD_BBnYdnbmgUk-AWDe8coPS3SJ0C0ENhv2hJCU7lexEN3jx9guyU47oSPX-h3xeMbgYkccKjXOfJt4vYa2_7ENQ2QL0ht3VhAC7S1423e9eOQHGT1yZtKFULCHZsYUESMsevITxm_xmpUlYTSh1NzrmFejCGQ5WNG5GlIrdczQnlse3GZmzFUz7IGXtMFMo64A_v5bAqYZyQ5x1EE-PlSVYlRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-gaSLeNxk_jeymUhyrHDmgnVMLzmVD_sUerpL4Jf5eSFK5UfNeLusjaZTE3GlyEjmJ4awF0StIt1-DtJjjXTwmhglC6fpSJM7pXp_C1Wm-VyEi0sghge6BzNdUYNSzn304wYSs-o2_me_I9_RkNdkJAha8fZCFFjUzFdKvTtwc2NvELUuDe5E8iXShecUiBE-a6nxfQZnHS6zFkEU0nEn8DCxawZT9kiDHiPNlrNgiPTbOP2U5Q5KS8C4cTASaUIT4TsEdEqtB2JPqhix7dl-x85T-y-jUEfOe21C0f8XHl_2Dg2vZ_C8AwkJTbkWBiiU4-kHqINbz6A2P5URHxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dERfJJoWXv2nL5y8Tdo_JjuxWky13ruwAe5UHVXCB8TLuHOnY_Y4qpHIV5rydPacO7gBnwKeMuZSAXQbcTnaj4PPcq0Uuzu4r0ungTtxgJnFeJ6JNMWGQ2myCR_xDePU6FATetXB_gd5xcUCHq2viqPaA2-sHIrXt3JRzRi59nUgdQCY8E111Urm5f4TgaUvIqCJPYtg7qkI8UjEIObqS-uvmw2Rgh2OG0ud4ivRU2VYW4RLkIOJuceFIc5xjIiwjuEjZdJIgG5J_vW5uhllEgDXDLQEHd181PrZm5sxuXc6UJ1YdP8iEdQvHLIz7D1bFnXUwXkgvxISFSpEYbGiBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=tV2sb6TUfayRnULpAQhRVqbWUUsh1HOvmiAJ3Sy9mhT9AgdZOoPVHNB_Q336aZL_MrnbzZvwYe7-63dI2Fro3okbGF31XdRF8fCbQQdVXT6DN6_5_J_Y3Ee-c23nV5xtg-qkZUqnvo22n0K_T38TPWxYDnS9DN1DM5tqS8aeSkf9E8A9V49zbp5M395TEmIxjTkPxobYuIzX_R2mCb2xTQUbrsxjoE0xBJoFE07nuVr3kdxmMwsmVWxEdGH0wYe8MwGlrPyle_-pTyLU5-YWlKYWjcmVNbRWfBxy7Te3yjM8l8NkvAxRUBiryYN4fDZVa_PvbJSEms-R9Kb45vhxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=tV2sb6TUfayRnULpAQhRVqbWUUsh1HOvmiAJ3Sy9mhT9AgdZOoPVHNB_Q336aZL_MrnbzZvwYe7-63dI2Fro3okbGF31XdRF8fCbQQdVXT6DN6_5_J_Y3Ee-c23nV5xtg-qkZUqnvo22n0K_T38TPWxYDnS9DN1DM5tqS8aeSkf9E8A9V49zbp5M395TEmIxjTkPxobYuIzX_R2mCb2xTQUbrsxjoE0xBJoFE07nuVr3kdxmMwsmVWxEdGH0wYe8MwGlrPyle_-pTyLU5-YWlKYWjcmVNbRWfBxy7Te3yjM8l8NkvAxRUBiryYN4fDZVa_PvbJSEms-R9Kb45vhxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=CvIsMNHY40No-dZOOpEP5X-l_wIEXQhM6bwRLvv8Uxv0QleuqbWArUpp-qUkyH_tcS81VqpVpT5wbKgWxLP0mqzlsEA1v8wDrfCXCf064JfdvxopxgODeZVEnDg-ylReRwodmcvyHgY1n0dMPkoFv0-50uHSqMixoQ_-nuN5chxrIk8IEFAjDbROYhnYP3GtdqKj4Mph0GEQnikPvhdooELq5f4nPV-kptlBbQywN8d4eyu-0lW857jtZ6_iMu-tr2-oJW6Z7LmCgaI7jL7MXwhczmNGN2JV03Q0curcCfTPfRS175iXAlXtDozIjDOB-QsbIN8FKubGCKHiLLPI9iG4GhmOoXv0OUt8KpHc-BcrHDGMfd8diNFf7kCaCDqjdS2hF3IMx3wUEcg-UMUjyBisXxj5VkIEVvbe--J3gneThqigBfWBaYyy1oxeySJqXagf1KUDzsBmNMI8K6JkC8Rnmr2ShooyIXAHXqE2NDEDG0ouJsBY09gyHDtnK4uI4wD3llX1ThTSYuJ9UZyikvrqW309oHxkNYjKmA63bGYX8vwSPBBOD2rRjAPmMs4vFRZE2WMbgLXzm2jk-W2Anm_fN4IZkx0l81bOb2QE0zLEm6Ykg86QIZawHS61sBoeSL44gMmPyJcdRBE6t4fPhOp17wnl-HYJjFocodmX-_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=CvIsMNHY40No-dZOOpEP5X-l_wIEXQhM6bwRLvv8Uxv0QleuqbWArUpp-qUkyH_tcS81VqpVpT5wbKgWxLP0mqzlsEA1v8wDrfCXCf064JfdvxopxgODeZVEnDg-ylReRwodmcvyHgY1n0dMPkoFv0-50uHSqMixoQ_-nuN5chxrIk8IEFAjDbROYhnYP3GtdqKj4Mph0GEQnikPvhdooELq5f4nPV-kptlBbQywN8d4eyu-0lW857jtZ6_iMu-tr2-oJW6Z7LmCgaI7jL7MXwhczmNGN2JV03Q0curcCfTPfRS175iXAlXtDozIjDOB-QsbIN8FKubGCKHiLLPI9iG4GhmOoXv0OUt8KpHc-BcrHDGMfd8diNFf7kCaCDqjdS2hF3IMx3wUEcg-UMUjyBisXxj5VkIEVvbe--J3gneThqigBfWBaYyy1oxeySJqXagf1KUDzsBmNMI8K6JkC8Rnmr2ShooyIXAHXqE2NDEDG0ouJsBY09gyHDtnK4uI4wD3llX1ThTSYuJ9UZyikvrqW309oHxkNYjKmA63bGYX8vwSPBBOD2rRjAPmMs4vFRZE2WMbgLXzm2jk-W2Anm_fN4IZkx0l81bOb2QE0zLEm6Ykg86QIZawHS61sBoeSL44gMmPyJcdRBE6t4fPhOp17wnl-HYJjFocodmX-_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKVxGuG2pHY8qnyqaOb0usqmx7fE7nRb65l6ogIEb6sP6eHv0aMSGibJ2F-WwzxVzIFk6T6f1hh6SG8BCfsPkpbrZORB88DLKvA3kv2DhcWtmFH-XC95oV6V1CDK3LMvFYE9rIfTCrtjWR25oMquSQR5NHkIMzNke14g5fjTE0p5QIOkrz17GMzu3j5otwv3aGA5JeCppQHm94j1_s-CO7T-c-nGGnzhzbHpf8RY3XzKotQLEAMljF71ZxTFdU3FrV7fyNAYEqdWf-0YYggfRlamh_fOgrGgCc6l1-HLGtNmaeSCC8LZXCHxYR4KQVKwF9h0tgaM2abZD6t-XujmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YM4E7gQyJ_xMpycQoKO6cfO4h6Jo9bLllgq9C7u17CGRJDOys-lkir9XoiDDrDvqdG4RLMvH88U-Ki_fXn-lz2Fdc_fdRn7VszlPzbJY74N_2lYiYEYpm6_54gS2IyCEY9QNnIsDPgUL5jUIueqiq6pQqoECQs5eb4XupemwLGpH-ZzuSJR_mRAFG2Ctx0TR_yqWaB8LRcNL823EKUNXuGSOnC5zLlR1AuQAOwTernC0rezXyWIwZPL0UZVrVUZVr16Bb3TXyWPRpeNEPnYKKaYHAv2tVFnTRKUTVMclr7OLc38RyGpkKFPY5pdg9FBGbENEkZZOyJZDAPpG57YwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlZkSeL4sRsjUZ1wn0bQVUe7vMJLtSCtbC-OivYkpVETAfmb1R0AjAnhetRf-9895ZAbFR3Ign05KMBADa-d_ROF8bOSgO6kvbj4xJ-nVMdSUtDWxd6wvzD22eKFL3hQ-xyiGsMhPr4yd_qWvRKLTYe3yWchFF3szzeNoUcetyq9HLdfh2kWUZvlYV5K-sZsOhA2lbo5RWAfrQo8oK-JI_4TJoIddvqIddoHVrXCZi07UJn7TIuf66b4CrdNI8DAGM4J1miJLJ5ryZ-NZtV93Bn70KTjMb9icotU5aXXvOTXydvXz3059nSoD7_CnB6Jc8LAf1kwPYqCadzB8jLDTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Q03kUwuA-QeaGDmfSN6u8Px3GsTIo54cQ5q8em0Qq85fu-BZ5VSs7km7E1R-Jo8E_IH7uC5z1s8TQYr1Ljg8PedWKvwDmParxKNQj0oyzsMJ2rUPpDza5h6kak2CXsHCCUEVvXTtedR1fN0lXoFxy5lt93nHapc_9Tj3HeBCSTJ6sDe6wrnT3YyYM_b59JyxWtAn8_gLCXavHd_KQzawTignP0OIjMOvlLdEJTqaN7XyPjBHyF31rVWVUHiCV5DI_7N2tbJKrxZWsky0MwxC6xBdCH4fT9b1gfD2OVxeqcK5mRRHQnTMtKdtl-9zqQ68Fdp3kud4W78BJ-MNWLVemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Q03kUwuA-QeaGDmfSN6u8Px3GsTIo54cQ5q8em0Qq85fu-BZ5VSs7km7E1R-Jo8E_IH7uC5z1s8TQYr1Ljg8PedWKvwDmParxKNQj0oyzsMJ2rUPpDza5h6kak2CXsHCCUEVvXTtedR1fN0lXoFxy5lt93nHapc_9Tj3HeBCSTJ6sDe6wrnT3YyYM_b59JyxWtAn8_gLCXavHd_KQzawTignP0OIjMOvlLdEJTqaN7XyPjBHyF31rVWVUHiCV5DI_7N2tbJKrxZWsky0MwxC6xBdCH4fT9b1gfD2OVxeqcK5mRRHQnTMtKdtl-9zqQ68Fdp3kud4W78BJ-MNWLVemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=tCQqMRVICrvzl6xJE91DUh8B2XbdU9kY2M-NmTqJyfRYMmRsqNpYFd6nG1LRKMokA1lqIRM0q9dw00t59ppGNvYMOt_u7XChC0m9VCxocUBCXJ8ZG4teduBkDF_HsvIG5ravXrQGR1b9kTnFk6Z1W5V5Jj6B1A2EpJHMIorxA8p-D180TyZqgrfkPIP23ZDJBVUxNr6D0sSIImP28CccguQclRKxYTAI3KP65Jg9JGwI43tVoBLWZfCxIq0_q3y_Xv9VoE8lcB6sYRiNyXRkowqeS1UKzZwrnFbI7FTG76ZR1s9CZAcHhhBhqnl_Kv-O8M7eXurCJcCMhuu2rO596Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=tCQqMRVICrvzl6xJE91DUh8B2XbdU9kY2M-NmTqJyfRYMmRsqNpYFd6nG1LRKMokA1lqIRM0q9dw00t59ppGNvYMOt_u7XChC0m9VCxocUBCXJ8ZG4teduBkDF_HsvIG5ravXrQGR1b9kTnFk6Z1W5V5Jj6B1A2EpJHMIorxA8p-D180TyZqgrfkPIP23ZDJBVUxNr6D0sSIImP28CccguQclRKxYTAI3KP65Jg9JGwI43tVoBLWZfCxIq0_q3y_Xv9VoE8lcB6sYRiNyXRkowqeS1UKzZwrnFbI7FTG76ZR1s9CZAcHhhBhqnl_Kv-O8M7eXurCJcCMhuu2rO596Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQWDi4euzMjgB1ZgE6yaO8CzH5j9WfNBR6-6rGkw2Q4ZFx8H1GHHwGf9CrLv3UMf2CQMFtjJtarCanpfS-0KS4NOCPbb3NzMroqSE5X1JXnTHlPFHO3hdxHUqaNYMIUtHC5LqduRmYu5x9WNW8jcAcjHP3UYI9Ui8UnGRCybd5fCCKHXNZB0lZ6B07lLIv71jiHnNNnoCX5V95cdgWKNnIbDtPp9zLZ9Eu5PI7dvHud03vAs_DbFwVmaKKtTyCZARDnNDuFG5PLkhqzk499uNrlVvDnXSFxtm0-_pS-SjMNp986P3heQamaQyAqdkqAU9FfNpHwlaRl0KVBxAQwhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=bvgoA2RgzY5kUlFrJhNPghkSHYcm4nJqEZzWBi7A5ux34586pkOf8F6FED2_FVH5ulZ97_nuZQLwVVGgHZpw2xobkM8QhsksJfgxWfXYjgIvSJn3r0p7E8Q6s7hffRvZxFTqDMKPBsMJm1LJyJurvc8CpmFMyRfOjoUHi45rTK37U-Gf6sARPZQ2vvuBsZvPPieynpyUlE-k3zGp0sKmSz44Lwbk9mutRiTOIOqiUm0u_3SMGGipoi9Dd74mYieHU37s5miDP2hutYhQJG7y8lIIjsvfY31MHFR4eXLjoqTD0jZU8_65HyOB45-c6pvFdg1EwtPxyhE3mjvF5OnF61fHeKft7LxsX2jf_Ttlo1sIXjWDF_A2u0mFXXcn5M5WQrQGhj_jJVj-GaV0W_p_CHlhKq2WSr_F2amPEHcRV2Kv_2pl8NibmwLStOPScU6TST3zTmByavm65JY3DJiU96VcfP4DnlkgBijuSf08sNdLA54XwgVZ6gpSFHHE_HlBUYKcyfcoLwZn3Ec418e9uMl201hUSKEpRucoXMqGKm60qk2AGg8dDe4LSQc-1-7WGtpX353qlESHvrwFgzhd8SU6lkYK8hY1_5yEVQHVbh2LP04Ify19JzXT10GHCjiJv0qcJJ_i8o33EZxjddHfRL6yz3nl89o4IivtmvdY46w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=bvgoA2RgzY5kUlFrJhNPghkSHYcm4nJqEZzWBi7A5ux34586pkOf8F6FED2_FVH5ulZ97_nuZQLwVVGgHZpw2xobkM8QhsksJfgxWfXYjgIvSJn3r0p7E8Q6s7hffRvZxFTqDMKPBsMJm1LJyJurvc8CpmFMyRfOjoUHi45rTK37U-Gf6sARPZQ2vvuBsZvPPieynpyUlE-k3zGp0sKmSz44Lwbk9mutRiTOIOqiUm0u_3SMGGipoi9Dd74mYieHU37s5miDP2hutYhQJG7y8lIIjsvfY31MHFR4eXLjoqTD0jZU8_65HyOB45-c6pvFdg1EwtPxyhE3mjvF5OnF61fHeKft7LxsX2jf_Ttlo1sIXjWDF_A2u0mFXXcn5M5WQrQGhj_jJVj-GaV0W_p_CHlhKq2WSr_F2amPEHcRV2Kv_2pl8NibmwLStOPScU6TST3zTmByavm65JY3DJiU96VcfP4DnlkgBijuSf08sNdLA54XwgVZ6gpSFHHE_HlBUYKcyfcoLwZn3Ec418e9uMl201hUSKEpRucoXMqGKm60qk2AGg8dDe4LSQc-1-7WGtpX353qlESHvrwFgzhd8SU6lkYK8hY1_5yEVQHVbh2LP04Ify19JzXT10GHCjiJv0qcJJ_i8o33EZxjddHfRL6yz3nl89o4IivtmvdY46w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SokH-eViD-yrCqRXIjZCyvcAjiM_E2XM2iXdK0CSEQskDPTRp146aY9eV0yjaNgpksy8gMKlwBjyLSxtiGZYDtp57MLQp2maBIAiwCpaBQolj4mmGRSjBZYznTJfIBuHbpq1F45sP3NB9qN8skBRwngoqtkQR86WvLvlbgaoCFywa23MRsTw_MKGNaK_Uf_rmAU97vDC4Aqgfnrek-xiSkjB7N2SqpRl0NsWBj9UAOIbAeK9gDIeUWfCYDU0wc0CZHA8HqaBklzUkddtwFzdvjMXqu3DZ-2LBOgs6h_krzUjRvLIs9tK809D-vv3hkPbUEbjMk1-AfASmHZrIfbvHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=SokH-eViD-yrCqRXIjZCyvcAjiM_E2XM2iXdK0CSEQskDPTRp146aY9eV0yjaNgpksy8gMKlwBjyLSxtiGZYDtp57MLQp2maBIAiwCpaBQolj4mmGRSjBZYznTJfIBuHbpq1F45sP3NB9qN8skBRwngoqtkQR86WvLvlbgaoCFywa23MRsTw_MKGNaK_Uf_rmAU97vDC4Aqgfnrek-xiSkjB7N2SqpRl0NsWBj9UAOIbAeK9gDIeUWfCYDU0wc0CZHA8HqaBklzUkddtwFzdvjMXqu3DZ-2LBOgs6h_krzUjRvLIs9tK809D-vv3hkPbUEbjMk1-AfASmHZrIfbvHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klRu_ck3nvlolRO9HQY_Vqz6sFo0NvcnMb3obwCwU6au3BEX6rqbkMUf1FIAMcCXJGyqPjbxFPiT5eHltAa1aTViDGJoUQ7530vk1P74m0pUsaiBbThluXi4qPKEo9UJA_EdcHKDnhniaHAfeKWHzFKWQc4myxOlibULl-aSkpcBGdYeW3ss4-e69BotIs9SbUxZvsowl6MJTEeorKZfb1gerlQe-d7P1GTS1975kdpP1kDMWMXt8wJ86t3ixMb9rsIlmfXBLOwHmW9C4vJfgzxmS94DgF6mXn142VgW57ci4jpcS-I5MMQ7NkZKbZXy8XOmK93g4kO4OVGXlC3YUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=QLseRJumJcldUSEQX8y1aUPBylLv9iWijpVkDlmpsRQiPAbGf3iAQap59qi5P2mzg-phoek-yug_LIm6mepNA9MiTC7hnJ-jcjVUmE_RpLYu0x2SU7SZJFzvS6sxDFMF42KnSRHkrlXXAy4wsvfv6Oe1ynUPsEUBHeBnIedWf_4cnklfJ7u-GdgSIMDt1jwX8n6keLvbCEceNLacXon27vtpd3loAJHpVzj1yxDNHeU0suV7lUgeaG9mrBhzxNEI0b5p2GMfgDW7YuFDjsaCCirr8wHok4mHXba8j8isR9j8DIIIcjqJa7RJdLaR8iB1g3RxZzHSEJdE1hK6qIrI0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=QLseRJumJcldUSEQX8y1aUPBylLv9iWijpVkDlmpsRQiPAbGf3iAQap59qi5P2mzg-phoek-yug_LIm6mepNA9MiTC7hnJ-jcjVUmE_RpLYu0x2SU7SZJFzvS6sxDFMF42KnSRHkrlXXAy4wsvfv6Oe1ynUPsEUBHeBnIedWf_4cnklfJ7u-GdgSIMDt1jwX8n6keLvbCEceNLacXon27vtpd3loAJHpVzj1yxDNHeU0suV7lUgeaG9mrBhzxNEI0b5p2GMfgDW7YuFDjsaCCirr8wHok4mHXba8j8isR9j8DIIIcjqJa7RJdLaR8iB1g3RxZzHSEJdE1hK6qIrI0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxIliOt5hlT4iSui_6R8OWwideLsVCT_nlN3ilYyJO8L1YTr_foWqLKzM3K-rK6KRezvSOMiKKeBMUiFymWoWIw_MrTjzFlX6Im_dfqcQ9TFpNGCS17Xf-4Y5dJ8y8sZHMbLPDQUJEFpRw0AuncAlMG2O7Fcr5d58EeWaHSr6rQUz5B9-7hku6sQituItRtYylHiHqSq9tOCZdNzy92vwURZULvo-2gD9eEro8gleZw1cZ-6ocnU0yNNOnKifEGYffCiyqUMb3mpf000BnWWHxj2KCjSNBBmydZ33e6shkmyzY3WKDwQrzuSA8XTOuCWk2TsV75gJJCfeOCtv4R6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLnZjVRlr89zWQhbMb8-S16nVd5nYFzWVb5MNmGkbdkio2S-HECd943Z_vKzr85Du0LYcbLlB5S8y7OXVSq-r0F6QjDRCvwrknJlP8X0z12piLzbae2pLZ_ITf6Y_C3m8r27XOUoHHCqCV3yWzhhRy8oJmGXEeW4n_rBMu0oL0Y2ngZbYEOgQ1_ErOZ9WiGOOsarlKMT2QsPmnpBaok4iUvygUHxFC_OIobeM9B3oWWPqWGUwVmift3iOMHE6E-T0aUAc4mFhRPouwMYQ50jMvZxbZgXe27f0mhpKVM-wXZ0NbHHFh-K4yHnrneLpmZmg0D1KIwI6mpAgDgDIpsnWg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=B2b52qxNkq_PFZ2jkdDcFBZ6zONLZuY4UoMvoqmIEHpPDbderRZk2ECFLfpdCoQDCSo-PoCXirdusrhtEnUU0eLhk5JE1xe9NtlhMn2RCrOTnTXm-4oJQuC0leTus3rlQb7Xnicl0x0gqO90OrI3BAx8O8FCh0Xqb5uQBQhtBXzd0VO1ww-xoz_Zy9GdsmtE0bvaOpPWLnVq7biTaNi2TTt2DiWRqCF2HTMuWBsfKyVIzaJ_c83IroExvKl6PaV_0cgZA5O6iY_3vlOHYI8CTqo4bF4-zvYXg4wM60PAPIaotXEMSjbGjN904e36OodbGICgK3YnR1-rAq7H1vwnb0eZzZqiX1HfeySDcXFnMDVUw-GuBuQe08qdg9SXxOSskJv44QkvJoXeGfG1MFGv575mz-TFn1pFKrOCf8By95n7wrxYw7qOXyE4AxiCjFuMvJjfY6R2RQWiS1j8bed4h6o-FuEBRmHRaDS9Yd6LHa61YBp8BHptI0Px6Z2HPZWLYLab6flyRTTtUY1XhWX9wL_y8H-fjZChYA5E2AYL9E8jQVuBzi1stY_LbUIjS0YCnp557OvvOEXhGFBlVzfLq1yTPD8E08dxVR8hij98kvwG9UAIx3vgmOS9KnPyqZbMEAeRqiAlaUF1Q3fbibDOCzaWCutqyINMaCzqA_G9JPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=B2b52qxNkq_PFZ2jkdDcFBZ6zONLZuY4UoMvoqmIEHpPDbderRZk2ECFLfpdCoQDCSo-PoCXirdusrhtEnUU0eLhk5JE1xe9NtlhMn2RCrOTnTXm-4oJQuC0leTus3rlQb7Xnicl0x0gqO90OrI3BAx8O8FCh0Xqb5uQBQhtBXzd0VO1ww-xoz_Zy9GdsmtE0bvaOpPWLnVq7biTaNi2TTt2DiWRqCF2HTMuWBsfKyVIzaJ_c83IroExvKl6PaV_0cgZA5O6iY_3vlOHYI8CTqo4bF4-zvYXg4wM60PAPIaotXEMSjbGjN904e36OodbGICgK3YnR1-rAq7H1vwnb0eZzZqiX1HfeySDcXFnMDVUw-GuBuQe08qdg9SXxOSskJv44QkvJoXeGfG1MFGv575mz-TFn1pFKrOCf8By95n7wrxYw7qOXyE4AxiCjFuMvJjfY6R2RQWiS1j8bed4h6o-FuEBRmHRaDS9Yd6LHa61YBp8BHptI0Px6Z2HPZWLYLab6flyRTTtUY1XhWX9wL_y8H-fjZChYA5E2AYL9E8jQVuBzi1stY_LbUIjS0YCnp557OvvOEXhGFBlVzfLq1yTPD8E08dxVR8hij98kvwG9UAIx3vgmOS9KnPyqZbMEAeRqiAlaUF1Q3fbibDOCzaWCutqyINMaCzqA_G9JPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M__d5s5UZ0kMi9RqKQep5CQOnOmkZN2SrxrIlE36Uh2FFjT-ofc_16E9na-FgLKDe5KK95_MHhF60MWXg8SxtxjyP8d_YAKgY4XMry-zaIl3Y34AjycdhyJ_UzxXJj1CCovMHA7oklb3f2IseuD3NK-HQdoHsHpguFF01LDVgf8ll63C-vFyyNDP6yPab-yjDVdsfy2avsnDjIrcHBkUOPYePp4H7UieQgqBazhPGnyVwsZ6Odb7CElB_gQDxv38WAmkB6Py9zDQQfWkEiYZJQ23kNASvTTZa85ICd0EuEqWXJOLlG9YugHGBXuyeYv1RKyR7bDlws0sAOfcenKVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPKqFznO-mXB-itKGWWkBZAGqIc9C186oHrbq6048wKzZvRzTJsuboLDw52h9KcGRJnlUobaXnuO8PUSG6cT8UfvNtb5uwca4gR1PO-ND_4k8DwCvW2CKj9ijkA2r93iHS7SMOR5uxe2j9fdSjJOPnrss3fBAfGwlnSKqJgSIZW3xKcqBWNuqDGUtjECiBrKkaT3hyqU06zZJZi9Xq1QwwGGUV7wjOJ5eB0d3OGMqUL9HDsB3bZJQO8-P1fuXnkRPyWN1emJ7Hw2SgwDYwm0eKpmiU1WZoB_jOK0E2X2HFx1Jd0L-0T6KW4vZjYYbybSxX9PBVAQP1Xh6Buxtf-L5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Adgc7UOveSq0OStKljA1TQc9Ou0CnGXO-CCnbFohNZlnyWdjSk8E6vufmpPUtcnW0kkHHlrmVUCDO-jlhj0Y8LYhC_9b4lz9QrWkigZjLTCq_ahX_ziCgCe2af7Tr2ICWVmhcOzSgQjlmTXs8wmbkTRmzgGrKf0o_ZrHiNReN-pjnNyL_WQqS1RefVs9q7r35uc0vUORr5lgSGBjXvQT2snpWrgEfOGvIQe_Hz5jCCbpkFfFYLuHBb302qAEz94KSNtjQlArTikAEHjg8ZUe_a4wzvpcwDc-LVu3JiSemkDoyq56xgX56PksyFRkjJyR3eGZt05echr7RQpm6n2kHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Adgc7UOveSq0OStKljA1TQc9Ou0CnGXO-CCnbFohNZlnyWdjSk8E6vufmpPUtcnW0kkHHlrmVUCDO-jlhj0Y8LYhC_9b4lz9QrWkigZjLTCq_ahX_ziCgCe2af7Tr2ICWVmhcOzSgQjlmTXs8wmbkTRmzgGrKf0o_ZrHiNReN-pjnNyL_WQqS1RefVs9q7r35uc0vUORr5lgSGBjXvQT2snpWrgEfOGvIQe_Hz5jCCbpkFfFYLuHBb302qAEz94KSNtjQlArTikAEHjg8ZUe_a4wzvpcwDc-LVu3JiSemkDoyq56xgX56PksyFRkjJyR3eGZt05echr7RQpm6n2kHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=k4q_PoCQN9XpH8TppU66RJt3EQsHnbU60bbdBdKppQwImCMOSZbA8pcM0rzKqn6YlI39PuPR-3KOdp0kuAH_Gi26Y7mZqu-_Qd2BREeRQLE79PIMNwcw7iN_Q50FQxd5hC69KQ8MQfUisQRzWbZs3d7NSyV4i_9KUXFM4EfdYN7VRmVQORXkt2QemGbu36vhQpEUQhWo-szL0XfFbfmgh6DN5E5zmBCkC8eizj73no8z0iVYpdXPYrAtIX_E58NepvsDhJ0JLUjYNBSn7Gt-bIDtqZaxzzM7dC5w5z7Yo3uM8SNXZPECdWgOGHZn439yuyOKm3LYh_Z7TV5HrQSGkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=k4q_PoCQN9XpH8TppU66RJt3EQsHnbU60bbdBdKppQwImCMOSZbA8pcM0rzKqn6YlI39PuPR-3KOdp0kuAH_Gi26Y7mZqu-_Qd2BREeRQLE79PIMNwcw7iN_Q50FQxd5hC69KQ8MQfUisQRzWbZs3d7NSyV4i_9KUXFM4EfdYN7VRmVQORXkt2QemGbu36vhQpEUQhWo-szL0XfFbfmgh6DN5E5zmBCkC8eizj73no8z0iVYpdXPYrAtIX_E58NepvsDhJ0JLUjYNBSn7Gt-bIDtqZaxzzM7dC5w5z7Yo3uM8SNXZPECdWgOGHZn439yuyOKm3LYh_Z7TV5HrQSGkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Mrj5AgZA9Ln6Eqd7iIMemdZycxbWRMJ8gOtk01jxw9fre9GQPEzZB0aUUVSkkOVlQW0XEjh4N1DCoH10uKlhAEbdbzmBA3vKsNxOlQiZ4CrpN9bahJ72q58gHyW-0o3SmPPlvMCLuwrFDZ9PJAtBu2VyTBBbPJPMXivtletd-iXHQI5bHeVDbJ9eahthm8_11sq1B7ZZ1aSq_SMB9-T9VvStfUac9N29jMFdCtJWO85_OtJBJl9Vyiuf3zlKFpne5YWPWPBlG3Ug37GBnedqJPEGER22ARRk2V9-3TNwyV1CXOXl0MyiZNLFrIGovjWHJm2Qa-HCozItinYGJfiNIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=Mrj5AgZA9Ln6Eqd7iIMemdZycxbWRMJ8gOtk01jxw9fre9GQPEzZB0aUUVSkkOVlQW0XEjh4N1DCoH10uKlhAEbdbzmBA3vKsNxOlQiZ4CrpN9bahJ72q58gHyW-0o3SmPPlvMCLuwrFDZ9PJAtBu2VyTBBbPJPMXivtletd-iXHQI5bHeVDbJ9eahthm8_11sq1B7ZZ1aSq_SMB9-T9VvStfUac9N29jMFdCtJWO85_OtJBJl9Vyiuf3zlKFpne5YWPWPBlG3Ug37GBnedqJPEGER22ARRk2V9-3TNwyV1CXOXl0MyiZNLFrIGovjWHJm2Qa-HCozItinYGJfiNIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiHpaJ4fuGcVNaC7Q6IC8FDb9GiZnZg1zNsSm976k7HnMFoQ1QReyObsRMeLV0T8y10j-LcAktDMEBip0DgFQzKZFubUmSk53iBus5nnbOyiiQeCco7oESO3483jYQIbWaT4Pk22xTcAnn0XXCNjptmZuTMDsRqzNE2iDuKbBHsIZGeDQ1rZburvm4tajb6pp_2ToIQVYLPNc0103IMLjVCiIQsDrlIuwyPuoUjQmbk4w5inFHvDXUJ2OhR5uggTBTdT-1MMIHIxWUmOZu5LWAtdSzjAqlEqdx0ievMe1ci7Hrcv7rrUU6pWFMjOSLsD4KXXYTIbrI2qpR5TrB1Dlw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LDRXx0xrEe2NCIqG89vBVtwP6vsXUqWozpd7z_lW7Yewu1kzf2W5xisidtg5-FmuFHKBoKMMI0JdwVw-KXHfYILxIFVYrLh6lC3BABhuWE3XHEGmrx4vVPcuERzADh-KlGWdSDO9rD8ar5p0h0c6Tt3B5TzJFDVAi6yvNDmekOlJrd3Z85PaeCUH5Rb9Sj8XLTrOCzP2BJPuaQUC2JtyAQ7FA9kdatiMAuH4pKAjlSJk9M8Ok7jFr3SebSZ-0P8ghtli6BcNG4R1PLRatvOjjNlEG7Ggp2gm8zJ3ZW-PGtMTafYJB6stcQZ0FkvvaRYWZfurTWhdC2EuN5268Xzjc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LDRXx0xrEe2NCIqG89vBVtwP6vsXUqWozpd7z_lW7Yewu1kzf2W5xisidtg5-FmuFHKBoKMMI0JdwVw-KXHfYILxIFVYrLh6lC3BABhuWE3XHEGmrx4vVPcuERzADh-KlGWdSDO9rD8ar5p0h0c6Tt3B5TzJFDVAi6yvNDmekOlJrd3Z85PaeCUH5Rb9Sj8XLTrOCzP2BJPuaQUC2JtyAQ7FA9kdatiMAuH4pKAjlSJk9M8Ok7jFr3SebSZ-0P8ghtli6BcNG4R1PLRatvOjjNlEG7Ggp2gm8zJ3ZW-PGtMTafYJB6stcQZ0FkvvaRYWZfurTWhdC2EuN5268Xzjc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gXQmpRsWSy_Sc2Bdt8SwRrOCphzX2kKoAzjmCJCjv5oL1R3VX_ua5XazxyZ1j4KdX73F8ghiRV959_Y7a2WcCM8DmjWyEpnfcxgdhWtjCOG1wTWQpftdZvhDd254xLAEwu3CPCe79WPJTmv0azER1VY-d-oC2UnoDKj5OGNxBAOLEf4NGZVJ0bizzouxLf_Fx9jY9qByWM0j2UFbnMArKizkU_kuYYwNeiTeo4XhyK6a4S5fjmrx8vTDfuQsH5XFSJe3PNyMN6MQgPSeHmDWoJZyxxXu8-Gzp07UM0K6j7DFEejuGcP3X81qTQ2t2mmeBP2coz-HOqFL1yTxAYtoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gXQmpRsWSy_Sc2Bdt8SwRrOCphzX2kKoAzjmCJCjv5oL1R3VX_ua5XazxyZ1j4KdX73F8ghiRV959_Y7a2WcCM8DmjWyEpnfcxgdhWtjCOG1wTWQpftdZvhDd254xLAEwu3CPCe79WPJTmv0azER1VY-d-oC2UnoDKj5OGNxBAOLEf4NGZVJ0bizzouxLf_Fx9jY9qByWM0j2UFbnMArKizkU_kuYYwNeiTeo4XhyK6a4S5fjmrx8vTDfuQsH5XFSJe3PNyMN6MQgPSeHmDWoJZyxxXu8-Gzp07UM0K6j7DFEejuGcP3X81qTQ2t2mmeBP2coz-HOqFL1yTxAYtoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4t2sioD9-SorIjwlEIb56sjOgG7ew6yt1ExvxTNfM5UEiQMfbge24xlK6ftVSVmLIx2Lp7i0NJgg_jOsZJqhD08dPkGEWd7hV4MqYU8EtgDxVtdTq1ON4LEBmnh6FzjbAcbMzWpESZYrCvx81vfuEXMRUF3Q7P-BWYyFkIByY4Hfh5f2seVbI8dyjkanWPG6t6HN4WzPbtHfKjptXF57oT_Z_gHB_bZnsY1r0eVg5VGzQNfxLBwpXdgAXgqzEZ2p1lAqJjN31WXqqcYDnRHHYxGkVZuPRVTsEuoYTlvl_zExs7CZrHt53Ub5uHE4EQH1U2MBPFouQN82LkL3kJzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=KuKnUU457Q4uUR2JQaF9o8xFG7Z_f7S3gEgg1lqm4t3K4C_mqNKkWUEpVIjVvb4nuzz9jCWtessrFtLBEynUwWTE4VgV8oM-8ZbKoOhJStUHdeVotku4zSe84pr4ZLQfYZX_rmhlza-9xEtiAzYL9kf24CdVdWqxhWpb3Eg_l8UYX0ctKmqMXgUYKjj9s_if5fnWZ6Z2KB4RG4BgUAkCZ_UOZPPHgtN6szW-Gc6ScsNNV9M1RohjuZl1ILw0oSlUKVLXSzK-GtXBSfkN2D7T8fJpJSKTQ2H-vHqe-I0rBZRlrPSclF5OuPSCKmDZ6Uf6BERy-ruKb_OOS2iSX7pc4Z8_6LEYkCUWunYuxTP7_NWrDNDQsnC2G3VtP4nyz8HJgaMEW70sQ0ITJwF5okpC1PRGIVyIVb3AUS11ISQ6rrfBTXtrCluO3HUjwk5bIWdz3qxsKgH292us0HKkAzOe50yMDDDIm2EpKpbHqMmqsrs3mezye_-asySjcMaC6oW_cV6h0yht1BvyoRt5wx5wgu7tEdEygo1vZB5ewg39jj4rDFjrhbPteULImV_7jpPpYr4SiaqUAGEsPlSZvA2da8KZxbLejbhNsls79_7ma9mkvOpK_SvZDmQGPyXRQnRFL-zG4VXLJcEZKtZNTT2g7UYp8wkxfXCkrJ4dYClgNH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=KuKnUU457Q4uUR2JQaF9o8xFG7Z_f7S3gEgg1lqm4t3K4C_mqNKkWUEpVIjVvb4nuzz9jCWtessrFtLBEynUwWTE4VgV8oM-8ZbKoOhJStUHdeVotku4zSe84pr4ZLQfYZX_rmhlza-9xEtiAzYL9kf24CdVdWqxhWpb3Eg_l8UYX0ctKmqMXgUYKjj9s_if5fnWZ6Z2KB4RG4BgUAkCZ_UOZPPHgtN6szW-Gc6ScsNNV9M1RohjuZl1ILw0oSlUKVLXSzK-GtXBSfkN2D7T8fJpJSKTQ2H-vHqe-I0rBZRlrPSclF5OuPSCKmDZ6Uf6BERy-ruKb_OOS2iSX7pc4Z8_6LEYkCUWunYuxTP7_NWrDNDQsnC2G3VtP4nyz8HJgaMEW70sQ0ITJwF5okpC1PRGIVyIVb3AUS11ISQ6rrfBTXtrCluO3HUjwk5bIWdz3qxsKgH292us0HKkAzOe50yMDDDIm2EpKpbHqMmqsrs3mezye_-asySjcMaC6oW_cV6h0yht1BvyoRt5wx5wgu7tEdEygo1vZB5ewg39jj4rDFjrhbPteULImV_7jpPpYr4SiaqUAGEsPlSZvA2da8KZxbLejbhNsls79_7ma9mkvOpK_SvZDmQGPyXRQnRFL-zG4VXLJcEZKtZNTT2g7UYp8wkxfXCkrJ4dYClgNH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkSqxD96PY4rTwermssjboTdVgI2SLWBtxdLAp0vCv2C4K2_7qiajr_gw0FOAqk69eN9OX9YMX3TkFvtwLEJiAUEyevOEsHWuBxLnpyCmqDrQx6s7lOHemysq9VgIkUqYpVyDBYJcvaZjFBc5Ck9pNLKnJ-ykNvE6TBotcU9WsOclgAEX15TEBWFUsh9nxzGUruUJukN3OCNN8uPBYjjbto8aB7Rp84ZnI28IL9tAXNui2DpEK14bPkwWCIuVbEVHz2IvYS5CefQgeYetLOKNDEpy-Le8WiYIwtDQU4sDceWXEpVtPEHYi1UcHHRmO9aPEOjcuBy0CE6GrsFzp4FQQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=CqfDJ8wog_YTJDeGTn-cNviD4bANFO3H1N-3nQQmYz8hvyr57qTsbwCaEdyM9NorKTB3kGy1s4VyXnH9Er8ZZEQ580zZoXLcXfH6C1oRNy7-sl9Z10-0tfW0atk2QB5HeMbN4JxWcUv8gQYA7eUsWxlurK1kS9ENyIhHbpfCfG0WO56-kYsObDIt3e5Vxqomda2I5rzTJ3IuyT_FTuFqUp3AMpHdd0f1o3TSOKOMDk4xcuCBlZATOO2Lqg6FQaN_HR9CAKhNiyU6g1kNxisZbSbDkbuLAqzDSsg8B7oHFwKJz0UG-sSczMt2gIWhFT78OR0VssWAtE2PeYjlOfKzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=CqfDJ8wog_YTJDeGTn-cNviD4bANFO3H1N-3nQQmYz8hvyr57qTsbwCaEdyM9NorKTB3kGy1s4VyXnH9Er8ZZEQ580zZoXLcXfH6C1oRNy7-sl9Z10-0tfW0atk2QB5HeMbN4JxWcUv8gQYA7eUsWxlurK1kS9ENyIhHbpfCfG0WO56-kYsObDIt3e5Vxqomda2I5rzTJ3IuyT_FTuFqUp3AMpHdd0f1o3TSOKOMDk4xcuCBlZATOO2Lqg6FQaN_HR9CAKhNiyU6g1kNxisZbSbDkbuLAqzDSsg8B7oHFwKJz0UG-sSczMt2gIWhFT78OR0VssWAtE2PeYjlOfKzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ow-rGf5M6xPikIbwlNJt84x4cDvgE0IMsaLWx88fFBIHTgqlpTOkGOtTW1CfybIb6-uj3KG0aXCXGcjia_p6iMh_FaUYGd1IvqBRv2q1Xgz9wvattyFHVsnV6YreKd8EOitIuaGj6Mrbcl4D_H_k4RxHwiuHQl0Z9Pw_Wk5NZTMMT8bV3N49-LZKMlwj4p-LndgnLosVH8CumQGLQXE5NUjRHBcdT_BUPdrnbt7O1K_MbBUV-S7-qmw5O_rUvWrUWcj1CUtfeUsqBAwOF89nB25Xd4JrJG9lCvoUB1ZM0RuNk1SnpYwxckamKxj67DOK_9Q8RfpQ166qvu5jpWG7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQLG9q5TpVmR35Iop6s1eN2wv_HypzVd6wru2ewPkOvudcmwDiviK-v69qJpBtj98tGP5tZWAhcPfPIvQAOVc68Cm2EYq1ZZ3e3D4N1Y_Ftlhb6ZpUvc9OBaijG1U2gFUsqeyJC6STwfFQySAfXYFDe3WMrCXwGfkhnhxMxkEAAl69OJlQbke641z_s5eNrrSjWQv6lv8vf6Eo3I72wkvrZZzxiO5MxpwAa1EVzAuODpYYRll_CnlIPgp3t9jEhHBEjXj3YN6sSCNut0-4zlYYZqQ5H7-np010M3QvN2dm1r-8JvuBDw5P12s3H_U98k_Rmr3f5h7wMbE0dw1hntZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN_uWYUgwPnqfzr54_MGvbS30D1eMoxBFkjdWCVc7mkrsye5G0rwnUmtNeswpDktf7Q6VDh9AKbwASp_kP-mPqESsNw02HOH-ELP-Bein4RvjLfi1-EE7CKFkJanArJt9dXhTrXOurAJ9yb9Hfx1cxxu4SbMq64Wx3q_l49Pk7wRKabABJCPqTOM8HKiFz_TZJvbNiDI5Bcokrnh3jaBiS-nCeUn1DlEgqKIW7dd4QSBpiEDaS9zK8j86_3rvhOYB_pNjzSOFUOhEFBlkLBvlf7GXijXDMWN6w6ErYjWmpmmJ_MIQU16IC1Xt8hUx2VXjh3qY9kyyk5pJ7_dNXJ-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=QeUgzpaGFDMrGUsNPOhzfEZSbcQTBjSNnuvivjJ-PkVarluheCCXop8rnWv3qL1QW_ufT8C9mV0XtwcQZFbvUIzclSEFmdW8y9iC3_FjIkpAjm6HC3DMlKAKEEvBnuBTNiJVuSyMkva0x1W0Z2I9RlEC7zKNMgypLHwXXXTuykDtmv9bLVLdHfyfGggkgGk9TT6OWV5GnSkFwPKu1iv3Q64kSNkPKVJ7jSyH1d1_WTKwJFRCvCEDBCT7SNOgcpVR_1OvEwwtJgLUuenxNLacrXDB3GEh1VbKwZ-troc2PZx1t2SGdUzpnkfp0XwcmiipGR-dv78lj5osYtQs6iey2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=QeUgzpaGFDMrGUsNPOhzfEZSbcQTBjSNnuvivjJ-PkVarluheCCXop8rnWv3qL1QW_ufT8C9mV0XtwcQZFbvUIzclSEFmdW8y9iC3_FjIkpAjm6HC3DMlKAKEEvBnuBTNiJVuSyMkva0x1W0Z2I9RlEC7zKNMgypLHwXXXTuykDtmv9bLVLdHfyfGggkgGk9TT6OWV5GnSkFwPKu1iv3Q64kSNkPKVJ7jSyH1d1_WTKwJFRCvCEDBCT7SNOgcpVR_1OvEwwtJgLUuenxNLacrXDB3GEh1VbKwZ-troc2PZx1t2SGdUzpnkfp0XwcmiipGR-dv78lj5osYtQs6iey2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crCWPmTBEhqryQ0nHbsaDplUybQPwNLes2jwz9WtkzHJmra3PsO45uFXgEnS5DvQ_E0p0OBs-AsaQY-stvz8fFWhcUgUxhLYxa8wBr6prpD7C2AmbaiS9jwYELcGFJ4lWa6uVGdulrO84VPrdJ7risVw4yUHg0wF7G2KFdl3AZ8W8tXoCOdt62TtFn23evRSHgfz0QQzJPq04CciagBeY9gnqjLf6NdEiAoFqqnsffLY_vdvivjK7QNcRvN_I5beGpR52lyINMM2XiE072fP-UJWdPo8VnUf0oDvt84ulI33tbedAK32w0w0qAgPQQ034rq_pMJsbr7raTw2vxel2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1j1w5ieNTqLiX4xs5v29J5BefYBaSg6zRE88wc10g3HTf_kXZfXkhb4DDhQL3q6Z3lyEN5Q_rKXkImxJ8vqTlCOrTU2l8p5r0Rut1zRfL0RT-jenTd1gJRMRsXQRojqL9_77_nI6BxhkqhQPnQYiY4G_r1iN6GT09Yoc-IYu2DwqnTbZw_zSf3_zKanF9k62s-saqDJov-r4kdzFI0nd_sXxJV1ECQlPqCqYuA8HVaxbJV93dALsIQXF9HVAs7dnBdq03gvMYzeQo0KymuyHaTYY1_l1GLhOVbwqz64_FAfXOdZSHzuIFSZ-59zRSpX7_KjdEivOzt4XiUEZWUptmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1j1w5ieNTqLiX4xs5v29J5BefYBaSg6zRE88wc10g3HTf_kXZfXkhb4DDhQL3q6Z3lyEN5Q_rKXkImxJ8vqTlCOrTU2l8p5r0Rut1zRfL0RT-jenTd1gJRMRsXQRojqL9_77_nI6BxhkqhQPnQYiY4G_r1iN6GT09Yoc-IYu2DwqnTbZw_zSf3_zKanF9k62s-saqDJov-r4kdzFI0nd_sXxJV1ECQlPqCqYuA8HVaxbJV93dALsIQXF9HVAs7dnBdq03gvMYzeQo0KymuyHaTYY1_l1GLhOVbwqz64_FAfXOdZSHzuIFSZ-59zRSpX7_KjdEivOzt4XiUEZWUptmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fV9uIPS3BqVODAQJOYb-Y106Q_OAehNuE0xZfnuK4o4mHlGIXnHlcd3Sr5HhaP2BHvZ8OznGzApPHMH3IF2VPobyoXbmLEaDf6BhlYMBycjiO9TmgCgaVpqzM_JwOUNYKGPfbgwFZ1ofgQRz8AKwuWOPKZk0xAIIJ0gce-zdZHjdfYCi7-JdcxQsZ2NEyI3bqKXjxNpGMPBbX18C5g7wU2HEX619DnT_VxlOLY3dZfNfTWBUGCjgNGHOLB-iSqVdv4mPg8zog77cZ2eOHDLutBNKs_EllySgowIaaG7Kdi_3Y4N3c3iNwvo5z7GEvYXmGU3cqJrHgmmspO8mk6RPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fV9uIPS3BqVODAQJOYb-Y106Q_OAehNuE0xZfnuK4o4mHlGIXnHlcd3Sr5HhaP2BHvZ8OznGzApPHMH3IF2VPobyoXbmLEaDf6BhlYMBycjiO9TmgCgaVpqzM_JwOUNYKGPfbgwFZ1ofgQRz8AKwuWOPKZk0xAIIJ0gce-zdZHjdfYCi7-JdcxQsZ2NEyI3bqKXjxNpGMPBbX18C5g7wU2HEX619DnT_VxlOLY3dZfNfTWBUGCjgNGHOLB-iSqVdv4mPg8zog77cZ2eOHDLutBNKs_EllySgowIaaG7Kdi_3Y4N3c3iNwvo5z7GEvYXmGU3cqJrHgmmspO8mk6RPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=K8dISjX4yFeVfAS6jhD64i_8_DDz2tBglf-3Tpg7ynlWHT_TugxrJBt5VZYvhCxgmKFSLLHRGRY-SDUEKD8fiux0ENhCzrVNJC3AAnh7tMy0MK6geOhJxiPv2tbd9uPTOLtE_Bwa9-kyKff5ab_u7-z7OK9ckaPLgt6ZoJPQ9cWcDotTSUA-adTKZ772-CXp9SLNj5M3KqLp-LoED4ju7wREorcoY6D5vqg6AABBVUwKdqmWOgWyGauiBwGl8rIFurNKStnCNVQkOOddD6v3zfv2prWYE1o8keav0XYsMFFlQgsI-2zq_k55-__jF1IVZ7zrZLnYf8PfRPf4sryBqmfAChnctCefKHbDjmgR7WzbBJt8En9NZENWa9wgXX9iltWlcZNjSCvXevlg5ix8T-t5tuxWZude_MIkql2HFYE68USs6mwmhLfHPaocw0rSfHJfpv7jVOeDaLO_OUYgTmLpbsJGMD5rMyW6ak-cyW0rcVJDMLuZZCkbahM5zyDqVwpGNO0vZHdLcHvlYMSrXmFtVggX0ps3Eg_mh3pUH5NwWT29QRDVzY04r0MCIc_uBvdbXK9I9-1cXNVHqXi7wW5Fqkzw8zGOAEiqMDbeGp0Fg49QzCKmmkau_jH4uefpZXcCC96zAzD9ItxtU1bal5DndIZuLb5MCQqXAbIxFUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=K8dISjX4yFeVfAS6jhD64i_8_DDz2tBglf-3Tpg7ynlWHT_TugxrJBt5VZYvhCxgmKFSLLHRGRY-SDUEKD8fiux0ENhCzrVNJC3AAnh7tMy0MK6geOhJxiPv2tbd9uPTOLtE_Bwa9-kyKff5ab_u7-z7OK9ckaPLgt6ZoJPQ9cWcDotTSUA-adTKZ772-CXp9SLNj5M3KqLp-LoED4ju7wREorcoY6D5vqg6AABBVUwKdqmWOgWyGauiBwGl8rIFurNKStnCNVQkOOddD6v3zfv2prWYE1o8keav0XYsMFFlQgsI-2zq_k55-__jF1IVZ7zrZLnYf8PfRPf4sryBqmfAChnctCefKHbDjmgR7WzbBJt8En9NZENWa9wgXX9iltWlcZNjSCvXevlg5ix8T-t5tuxWZude_MIkql2HFYE68USs6mwmhLfHPaocw0rSfHJfpv7jVOeDaLO_OUYgTmLpbsJGMD5rMyW6ak-cyW0rcVJDMLuZZCkbahM5zyDqVwpGNO0vZHdLcHvlYMSrXmFtVggX0ps3Eg_mh3pUH5NwWT29QRDVzY04r0MCIc_uBvdbXK9I9-1cXNVHqXi7wW5Fqkzw8zGOAEiqMDbeGp0Fg49QzCKmmkau_jH4uefpZXcCC96zAzD9ItxtU1bal5DndIZuLb5MCQqXAbIxFUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=oiPlLuB818eOx6oMpagp7V3iT5XXqZPYZsR6J1JeJ_xG88Smql8NJE2kiicYU5xJAlRSEC5_I2R0n96Py0uzmFIRsW8nJ--e6scsfzdhTgsot_S_AVuXyp_1eHBpn7Qq9xbiDnDQI9xU1MY00SqDc0impx-Izek2g5upFUUSYkHNNF5hySIAl1powP1pBGCxQm4nbY2bBOmw1pNSgV19Hi5HsO1eZW_sNkUtXIEq5S01B8H_ieJoPLZdTDIklM19qFpXoCosLVLOcUOUobGVvtUGeO9MY9Ujxw9axMYYWkiCJJNv4RuAGauDnUvqjiHKS0iLyowW81CLFdppzDgQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=oiPlLuB818eOx6oMpagp7V3iT5XXqZPYZsR6J1JeJ_xG88Smql8NJE2kiicYU5xJAlRSEC5_I2R0n96Py0uzmFIRsW8nJ--e6scsfzdhTgsot_S_AVuXyp_1eHBpn7Qq9xbiDnDQI9xU1MY00SqDc0impx-Izek2g5upFUUSYkHNNF5hySIAl1powP1pBGCxQm4nbY2bBOmw1pNSgV19Hi5HsO1eZW_sNkUtXIEq5S01B8H_ieJoPLZdTDIklM19qFpXoCosLVLOcUOUobGVvtUGeO9MY9Ujxw9axMYYWkiCJJNv4RuAGauDnUvqjiHKS0iLyowW81CLFdppzDgQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfAJJGBW5t6kqgEW_m2SgaZ6h8O31Ew9cj7sddq7pqUVvfsEM6hAOnK9Sq-s7WV6QlXPVT3zIu3zHc0rs76VITkeOZe24JB9VzMsdr72RIo54LA-QHD8s3dUCocpbBADpCJdcyquXbvGfTfUEF5fwIn-gVbCkTnsTPqlkGBxO27pukPY27vKepgG-0uP2Ffj-ztzBFF8tZOimkd58wLmm8MmE0xbaQi0UYg6M3MRZORJ-hl6T8HXb4FJYAeJYBDokqcO3Kb5nl0NezZB_gs6G2goPl6BFFEO_Tu51tgXTucPWTyxF648gnxbraviYph_8SHMxsSHllgyz1N3VvuSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Y-hBAm2wbM_l7C2zkFHWaWf46oXWL799iJUkvpggWSoYNC-g-E6eg8NIC6XgmX_n7-R-C-f7RJAjSXLCvag2Q4eXnWZxwZc0AIFOQwVorIllENCHkqGoWHGOb1p5Db6gRJz_b5qxltV4h9VCHxqwJu1YhsJENFVNBJ5V31Gw7JaA9BwbgdEB1XbuORCCq7e2MVc7OEVFc17WWGkYBpLwyHHN07kHcsT2UghtE6Xk5AMmfhtVxgJkKv8Xk7gMXT7s_gOD7bi4dZYUEyzJJrmjknm4lwl3abCXNhh-zQol1Ah-7GJA6ZnzgTrtwC3vvd4pRtHf-2Mx7Xx7T3gQy_8VKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Y-hBAm2wbM_l7C2zkFHWaWf46oXWL799iJUkvpggWSoYNC-g-E6eg8NIC6XgmX_n7-R-C-f7RJAjSXLCvag2Q4eXnWZxwZc0AIFOQwVorIllENCHkqGoWHGOb1p5Db6gRJz_b5qxltV4h9VCHxqwJu1YhsJENFVNBJ5V31Gw7JaA9BwbgdEB1XbuORCCq7e2MVc7OEVFc17WWGkYBpLwyHHN07kHcsT2UghtE6Xk5AMmfhtVxgJkKv8Xk7gMXT7s_gOD7bi4dZYUEyzJJrmjknm4lwl3abCXNhh-zQol1Ah-7GJA6ZnzgTrtwC3vvd4pRtHf-2Mx7Xx7T3gQy_8VKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tG1RyYFSfPJxLYKSv3FtcqAvhb1E7Zpkw0VHxsgM9g4hAUw0UPIQEazV3ZRd6vc_cTalEq1jqJEOcD7Eegfn3a0qt4_rB2m8PYNjKoVSXH2mNktq0y4-hU-zqF_CvvrPBRa4aJmGLKU_r0gJvqjISY8TQlYhzocf9P5viNf0jZcWmsknoCo2Lat_T81eWo1uHn6EmgzJkn_c_rFuKXZEBZmjRaFe0mG2kb7b0o5PwkCxnQwUnh6dHeGCbZTVenFzRH-TCV_f-GSugiVKdKt_grI7piqrqMI4bYVftYil_Qd2jP9__db2exPJayV4FDhu4B3L23PVO86-gX9OO7m0MrAUuxrxUc2tI8OETRiwnwA3yps3g2DATjAe2BcOPjNq-kwMfTc-nsnHaiLAC-tXwrh9SSq7JGkd0GoQVGr6rtSqnmYNhTN9s-SZ2s2tF-1YKYTV4TASBxbPehcksryIlmTqFjgjLp_OpQExOEK7hxCM8tpC61_XzSMzPVP24wx2799Skg2krBQj9_icYeCuP_uOECl_jpeuWt84UZCw-Dkgek39EjmjnAbeulolBlMstPpshrs8MsilNkSVTeOfdBaHCWQy1uDuXcQzmmiL0hyEuTAmOhn4gpkowruaYwfqswHsO34_W5u8HT8kJVO6k4kg4ULd0YOMZLEEBDcAZ3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tG1RyYFSfPJxLYKSv3FtcqAvhb1E7Zpkw0VHxsgM9g4hAUw0UPIQEazV3ZRd6vc_cTalEq1jqJEOcD7Eegfn3a0qt4_rB2m8PYNjKoVSXH2mNktq0y4-hU-zqF_CvvrPBRa4aJmGLKU_r0gJvqjISY8TQlYhzocf9P5viNf0jZcWmsknoCo2Lat_T81eWo1uHn6EmgzJkn_c_rFuKXZEBZmjRaFe0mG2kb7b0o5PwkCxnQwUnh6dHeGCbZTVenFzRH-TCV_f-GSugiVKdKt_grI7piqrqMI4bYVftYil_Qd2jP9__db2exPJayV4FDhu4B3L23PVO86-gX9OO7m0MrAUuxrxUc2tI8OETRiwnwA3yps3g2DATjAe2BcOPjNq-kwMfTc-nsnHaiLAC-tXwrh9SSq7JGkd0GoQVGr6rtSqnmYNhTN9s-SZ2s2tF-1YKYTV4TASBxbPehcksryIlmTqFjgjLp_OpQExOEK7hxCM8tpC61_XzSMzPVP24wx2799Skg2krBQj9_icYeCuP_uOECl_jpeuWt84UZCw-Dkgek39EjmjnAbeulolBlMstPpshrs8MsilNkSVTeOfdBaHCWQy1uDuXcQzmmiL0hyEuTAmOhn4gpkowruaYwfqswHsO34_W5u8HT8kJVO6k4kg4ULd0YOMZLEEBDcAZ3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTLy-huSWg9kMMVcuJzt6dcOycome9QhJZ9MDDDyMp5rBOGErrOZgGNw8vJahAueIIFkCUs_QxlxJN4szIawxMKJyFahqDeeObAquHDhgopgqLbhXlnt1QBmDWShOynSTnp-Ib52gjGTVSX6IW6tFSqM1eXKB_zRMEnvmK-JtrDpnfuQcqhdlmqhfjmdL0XiX0Y5jCYLfLxSkkwis9C1qRVtuykq3SoTQku5lyUrhDjvMEyU0r0_4RT-0d4W4ZX77KYKEcpJ1qAVFEpJA6aPC15IsbPM0oGY-J9FczGgs9I94l8beH6sUGAM8TlyvyEV0XFVPlDG2zZjdRSVFbFb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=nTniflNSgG-VkdEV7pfigWZRT5kVHke9JoEq3FNFLR_9OeH4WGLewN_Bc-dTA_LPzEHOYh9bva9umSKXwzAcKO6oD-3yJns4ikApBA7nHpx6ojT4IGvjrzGCG4lP58wBRaqvXMF2S3c-7XYZIWgkMYo0taF-l6fH6iulLI2Y62Gn65Pc-sngbjs7dqsTtaO03z9wfofDkUeavF9ng9EtEi0wqKp-TruGSjIbui0kEf6jAo7peIHZbSudaTH-9inNyIoElyB7DmfSNhYVdzcJKuKil6kSLHWOL6Pxlmj7pitN1R8AuT_fp5dXyUAtawomV7K9Qz2WYvizKeuJFnDqMCZtZZf0OAVFIbVT7vRnX5feWX9m7hflX3_qLfSbzDzyGvmYKU7-5dstel-DqWO08dWcWmPuvWd8avYkUEsYaOQ1MOUIb_irHb8IRq8eoy4V2g-g6dWgW5cMpYMb7GJSaBOux7m3iw4ZhAZcA-32VpVWOzB8sAehugNoNDid1sRicJ6xQ0-euHdU0ipToM4dBSWT1mQhQ3zZiguNpKYWYrUkl6uIgUqQ3gK971Ajd63Hz2YXNUM36gDdVRKo8IArYenDLG0YXAmYkPXCV8M_0obK0q4I6JXWlJZBV9hWu0DkXuOLYCzNNdguu-W4H78bSoOfgcEOiWITgrm214Ky1f4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=nTniflNSgG-VkdEV7pfigWZRT5kVHke9JoEq3FNFLR_9OeH4WGLewN_Bc-dTA_LPzEHOYh9bva9umSKXwzAcKO6oD-3yJns4ikApBA7nHpx6ojT4IGvjrzGCG4lP58wBRaqvXMF2S3c-7XYZIWgkMYo0taF-l6fH6iulLI2Y62Gn65Pc-sngbjs7dqsTtaO03z9wfofDkUeavF9ng9EtEi0wqKp-TruGSjIbui0kEf6jAo7peIHZbSudaTH-9inNyIoElyB7DmfSNhYVdzcJKuKil6kSLHWOL6Pxlmj7pitN1R8AuT_fp5dXyUAtawomV7K9Qz2WYvizKeuJFnDqMCZtZZf0OAVFIbVT7vRnX5feWX9m7hflX3_qLfSbzDzyGvmYKU7-5dstel-DqWO08dWcWmPuvWd8avYkUEsYaOQ1MOUIb_irHb8IRq8eoy4V2g-g6dWgW5cMpYMb7GJSaBOux7m3iw4ZhAZcA-32VpVWOzB8sAehugNoNDid1sRicJ6xQ0-euHdU0ipToM4dBSWT1mQhQ3zZiguNpKYWYrUkl6uIgUqQ3gK971Ajd63Hz2YXNUM36gDdVRKo8IArYenDLG0YXAmYkPXCV8M_0obK0q4I6JXWlJZBV9hWu0DkXuOLYCzNNdguu-W4H78bSoOfgcEOiWITgrm214Ky1f4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=dv9t2Hy1hDb9zZ8UKskwC8VMULi21N68a8dsG0DIHkMQh6hmAZ9TcI7_4wrUpwbVihPqQdFHVGam85TSLn-RuQe7SMH4VOUX9AXsOQoLyQMthX1fgREosK-i1oHnFMN2R5VhDvz-VUuY4Iqzdp8sckkNAMmtSOHe6xIkY-WtafAonYW7egavSvtkMhqCIS4s8TxhNwwyRNl2Wz28yt8jHMRqSJyTCBbuB0qiy2LbeMKL9Da6UH2qNNWEPRLcbR9zM6xCA-1xW_k8Zx9BXWcoE-IFPwuZrZlaZEKL24F16vfqJ2GNFK_nt-OGbP7Dfsew9eePVGH439Vb9bGv6NEjq4PRVScx5c3pnUkn5fKt5bK6ZaLczuZrt1n2GIfXbp_1RXXwJlVMNMS2hGs-cMg8-QFTfm8nL8JK3SAd436m94HtE6_WSU7xF1pcfqXj1QhJPeelNbefIcRWQ46IxhR7BYsYff_-UlH5XZYl3jLeSdeX2UP6mKb8avk3_2AeuRyMhKNRBG71o4qOfaH3OqiHJzSkhCLsos70hvdBzCt46n7rZOudHHr1LbFWhJdpamjtUQOalVhxQYdzzYb_rPD2In4bYQMVB3oEUKXfC7glmI2Ap6JSAGTfgTXO-tujYrAxFWNTo9q4DY4clY-8cxfWIrJj4RfrttxGeR0e_4FsPlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=dv9t2Hy1hDb9zZ8UKskwC8VMULi21N68a8dsG0DIHkMQh6hmAZ9TcI7_4wrUpwbVihPqQdFHVGam85TSLn-RuQe7SMH4VOUX9AXsOQoLyQMthX1fgREosK-i1oHnFMN2R5VhDvz-VUuY4Iqzdp8sckkNAMmtSOHe6xIkY-WtafAonYW7egavSvtkMhqCIS4s8TxhNwwyRNl2Wz28yt8jHMRqSJyTCBbuB0qiy2LbeMKL9Da6UH2qNNWEPRLcbR9zM6xCA-1xW_k8Zx9BXWcoE-IFPwuZrZlaZEKL24F16vfqJ2GNFK_nt-OGbP7Dfsew9eePVGH439Vb9bGv6NEjq4PRVScx5c3pnUkn5fKt5bK6ZaLczuZrt1n2GIfXbp_1RXXwJlVMNMS2hGs-cMg8-QFTfm8nL8JK3SAd436m94HtE6_WSU7xF1pcfqXj1QhJPeelNbefIcRWQ46IxhR7BYsYff_-UlH5XZYl3jLeSdeX2UP6mKb8avk3_2AeuRyMhKNRBG71o4qOfaH3OqiHJzSkhCLsos70hvdBzCt46n7rZOudHHr1LbFWhJdpamjtUQOalVhxQYdzzYb_rPD2In4bYQMVB3oEUKXfC7glmI2Ap6JSAGTfgTXO-tujYrAxFWNTo9q4DY4clY-8cxfWIrJj4RfrttxGeR0e_4FsPlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hRAcxjY-f8JCcJtG7msoBwXaT7W67mxl_c2-YIQMq3UMoKKvPsFjumZR9u-B_RPADPnUQV7D9PHsp0zAUJ5ZHsNYRNWsZBsd8w7sF3JvfFSJcfZJfo8PygL08VU7NOmQZsJTG8E2ZgIs9RK48TA5woWsKaqhrOjzHrVMItFyqFZkEDAGcu4ruDOsVj1VSKzss2kyrVxK6aWGocqUig2fROYFY6bTRinSXzn5Frs4t6SlFXmd9XCVFBAu66HUdga5cxmQicRtSx_HfwZoHw3UPpjoqSm3e4pMkuZHnI7NV80w1n0dnfBCzfxLt5-dL44ni6YBhAi5C-2P25hH3Ai0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hRAcxjY-f8JCcJtG7msoBwXaT7W67mxl_c2-YIQMq3UMoKKvPsFjumZR9u-B_RPADPnUQV7D9PHsp0zAUJ5ZHsNYRNWsZBsd8w7sF3JvfFSJcfZJfo8PygL08VU7NOmQZsJTG8E2ZgIs9RK48TA5woWsKaqhrOjzHrVMItFyqFZkEDAGcu4ruDOsVj1VSKzss2kyrVxK6aWGocqUig2fROYFY6bTRinSXzn5Frs4t6SlFXmd9XCVFBAu66HUdga5cxmQicRtSx_HfwZoHw3UPpjoqSm3e4pMkuZHnI7NV80w1n0dnfBCzfxLt5-dL44ni6YBhAi5C-2P25hH3Ai0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eCV_m5IejBq1-2Kibo1C5lwPORQ7qsLSLYkSdZGrle9-1kDV09edyZJ_GU88vkifDSg0Mtzf88ushRcx7NBM7DYawSck7wublsytzBOlN9QtOTLAH5vH2aVkR8XCG4UMQzi9Liz6mHqg_ovD5ay3Fq-DEclE4oGip19mCfIbHoaZfkqbT1fsX0o39bLy39B_40a1I7URVbBkjGQ6Yho33Sxe7DdRa_M2p0JXo-jY-MEmDkMD3oRG-qWEVEaxjrrcRQNoZOYrqGnw2JyNYmpqcitYMB05yTE48AhFkVAyj7geFNv38gzQKzxIPzqjeds7dqPklIKijBWW8mvg9Va1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eCV_m5IejBq1-2Kibo1C5lwPORQ7qsLSLYkSdZGrle9-1kDV09edyZJ_GU88vkifDSg0Mtzf88ushRcx7NBM7DYawSck7wublsytzBOlN9QtOTLAH5vH2aVkR8XCG4UMQzi9Liz6mHqg_ovD5ay3Fq-DEclE4oGip19mCfIbHoaZfkqbT1fsX0o39bLy39B_40a1I7URVbBkjGQ6Yho33Sxe7DdRa_M2p0JXo-jY-MEmDkMD3oRG-qWEVEaxjrrcRQNoZOYrqGnw2JyNYmpqcitYMB05yTE48AhFkVAyj7geFNv38gzQKzxIPzqjeds7dqPklIKijBWW8mvg9Va1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZKa_TYB2yJ2it33XVJ5hmfKvhvFSpF4lCoqeaxjvmRkzDLyxyQwFsz6JIGu-7KLad2jf24q94d5W_BgPoX6YjqFptP-8jx6MWSW52byda76zQjsdzf4he9rZGLbwxlXaIOuwldGD5DfsiVoPbwLEafFIW485nRlIDACdljytpIIwOvltJwFshk1_GLqSLS1_SKjLjuXTnQfj0MhWPwTrOSodNANE4c00N67WlfhqOdeOADBzcJG2Apdh4F7zXpzlx-ButyOkuz3VTlKM7d3ACoUwVFPY--txurJatU1jvMvvFxcixdOI6lE2IwWvTMyAUxkWQmoEoyVk9UkEe5FdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZKa_TYB2yJ2it33XVJ5hmfKvhvFSpF4lCoqeaxjvmRkzDLyxyQwFsz6JIGu-7KLad2jf24q94d5W_BgPoX6YjqFptP-8jx6MWSW52byda76zQjsdzf4he9rZGLbwxlXaIOuwldGD5DfsiVoPbwLEafFIW485nRlIDACdljytpIIwOvltJwFshk1_GLqSLS1_SKjLjuXTnQfj0MhWPwTrOSodNANE4c00N67WlfhqOdeOADBzcJG2Apdh4F7zXpzlx-ButyOkuz3VTlKM7d3ACoUwVFPY--txurJatU1jvMvvFxcixdOI6lE2IwWvTMyAUxkWQmoEoyVk9UkEe5FdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WGlLWt59J-kKrngg_oBuWYmWIoGdCB3dDR2KE3jUXNz-CLjiJyWcJdxyNUBXAqX-REjJ8lMnjH1ohtVErdQ7LK1dM4EBfqOMszo1a205U22MffYl4ArghtVYVVUqXk0XADhbSdlvc3s8GL2H1y4e_9jHR3yVtWdzKiKcHAGOQ2TFMt8bhPcNKDDEMNRY9cZMGZgYADKzJGCTajSPjVDPw2t_hTT3UYxIjBZ8W2iUC5dBCpDc-yjbsdYH-vg_XCxf8KJB8RfSRg-9l3q2o6T7e0b6TmF_EofovVGEVjFwCMtHc8lIPBRaMX56E2voxFZ3a4fgl4QVVWhAucAd97UFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WGlLWt59J-kKrngg_oBuWYmWIoGdCB3dDR2KE3jUXNz-CLjiJyWcJdxyNUBXAqX-REjJ8lMnjH1ohtVErdQ7LK1dM4EBfqOMszo1a205U22MffYl4ArghtVYVVUqXk0XADhbSdlvc3s8GL2H1y4e_9jHR3yVtWdzKiKcHAGOQ2TFMt8bhPcNKDDEMNRY9cZMGZgYADKzJGCTajSPjVDPw2t_hTT3UYxIjBZ8W2iUC5dBCpDc-yjbsdYH-vg_XCxf8KJB8RfSRg-9l3q2o6T7e0b6TmF_EofovVGEVjFwCMtHc8lIPBRaMX56E2voxFZ3a4fgl4QVVWhAucAd97UFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=sH6-qOyYi9yx5nVftXdR9sW2JTOHlrFv0wWZERx6oTjwbDjogLHgNbpnrfVVfnyCHq4VdfAvB5mQ7TiWal5_TuGMRmd8vw3TB9aRcoQxTv_UjFCls0_AYgGim3I2Vu2g7V2zDOdji-Pi--ZyEzgeaAAAxznyHj4uqZgBjGI0qet630zVeKKeKSxHCIb925bhQW_CZRmiqgaF6nD5Ih5bUcyx50RVB8lWnmursksuiVU6VCU6W5HBN81iP4pCo8X0lF9-0VaAYDHcJvOPF_eVl6VjuE9e0jeW1adW5jIuu6Bf8iw40Ey_ZZGCV4DcdpEnGn3T4-HlvkCEY_SLJDGdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=sH6-qOyYi9yx5nVftXdR9sW2JTOHlrFv0wWZERx6oTjwbDjogLHgNbpnrfVVfnyCHq4VdfAvB5mQ7TiWal5_TuGMRmd8vw3TB9aRcoQxTv_UjFCls0_AYgGim3I2Vu2g7V2zDOdji-Pi--ZyEzgeaAAAxznyHj4uqZgBjGI0qet630zVeKKeKSxHCIb925bhQW_CZRmiqgaF6nD5Ih5bUcyx50RVB8lWnmursksuiVU6VCU6W5HBN81iP4pCo8X0lF9-0VaAYDHcJvOPF_eVl6VjuE9e0jeW1adW5jIuu6Bf8iw40Ey_ZZGCV4DcdpEnGn3T4-HlvkCEY_SLJDGdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iKW0rYOuL2NlMWoUScnV1mY-W_TDzchacR9OyLPXPddEzmMBzSMreLzBTr5ZnXjbLrA4An_RVLrjP4helKe-2Kl34rQTfX35VAEdX8gQ5LYkG4tdf3ECNWugQ9mAsRU_dVDqHtU0XJrD9KoPIecPKZ3Zf44V1QajEUyEDPKYiqwBheGpGtEMBpJtHyXdOZ3letdZR2ymhYhnBX8cYyYjgQtFD5GiY3Rb6nZMSUZ1SeV1NMk_ABUsaCZF84A6s_r0IC9VefxVfFJrU-JQsJsBL2FTkogy_HpEQ5ZB-ddsgVV9MiL1iEiR4FUXL5gpwrcHf0S6fpem17Yd97oVXNp5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iKW0rYOuL2NlMWoUScnV1mY-W_TDzchacR9OyLPXPddEzmMBzSMreLzBTr5ZnXjbLrA4An_RVLrjP4helKe-2Kl34rQTfX35VAEdX8gQ5LYkG4tdf3ECNWugQ9mAsRU_dVDqHtU0XJrD9KoPIecPKZ3Zf44V1QajEUyEDPKYiqwBheGpGtEMBpJtHyXdOZ3letdZR2ymhYhnBX8cYyYjgQtFD5GiY3Rb6nZMSUZ1SeV1NMk_ABUsaCZF84A6s_r0IC9VefxVfFJrU-JQsJsBL2FTkogy_HpEQ5ZB-ddsgVV9MiL1iEiR4FUXL5gpwrcHf0S6fpem17Yd97oVXNp5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FqS4ztUhl5az9HUCTz_7dLgE5Rz13NfSP2G0dQraeH2Xa5OTfsOuEcTXemeK6cWbq-X_MAafjbVx2XLnMel8g8mrhTUe7k6laHKH5_cYnTkwdQst5cB5tzXxNmLzwN2EbxAIdAB4IbtN0wWe1k8CeUmDONMyUtyJ7j0m5Yo3eV5u3Apbq6g_H5B0yt5a5n4pSb3up3k1Q2QSoID2ti1uxXYQkN62Ygi4EXs1RT8c7HAUiyaMDFyNfMSFh3__-ZoRQGktGjKZAx-wz3QNkg8NqOy4a_nFzuhnmTOo8GuJI4BSL-8bu4XX5udNEccuFck6NR3nZzuhwIqfSV5iBh9-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=FqS4ztUhl5az9HUCTz_7dLgE5Rz13NfSP2G0dQraeH2Xa5OTfsOuEcTXemeK6cWbq-X_MAafjbVx2XLnMel8g8mrhTUe7k6laHKH5_cYnTkwdQst5cB5tzXxNmLzwN2EbxAIdAB4IbtN0wWe1k8CeUmDONMyUtyJ7j0m5Yo3eV5u3Apbq6g_H5B0yt5a5n4pSb3up3k1Q2QSoID2ti1uxXYQkN62Ygi4EXs1RT8c7HAUiyaMDFyNfMSFh3__-ZoRQGktGjKZAx-wz3QNkg8NqOy4a_nFzuhnmTOo8GuJI4BSL-8bu4XX5udNEccuFck6NR3nZzuhwIqfSV5iBh9-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7B62Qc4YWUk4ckhlOiSVlvO5i0tvi4CxJlVkrtWoTHOW_2-ZPD5tzlUpzE3FqvoCG0WRCBrU7kAmHknqwF1oMO2UpzQzmX8Be7Wz8QUMdUW-8sv17MduT8UTYOrG0orFmnf73Gh881GtusxDsMOe8K8KZkgxLhmzTUgaDrHIW6mL0Xem5SxGU6FHKVk0ZqHjkBBCPlYUIyDScLdVmI7HPlO7w_zZlDhSqCdhqqJOnLysICRO5thWNmCFDmE-Ysd5TDn59Xu2DTwO43TDlF_E2Z0uAOmfjvt49YJaxSqyjKgn--Lulb2ChTnZOzWqE9YSRw6IZ3T8mfBjmLqWeWAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=mTftESuU37Y46NCrO4PxZv_z7igNjmuOC3Pn5pS6YFXcbnwl-a72jq5Fb_EadRvxV9KO-JVDZ7qQjfehU3EmicXXhUaRWYqzjsqm67qAUsuEx0sweumuQghqPTCXnTaT3l6lqC48BRz0D89-Q_UxvtJPmZfDeis3ZK1JiDOrsxLbBu-zMGfLxHkP9G-qFBEd-m8-mVBD_fMlBwfZ11jBTuQtTtFh-6XbOL5Yqt9UKpT4aw3mMLWp2-At6zYEEz-IdsvYmwwRfIpiKsp2g6JjhODAuHwBG58Q7RdGWCYAInX9VYlLPyY_QEylw1HJ-aow9r04CCGeowtbVKQpl3x7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=mTftESuU37Y46NCrO4PxZv_z7igNjmuOC3Pn5pS6YFXcbnwl-a72jq5Fb_EadRvxV9KO-JVDZ7qQjfehU3EmicXXhUaRWYqzjsqm67qAUsuEx0sweumuQghqPTCXnTaT3l6lqC48BRz0D89-Q_UxvtJPmZfDeis3ZK1JiDOrsxLbBu-zMGfLxHkP9G-qFBEd-m8-mVBD_fMlBwfZ11jBTuQtTtFh-6XbOL5Yqt9UKpT4aw3mMLWp2-At6zYEEz-IdsvYmwwRfIpiKsp2g6JjhODAuHwBG58Q7RdGWCYAInX9VYlLPyY_QEylw1HJ-aow9r04CCGeowtbVKQpl3x7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jDmrVKmTZaSkxzpXX5oa8A5a9wsDlaEdR4CXs8vxstT_yZvmj3U9KBs_wrySQMO1Frm4ATJ7mc6X8lDxNZiq8vsVgSF5LJfu3bHqA_cgtnNJrd51WjLHZ4q6jbOb7vci9LkPCCf3PJothCPs8uG-qS-VQea6LY_86ybled685jOyMiUYtVpDoP3FdzUonXJ2OjhAl4Gq9Fc35CEm9It9AoWIRjPyQhv-vGFqo4DiVkDeyuPlk_Nl6isAi4PVuV_6gClhHIqY3a7iDMEUJ0WHOAYSx9DF0pRlD6nOWFRDByqT-9vNv9BAIF_LYcnGd5zS6n45vyJhOqNUmPLwRL336g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=jDmrVKmTZaSkxzpXX5oa8A5a9wsDlaEdR4CXs8vxstT_yZvmj3U9KBs_wrySQMO1Frm4ATJ7mc6X8lDxNZiq8vsVgSF5LJfu3bHqA_cgtnNJrd51WjLHZ4q6jbOb7vci9LkPCCf3PJothCPs8uG-qS-VQea6LY_86ybled685jOyMiUYtVpDoP3FdzUonXJ2OjhAl4Gq9Fc35CEm9It9AoWIRjPyQhv-vGFqo4DiVkDeyuPlk_Nl6isAi4PVuV_6gClhHIqY3a7iDMEUJ0WHOAYSx9DF0pRlD6nOWFRDByqT-9vNv9BAIF_LYcnGd5zS6n45vyJhOqNUmPLwRL336g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kG2SF5Km2eizm91JlL6y01lenU55OpgIs48PZNI7zpSzPt1SaiEEIrw54Hm42KRD_1F4WFi3D36wtBOsHT0YQ5RRBvyow7PNvKqwi0zEiD4Ee0M8GGYJzaUjnv1fVC-jMyiotgNPvFoBMBg63JnCH3_jee6BmXxs82juKGmnGRuesFX9LQeZFi9DVtD-6WLogmJ3acSL1kkdFiaCUU2syKv1RR0XMH9Ik7x5LT9YnOUC1y77NgUlSVxEyLRBtTEP5ajBvBfWVMf5BGs6Be8PekSGDSWqqSpdKMJikSxqse1_j0n4YEedSi94GuJbOs3bGwYLZgE_dPZkhA90NpkNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=kG2SF5Km2eizm91JlL6y01lenU55OpgIs48PZNI7zpSzPt1SaiEEIrw54Hm42KRD_1F4WFi3D36wtBOsHT0YQ5RRBvyow7PNvKqwi0zEiD4Ee0M8GGYJzaUjnv1fVC-jMyiotgNPvFoBMBg63JnCH3_jee6BmXxs82juKGmnGRuesFX9LQeZFi9DVtD-6WLogmJ3acSL1kkdFiaCUU2syKv1RR0XMH9Ik7x5LT9YnOUC1y77NgUlSVxEyLRBtTEP5ajBvBfWVMf5BGs6Be8PekSGDSWqqSpdKMJikSxqse1_j0n4YEedSi94GuJbOs3bGwYLZgE_dPZkhA90NpkNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=MzMA67-aOA1AaZLVMQxOGpmaJCCUZHCEfdV3kdWecZm_rgqhWWFCY_kcq39netuNz6Rkw28zt1ziYeTE3kVXSUrYBw1Sr-wz4gwP7egkR5IJIXjWC06z3ZJoepEfVKQd2wEmH7tzMxCu8noBtB0xn6WAyflzsObDpEuzhIYJm2FjcuvMn70fom9yjObNQBGRqzicRdxT_UYlZHUb4P7963DFxjpkwdDe_Tw-95G6LuXW27vFZTilQyTv3Y18mLYAF0V68V52umIZ2gdEsftC3aQn8tUHQZ8LOKqJSp2jt2BIonWcYe_N2IBlapB2RIGNROmZeyzabG-zvTvu1iUOLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=MzMA67-aOA1AaZLVMQxOGpmaJCCUZHCEfdV3kdWecZm_rgqhWWFCY_kcq39netuNz6Rkw28zt1ziYeTE3kVXSUrYBw1Sr-wz4gwP7egkR5IJIXjWC06z3ZJoepEfVKQd2wEmH7tzMxCu8noBtB0xn6WAyflzsObDpEuzhIYJm2FjcuvMn70fom9yjObNQBGRqzicRdxT_UYlZHUb4P7963DFxjpkwdDe_Tw-95G6LuXW27vFZTilQyTv3Y18mLYAF0V68V52umIZ2gdEsftC3aQn8tUHQZ8LOKqJSp2jt2BIonWcYe_N2IBlapB2RIGNROmZeyzabG-zvTvu1iUOLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECyJFox0uKMdPhIT18XdstiQZO_6L1oVeQVHirNS9Jd2GIn3zHVKn_3yT9qs4ifeSHHvnX-T0EnEcrcZpaQQ_c1TedMxs2fTo9to6yMEqyYiJDNpMQE2WVGXMGN0M5dJ0u9kjdIumS6fHZHkD_yRObTSoLTlIPj4MObtGPqCEjBvgp62cgHDPKPSg6gK-N6Ysg_6cgKxT8PkFc9BSlp3DU5y3Pdc-qfyKSYEz9VL4DjyIoX3I2V5p0KNRv8zDQSaWC-brwiTGKleCimyXOVNvtLzbiHYY8etG7OVLfnT7eBoPCax6K8uvFf-k3unAoWCyjjEH71bC91W9Fz8XbNaBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lcnV1XXRbuIb_lZd3JHUa5Q3xESUuGKtMCx1BfBWzdU6_UFWEU-fYqEyIw7x5C8TLD6P_8Ct_n9EbnIc30_DdR8ht9D60t70pVM5fRHMCI9Zxx0_qZH2qrt3mfBzOh4JuF62c7-9V5NxYsfqQBZAFsLE9wOHn3XqKdfoCTmICCfiHXqYO0LC3zFHQ0-0FcSMBlR0feYLqc_NrEqve7E3Y6yXzahACDItB38ACZpb6L51qvJQXmHUkDKSddr3ZBk27IbMSgN_MwyBy3ivuesRpC41JYYS-qtYL2nWQuWRyzQJj4tl3EcodRoLsHKpwEqDqEBMNcdU16b6HiECuiG7JzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=lcnV1XXRbuIb_lZd3JHUa5Q3xESUuGKtMCx1BfBWzdU6_UFWEU-fYqEyIw7x5C8TLD6P_8Ct_n9EbnIc30_DdR8ht9D60t70pVM5fRHMCI9Zxx0_qZH2qrt3mfBzOh4JuF62c7-9V5NxYsfqQBZAFsLE9wOHn3XqKdfoCTmICCfiHXqYO0LC3zFHQ0-0FcSMBlR0feYLqc_NrEqve7E3Y6yXzahACDItB38ACZpb6L51qvJQXmHUkDKSddr3ZBk27IbMSgN_MwyBy3ivuesRpC41JYYS-qtYL2nWQuWRyzQJj4tl3EcodRoLsHKpwEqDqEBMNcdU16b6HiECuiG7JzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=R1o4A__mNeVpxbQrxTpGeESyX_aHwPlyjPqPhl5U5UuONUec6J5o3TU6t0Crp8ObHcgjVWkSqKZcuMbY6hDvo64v0w1aTg-gQOskecb6HtaQZOyqPmkTRLvrPg2YhlNFnx183iquQu22A5fPUdwZVY1Ub4ZM_HJdj_Ys9kok4Gmnbgw8jB4SyMBwzrPPsXIVXtMyvCnnZz8AWh-cwT7ev5hBYs3mO-GJzQ5op5aja7Qrv5orJKpOvEmKGiKTGtoQ7GrZXblbr4gT9SNWP95Fd-93rsWkBkzN6Vad1ACDI9Cz_eNfZEnEluAwvHBF2eT1uJ6p7AF0h390TujV_YRhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=R1o4A__mNeVpxbQrxTpGeESyX_aHwPlyjPqPhl5U5UuONUec6J5o3TU6t0Crp8ObHcgjVWkSqKZcuMbY6hDvo64v0w1aTg-gQOskecb6HtaQZOyqPmkTRLvrPg2YhlNFnx183iquQu22A5fPUdwZVY1Ub4ZM_HJdj_Ys9kok4Gmnbgw8jB4SyMBwzrPPsXIVXtMyvCnnZz8AWh-cwT7ev5hBYs3mO-GJzQ5op5aja7Qrv5orJKpOvEmKGiKTGtoQ7GrZXblbr4gT9SNWP95Fd-93rsWkBkzN6Vad1ACDI9Cz_eNfZEnEluAwvHBF2eT1uJ6p7AF0h390TujV_YRhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdwOKSXlczxtvjymaxPy3pBsPbgYY5Omgz-Xc5UIZ5E8uxz2kV0jWpazpWWFvth7MdJJojWSmyN8xWN6gXsOlIjx19Q1MkusBXKezaN1h2UWhZvCS1s8duq_byO3a_IzK3taSB1Lay3d_5sbRjpLmUQAIuVmETGoqeblTQapm4Tp7_ZKEC4TRutQ-uxq7GMXUr_OkBA78VTFeC8o3Mv1GW7sw_OnyqpkGEstpazQDm3GiZ5huuet94bGxTeIKm32PUpknv-x0IGVL0tIYyv7tfwm9maA_IPBwWdBpuDfkzxhqdLIwCqPSNzoCLpkfYzgIfvsEQmERdPnYPBB6DEVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ug5Y-KDhWOGLTWlfoYAfR4HrJOqwjv5UHpbvC7NksON4kd4eQ8bKIVIxY8kHo_sUEH6ykKp3-iJblXT2pu44rzyoR7xiWaYmL6YOZWDssbg-65b5I9TAKzuFA6Wk4RcxdubeyqdKZbIaLhhKS3FKv0oOHFbD40s1vOqNnA502pTqDA2uekGWK0NZpLEoIKBxnc40Vxjcf1zxSwHShl4WqVFdSvwhlMX_c9j1wFzB9igP8alSISBBpYYErfj0xG_tGghWv7nCjKeqE37CliRQswyUWQ6CdrhmUxXVl1XQbl9ZCns7leRvMPyYArjq36ch2nZz9dhi23pCyQNxvEbhEg.jpg" alt="photo" loading="lazy"/></div>
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

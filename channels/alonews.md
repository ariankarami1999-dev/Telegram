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
<img src="https://cdn4.telesco.pe/file/LQgPBxoFaJQUZNJESKBeODd94U90dEuPeW4PTTVv44_uC2VQVRJrZjny49ZKP-KNnNqtjU_d53Z0RJ1PKInc5UQuFBM9FUOIJ8tujCaUWnClMa4BI_jZtVlFuU0H7_-AQq83OGPmjPq7xZ9gjgNWY_lqaM0xk45LtfHcKGiM_GZ3plxj--Ia8nsPJ91vwZxUxPRZ1wGzDJGOcy_xI_X0lQI8D1z1Mh05E8qNY9gM3HEUghgbkP7yB15Z0JDP3J1LJjyqW127ReqPQW8s9VLZKuSAdxOg-JmpdY8gI7_4SqAIBbbbDwFJZKyK1KyxITTFVXTEFzcGAW6Mj-7Cd5zZww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-151417">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7RbgrDoaBnDnwvM1USNc9aqGf0bGvK98jvF49eM41sm6gsj1uClFS0BDZXpg_Ko0id0pNaphw18KX90ERSxrWsbeme3XIuRBw0khJTRF3mhGH0niY7ViO3xvOso_i9gaifo9qv6LSYPGktU7ORGSMjFChtU3CB0SCMEqJ2Gj-GtsTSsauNgCVpY7h-7eDcoALfdUdstSK08aMaqkIinefSywo7Kv3gs1zGokUwXNSLxiDLc8fdNhRkSv87tNDBGyYz_eIcivvPR2exJ23ZMM5D0YbHekCcEBnh1xZREWUSouozT69cthds4SyRWwspksnts2rKoJzy54bZFqyXwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔴
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/151417" target="_blank">📅 13:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thfjf33t_OCa78GLr-x-iwvoibqpAfup4CYYBEbxd49xWg6-9q_4imtvUdkW2WnRy6OROymGH71y2fFIWmnoBfTogsImUP5tC9-u3R5Y_SWA5tn9Ejo7v8lrsAIz568qCPvsp-eqAPSPrWUPS2FC1iHkTFPQhk1-hDUQmR_aOYRwfzQtiLtzngqswMri238VfSPJkt4tw7O6mTfpra9eq5uanzYtgcJDmkEZxVvXNrrP0zk-HbGxISU1Iah2_peI02g6rnd58mzuaTyowOTfJTaEbZtpE3KTGlaJYWWkFu2t3pr8cR4jjPAEKHuogMKQ2UNf_XUa2dp4qByxRvwzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زهرا عبداللهی خبرنگار پارلمانی: یک نماینده مجلس در ملک مسکونی بدنبال زیرخاکی بود
🔴
اسناد موجود است. خانه در بستری تاریخی قرار داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/151416" target="_blank">📅 12:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6513d8ae0c.mp4?token=JUDEdYx3VtEzmlaA4-RwDMppr65LxwYuv-c0647y5A3M4fql6TdcSnx5slXXvsPD2GHZq2-VwMoLQQEpuso8ogrOI-Kzq4t5mZxGUDQc5uwii0zmEd5cr77N86IHDlq3tU0r9TWo4VL1UAZwGTaO0Ft7CyadQH080Fp6iWzv6fhIamarWddWK2RmuGialBjcIAlE8t6Uif1atd7r7Qan_FVAXnmgJAkbVM0tOtih8weYBCkbgJ_ES6hgUiN_l0v3DXnfXKQJP6yeil1YeY25p6M2ZUEvSfqUL0W_WSqc8pZT5WNIGMg1FRFFXgL3SrQXK2dv7-eh3L_LEm5m2xAX5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6513d8ae0c.mp4?token=JUDEdYx3VtEzmlaA4-RwDMppr65LxwYuv-c0647y5A3M4fql6TdcSnx5slXXvsPD2GHZq2-VwMoLQQEpuso8ogrOI-Kzq4t5mZxGUDQc5uwii0zmEd5cr77N86IHDlq3tU0r9TWo4VL1UAZwGTaO0Ft7CyadQH080Fp6iWzv6fhIamarWddWK2RmuGialBjcIAlE8t6Uif1atd7r7Qan_FVAXnmgJAkbVM0tOtih8weYBCkbgJ_ES6hgUiN_l0v3DXnfXKQJP6yeil1YeY25p6M2ZUEvSfqUL0W_WSqc8pZT5WNIGMg1FRFFXgL3SrQXK2dv7-eh3L_LEm5m2xAX5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: اقتصاد ایران در آستانه رسیدن به وضعیتی قرار دارد که تعداد بسیار کمی از کشورهای جهان تاکنون از نظر شدت وخامت اقتصادی تجربه کرده‌اند آنها مردم ایران را در شرایطی قرار داده‌اند که اکنون در آن به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/151415" target="_blank">📅 12:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjNftl9I_GCdSAsVOCu9ESDhB9tlM1XdMaAk2bFZdPW2W4KJLJIKwuP7-dphBodm7RG-B1zjy6UKS9sIhWGmphmBv7WuEbMbBRcfaCJT71nJSeJ2ab4rPWVGtx_0CJETYNh6SG970qUbJqrqPxYdnSepJ9tN0N_xZ8oElI62XMGSWWJNpVyKAZl9wgyxgZmuVrNkPnkeCAWBtL3pIBye-3VuSeLebL-qQab4c98-vUfR7rkM2Wqtmy50o6X0FxNjjmDgaS5fI8zpcyMMtMhpcLcXcHsP1RMRhhcrufGvwOjDxZfDF2ULq6G6STV4txmn99iOY-qC1N8ZhlD0nL5faA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل خبرگزاری قوه قضائیه به نقل از سخنگوی این قوه: حمید رسایی بیش از ۶۰ شکایت،‌ ۲۵ مورد قرار مجرمیت و جلب به دادرسی و حداقل دو مورد محکومیت قطعی داشته که سوابق آن موجود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/151414" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151413">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609f1372f3.mp4?token=pD4-rhNN-bvsIFEhGT2kRcr_ETpElZ6Rba5Ei2bRYbPkKf4FvfHd1jc5y87EF510voW5HMK1i5-TcfOX4SwwuukFuYYBrkLAY7RSqyMSbSyjJZMYFOVa8Uka_9sU8Y-auDz4BeuBnCUWSxVKwkHL1Eb-otoMNQ0pTjJaWet3w5VzBnaUpswAcv_7IMKhCHNKqi2h_X6L_QpwtfuF5p9BjhCR4S4jPNzBwvERl38xJlNsH1dIfINWxIlnhTcX1y3-9iVNvyzpIy2QSVhVNpSBSF1DIDNDUUED8dCLL0ZPhbUImiHQkflt_mxrIWbSPTkT6LA7AxrM9xWpYJkHEB-ubA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609f1372f3.mp4?token=pD4-rhNN-bvsIFEhGT2kRcr_ETpElZ6Rba5Ei2bRYbPkKf4FvfHd1jc5y87EF510voW5HMK1i5-TcfOX4SwwuukFuYYBrkLAY7RSqyMSbSyjJZMYFOVa8Uka_9sU8Y-auDz4BeuBnCUWSxVKwkHL1Eb-otoMNQ0pTjJaWet3w5VzBnaUpswAcv_7IMKhCHNKqi2h_X6L_QpwtfuF5p9BjhCR4S4jPNzBwvERl38xJlNsH1dIfINWxIlnhTcX1y3-9iVNvyzpIy2QSVhVNpSBSF1DIDNDUUED8dCLL0ZPhbUImiHQkflt_mxrIWbSPTkT6LA7AxrM9xWpYJkHEB-ubA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا: «فکر می‌کنم تمام دموکرات‌های کنگره حتی به درمان سرطان هم رأی منفی می‌دهند، چون نمی‌خواهند ترامپ بابت هیچ کاری اعتبار یا پیروزی‌ای به دست بیاورد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/151413" target="_blank">📅 12:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151412">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b38e5687.mp4?token=HFFdCjtZBHHCUqjQHpORY6i7eRkevMc2BL_mOTF9WmThT-dOxs8TUCzq2l7iOyOGKi1KWRm5Yw0cxqC7FA9KcieXmO6pH7bERDyoa1fAaGg-GX-XrE0qH7O4GHxzCKmE9Uth-ojZ_NcGv9HgdB8S_aa7jU6S9OJOhagrDyVF6wCpUiY33SFEUiD6KKMKi1snhzte27n9AWUfnplTb2ICUdn98O3mMqCc-Rd9cnKEHKygBT07Zp7wTWF9VQr2sfIKj2izSXDmAQT2l5_fkpZIv8dQpUTq2q2TDeZMWt5SQyj-gfEBWqijNysa5smrpxikc623aMDEYMKowFKH2tz8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b38e5687.mp4?token=HFFdCjtZBHHCUqjQHpORY6i7eRkevMc2BL_mOTF9WmThT-dOxs8TUCzq2l7iOyOGKi1KWRm5Yw0cxqC7FA9KcieXmO6pH7bERDyoa1fAaGg-GX-XrE0qH7O4GHxzCKmE9Uth-ojZ_NcGv9HgdB8S_aa7jU6S9OJOhagrDyVF6wCpUiY33SFEUiD6KKMKi1snhzte27n9AWUfnplTb2ICUdn98O3mMqCc-Rd9cnKEHKygBT07Zp7wTWF9VQr2sfIKj2izSXDmAQT2l5_fkpZIv8dQpUTq2q2TDeZMWt5SQyj-gfEBWqijNysa5smrpxikc623aMDEYMKowFKH2tz8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا: «دموکرات‌ها حتماً تلاش خواهند کرد ترامپ را استیضاح کنند؛ احتمالاً در روز اول یا حداکثر روز دوم
🔴
یادتان باشد که آنها پیش از این در همین کنگره نیز مواد استیضاح را ارائه کرده‌اند. منظورم این است که آنها کاملاً آماده این کار هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/151412" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151411">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
تو یه ربع تتر تا ۲۵۱ اصلاح کرد، الان  برگشت ۲۶۰
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/151411" target="_blank">📅 12:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151410">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
محسن پاک‌نژاد، وزیر مستعفی نفت ایران: استعفای من ارتباطی با صحبت های ترامپ ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151410" target="_blank">📅 12:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151409">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
روبیو، وزیر خارجه آمریکا: ایران فرصت‌های متعددی را برای دستیابی به توافق با ما درباره برنامه هسته‌ای خود از دست داده است.
🔴
ایران هرگز به یک برنامه هسته‌ای دست نخواهد یافت و در حالی که تلاش می‌کند نیروهای ما را از منطقه خارج کند، رئیس‌جمهور ترامپ این موضوع را نخواهد پذیرفت.
🔴
ما نمی‌توانیم بپذیریم که یک کشور به‌تنهایی بر یک مسیر مهم دریایی کنترل داشته باشد
🔴
باید مسیرها و منابع متنوعی برای تأمین انرژی وجود داشته باشد
🔴
تنگه هرمز باز است و حجم نفتی که اکنون از این تنگه خارج می‌شود، دقیقاً برابر با میزان نفتی است که پیش از بسته شدن آن از این مسیر عبور می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/151409" target="_blank">📅 12:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcG1IBtYm4BIlkCGWTT67E8cBMk8OUqQHl8jqrQzm6JbSlh-okwaL-leosu3hqxqjWlyRJL3jOcKMFAoHO8-Ol38V7BOf6f71Ut-PlzGzxfnhdhSM1ctxmwehymazpQhdTShQM2CtRSv2kkJ1-Oadw8ew9KJnh0QznAiVie6czCnCoohQc15R1SDDtmMpWninFEjl4Aee_fLMY1uMQLh3MVVK00ptVDX6Z0ViTJgoajmihjsQIFg10S5l3RBIglfSQN2cM2sa0L6XMJrRcUPbfLFfpdpfHs4ah3uWwfOOoGJVTZ92spWnNAOV6-7nH2JEoNktWlAeRTNBrUblKPN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f99fbadfe5.mp4?token=G-92ZjoN90avqg98HLZhJRRwUizX4zuQrrJousHZTPWbE9JUWUzptrkCWLOHYj5JxpsIhpzio7wXgJjU2ttD29euB3Z8cEulLg_ssJv9Gn4aR7rsm9IfF0aeQ28_a97gcZR9NSSVCUE0bO_ykono8ZskOdAVA2BTQWlWPkba_pLNXaJJ_15bGpjQka2cG1cbGumJbHbCC235F614CJTEpH6psHPjnzP7B_yVTnp5Ls1lCpqBysiTMTRjB7DzGEmeYpP5Zgv5zLoyXp_DZxwmcUVR3-C66iOb4IWHmifaqkYN1oIlUuQ6OXNoQpg4lOOXR6tAwCamJ7jnJZ1Ul7UbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f99fbadfe5.mp4?token=G-92ZjoN90avqg98HLZhJRRwUizX4zuQrrJousHZTPWbE9JUWUzptrkCWLOHYj5JxpsIhpzio7wXgJjU2ttD29euB3Z8cEulLg_ssJv9Gn4aR7rsm9IfF0aeQ28_a97gcZR9NSSVCUE0bO_ykono8ZskOdAVA2BTQWlWPkba_pLNXaJJ_15bGpjQka2cG1cbGumJbHbCC235F614CJTEpH6psHPjnzP7B_yVTnp5Ls1lCpqBysiTMTRjB7DzGEmeYpP5Zgv5zLoyXp_DZxwmcUVR3-C66iOb4IWHmifaqkYN1oIlUuQ6OXNoQpg4lOOXR6tAwCamJ7jnJZ1Ul7UbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از غزه ۳ سال پس از آغاز جنگ با اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/151405" target="_blank">📅 12:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
امروز یه دختر ۲۳ ساله تو مشهد بخاطر توهین به ائمه حکم اعدام گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/151404" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bedLnp68QJYtZqwS2GASxQTW0fa9GrEnN8iTRCSonFp1YZsvsoPb5K_rjklYigBi-oXlj_U_aPqaYW71veGYx4s2tPEjV_oQvzZFZni-6JzwcYY3-75mRBcgpg-_TwKosK78s-r3HpErXGXjx7L75_ZUYrKKxNR1I7jkvvQwSl-CVMjjUfWi7UWNOw5Zma7heZ0O33BRzezMfMrzD5l7TWAKqS1D-MfB4j6qojoT0i6epJvNQhbLn1LEysHQh21Z6uSeTfPQuPlVXBfXA0RcWDqQyisvmQRi0wNFWwGY2rvs-sgQSYgrBcD5gRI4eGCylLgZZMWtgEAv5OuuYeWcKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3shxWuixK7GFpb3mBTA9LPm84HHOdsyIezdQ9dt369dngHuW-GrJcOAipBXi7Kjfe7OEHxdckarQzu6AOCM4b_uxQvYTHIprsn-tXAVf2jwXukFpiGW5jVEyXljqZJjnJzOSazBn8USe9KRULZ1pGhWEgA75mori_kUeMDrN6teLbfBLRgIl2bOTdl7VlPPmNCN2hTBp1mHPMePMldH6ZL2QWxPEoU_VpCdhd3mWB_sr_ypzZq86jepbLqCLuXteKDaz6O7hJjHRaTq8gnP9SjSwFCkl5AHL33eyv71KetRdDbh6uzYTab7udC3_itIe9BVoPQo2B-Hcvd0vrniRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr_zUokrvf7tMuhkCNuDeoN8KJdcodkNrqJeobEG6Qom5yXuSowicer_HrMKwEuM4eKDf1vpT3fsCrVSMVR_NgeEDQjSS2Rg4UD4NfP8-K5AYtoiZywMppirI_z939Mv37bP6dzIJUk0WljjWvIEiG_LNpkyTPcwOPSDSM4XrNBBI-IYKFKu9-WcfqhADglSWFdvsx6FvMn-pvfO62s7Ty0aZxcRLgSOLRMshDvHsKCZ3-bLeAiO16ptRwdxivU7wTPQULqT1I8pgCngv1Ks-mRq9RHfbP6NjurvGlp_6hA-4phONrB-eELvwsw7EAjQeQ_12la63uaDVgeTcy75sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwLc7mM24uVKsbUBz7ZryZh9wQv49aY3SidHCF1-1I2-Pf0ulKYaSog1hFGWQWo4r2OVyKUbzvcp6OSE4OWtmIoJKuExsgzviVoGIXNRUKbv15JnMxA-ruG2BnVr2gvuvkKtYX1wguqrSr6AhlyBcC-UTXFx7bYWSYCEI6mSIw7h9I0ss5eacU-gahBNrYP9p1R2v75PjAstfJMuWEfKSd55ISwSfZAwxhy9FtoH93eqXWstqUxC68aBG2lC_RaumU9RVnMSbNsu6kFr_gkJwEQjOC5-wJrViJpissKMH3k4eW-efa8CXybxw2nSuoHMgZwoA-Rm0GVk5HiIm2nGfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آموزش شلیک با ضدهوایی به جانفداها برای زدن جنگنده F35
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151400" target="_blank">📅 12:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
👈
جبهه پایداری افغانستان(طالبان) بادبادک‌بازی را در هرات به دلیل تحریک بانوان ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151399" target="_blank">📅 11:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پزشکیان: به جای پرونده‌سازی و طرد دیگران از دایره اجتماعی باید تکیه‌گاه باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151398" target="_blank">📅 11:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40b98ab50.mp4?token=AYxHVZ9h_fkMmu96g_lga3zfmg46C1ekWPysllX57IwKSuYQ_jRmfWnAY0RPTyXZqxcA6lHEpUiy-12nuqAAhnZ7dwAg_vQocWus5Hv7dMai3xT0kZBkGn8ox42xe7VgPVgMIkcX0tj4JL2er5L-pMJcO5Xu9eIJJwGNNOl6AEioGxrv5Y7X855GMzN2HhrbdPrsgA4HlDldKVn9N6oI3rFqrpkn-W9x-UCL_-DG8PnJriZmGDy-wEGp5l-Tqyx4vAnD5y7h6TKbHOz5Y4-R7aXXUQFqaqenuzedE67gFmrcLINDPkLe8voNH0HTAj65Fr7rk9ADxAPtrr60D2m9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40b98ab50.mp4?token=AYxHVZ9h_fkMmu96g_lga3zfmg46C1ekWPysllX57IwKSuYQ_jRmfWnAY0RPTyXZqxcA6lHEpUiy-12nuqAAhnZ7dwAg_vQocWus5Hv7dMai3xT0kZBkGn8ox42xe7VgPVgMIkcX0tj4JL2er5L-pMJcO5Xu9eIJJwGNNOl6AEioGxrv5Y7X855GMzN2HhrbdPrsgA4HlDldKVn9N6oI3rFqrpkn-W9x-UCL_-DG8PnJriZmGDy-wEGp5l-Tqyx4vAnD5y7h6TKbHOz5Y4-R7aXXUQFqaqenuzedE67gFmrcLINDPkLe8voNH0HTAj65Fr7rk9ADxAPtrr60D2m9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: گاهی مردم به دلیل عملکرد ما از ما دور می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/151397" target="_blank">📅 11:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
۷ اکتبر ۲۰۲۳؛ روزی که جنگ اسرائیل و حماس آغاز شد
🔴
در صبح ۷ اکتبر ۲۰۲۳، گروه حماس حمله‌ای گسترده را علیه اسرائیل آغاز کرد. این حمله با هزاران موشک از نوار غزه و نفوذ نیروهای مسلح از طریق زمین، دریا و هوا به مناطق جنوبی اسرائیل همراه بود.
🔴
مهاجمان به چندین شهر و شهرک اسرائیلی، کیبوتص‌ها و محل برگزاری جشنواره موسیقی نوا رسیدند. در جریان این حمله حدود ۱۲۰۰ نفر کشته و ۲۵۱ نفر نیز به گروگان گرفته و به غزه منتقل شدند.
🔴
این حمله که به‌عنوان مرگبارترین حمله علیه اسرائیل در تاریخ این کشور توصیف شده، واکنش نظامی گسترده اسرائیل در غزه را به دنبال داشت و به آغاز جنگی انجامید که پیامدهای انسانی و منطقه‌ای بسیار گسترده‌ای داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151396" target="_blank">📅 11:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=u4I6dnqOAgC60SSmtT28ZTWHQ981lwFCNJnreyO5ND_bwhHy3yMXeMZEWZkKztMFbNpvEjpVVfsA77cCOvcyhwwYzWSaGkieroLYWX6jn7ffivlFLyCppcPUH3g1XAxnwgKmLT4ugY8h9PGz06XuHRjZOue_14BJVjQGul28ksS_QvIME67-bTPgbmJCH6-o-GA2Im1dvDAMIUqCqOmb35_jXODZbAziDCF-YMa7QNOfKZmC1G4lF8oSjdIOOGtq3ydMvb5902rZI8D8c4FOgYmJu03y8a6n_w0F_f8QKR03wNsJHJR8iO5vPP2gSycgvKmmeDXtft8OYTl20fnZnCytGSg34NnJN0YRS7fmG4cEXqIwPOgu3l4t-20tk8Jo6_emPVpIw1h_YCCUnDcE9xljYglk4AWkl8N____0UUGLnAcQYqRvGj-8zZYnjFeA7WGaJmWe0BGeHJvnemsPoq4OtP4MT3WK9h2xqszVGoGdGZZ2RDhmrKdLP18-iAYksjQVUt0cwVu8rnJVnrmtGNExags1pUJ92wSpiP6vz8tABLSeqk0xY7izKPxy6JM-8w6zOGPKCSY7IdynHugoFI-ln8ceYE9Avzx7NFn7kkaJv9BBVdU6rwz_qjyDcQWBnpGOo5YcqXmaHOfzyr3ffKjyRvkXD3cVhLWnC1R_HcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d6d557b6.mp4?token=u4I6dnqOAgC60SSmtT28ZTWHQ981lwFCNJnreyO5ND_bwhHy3yMXeMZEWZkKztMFbNpvEjpVVfsA77cCOvcyhwwYzWSaGkieroLYWX6jn7ffivlFLyCppcPUH3g1XAxnwgKmLT4ugY8h9PGz06XuHRjZOue_14BJVjQGul28ksS_QvIME67-bTPgbmJCH6-o-GA2Im1dvDAMIUqCqOmb35_jXODZbAziDCF-YMa7QNOfKZmC1G4lF8oSjdIOOGtq3ydMvb5902rZI8D8c4FOgYmJu03y8a6n_w0F_f8QKR03wNsJHJR8iO5vPP2gSycgvKmmeDXtft8OYTl20fnZnCytGSg34NnJN0YRS7fmG4cEXqIwPOgu3l4t-20tk8Jo6_emPVpIw1h_YCCUnDcE9xljYglk4AWkl8N____0UUGLnAcQYqRvGj-8zZYnjFeA7WGaJmWe0BGeHJvnemsPoq4OtP4MT3WK9h2xqszVGoGdGZZ2RDhmrKdLP18-iAYksjQVUt0cwVu8rnJVnrmtGNExags1pUJ92wSpiP6vz8tABLSeqk0xY7izKPxy6JM-8w6zOGPKCSY7IdynHugoFI-ln8ceYE9Avzx7NFn7kkaJv9BBVdU6rwz_qjyDcQWBnpGOo5YcqXmaHOfzyr3ffKjyRvkXD3cVhLWnC1R_HcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زد و خورد و درگیری در پارلمان ارمنستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151395" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=R3Lwy50hK4PduO4RF_bJ6hGlBGmoERDx077FHgEnbYKZDi4jAptbc8Qah3Yxarcw5e5unu0oPQ5p7PP3tY6J4FdLce7wWp2XasEqN06HI5UR0uJic-aeCY9Tql4S6tPJOB8u-XOU70KsDYFtmQcfXyNmc621jGEJQKNPfSaAsP4D9PD6Tya8wCyitQHJYX4GpH8oO3qtCJRUutevWXBywiPVQPqHFzuq355e7pRJlr19Yt8d9J56GQKaQ0DHauvb8UeGI96IY8vkZacfWizh0xGhOtwPQzQXCmyvzfowxaGrHH_CUXAj3YGA2xHz06tUpWCyv0jJGi57We6Xf8726g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=R3Lwy50hK4PduO4RF_bJ6hGlBGmoERDx077FHgEnbYKZDi4jAptbc8Qah3Yxarcw5e5unu0oPQ5p7PP3tY6J4FdLce7wWp2XasEqN06HI5UR0uJic-aeCY9Tql4S6tPJOB8u-XOU70KsDYFtmQcfXyNmc621jGEJQKNPfSaAsP4D9PD6Tya8wCyitQHJYX4GpH8oO3qtCJRUutevWXBywiPVQPqHFzuq355e7pRJlr19Yt8d9J56GQKaQ0DHauvb8UeGI96IY8vkZacfWizh0xGhOtwPQzQXCmyvzfowxaGrHH_CUXAj3YGA2xHz06tUpWCyv0jJGi57We6Xf8726g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابداع یک دین جدید توسط نبویان
🔴
نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151394" target="_blank">📅 11:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151392">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhwvqkuXwLviZT0XU7esMZpWmMpH6HWVy2nM7vdT4JPWsgcHAeOky7xcXcRULp0O-Ec6YqRqaZoS9m935UuvUi2-u97mMGOrOcDDAEH_V3_6D4-ZDiujUbGVHka6ExNjdw4PaA9O4uun2CuIfjgS7OcV24_on2I1q_IH675wjXGXHJUaFPkNIv9QIrxRjZULH3YaEoyeOqoHuz7IOD4DO9LJbS2CqbzZ4x0c_R6hDxQqymT4I2lEnfqZDonAIvK5difFheRiblJRSFkfesTLhLirz6ozC1Bvb5J3sbiVjFwVc2IkPWT4gTguafXAiUqIDWwINuj32N5TCJ1wUKJz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciTcnNcSjHuSX33WW2PEQWOGBG2ggpTMdrVzkutS_AtDN8anWNERB_PMmNilH1loZ4kTnYkfjbdetA7wG-5hG62X65aMLw5hfL2w8G1GrIT4aoYC3cWZv2Vp-P5jG2XipPYYsTJBLAkTa6f6tXmA_f_bYqIiLhvNe6JYQQn9gowU5bBdF3HjQDka7V27-fRp1TdKBlqh1tp9FoO5KDY0Up0vMncn9p4V6t-_ZBXncwcQwF8DhX9vX33O94cUaHaT9y1UjEQpkMIqVE8-pFRErJBM-dInW_eu65qFwuMdJGOXU6dnZmCy-hoQSdEJBTMYcL-lh4lQcOKDPsIDN5tKBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اطلاعیه یک تئاتر قبل از نمایش
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151392" target="_blank">📅 11:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151391">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUvpOAmMiboKbyV7koBFqYyjdrqQUGCu_XutjiG010nl6avOlGdqB1s9UdAFvGXB_qQVE7-c1Q2eP_inDVOAauuPv4XDxlyTxliwtzGkdZYdnU_g4-6BDIsU60b46Vd38ESc_CpjWtj9M2RzhqX9FVUQn4kmlNH-iXBah3bFmslgQPzBr8INXkO9f1CixMqNy1OjrJBRWTfTgSUDI3TNvGjkfGvxt7FH2buvtdfCt5LnMnGB029d3KnD0A2gLChpTL5peZMmfvxPSLszmguPI5wCtIRrDBWboV050EqUHRlQbcDCdwntlr2EWHXZcD04sze07hb5BeA_Rp7moeo2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سعودی و بریتانیایی برای سوخت‌گیری به سمت یمن حرکت می‌کنند تا حمله‌ای را آغاز کنند. همزمان، تعداد زیادی از هواپیماهای آمریکایی در تنگه هرمز، نزدیک به سواحل عمان، مستقر هستند تا از عبور کشتی‌ها اطمینان حاصل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151391" target="_blank">📅 11:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
آمريکا به قطر گفته ایران اورانیوم رو باید رقیق کنه و هرمز هم کامل باز کنه بعدش مذاکره کنیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151390" target="_blank">📅 10:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbda2a8b80.mp4?token=PleVDoPPKQLQypAH_EtYgmI2UaUv26jeODozTAai4sneHPsv4m1IwFOwBW34p_dm1lMpAHtxp04HABKm0W7YfPsed86UUOv9ZBOjQgEreaGOL2E-eHca43hgzl0sd13-2RPKJ5q7auE6A9uwCTQQa0-9Z_rZdHzQSXEn_lEcT1fs_0IhTP9GhK7Srykg-OH_LOcUndRjVMZ8tzLjRbdjTygXJoaau1EkH0RmKUy5UX2tCwA0G_Lf08b0wztja6bZzAzRmVZSxss1aUKcjvynaZebvWovBp4wGT90uWgjTB3r0ycSasyROYrifIWu9UBNm0vez7rgUGPtmxOQD9zNNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbda2a8b80.mp4?token=PleVDoPPKQLQypAH_EtYgmI2UaUv26jeODozTAai4sneHPsv4m1IwFOwBW34p_dm1lMpAHtxp04HABKm0W7YfPsed86UUOv9ZBOjQgEreaGOL2E-eHca43hgzl0sd13-2RPKJ5q7auE6A9uwCTQQa0-9Z_rZdHzQSXEn_lEcT1fs_0IhTP9GhK7Srykg-OH_LOcUndRjVMZ8tzLjRbdjTygXJoaau1EkH0RmKUy5UX2tCwA0G_Lf08b0wztja6bZzAzRmVZSxss1aUKcjvynaZebvWovBp4wGT90uWgjTB3r0ycSasyROYrifIWu9UBNm0vez7rgUGPtmxOQD9zNNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جانسون، رئیس مجلس نمایندگان ایالات متحده، درباره ایران: ایرانی‌ها شرکای مذاکره‌کننده قابل اعتمادی نیستند.
🔴
آنها دروغ گفتن را بخشی از دین خود می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151389" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd6dbe0190.mp4?token=NK78pWNHzf-JG1MDLmlfx5l0VsPuXLEcJRjfVQVtLndHQiovDq5bgBFM7fxz8-edhJjxTVFHUJD7QI769EBQjCC1mypK8WwHFW58R1toCZHTdapbssNtZTQxscMb-BmgledBVnYkAA-qRwrWkH6M8NpFUoFLrE_5Rg99ISuAS0MOZtXNrn2YFp4-WuuVOL__OKvRULFhT5yelaRLumOUFuvC4u5SJlKjGijrsdEVQGUqCvEwik2dPJiytKrY-srpQgBKya_kAy1F4f6fCjhMYRg3gdmVtCa72gB0jtIoxaY0BYiXaAzFcIVXYBAip0AanDEO0dhUi6ntmRDimY_Iyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd6dbe0190.mp4?token=NK78pWNHzf-JG1MDLmlfx5l0VsPuXLEcJRjfVQVtLndHQiovDq5bgBFM7fxz8-edhJjxTVFHUJD7QI769EBQjCC1mypK8WwHFW58R1toCZHTdapbssNtZTQxscMb-BmgledBVnYkAA-qRwrWkH6M8NpFUoFLrE_5Rg99ISuAS0MOZtXNrn2YFp4-WuuVOL__OKvRULFhT5yelaRLumOUFuvC4u5SJlKjGijrsdEVQGUqCvEwik2dPJiytKrY-srpQgBKya_kAy1F4f6fCjhMYRg3gdmVtCa72gB0jtIoxaY0BYiXaAzFcIVXYBAip0AanDEO0dhUi6ntmRDimY_Iyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسپوتنیک: یک هواپیمای مسافربری کانادایی و یک هواپیمای مسافربری آمریکایی در فرودگاه لس‌آنجلس در ایالات متحده با یکدیگر برخورد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/151387" target="_blank">📅 10:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffca39c1b.mp4?token=cxDiewJTMP-m_NK02eUTUBQnRhnI-ODMIs15JKKqBeyDYDRkgFpsOYraDfGkqGIzUC7gefUK_jfncYXTNTOZQ8XaF7wLmuQUQbUWFJJ7w4sG1mJeXZhozoxY02R6ACtPLDqEZ20si6SQeY9rD7eSyvn_vsIaVKGm8uVQx0Vr6vUTNRR7w7gplvhqGTBd1AGZ5uk7S6htzqKflav61WKZB61XXlnuOWaUDOmKfvfoziibq5KHqIdPq0mmmllwSlBIPz0FfGWc7-jVRZNF5rsDGD6rWlcGAjTxVpiVffq5sVXe98N_VRR04fSQwPmujqBfTNZ8mnrSSm8TYJCblNFWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffca39c1b.mp4?token=cxDiewJTMP-m_NK02eUTUBQnRhnI-ODMIs15JKKqBeyDYDRkgFpsOYraDfGkqGIzUC7gefUK_jfncYXTNTOZQ8XaF7wLmuQUQbUWFJJ7w4sG1mJeXZhozoxY02R6ACtPLDqEZ20si6SQeY9rD7eSyvn_vsIaVKGm8uVQx0Vr6vUTNRR7w7gplvhqGTBd1AGZ5uk7S6htzqKflav61WKZB61XXlnuOWaUDOmKfvfoziibq5KHqIdPq0mmmllwSlBIPz0FfGWc7-jVRZNF5rsDGD6rWlcGAjTxVpiVffq5sVXe98N_VRR04fSQwPmujqBfTNZ8mnrSSm8TYJCblNFWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز عده ای تو خیابون پاستور جمع شدن و به پزشکیان و قالیباف اعتراض داشتن؛ شعارشون هم این بود که «پزشکیان و قالیباف رو میدیم، اورانیوم نمیدیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/151386" target="_blank">📅 10:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
🔴
در این گزارش آمده است که:
🔴
سال ۲۰۲۲ 1 دلار = 90 افغانی
🔴
سال ۲۰۲۶ 1 دلار = 65 افغانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/151385" target="_blank">📅 10:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyF7VTgeqSC8H4JjYpEKNs-pTWI5VKvOdpDjtAMfeSXUVraAxvL86XS7Zqarct5OdUvYs2gSO-YhhyK0CBMODnUqb5GsErZ0R-9NsVJgMY4EO_quCdLQs5TADJDqUtKN4ON0S-TIBfl-0zPQWX-Md4ulFnUbuoxz5GWINcc-aNRRtlEHqXY9IcZdazniu3xgR0-uN1eSq7nv0-J-usPnok8_E-TL__L4HVxkL680VU1znN0IBy2ob1j0UaysUNRBp5i52wIsnpLF1uAkacpR_HPi8iTHc809AgeLMR5gdT6stl7cTiYG5n_YhwIbMIiZdIcz6nlzQqsWKG8Km9NfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور اقتصادی قالیباف: جنگ بدون تحمیل شکست اقتصادی به آمریکا به پایان نمی رسد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/151384" target="_blank">📅 10:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
مدیرعامل آبفای تهران: ذخایر سدهای تهران نسبت به سال گذشته ۱۵۵ میلیون مترمکعب افزایش داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151383" target="_blank">📅 09:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: فرودگاه ملک خالد در ریاض با چند فروند پهپاد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/151382" target="_blank">📅 09:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رضایی، عضو کمیسیون امنیت ملی:
نزدیک به ۸۰ درصد از افزایش قیمت ارز، منشأ داخلی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151381" target="_blank">📅 09:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عبدالله گل، رئیس‌جمهور پیشین ترکیه:
ایران باید از فرصت کنونی استفاده کند و پیش از تضعیف موقعیت چانه زنی‌اش، دستاورد‌های خود را به ثمر برساند
🔴
تهران باید مراقب باشد تا امتیاز‌های کوتاه مدت را با دستاورد‌های بلند مدت اشتباه نگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151380" target="_blank">📅 09:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فایننشال تایمز گزارش داده مالکان نفتکش‌ها برای حفظ عبور از تنگه هرمز، به برخی کاپیتان‌ها ماهانه تا ۱۰۰ هزار دلار دستمزد و برای هر سفر ۵۰ هزار دلار پاداش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151379" target="_blank">📅 09:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عربستان: روزانه ۵.۸ میلیون بشکه نفت را از طریق خط لوله شرق-غرب، منتقل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151378" target="_blank">📅 09:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پزشکیان: قرار نیست فقط تئوری یاد بگیریم؛ باید مشکل مردم را حل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151377" target="_blank">📅 09:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان: همه کارها را برای خدا می‌کنم؛ دنبال پاداش نیستم /از روزی می‌ترسم که خدا از من سوال کند که چه‌ کار کردی
🔴
اگر ما بدون اینکه به کسی گیر بدهیم، گره باز می‌کردیم و مشکل دیگران را حل می‌کردیم، شرایط‌مان این طوری نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151376" target="_blank">📅 09:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65824f8828.mp4?token=F_uKJqiRSIVU_pJUMPvBQ8lC8FuB0hNvPM0-CI5R0m0vqF14vLvRgAvOeRrHuiLhtMJ4uJ9gCHO5P7wGKNg2vma1XBf_169ZgcqmVYYsIndkY0BcQ_6Mpyq0YB8N0F0OTo8x7gYEep2gOOP2VFotFaVK5OGeVE9m5acc3yPF8J3KrloSsRv8haX6tHldK9MTRdSTX6-PNKRf1rp-qcZXlvbZa8eDru8QOsr1KA3fwjofMv9x9EIJeAg4mC2v-6UBIZy0JhXUjC37iCnwWGgrHSSFHQz1N9GeT-tdF5i-Jq0gBoljr-jOp9spPGOPxICyWNxlkow9sMHbZVM6T1GcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65824f8828.mp4?token=F_uKJqiRSIVU_pJUMPvBQ8lC8FuB0hNvPM0-CI5R0m0vqF14vLvRgAvOeRrHuiLhtMJ4uJ9gCHO5P7wGKNg2vma1XBf_169ZgcqmVYYsIndkY0BcQ_6Mpyq0YB8N0F0OTo8x7gYEep2gOOP2VFotFaVK5OGeVE9m5acc3yPF8J3KrloSsRv8haX6tHldK9MTRdSTX6-PNKRf1rp-qcZXlvbZa8eDru8QOsr1KA3fwjofMv9x9EIJeAg4mC2v-6UBIZy0JhXUjC37iCnwWGgrHSSFHQz1N9GeT-tdF5i-Jq0gBoljr-jOp9spPGOPxICyWNxlkow9sMHbZVM6T1GcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: بارش‌ها به صورت پراکنده در بخش‌هایی از کشور طی ساعت‌های آینده اتفاق می‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151375" target="_blank">📅 08:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نتانیاهو بار دیگر خطاب به شهروندان اسرائیلی : به شما قول می‌دهم، ایران پیش از انتخابات به ما حمله خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151374" target="_blank">📅 08:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151373">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA6UjeEWNAclXg0fGsMygi3YmkG7Y8O6xmeCrNV4Fjg7BZcpG7SkG5JJOJ-Ao5dpOBI3CVA-kAKXya6pG0W6LVqrC0J39NWbEAOZ4WnEtg_FPBud6YxJg0NVz-qy0EVFi1MbuTp4VgBqMVxB6cdA20YEll7uHyw86Tl22X3EYikeZaOdG5TE6wURytbeKhk7YMXxAUVeU4b2aQ-mjmmW9v9ZArqaNqqWnxdWNqMip3STsRf5CQ8hac_dYgkNwidco-i7n_QlYOd2szDrgcFze5x8MXI3crR8NEgEs-3M8wb_9bwMh_-gH-yhhHA6MU-7E34D9z4JIVTyYLv1XbwPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوین در ۲۰ دقیقه نزدیک به ۲۰۰۰ دلار سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/151373" target="_blank">📅 08:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151372">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیروهای حوثی مدعی شدند یک فروند پهپاد مسلح شناسایی CH-4 عربستان سعودی را در آسمان استان الجوف یمن سرنگون کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/151372" target="_blank">📅 08:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151371">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ونس: ایران باید برای پایان دادن به جنگ، توانایی‌های غنی‌سازی اورانیوم خود را کاهش دهد
🔴
مشخص نیست ایران چگونه تصمیمات خود را می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/151371" target="_blank">📅 02:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151370">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIncuUvQuBM3a01RBchnEplP-XdtoBmb7HtaQ1DdnttThRtb79orUZj1eaTwiDa44SSYTxCNYRkPCp5iDT1beaw8vzDn-BswP2T5U_5Rer4bNGpgtlkaKn-IRxN7-W2KwnwdMvkml-uV0mYPqb5E_M3oGe0g3jvsZCNQER1KvMHdSL3L57xyxjrOwZHKlXAnlgo1AKOWmNBUePzE9EyI6761p-tw2gnFzCGv0hrc3UaG-LkFayAdoMaqMoYhFFRZejlCN6DqekQfU-_1FoBSMyRo7sXLdwEszg8gao8lkhzzZHcUaoWdRykmbC6srwM7EXi3fitLwzU1-aKmCfJekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری حامد بهداد در حمایت از مهشاد کشانی و جاویدنام علیرضا سپاهی
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/151370" target="_blank">📅 01:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151369">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
👈
ترامپ :
رژیم ایران باید مدت‌ها پیش نابود می‌شد، زیرا با گذشت زمان، مقابله با آن دشوارتر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/151369" target="_blank">📅 01:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گریه های مسی تو اتوبوس تیم ملی در راه ورزشگاه  @AloSport</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/151368" target="_blank">📅 01:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gedL_NjjqnYFZapQaUdDxg9CIIKhdFQNYnhRY0oHhkLrxjWcJXrW3b9B1hMscnwUQ5dRLmruKt1Jy6qrOACbawmp3ACyMPn3q9azNoZT-6yYxaJF7_JFumu56gynfmQNgt4A7OCZTieDgnW4fOJKU_q4wLp5ivjovJsjAuiM78HOOk7dJL28I0p_5_LrNyjKYjpkY9sHcYUn8imF6lij9EVlTmJlLz1hzIhkWVEebWP9RrIKby18JsoTMoq5fchnALthoz9tqA9O8OynOklnm1N-vpdZ2pYlYg0z_JpzHzr3I1GqdSQxhABCsGrnfxMUvBa_ZP8G7sffvkqwt6qB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی:
بر اساس اطلاعاتی که به دستم رسیده، ذوالنور، نماینده انقلابی قم تو مجلس، درحال حفاری غیرمجاز برای پیدا کردن آثار تاریخی و گنجه !
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/151367" target="_blank">📅 01:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAgHj_9_fWhDABZY87d2FPElNmFrLOqwh-i2btxXsryreDNhSwibLYPhukqs_Ik2nSK7bzlqazFu0Tm_RAag8y62Y0y8nrrWR7hH-ypEt6-8K3sEx1hZZrsr1uOReaxq9xEbp03E1QmR86a7KI7CZHsybBYkWMzcMJIT0HZvJFwm5dZWlospsDlQK7-FC7yHFH1bh1GFvS1SPLnjvG7JThIMx6KaSjmVMK6_O38c1hl6p0aGW_8OGVDmhsI7T3lla61biMVLjCVFvu9lu0KpJRT6Aa3MqSwxwh6hTMTV6d9kmrABSBawGN2wL_7Kwm71rRPlSWjczfZCtJAeX4RCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
هر ۱گرم کوکائین در بازار ایران‌ معادل ۲.۵گرم طلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/151366" target="_blank">📅 01:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcQh7H-YrFVv3qnfH8_qpoiLWX2vp5BkT2lnz6nRkCW81VRCugRaksildZDS_Ls-VixN6Q268VB9jkPUoVcwtB2myRdaRzlyFxMpbt4N7ClRL7LzXZmILbY5gT82NlpsEK7TtptphCjkKVOZrZ_p7Ix48AhTcYE9GS-exw5LWE10F8r2mwfUgD8Q3qMPDDE2wNQjPaN8W76TnWuLYIXALauEo5pF9bWJQFp-xJupart_CGZU7m0ILVBZB8gmM_OZqyA4brbhI84Zv37hVgT-ErPgfjOlv0U-kDZgJoUkr79e58Qz67DgFpFtqxHkJjiADZz3yT7yKQjlbeV1Xhwjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی:
بزودی سیم‌کارت با قابلیت درآمد زایی عرضه میکنم
🔴
پ.ن: خدا بخیر کنه از دست این دزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/151365" target="_blank">📅 01:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151364">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Mj8SAmxvm7ERNOg-qiIZPl9LIeBnsFOsxsWqd20Q4WWQBxtmqzFwcdAl2Pj2cCpAzHpeLdYDL_YSpErcgENSujxfLxqA99-xxoo5J_-plR0heNjUCZgN85zLDczXMIB1miwkGMaM8j2Ruxs8HpdZglVXmsl0t7MUjFRksi7FRqw_bSeeT9f8Jb6Nkdu1wWS3u46PCTy90qbL7Dc5IkzQDrgObiTlv499_Fm-3aX9iNN59LElHLNKPWNyFyld5Rz2IUVf_pgEyDdyhmdaUYQsCar-wd2rwynix0V__96bQyX9gEvBqLoR2_vEvmFR5nPif2M5dil57KMl0xE1CuijEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Mj8SAmxvm7ERNOg-qiIZPl9LIeBnsFOsxsWqd20Q4WWQBxtmqzFwcdAl2Pj2cCpAzHpeLdYDL_YSpErcgENSujxfLxqA99-xxoo5J_-plR0heNjUCZgN85zLDczXMIB1miwkGMaM8j2Ruxs8HpdZglVXmsl0t7MUjFRksi7FRqw_bSeeT9f8Jb6Nkdu1wWS3u46PCTy90qbL7Dc5IkzQDrgObiTlv499_Fm-3aX9iNN59LElHLNKPWNyFyld5Rz2IUVf_pgEyDdyhmdaUYQsCar-wd2rwynix0V__96bQyX9gEvBqLoR2_vEvmFR5nPif2M5dil57KMl0xE1CuijEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد شیوع بیماری طاعون در روسیه، آیا با پوتین صحبت کرده‌اید؟
🔴
ترامپ: قرار است خیلی زود با او تلفنی صحبت کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/151364" target="_blank">📅 01:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151363">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اسکات بسنت:
ایران وزیر نفت جدیدی انتخاب کرده، ولی الان این وزیر نفت، چی رو مدیریت میکنه؟ چون از ۲۵ اوت به این سمت اونا حتی یه بشکه نفت هم بارگیری نکردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/151363" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151362">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM-B-DFTJIolrPDTJVY0vGvX5__U8-YkFRQgmTjXQyZGWRmGsfKKnB8ChQ3zou4t1ATA6O9QO2FPegMEo7BWyjcM84twBS-l9nfdA2hdNF5md_EqOb43HCmntiSaoPfQjAUlkIMGBH11uOUtG7RfyNlGMYhw34dP4Tt3sZpOFf1ciRP3-5RikvD1bgnQ5wn7Ox7qjoJa41D2Lmitf3_HxJlxxCI26vSi836FHd_fujDLL_s7BJYEhkNSxkcBNiuWTlYQg4MWt-rmLqz9xkyrMWw21fKGZGgt2sjUCpl_glJv4OJ7N_XfHQsbDwbCnB6czsVCuQha3sMY9wnvr55rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: دشمن میخواست اقتصاد مارو خراب کنه اما هیچی نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/151362" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151361">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd964e9cf0.mp4?token=EfBNOkFhZc1iVRLahtDKbYTIDxwtcWdIRsl8OwETDvvAUpvpowSZo5_PAFh8u99cpm9VSfYu29CVV4k2cXu8eYaKyc6EDjOe2-_kQLjVW0tTJ8Z89euYXRhqdLX6gLRP8m0MadqD8_erOokygTNymS_76TLSVhMlQzg9hV35R237M7ms7iGq6DR7lQ6MnBzZLSDWfvn2JWzCgzgBm-CakGW40XFGAcSlhQtQZDynfvxJ8fCIOBfUGwza3SCRb-2AZ9y_g0XVM7fSJhXboFtdf1VAuNUjFiMHMIdRn_UJgT9JG3gNx71IcHeA6fBWP_c6uCku8ztQAsPen8rTSgbiYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd964e9cf0.mp4?token=EfBNOkFhZc1iVRLahtDKbYTIDxwtcWdIRsl8OwETDvvAUpvpowSZo5_PAFh8u99cpm9VSfYu29CVV4k2cXu8eYaKyc6EDjOe2-_kQLjVW0tTJ8Z89euYXRhqdLX6gLRP8m0MadqD8_erOokygTNymS_76TLSVhMlQzg9hV35R237M7ms7iGq6DR7lQ6MnBzZLSDWfvn2JWzCgzgBm-CakGW40XFGAcSlhQtQZDynfvxJ8fCIOBfUGwza3SCRb-2AZ9y_g0XVM7fSJhXboFtdf1VAuNUjFiMHMIdRn_UJgT9JG3gNx71IcHeA6fBWP_c6uCku8ztQAsPen8rTSgbiYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت بعد از اعدام علیرضا سپاهی:
🔴
عمویم محسن ‌اژه‌ای دمت گرم، اصلا اذون صبح یه جور دیگه با دل آدم بازی می‌کنه.
🔴
وقتی اذون صبح رو میگن میفهمم یکی از دشمنان خفه و سقط شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/151361" target="_blank">📅 00:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151360">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بمب خبری
‼️
🔴
گاتزتا دلا اسپورت: رونالدو بخاطر خیانت همسرش عصبانی بود و برای همین اردوی تیم‌ملی را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/151360" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151359">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Rduu8UvLUMftFi1gtBn-y2w0ohCu3GI8BHBsVUBJxjHV2o_8RR5v0a9BtRxCVerZxIZZsB5lBNXm7ZBYuaAwMF2Vb9duCEsrJwI7CMoVl8qB2OqxPzo8sH64RajZnNbrYTCvngFS0VvvC3h6-f0IGWpnIzOeH4uPm06hD-DWyv62a8e1w8rDFl9rcDcUbGMd_w-3Gyq1IP2G-LPf4Jk4QS2WG8ku1h-yqLPEv51MmwxglkF4ccRyak35bOHhFHgywhb5USXj4GtEuJXe1vL5uJinptxGWNPU2EFcTyfeC-LeqQFvNf3LMZao0UEhVtZ9Iq3fdpMm0dSY_JFteBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمب خبری
‼️
🔴
گاتزتا دلا اسپورت: رونالدو بخاطر خیانت همسرش عصبانی بود و برای همین اردوی تیم‌ملی را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/151359" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: ما 8 جنگ را به پایان رساندیم!
🔴
فکر می‌کردم پایان دادن جنگ روسیه و اوکراین ساده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/151358" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=T6Zsl4bFgpPiWxRlsiHLl2cSXltsF12DnSdo99rVTHHh5vRscMxQOnO0_HTN7bmNT1-ogY8DeHFm_FlB06N45lOS7TrPidlrMM6od5BnUzwQWI76RQ5-KsN1-NxqOghf9zoKDyLATJHElU9q0uEcc2vxpQS8iKbORGkhItjFT-x1MzjPIAOnUF2MVocGVS31hbsZzS1-sow6ZhirLF0ZFqgY6KHLZ6BNirS_v5u-XzFKBw6PaiXYvcTCrNTpB4tePYWUnjzAAOw_9JSYJXIFXpExL8WTqPG8EcYA0kzmamAcm6YljkJfVnf4UypkTlOeIGWtBe_9dZO9VMLyLKGlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=T6Zsl4bFgpPiWxRlsiHLl2cSXltsF12DnSdo99rVTHHh5vRscMxQOnO0_HTN7bmNT1-ogY8DeHFm_FlB06N45lOS7TrPidlrMM6od5BnUzwQWI76RQ5-KsN1-NxqOghf9zoKDyLATJHElU9q0uEcc2vxpQS8iKbORGkhItjFT-x1MzjPIAOnUF2MVocGVS31hbsZzS1-sow6ZhirLF0ZFqgY6KHLZ6BNirS_v5u-XzFKBw6PaiXYvcTCrNTpB4tePYWUnjzAAOw_9JSYJXIFXpExL8WTqPG8EcYA0kzmamAcm6YljkJfVnf4UypkTlOeIGWtBe_9dZO9VMLyLKGlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: می‌گویند: "ما برای شش ماه وارد ایران خواهیم شد."
🔴
ما واقعاً این موضوع را به محض اینکه بمب‌افکن‌های B-2 به هدف خود رسیدند، پایان دادیم، زیرا آن نقطه پایانی برای برنامه هسته‌ای آن‌ها بود و این ۹۵ درصد دلیل انجام این کار ما بود. شاید حتی ۱۰۰ درصد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/151357" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673z_-IjXnwIj3vUyeZvKce5JWMR6kemlxmbUPVOCYjWCQOur8lcw44gYopss3TpJtz6A2oNOuYaL9-FdROvQHpKANic3yHpk0-caRoySDqTzNk4bQUKadbbjv2ilbM-4wqLzqFwBIwcZnoe3okQ0iGO6GVCFLOlsRPIbIvY1-b3GQv46vnw_KlKgsqCvBVFkMxa7EcMS2qUktm2adzhOn58mFlDRpecFEfr_L5mRyzRZFhjXIznR8KRgcTFH4iIqpEKjR6gYD5Bz72Z_O1NWUtsvGiHrmjC17Ft8rLOy_ayHpVehwh8j490xW3g96S2j014YfYOApJACMcOOO3GTgIec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673z_-IjXnwIj3vUyeZvKce5JWMR6kemlxmbUPVOCYjWCQOur8lcw44gYopss3TpJtz6A2oNOuYaL9-FdROvQHpKANic3yHpk0-caRoySDqTzNk4bQUKadbbjv2ilbM-4wqLzqFwBIwcZnoe3okQ0iGO6GVCFLOlsRPIbIvY1-b3GQv46vnw_KlKgsqCvBVFkMxa7EcMS2qUktm2adzhOn58mFlDRpecFEfr_L5mRyzRZFhjXIznR8KRgcTFH4iIqpEKjR6gYD5Bz72Z_O1NWUtsvGiHrmjC17Ft8rLOy_ayHpVehwh8j490xW3g96S2j014YfYOApJACMcOOO3GTgIec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من مدام از رهبران جهان تلفن‌هایی دریافت می‌کنم که از من [به خاطر جنگ با ایران] بسیار تشکر می‌کنند.
🔴
من گفتم: "خیلی خوب. چه زمانی می‌خواهید برای آن هزینه را پرداخت کنید؟"
🔴
ما بارِ کل جهان را بر دوش خود حمل می‌کنیم. ما از انجام این کار لذت می‌بریم، زیرا ما قوی‌تر شده‌ایم و دیگران ضعیف‌تر.
🔴
آنها فقط ضعیف شده‌اند. آنها ناکارآمد شده‌اند. ما کارهایی را انجام می‌دهیم که هیچ کشور دیگری نمی‌توانست انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/151356" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76faad4536.mp4?token=U9NRIBAgAblcllc7TEGu9UfjJKS5-OBhSWp8tY7piyeEyWw7_rCl8YWiJp-2GR8NOApyXp5s79giE_Dq5JW1HcqM6dRfjyK91eRsQeweQCqTa9tnjrLf9272TaV0nJkyh5JjiQY_NC9Qprg3JS55tXsKJAviPJthqErT3Fpao4xH8z5PE3K2v465_CgdvZzA7phXq1mUe2_PBSHRfmQdnw25zFWkUGoB7sBFLHCLElZKeGT9s69NTqnJ2aoFR6ODC-fUj7jau5bl_9u8zOAt8GYVG3yhr0J-galFpFpHzyw37WFH5-LWpTUSsw2wGIytTX-0e5yK216MWqGpCX8Z2RqiHMONJ4vIMB9nyoadilIRQE7NYxNrQvBONrdQjNtOs5xKKF4srQtgycyrC7cBAyYv1ODW43-zd3-3c-mjNMvr2NldG2cl8LpO685z789UatsfVhAcCw-EhPvcEc5EW6XnrU0rnKfBItlcK3xjX-pvZ5v_NwWwyM3o5KU81scno0IwCWMDlnI4DTtxvC6u9Y24LtNnesiv0VC5IjRAu9OdmTQUxnO8gPaSHUMP_DgmqmynvQpQFx5myJzWSP0WnH4uNmFrVJ9bkfvuo8F7XSzblEPIuDWgCtNXyQF5HBwhlSyTHJR7s60s65cY3e49nxBRklp8JWsJJ2tt97GmE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76faad4536.mp4?token=U9NRIBAgAblcllc7TEGu9UfjJKS5-OBhSWp8tY7piyeEyWw7_rCl8YWiJp-2GR8NOApyXp5s79giE_Dq5JW1HcqM6dRfjyK91eRsQeweQCqTa9tnjrLf9272TaV0nJkyh5JjiQY_NC9Qprg3JS55tXsKJAviPJthqErT3Fpao4xH8z5PE3K2v465_CgdvZzA7phXq1mUe2_PBSHRfmQdnw25zFWkUGoB7sBFLHCLElZKeGT9s69NTqnJ2aoFR6ODC-fUj7jau5bl_9u8zOAt8GYVG3yhr0J-galFpFpHzyw37WFH5-LWpTUSsw2wGIytTX-0e5yK216MWqGpCX8Z2RqiHMONJ4vIMB9nyoadilIRQE7NYxNrQvBONrdQjNtOs5xKKF4srQtgycyrC7cBAyYv1ODW43-zd3-3c-mjNMvr2NldG2cl8LpO685z789UatsfVhAcCw-EhPvcEc5EW6XnrU0rnKfBItlcK3xjX-pvZ5v_NwWwyM3o5KU81scno0IwCWMDlnI4DTtxvC6u9Y24LtNnesiv0VC5IjRAu9OdmTQUxnO8gPaSHUMP_DgmqmynvQpQFx5myJzWSP0WnH4uNmFrVJ9bkfvuo8F7XSzblEPIuDWgCtNXyQF5HBwhlSyTHJR7s60s65cY3e49nxBRklp8JWsJJ2tt97GmE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تنگهٔ هرمز متعلق به آمریکاست؛ جایش همان‌جاست و همین الان هم در همان‌جا قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/151355" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69e4b8c78.mp4?token=isZQSNd6RZNyRveTWmIrgExg89_ljBa_-E3hWldEFB9NztYZzmuZO87VmOarhW87CpFoZ9tsNekGqfAIZwPQuLZLi9qSKTHv-NHRnS4bjRW3RMWWxncMllP_qJTUjyjb1C3I7hcZihPhaOlYaf7AFpY-xka4IDjatYBWkPhhWcJ3jck_3gjSyggJU67tijKxWIIziOFHdkNaEWeysB3LWlaOJhmrh8ylc-Ndox4QyC4ptvSPXamzkHNhOqgJfAs40zdpicyeI2sEMfMPni3pIlFnQlY7UiA-W1ZtkDRV8avOzVtnrhn_sILPiCIJkdG9FY6rYJ_wME4yciYy0pO68Iu4yehxk9f3LXFxku4PY-JmlT6nTX_YJR2ecpKcvlp41wuUbrSz2xHNZOXFJEbnkdxZycQYq5oBaUYM7buNyVNv0LtZu6nFH7604w1mOKoaIdct4nSElEYZaBknTdrx_Xa0ChAeovW-j35C_D9Io2D5fPU03-8dhfLGbUjtHIUjDcquEVz9OcfGCkURCql_xB7mq61M_KkmC9Qmk-Pzs0RBVMOqOY1m5uKs2j1N1JmpuAcAJjg_mB76Rx62nUJUG3elHz3GEXe1YztgWwykBAjtcnTrL7BgQ5KdBJe0X2csfzOFNvp-9cId0E1qPWpY49djqVTeI33TFWQA2YxvpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69e4b8c78.mp4?token=isZQSNd6RZNyRveTWmIrgExg89_ljBa_-E3hWldEFB9NztYZzmuZO87VmOarhW87CpFoZ9tsNekGqfAIZwPQuLZLi9qSKTHv-NHRnS4bjRW3RMWWxncMllP_qJTUjyjb1C3I7hcZihPhaOlYaf7AFpY-xka4IDjatYBWkPhhWcJ3jck_3gjSyggJU67tijKxWIIziOFHdkNaEWeysB3LWlaOJhmrh8ylc-Ndox4QyC4ptvSPXamzkHNhOqgJfAs40zdpicyeI2sEMfMPni3pIlFnQlY7UiA-W1ZtkDRV8avOzVtnrhn_sILPiCIJkdG9FY6rYJ_wME4yciYy0pO68Iu4yehxk9f3LXFxku4PY-JmlT6nTX_YJR2ecpKcvlp41wuUbrSz2xHNZOXFJEbnkdxZycQYq5oBaUYM7buNyVNv0LtZu6nFH7604w1mOKoaIdct4nSElEYZaBknTdrx_Xa0ChAeovW-j35C_D9Io2D5fPU03-8dhfLGbUjtHIUjDcquEVz9OcfGCkURCql_xB7mq61M_KkmC9Qmk-Pzs0RBVMOqOY1m5uKs2j1N1JmpuAcAJjg_mB76Rx62nUJUG3elHz3GEXe1YztgWwykBAjtcnTrL7BgQ5KdBJe0X2csfzOFNvp-9cId0E1qPWpY49djqVTeI33TFWQA2YxvpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها
رهبر تروریستی ایران
منفجر شدند و از هستی محو شدند و مستقیم به دروازه‌های جهنم فرستاده شدند.
🔴
رهبرانشان رفتند. بزرگ‌ترین مشکلی که من دارم این است که هیچ‌کس نمی‌داند چه کسی کشور را اداره می‌کند. شاید این چیز خوبی باشد.
🔴
خامنه‌ای را یادت هست؟ همه‌شان از بین رفته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/151354" target="_blank">📅 00:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عربستان به یه پسر ۲۴ ساله، بخاطر کامنت توهین به پیامبر حکم اعدام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/151353" target="_blank">📅 00:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151352">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf346aec4.mp4?token=aO1KQp-hG0qIIDkBKnfErcjhnq17-etH2do727hxp5hUAsYQ6WSA-KaBMVEKg1sAxVn6epl_B5aT3RcZdhT1kp0I5kzEbiWV8YszP3Ytg0ISOPxyZnB4x0DkaOaDZ5VRRWDMu7eo9mbOND_iqEHwlfOxkTmqc0MVxjk_83mDVugzfxGHfDg5NUbRdLq8Oxtlri3_Vy9vVssChM0NcGWWC6CAC_9ufsDDdoV-e4CPomrIUh6Fw38xf1XjXauiMi9lIezVcAmLjxvxpJj4xS3FIQXH54R08-HnC59hTN7CYrmSkQm6mcBy2l8Onq1Y_t63xdynm33UfqhQHvwFvtfFog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf346aec4.mp4?token=aO1KQp-hG0qIIDkBKnfErcjhnq17-etH2do727hxp5hUAsYQ6WSA-KaBMVEKg1sAxVn6epl_B5aT3RcZdhT1kp0I5kzEbiWV8YszP3Ytg0ISOPxyZnB4x0DkaOaDZ5VRRWDMu7eo9mbOND_iqEHwlfOxkTmqc0MVxjk_83mDVugzfxGHfDg5NUbRdLq8Oxtlri3_Vy9vVssChM0NcGWWC6CAC_9ufsDDdoV-e4CPomrIUh6Fw38xf1XjXauiMi9lIezVcAmLjxvxpJj4xS3FIQXH54R08-HnC59hTN7CYrmSkQm6mcBy2l8Onq1Y_t63xdynm33UfqhQHvwFvtfFog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من مطمئن نیستم که شجاعت ورود به زیردریایی‌ها را داشته باشم.
🔴
شماها آن‌ها را دوست دارید، اما من ترجیح می‌دهم روی سطح دریا شناور باشم
🔴
بنابراین، من ایده یک زیردریایی خودکار را دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/151352" target="_blank">📅 00:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151351">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISiiXNxWmtZFaOhTOuNlrJjXptQZO7-Caf2NwtKu6L4VSZs9JpXvo6iTUqjvZttIaB_NcAF9TRWaIbBPJBhJcE03bHM4vVpy5NTzoJA5v3K0Nc0ZbmbAq4FMoQieuoyTONJ25tIPXYd6iN3lWqF2oicYlKHd4W9EtPBhWKTAmGSRMfDzpX7EzfrxBKi38_-_jkXSbuVN_Z6yoyjYodYHRSJ6Fpf5ilKLtLhMlBGKBNC3HqyA92UzxzkyFcWsRrBQKtIHdJBQthHDiGuqrdkwUUfHN0bnDMXLqwBj2g7Q6dFF1Wxq4aAX-ekIJQ16bbkIVEVtXk0YF3pr50GVrLGXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوررری / سفارت آمریکا در مسکو، اخطاری بهداشتی صادر کرده است، مبنی بر گزارش‌هایی مبنی بر یک مورد مشکوک از بیماری طاعون ریوی در منطقه ایرکوتسک روسیه، که منجر به یک مورد فوت شده است.
🔴
این سفارتخانه اعلام کرده است که گزارش‌های مربوط به اقدامات قرنطینه و بسته‌شدن بیمارستان‌ها در ایرکوتسک را زیر نظر دارد و هشدار داده است که دولت آمریکا توانایی محدودی برای کمک به شهروندان آمریکایی در روسیه، به ویژه خارج از مسکو، دارد.
🔴
همچنین، این سفارتخانه بار دیگر بر توصیه سطح ۴ خود مبنی بر "عدم سفر" به روسیه تاکید کرده و از شهروندان آمریکایی که در حال حاضر در این کشور حضور دارند، خواست تا فوراً آنجا را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/151351" target="_blank">📅 23:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3279701bab.mp4?token=hsBhzGDYLx3WVYyEQEM9Ac6WIN1ghYzSAyghkj1rjNmcli6J__Ac3iuoF4xEwyTdXn8FQipBydKDpJnxbKLHBR_0kZPITO6ScBmwftA56NHsoUW2ZzZTmlXeRzImXT5HVoYV7Jjvd7xGFb1CFRyRfazC9X1Qg6SsTJ87TaaYDmZBcGVzliuUFxgvk4WPYvFMDpfYp0pTiLHK0WqXntYrfBF7C25UtYvuZhtiHXo8-gLSD3PcDSfVSGrfmam3yGw1BRoX3UUpuu5sJnkionXvY3UpARcnyDyaT26GprGYBPR1sH3w6zd_dNOVjOhn9Bb4pemq-Vza59YjYBxeryhEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3279701bab.mp4?token=hsBhzGDYLx3WVYyEQEM9Ac6WIN1ghYzSAyghkj1rjNmcli6J__Ac3iuoF4xEwyTdXn8FQipBydKDpJnxbKLHBR_0kZPITO6ScBmwftA56NHsoUW2ZzZTmlXeRzImXT5HVoYV7Jjvd7xGFb1CFRyRfazC9X1Qg6SsTJ87TaaYDmZBcGVzliuUFxgvk4WPYvFMDpfYp0pTiLHK0WqXntYrfBF7C25UtYvuZhtiHXo8-gLSD3PcDSfVSGrfmam3yGw1BRoX3UUpuu5sJnkionXvY3UpARcnyDyaT26GprGYBPR1sH3w6zd_dNOVjOhn9Bb4pemq-Vza59YjYBxeryhEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در دوره اول ریاست‌جمهوری‌ام، ارتش ما را بازسازی کردم و در دوره دوم نیز تا حدودی از ارتش استفاده کردیم.
🔴
آنچه ما انجام داده‌ایم، شگفت‌انگیز است - و همه این‌ها برای صلح و خیرخواهی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/151350" target="_blank">📅 23:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72aac66a14.mp4?token=UsrBPog7t7ecdbjUONQIiTAoMCsJTfFwbSkSM1s_EToY5Qht5ZKApPzoVch8maV8b144YIrIhzHjPsoPexk38wKng29aLIeMyS43f-56h_yHZY424-zoVmNt-cqmhqFyb24IRXTnJPjniERTb-AZzLMTFCCky7lKGEVOVZ7JERLmexDGZL9_ikoqioYTcYS-po8TtJgT6iuoy0yeBht-0sihBy9dc1VREMke7xl5i_XHz41LKzG7mOosMAuR1jt7kaI3R6tNa0o_vI2Pp-J6ldhSGnhfVlDoXFRgoDGVLZPSARvD7_NXoMyNh3iOjODDO3kKtc2XvzG7r2sx3tDs2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72aac66a14.mp4?token=UsrBPog7t7ecdbjUONQIiTAoMCsJTfFwbSkSM1s_EToY5Qht5ZKApPzoVch8maV8b144YIrIhzHjPsoPexk38wKng29aLIeMyS43f-56h_yHZY424-zoVmNt-cqmhqFyb24IRXTnJPjniERTb-AZzLMTFCCky7lKGEVOVZ7JERLmexDGZL9_ikoqioYTcYS-po8TtJgT6iuoy0yeBht-0sihBy9dc1VREMke7xl5i_XHz41LKzG7mOosMAuR1jt7kaI3R6tNa0o_vI2Pp-J6ldhSGnhfVlDoXFRgoDGVLZPSARvD7_NXoMyNh3iOjODDO3kKtc2XvzG7r2sx3tDs2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : حزب جمهوری‌خواه به سرعت در حال پیشرفت است. امروز کسی گفت: «من تعجب می‌کنم که چرا؟»
🔴
من مجبور شدم به میدان بیایم و این کارها (گردهمایی‌ها) را انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/151349" target="_blank">📅 23:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca07627b0.mp4?token=A2s5AZh95qUOSfJsUIiIVKPQjWNIyRBTntJUzmLb6qWnburv-xo2HP8AAWzCcBuYP6lMmE_ZKEj1Py4UTujD3lm1leeF5Ux0FXiZl4Ht0HV7OpNJHh0KsVwYymssZ6wqwcGrhLhE5a3e5AXFc6eXQSYLPvTfOkMhjnMfaZXtcRCAhjMKDO218u8EFW8FA0R5OIACjz-1XAwPwils-_nOBxYuX5TU6xXXriSxRb5xjCkoquoL63wnZHBXGracDj5SGb6u21mtWvAhD7ZooeHYIwnwpMQICfHoIfqJxWH4Inn1zOVgesmv97tCTDlgSpHBenrID_IN9tC247H2Q5Il3gEyL4La3-oEwMo3deRRp8ZP4ADpx3ACyvMe6CnzGBnf4MJcuxoXE5a1XRXLGeo5efWMiNswwHOGrWxwwvS3NSp-2alhGOgHooiGHHFiUbqiLnJgoUmdsnNn6rKiqLSWNU2s8f92_fwPAdaqrRwHyZjCQsmlDtwZiUEOK7h0arJzIPB-epSiAt4Xxrk-3CfOoh6aAq0dPklsMJ6HufjIz92lv4jSh4JzwxSSQWJta31E9CDuD4EgNUhM9l_05lUOYNbMS-l_6ESXeDBXdD5P8dNKI1co2cDFt-vEiFcc4nRe-Q1xKGsu4pzh2RVU4Fll-dhfHM8nENqkxswoR1n6lg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca07627b0.mp4?token=A2s5AZh95qUOSfJsUIiIVKPQjWNIyRBTntJUzmLb6qWnburv-xo2HP8AAWzCcBuYP6lMmE_ZKEj1Py4UTujD3lm1leeF5Ux0FXiZl4Ht0HV7OpNJHh0KsVwYymssZ6wqwcGrhLhE5a3e5AXFc6eXQSYLPvTfOkMhjnMfaZXtcRCAhjMKDO218u8EFW8FA0R5OIACjz-1XAwPwils-_nOBxYuX5TU6xXXriSxRb5xjCkoquoL63wnZHBXGracDj5SGb6u21mtWvAhD7ZooeHYIwnwpMQICfHoIfqJxWH4Inn1zOVgesmv97tCTDlgSpHBenrID_IN9tC247H2Q5Il3gEyL4La3-oEwMo3deRRp8ZP4ADpx3ACyvMe6CnzGBnf4MJcuxoXE5a1XRXLGeo5efWMiNswwHOGrWxwwvS3NSp-2alhGOgHooiGHHFiUbqiLnJgoUmdsnNn6rKiqLSWNU2s8f92_fwPAdaqrRwHyZjCQsmlDtwZiUEOK7h0arJzIPB-epSiAt4Xxrk-3CfOoh6aAq0dPklsMJ6HufjIz92lv4jSh4JzwxSSQWJta31E9CDuD4EgNUhM9l_05lUOYNbMS-l_6ESXeDBXdD5P8dNKI1co2cDFt-vEiFcc4nRe-Q1xKGsu4pzh2RVU4Fll-dhfHM8nENqkxswoR1n6lg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، اکنون ونزوئلا را به عنوان یک "سفر" توصیف می‌کند: ما روابط بسیار خوبی با ونزوئلا داریم. ما میلیاردها دلار نفت از آنجا استخراج می‌کنیم.
🔴
ما هزینه این سفر، این سفر کوچک، را بارها و بارها پرداخت کرده‌ایم.
🔴
همانطور که می‌دانید، "پیروزی از آنِ فاتح است". این یک عبارت قدیمی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151348" target="_blank">📅 23:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خواهر تتلو «امیرحسین مقصودلو» خبر از عفو برادرش داد
🔴
شرط دادگاه پاک کردن کل تتوهای بدنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/151347" target="_blank">📅 23:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ac1779ac.mp4?token=l-HccnBJj0jYF21F96yN4a-EEelcWbf_TpkX8F2elDNXkHdx0zd-cGdbulF9LTiDJdLAQdUWw1ALfb6M7OJ9Gg76rGhpbZJV3gs9zxkzjQD8YtWhLs7m1kAnHxQiYjGxSipJHPMhGfHqem-u6uHFC2-yu2P37VAFFpsvqZrWtfv4t-d82AoGKJnbI5eUnwAsj4M680uil-ydzNXdMpgImF_y9PJF_iURlf8wjd8Oi3UU10jGwD3cRAlWAFqNtiucBykWGOhh_fOkAiFACub8Q-W3YxlvhMxzDi6_9dXQLUsP4U-7H8oL-Gceq8t_hq5lb-ogG43SDM10pL1dpcfhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ac1779ac.mp4?token=l-HccnBJj0jYF21F96yN4a-EEelcWbf_TpkX8F2elDNXkHdx0zd-cGdbulF9LTiDJdLAQdUWw1ALfb6M7OJ9Gg76rGhpbZJV3gs9zxkzjQD8YtWhLs7m1kAnHxQiYjGxSipJHPMhGfHqem-u6uHFC2-yu2P37VAFFpsvqZrWtfv4t-d82AoGKJnbI5eUnwAsj4M680uil-ydzNXdMpgImF_y9PJF_iURlf8wjd8Oi3UU10jGwD3cRAlWAFqNtiucBykWGOhh_fOkAiFACub8Q-W3YxlvhMxzDi6_9dXQLUsP4U-7H8oL-Gceq8t_hq5lb-ogG43SDM10pL1dpcfhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «ما کمی از نیروهای نظامی استفاده کرده‌ایم؛ اما تمام این اقدامات را برای صلح و حسن‌نیت انجام داده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/151346" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d5c29e4b.mp4?token=lY0yD5eGE7EV2c_PR5QE2E0lWQvBUj2slL7ohxZmM85D-P2Q-VdVRQyC-D49rXGA73S4h3RSqrSStJKJormws4xSTUL1sRlUE3nj0QCptYosTNSotK8Jt-59N7qe92nHTTE5Es1AnG1tRzeCVZeFmhLz03zk_8rZODYYFsai1tqFwoWjlwrGPDAY-n55tgvYtrDbWsFWT61K-WGgBKPAWGw1nmuVrMmqKayIZ9tswkg4kE8vrnXwulTpTyHEHzaJWXvAww2gBLq9HBx4KZURT8qFyq469oWFoaTOtGznwWF7VLP2KISWvseE1H035cZkzUKjxXJ1-eqsKtIxJrQPUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d5c29e4b.mp4?token=lY0yD5eGE7EV2c_PR5QE2E0lWQvBUj2slL7ohxZmM85D-P2Q-VdVRQyC-D49rXGA73S4h3RSqrSStJKJormws4xSTUL1sRlUE3nj0QCptYosTNSotK8Jt-59N7qe92nHTTE5Es1AnG1tRzeCVZeFmhLz03zk_8rZODYYFsai1tqFwoWjlwrGPDAY-n55tgvYtrDbWsFWT61K-WGgBKPAWGw1nmuVrMmqKayIZ9tswkg4kE8vrnXwulTpTyHEHzaJWXvAww2gBLq9HBx4KZURT8qFyq469oWFoaTOtGznwWF7VLP2KISWvseE1H035cZkzUKjxXJ1-eqsKtIxJrQPUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/151345" target="_blank">📅 23:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7257ff1afd.mp4?token=QrAfWGMYh1PE8pCYePGjRFWpxyJjImmncSfEvHbLQy7DG7crDQmFqM4iIY4CqUrntSnVnKJlJ0HkQmMMI0qbpqTNCJdC3WfzRQI6E95UrQ-3kf5m7Uzbwcj47HEpcsGAWkScvCut8yR6rpZRG1RiScTGrApuxFTj_fIiMcXf33UJfb4q__mw0glYN1kB659AUS9AQeKcvAATi6Yagam2t3UqpdsMPXMSPxCQWlbTpIG0TFce9e_IwN9h-HWc-4NMA1SZnQ9BHM4xkwftgJRVVjDOBkCbJ46Lhvw3kym08NTPsaVxOyJS3MXbMBi4g-gzFeSFn0Tucf7WZgY2zHPRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7257ff1afd.mp4?token=QrAfWGMYh1PE8pCYePGjRFWpxyJjImmncSfEvHbLQy7DG7crDQmFqM4iIY4CqUrntSnVnKJlJ0HkQmMMI0qbpqTNCJdC3WfzRQI6E95UrQ-3kf5m7Uzbwcj47HEpcsGAWkScvCut8yR6rpZRG1RiScTGrApuxFTj_fIiMcXf33UJfb4q__mw0glYN1kB659AUS9AQeKcvAATi6Yagam2t3UqpdsMPXMSPxCQWlbTpIG0TFce9e_IwN9h-HWc-4NMA1SZnQ9BHM4xkwftgJRVVjDOBkCbJ46Lhvw3kym08NTPsaVxOyJS3MXbMBi4g-gzFeSFn0Tucf7WZgY2zHPRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خواهر تتلو «امیرحسین مقصودلو» خبر از عفو برادرش داد
🔴
شرط دادگاه پاک کردن کل تتوهای بدنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/151344" target="_blank">📅 23:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/151343" target="_blank">📅 23:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/151342" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
معاریو عبری: برآوردهای نظامی می‌گه اسرائیل احتمالاً خیلی زود قراره تو یکی از جبهه‌های منطقه وارد یه عملیات نظامی بشه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/151341" target="_blank">📅 23:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3wnOyZdADqBC33gPtBG_mGQGv8yCJ1J397dzUhg8AK2cM-MUQ3itDQszBFDCAkPs748RmAjMfMWqG0jQnTeIhChQEkFkvrDV5bXfJZCW1kn1iyowaYAcwa2ySo1c7T8RgBz2epU5NKnW81gHNzRt_u2_nDNNsGXJ23pFaqBRQe7pB27cwWZSdBRN46XvL63oCq7ZkU_E-K7cLig7C2wttUZ6NmgiRd4OB3LbsK7Ey6Mrxmd00xow37do1Hr8HROTMB1ug0QOD33MrP48OPvkhf9uFFV8h_sRhqKMV3sjEwmhTujeyJ9R2g7WeU5GMGiof_o2BYJmFmaw90HHlyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب نصب شده تو پارک با موضوع عفاف و حیا و تشبیه بانوان به سوراخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/151340" target="_blank">📅 23:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b88401b5.mp4?token=gHyHcWMW7Ud-mGXqN8FT96rJVrs-pu2U_DzO0A4VoB433ZcMedSrT4gHmG3x733-XmH8UQKiOtIEnUl1mi2bYhCWRHNHjojz2Ef6Y-xmqhj8Ak-5wbFX0UJjRKDNvwuVai8Y4vHu8ujpfjHrM1RrqegPpV1qAijYxURSUnkd8CjN8hLONhYUhNQq6QlfGz9aZbCrqK-P86lZwm-vmUv2NRlGBTUDjc8gcp1WSFsgF89rWkzTAS1jKLMUEPTPzkES7mowtOmlNRdNlWzRRBm9OXw2RqpU58zAgma8NnfLGdPwJC9X8vdKVs1Cxaf6HIqhCiF6ms8R65oW6p2t2Tybww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b88401b5.mp4?token=gHyHcWMW7Ud-mGXqN8FT96rJVrs-pu2U_DzO0A4VoB433ZcMedSrT4gHmG3x733-XmH8UQKiOtIEnUl1mi2bYhCWRHNHjojz2Ef6Y-xmqhj8Ak-5wbFX0UJjRKDNvwuVai8Y4vHu8ujpfjHrM1RrqegPpV1qAijYxURSUnkd8CjN8hLONhYUhNQq6QlfGz9aZbCrqK-P86lZwm-vmUv2NRlGBTUDjc8gcp1WSFsgF89rWkzTAS1jKLMUEPTPzkES7mowtOmlNRdNlWzRRBm9OXw2RqpU58zAgma8NnfLGdPwJC9X8vdKVs1Cxaf6HIqhCiF6ms8R65oW6p2t2Tybww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره انتخابات میان‌ دوره‌ای: فکر می‌کنم عملکرد بسیار خوبی خواهیم داشت
🔴
فکر می‌کنم در انتخابات میان‌دوره‌ای عملکرد بسیار خوبی خواهیم داشت.
🔴
تجمع‌های انتخاباتی من واقعاً در حال تغییر شرایط به نفع ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/151339" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: ما دلار بسیار قدرتمندی داریم؛ دلیلش این است که عملکرد خوبی داریم.
🔴
دلار قوی باعث می‌شود تورم نداشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/151338" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: انتقال نفت به سطح پیش از جنگ بازگشته و گاهی از آن هم فراتر می‌رود
🔴
فقط طی چند روز گذشته، حجم عظیمی معادل میلیون‌ها بشکه نفت منتقل شده است.
🔴
اکنون انتقال نفت در سطحی انجام می‌شود که با پیش از جنگ برابری می‌کند و گاهی حتی از آن فراتر می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/151337" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ درباره ایران: وزیر نفت ایران همین الان استعفا داد. او گفت: «ما نه اقتصاد داریم، نه نفت داریم، هیچ‌چیز نداریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/151336" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151335">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هیمتی: بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود؛ ده روز از این دو هفته گذشت و اتفاقی نیافتاد
🔴
من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/151335" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فاکس نیوز»: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/151334" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تحلیلگر صداوسیما: آمریکا چون دزدی می‌کنه دلارش بی‌برکته و به همین خاطر مردمش گرسنه هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/151333" target="_blank">📅 22:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/151332" target="_blank">📅 22:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/151331" target="_blank">📅 22:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=IKd0JBNjwJwxLrOKPtgoTMrqzET8BNmWSy_Q49nimSdwgg5u01K4M3DHiEkhQwyvyXpEk4-tm4l1AYX5N4PFGjWJK3a9sYBydPrNXWZxDfIYJy3gcmCgpBdjDoyoiNZUXtfm9KCO3I41EUHXdL8f6qUCNmdwfnnDJ-drpapFkYcNlZT1YAugIK-IRbK9YF7pwlfTE8s1YsRo0rrXVIn5g8Zq3Z3R6WLsY4Zzuhq7QsS_Jt3cY9vAKl9ygfPPgQKJ5UjIzERFfcMMJKsMiTPMXYz56yl0oAGuJmJlSIi85r0HHVVdNzXvuGAs96EqFrHC5_WvKPbllrRb9dHYZCt2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=IKd0JBNjwJwxLrOKPtgoTMrqzET8BNmWSy_Q49nimSdwgg5u01K4M3DHiEkhQwyvyXpEk4-tm4l1AYX5N4PFGjWJK3a9sYBydPrNXWZxDfIYJy3gcmCgpBdjDoyoiNZUXtfm9KCO3I41EUHXdL8f6qUCNmdwfnnDJ-drpapFkYcNlZT1YAugIK-IRbK9YF7pwlfTE8s1YsRo0rrXVIn5g8Zq3Z3R6WLsY4Zzuhq7QsS_Jt3cY9vAKl9ygfPPgQKJ5UjIzERFfcMMJKsMiTPMXYz56yl0oAGuJmJlSIi85r0HHVVdNzXvuGAs96EqFrHC5_WvKPbllrRb9dHYZCt2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل هوادارای لیونل مسی برای خداحافظی در آستانه آخرین بازی این بازیکن برای آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/151330" target="_blank">📅 21:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فکت : آخرین باری که روسا گفتن وضعیت تحت کنترله، ۴۸ ساعت بعدش کل اروپا درگیر تشعشات هسته‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/151329" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
عمان: یک کشتی در مسندم هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/151328" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره: در پی گسترش اعتراضات دانش‌آموزان، دولت فرانسه مدارس را تا آخر هفته تعطیل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/151327" target="_blank">📅 21:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ثابتی: رسایی جز افراد بزرگ تاریخ ایرانه حقیقت رو گفت و روی حرفاش ایستاد و رفت زندون به خاطرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/151326" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شرکت ایران خودرو مجددا درخواست افزایش قیمت 40 درصدی تمام زباله های خودش رو به دولت ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/151325" target="_blank">📅 21:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
گزارش دو انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/151324" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BV07fJovQcYPI9BmMEKid8eQuuOO4Zj9XXHoaziTCvwD6R-UxYo4qz0zJ15LgXDZW_zzxznz8pofWegdhzwHaQQ4mMq1N8jZ7heGmiTU_mm4YQoJuK2dka2sYQQ4V2Tg_1bnCqaf9J4xx7CAGpZ_-TmIm-4ZYhd3Evb2IrQMkZQukPSZSMl7qV0CX9phmXXLzSXtY7Q6P_QQaAu_O1BwLXqeU9EtnQdO64XbDa-EVdMgRKx1016kqYke4ADJ0tyCnY7molCwCdLnJjfej3aZgpFUa8YCV5HhuFKb7zzPJZ-RkzXdmu31fkvSWywBtkfkFy-3QHhX2yMR1r4lc5nPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTymW2ANsQirxYAHPsPtWpFRhuA0Ljw8TQJHU9C94x142gaRC9fsbE1_vfwz1VO0_oQ8HiUmXLj902I6ygg7ZtE7fzglrmCXWdn5ZulI4iK6dwDLUy_GoV5Io_DF7aJa5S1nWBxE9R5toNopD-9fREfp0G1hKFzf8USnUvzIOmpXsbYIm9SLgrOFeR2r1-wH8KxAr7TIlu9NfKpXc5p-aCjSsw4BmiatFKYsv05nplS1ck6J5ggEUNxnRqs9icJSpQEufYw7xJutaN0ivD6SzrTlEYfYn-Aks4FqtCrs64KbeWZuiA9vFZiVtMWQwz45L2cqhRhdKeo9nwyNTYRk8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی از ستون‌های دود برخاسته از تأسیسات آرامکو در روز گذشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/151322" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / روزنامه عبری «معاریو»: برآوردهای قطعی نظامی حاکی از آن است که اسرائیل در آستانه انجام یک عملیات نظامی در یکی از جبهه‌های منطقه قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/151321" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فاینشنال تایمز: مذاکرات ایران و آمریکا پشت پرده ادامه دارد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/151320" target="_blank">📅 20:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مرگ مشکوک در آزمایشگاه ایرکوتسک روسیه؛ آمریکا از احتمال بروز طاعون ریوی ابراز نگرانی کرد
🔴
وزارت خارجه ایالات متحده: گزارش‌ها را با دقت زیر نظر داریم
🔴
مسکو اطلاعات دقیق را «سریع و شفاف» منتشر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/151319" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الجزیره: رهبران دموکرات، شوخی ترامپ درباره اجازه دادن به ایران برای بمباران لس‌آنجلس و سن‌دیگو را محکوم کردند
🔴
آن‌ها رئیس‌جمهور آمریکا را «آشفته و خطرناک» توصیف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/151318" target="_blank">📅 20:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTaawvfS0gbeDa_wYkr87v_Kd8OlM0R_KuIlOViyRwnkobU9eM3crkJD5HJOerXkHpl5j2MFgZ0Mx_lM1sMIMEqSgN4v4hqD6KREApmpH8M1gfsNbjFoYpSZhdqC0DC75E6hmGmIe7AR9qr-oNrlCxs_5ile1_qCanq7W-cLKBNcgZIbS5SK2lIHw5twC3moh8NSrLH2D8BSur0VBgWc8vVrLa-2UZGi70iWGevW3hDcV0mWkiQaBaz889F2WZ-S2G-OKe4IUhRoaF3k5vNoTg3djWPsOOraTAjNpUgo8dR-97xdL3TeKm_JYy3B9GIl3VZwQy9md_UihzRgOAnboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد پروازها در فرودگاه القریات عربستان سعودی، در نزدیکی مرز اردن، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/151317" target="_blank">📅 20:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ریانووستی: یوری اوشاکوف، دستیار رئیس‌ جمهور روسیه اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور این کشور در جریان سفر خود به ترکمنستان برای شرکت در نشست سران کشورهای مستقل مشترک‌المنافع، روز جمعه نهم اکتبر با مسعود پزشکیان همتای ایرانی خود به‌صورت دوجانبه دیدار خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/151316" target="_blank">📅 20:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/151315" target="_blank">📅 20:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یک مقام قطری: مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد و پیام‌ هایی بین واشنگتن و تهران رد و بدل می‌شود و قطر نقش میانجی را ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/151314" target="_blank">📅 19:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رایتل رسما اعلام ورشکستگی کرد و سهام خودشو به مبلغ 130 همت در مزایده قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/151313" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر کشور برای انتقال پیام امیر قطر به پزشکیان عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/151312" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151310">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=KrhjulZkvVMLtvTQV364dlOAw1BOPJ4lhrscv7UkUm5658rZa7A38N9B5LmmELsim6oXyIUUm3Axu94_MP7Df2yxsqcl8ZqaAnTdt5toJfQcOzY61xqKb74oO6DfQkeSXFAJgJs4Qds00pk1URvhN83GJcUi5_VmW5ZhoTTJ2g1Qb9FWaluyegf7xqbpLyqzT-52i9p6ddjuDM7AX8CJ9l5eThsjFrFmEJGvE9UsLU9rumtlGEBdrydgMvsWyLmhUXQ8pLitxZLRxypI3aNKv7FPu-0ctOusy3efZmLGSvRdGQsBUwvp1WuIY6dMGhtjraTkWD7pcUJ6ENI3UMcB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=KrhjulZkvVMLtvTQV364dlOAw1BOPJ4lhrscv7UkUm5658rZa7A38N9B5LmmELsim6oXyIUUm3Axu94_MP7Df2yxsqcl8ZqaAnTdt5toJfQcOzY61xqKb74oO6DfQkeSXFAJgJs4Qds00pk1URvhN83GJcUi5_VmW5ZhoTTJ2g1Qb9FWaluyegf7xqbpLyqzT-52i9p6ddjuDM7AX8CJ9l5eThsjFrFmEJGvE9UsLU9rumtlGEBdrydgMvsWyLmhUXQ8pLitxZLRxypI3aNKv7FPu-0ctOusy3efZmLGSvRdGQsBUwvp1WuIY6dMGhtjraTkWD7pcUJ6ENI3UMcB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/151310" target="_blank">📅 19:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/151308" target="_blank">📅 19:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
👈
پاکستان: خبر استقرار ۳۰ تا ۴۰ هزار نیروی نظامی ما در عربستان، ساختگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/151306" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
